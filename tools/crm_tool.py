import csv
import os
from datetime import datetime

# Veritabanı dosyası
CRM_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "crm_leads.csv")

def init_crm_file():
    """Eğer CRM dosyası yoksa başlıklarla oluşturur."""
    if not os.path.exists(CRM_FILE):
        os.makedirs(os.path.dirname(CRM_FILE), exist_ok=True)
        with open(CRM_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Tarih", "İsim", "Telefon", "Bütçe", "Talepler", "Durum"])

def save_lead_to_crm(name: str, phone: str, budget: str, requirements: str):
    """
    Kullanıcının bilgilerini ve taleplerini CRM veritabanına kaydeder.
    """
    init_crm_file()
    try:
        with open(CRM_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                name,
                phone,
                budget,
                requirements,
                "Yeni Lead"
            ])
        return f"{name} isimli müşterinin talepleri CRM sistemine başarıyla kaydedildi."
    except Exception as e:
        return f"Kayıt sırasında bir hata oluştu: {str(e)}"
