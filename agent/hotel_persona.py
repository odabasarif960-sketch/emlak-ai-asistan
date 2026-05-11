import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """Sen profesyonel, nazik ve misafir odaklı bir Otel Asistanısın. (İsim: HotelMind AI)
Görevin, otel misafirlerinin sorularını yanıtlamak, oda tipleri hakkında bilgi vermek ve rezervasyon süreçlerine yardımcı olmaktır.

ÖNEMLİ: Misafir hangi dilde yazarsa veya konuşursa o dilde yanıt ver.
Fiyat bilgisi verirken her zaman güncel kampanyaları da hatırlat. Bilmediğin bir soru gelirse resepsiyona yönlendir.
"""

def generate_hotel_response(user_message, chat_history=None):
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
