import os
import sys

# Proje ana dizinini yola ekle
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.pinecone_client import load_data_to_pinecone
from agent.persona import generate_response
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("PINECONE_API_KEY"):
        print("HATA: .env dosyasında OPENAI_API_KEY ve PINECONE_API_KEY tanımlı olmalıdır.")
        return

    print("=== EMLAK AI ASİSTANI TEST ARACI ===")
    print("1. Örnek ilanları Pinecone'a yükle (Sadece ilk kurulumda 1 kez yapılmalıdır)")
    print("2. Asistan ile sohbet et (RAG Testi)")
    
    secim = input("Seçiminiz (1/2): ")
    
    if secim == "1":
        json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "sample_listings.json")
        print(f"'{json_path}' okunuyor...")
        load_data_to_pinecone(json_path)
    elif secim == "2":
        chat_history = []
        print("\nAsistana mesaj yazın (Çıkmak için 'q' yazın)")
        while True:
            user_msg = input("\nSen: ")
            if user_msg.lower() == 'q':
                break
                
            response = generate_response(user_message=user_msg, chat_history=chat_history)
            print(f"\nEmlak AI: {response}")
            
            # Geçmişi güncelle
            chat_history.append({"role": "user", "content": user_msg})
            chat_history.append({"role": "assistant", "content": response})
    else:
        print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
