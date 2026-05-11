import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_property_image(image_url: str, specific_question: str = None):
    """
    Kullanıcının gönderdiği ev/oda fotoğrafını GPT-4o Vision modeliyle analiz eder.
    """
    try:
        prompt_text = "Bu bir gayrimenkul fotoğrafıdır. Fotoğrafı bir emlak eksperi gözüyle analiz et. Odanın/evin durumunu, kalitesini, aydınlatmasını ve öne çıkan özelliklerini kısaca özetle."
        if specific_question:
            prompt_text += f"\nAyrıca şu spesifik soruya da cevap ver: {specific_question}"

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Görsel analiz edilirken bir hata oluştu: {str(e)}"
