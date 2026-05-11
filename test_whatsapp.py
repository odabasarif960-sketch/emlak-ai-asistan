import requests

url = "http://localhost:8000/whatsapp"
data = {
    "From": "whatsapp:+905551234567",
    "Body": "Selam, İstanbul Kadıköy'de 3+1 kiralık daire var mı?"
}

print(f"Mesaj Gönderiliyor: {data['Body']}")
try:
    response = requests.post(url, data=data)
    print(f"Durum Kodu: {response.status_code}")
    print("Gelen TwiML Yanıtı:")
    print(response.text)
except Exception as e:
    print(f"Hata oluştu: {e}")
