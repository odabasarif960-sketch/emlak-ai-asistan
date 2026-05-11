import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# We will implement these tools later or adapt from original
# from database.pinecone_client import search_listings
# from tools.calendar_tool import get_available_slots, book_appointment
# from tools.crm_tool import save_lead_to_crm
# from tools.vision_tool import analyze_property_image

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """Sen profesyonel, nazik ve çözüm odaklı bir gayrimenkul danışmanısın. (İsim: Emlak AI Asistanı)
Görevin, müşterilerin taleplerini dinlemek, bütçe ve lokasyon tercihlerine göre onlara en uygun ilanları sunmak ve randevu ayarlamaktır.

ÖNEMLİ: Müşteri hangi dilde yazarsa veya konuşursa o dilde yanıt ver.
Eğer araçlardan dönen ilanlarda tam eşleşme yoksa, dürüstçe olmadığını belirt ama en yakın alternatifleri sun. Asla sahte ilan uydurma.
"""

def generate_emlak_response(user_message, chat_history=None):
    if chat_history is None:
        chat_history = []
        
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    for msg in chat_history:
        if msg["role"] in ["user", "assistant"] and isinstance(msg.get("content"), str):
            messages.append({"role": msg["role"], "content": msg["content"]})
        
    messages.append({"role": "user", "content": user_message})
    
    # Tool integration will go here, currently returning simple completion
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7
    )
    
    return response.choices[0].message.content
