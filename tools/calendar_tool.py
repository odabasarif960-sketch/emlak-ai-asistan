import json
import os
from datetime import datetime, timedelta

# Randevu dosyası (Veritabanı niyetine)
CALENDAR_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "calendar_events.json")

def init_calendar_file():
    if not os.path.exists(CALENDAR_FILE):
        os.makedirs(os.path.dirname(CALENDAR_FILE), exist_ok=True)
        with open(CALENDAR_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)

def get_available_slots(date_str: str):
    """
    Belirli bir tarih için boş saat dilimlerini getirir. (Format: YYYY-MM-DD)
    Mock sistem: Sadece 10:00, 14:00 ve 16:00 saatlerini teklif eder, eğer doluysa çıkarır.
    """
    init_calendar_file()
    try:
        with open(CALENDAR_FILE, 'r', encoding='utf-8') as f:
            events = json.load(f)
            
        # O güne ait dolu saatler
        booked_times = [event['time'] for event in events if event['date'] == date_str]
        
        # Standart boş saatler
        all_slots = ["10:00", "14:00", "16:00"]
        available = [slot for slot in all_slots if slot not in booked_times]
        
        if not available:
            return f"{date_str} tarihi için maalesef boş randevu saatimiz kalmamıştır."
            
        return f"{date_str} tarihi için boş saatlerimiz: {', '.join(available)}."
    except Exception as e:
        return f"Takvim okunurken hata oluştu: {str(e)}"

def book_appointment(date_str: str, time_str: str, customer_name: str, property_id: str):
    """
    Belirli bir tarih ve saat için ev gösterimi randevusu oluşturur.
    """
    init_calendar_file()
    try:
        with open(CALENDAR_FILE, 'r', encoding='utf-8') as f:
            events = json.load(f)
            
        # Çakışma kontrolü
        for event in events:
            if event['date'] == date_str and event['time'] == time_str:
                return f"Üzgünüm, {date_str} saat {time_str} için randevu zaten dolu."
                
        # Yeni randevuyu ekle
        new_event = {
            "date": date_str,
            "time": time_str,
            "customer_name": customer_name,
            "property_id": property_id,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        events.append(new_event)
        
        with open(CALENDAR_FILE, 'w', encoding='utf-8') as f:
            json.dump(events, f, indent=4, ensure_ascii=False)
            
        return f"Harika! {customer_name} adına {date_str} saat {time_str} için {property_id} nolu ilan gösterim randevusu oluşturuldu."
    except Exception as e:
        return f"Randevu oluşturulurken hata: {str(e)}"
