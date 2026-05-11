import os
import json
from openai import OpenAI
from dotenv import load_dotenv

from database.pinecone_client import search_listings
from tools.calendar_tool import get_available_slots, book_appointment
from tools.crm_tool import save_lead_to_crm
from tools.vision_tool import analyze_property_image

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """Sen profesyonel, nazik ve çözüm odaklı bir gayrimenkul danışmanısın. (İsim: Emlak AI Asistanı)
Görevin, müşterilerin taleplerini dinlemek, bütçe ve lokasyon tercihlerine göre onlara en uygun ilanları sunmak ve randevu ayarlamaktır.

ÖNEMLİ: Müşteri hangi dilde yazarsa veya konuşursa (İngilizce, Rusça, Arapça, vb.), kesinlikle ama kesinlikle o dilde yanıt ver. Arama sorgularını Türkçe yapabilirsin ama kullanıcıya cevabın hep onun dilinde olmalı.

Kullanabileceğin Araçlar (Tools):
1. `search_listings`: Müşterinin talebine uygun (lokasyon, fiyat, oda sayısı) ilanları veritabanında arar. Bir müşteri ilan sorduğunda MUTLAKA bu aracı kullan.
2. `get_available_slots`: Evi göstermek için belirli bir tarihte (YYYY-MM-DD) takvimdeki boş saatleri kontrol eder.
3. `book_appointment`: Müşteri evi görmek istediğinde ve saati seçtiğinde randevuyu kaydeder.
4. `save_lead_to_crm`: Müşteri bilgilerini (isim, telefon, bütçe, talep) sisteme kaydeder. Potansiyel alıcıyı yakaladığında bu aracı kullan.
5. `analyze_property_image`: Müşteri sana bir ev veya oda fotoğrafı linki gönderip yorum/analiz isterse bu aracı kullan.

Eğer araçlardan (tools) dönen ilanlarda tam eşleşme yoksa, dürüstçe olmadığını belirt ama en yakın alternatifleri sun. Asla sahte ilan uydurma.
"""

# Tool (Function) tanımlamaları
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_listings",
            "description": "Veritabanındaki emlak ilanlarında semantik arama yapar. İlan bulmak için kullanılır.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Arama sorgusu. Örn: 'Kadıköy deniz manzaralı 3+1'"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_available_slots",
            "description": "Belirli bir tarih için takvimdeki boş randevu saatlerini getirir.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date_str": {
                        "type": "string",
                        "description": "Tarih, YYYY-MM-DD formatında. Örn: '2026-05-02'"
                    }
                },
                "required": ["date_str"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "book_appointment",
            "description": "Belirli bir saat için ev gösterimi randevusu oluşturur.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date_str": {"type": "string", "description": "Tarih, YYYY-MM-DD formatında."},
                    "time_str": {"type": "string", "description": "Saat. Örn: '14:00'"},
                    "customer_name": {"type": "string", "description": "Müşterinin adı."},
                    "property_id": {"type": "string", "description": "İlanın ID'si. Örn: 'ilan-1001'"}
                },
                "required": ["date_str", "time_str", "customer_name", "property_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "save_lead_to_crm",
            "description": "Müşteri adayının bilgilerini sisteme kaydeder.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Müşteri adı."},
                    "phone": {"type": "string", "description": "Telefon numarası."},
                    "budget": {"type": "string", "description": "Müşterinin bütçesi. Örn: '5 Milyon TL'"},
                    "requirements": {"type": "string", "description": "Müşterinin aradığı ev özellikleri."}
                },
                "required": ["name", "phone", "budget", "requirements"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "analyze_property_image",
            "description": "Emlak/Ev fotoğrafı linki verildiğinde GPT-4o Vision ile fotoğrafı analiz eder.",
            "parameters": {
                "type": "object",
                "properties": {
                    "image_url": {"type": "string", "description": "Fotoğrafın tam URL adresi."},
                    "specific_question": {"type": "string", "description": "Opsiyonel. Kullanıcının fotoğrafla ilgili özel sorusu var mı?"}
                },
                "required": ["image_url"]
            }
        }
    }
]

def execute_function_call(func_name, kwargs):
    """Gelen tool çağrısını çalıştırır."""
    if func_name == "search_listings":
        # Çıktıyı LLM'in okuyabileceği string formatına getiriyoruz
        results = search_listings(**kwargs)
        return json.dumps(results, ensure_ascii=False)
    elif func_name == "get_available_slots":
        return get_available_slots(**kwargs)
    elif func_name == "book_appointment":
        return book_appointment(**kwargs)
    elif func_name == "save_lead_to_crm":
        return save_lead_to_crm(**kwargs)
    elif func_name == "analyze_property_image":
        return analyze_property_image(**kwargs)
    else:
        return f"Hata: {func_name} isimli bir araç bulunamadı."

def generate_response(user_message, chat_history=None):
    if chat_history is None:
        chat_history = []
        
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Geçmiş sohbeti ekle
    for msg in chat_history:
        # tool_calls ve tool çağrılarını temizleyerek history'i basitleştir (veya desteklemek için direkt ekle)
        # Basitlik açısından tool mesajları varsa atlıyoruz veya tam OpenAI formatında tutmalıyız.
        # Bu aşamada sadece user/assistant text mesajlarını tutalım:
        if msg["role"] in ["user", "assistant"] and isinstance(msg.get("content"), str):
            messages.append({"role": msg["role"], "content": msg["content"]})
        
    messages.append({"role": "user", "content": user_message})
    
    # OpenAI ile etkileşim (Function calling destekli)
    print("OpenAI'dan cevap bekleniyor (Tools aktif)...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
        temperature=0.7
    )
    
    response_message = response.choices[0].message
    
    # Eğer asistan bir araç kullanmak isterse:
    if response_message.tool_calls:
        messages.append(response_message) # Asistanın tool call niyetini mesaja ekle
        
        for tool_call in response_message.tool_calls:
            func_name = tool_call.function.name
            func_args = json.loads(tool_call.function.arguments)
            
            print(f"Araç çalıştırılıyor: {func_name}({func_args})")
            func_response = execute_function_call(func_name, func_args)
            
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": func_name,
                "content": str(func_response)
            })
            
        # Araçların sonuçlarıyla LLM'e tekrar sor (İkinci tur)
        second_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7
        )
        return second_response.choices[0].message.content
        
    # Eğer doğrudan metin döndürdüyse
    return response_message.content
