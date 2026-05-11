import os
import json
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "emlak-portfoy")

# Initialize clients
if OPENAI_API_KEY and PINECONE_API_KEY:
    pc = Pinecone(api_key=PINECONE_API_KEY)
    openai_client = OpenAI(api_key=OPENAI_API_KEY)
else:
    print("UYARI: API Key'ler eksik. Lütfen .env dosyasını kontrol edin.")

def get_embedding(text):
    """Metni OpenAI text-embedding-3-small modeli ile vektöre çevirir."""
    response = openai_client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

def init_pinecone_index():
    """Pinecone index'ini oluşturur (eğer yoksa)."""
    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]
    if INDEX_NAME not in existing_indexes:
        print(f"Index '{INDEX_NAME}' bulunamadı, oluşturuluyor...")
        pc.create_index(
            name=INDEX_NAME,
            dimension=1536, # text-embedding-3-small boyutu
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
        print("Index oluşturuldu.")
    return pc.Index(INDEX_NAME)

def load_data_to_pinecone(json_path):
    """JSON dosyasındaki ilanları okuyup Pinecone'a yükler."""
    index = init_pinecone_index()
    
    with open(json_path, 'r', encoding='utf-8') as f:
        listings = json.load(f)
    
    vectors_to_upsert = []
    
    for item in listings:
        # İlanı anlatan kapsamlı bir metin oluştur (Vektörleştirmek için)
        text_content = f"{item['baslik']}. {item['tip']} {item['durum']}. " \
                       f"Fiyat: {item['fiyat_tl']} TL. Konum: {item['il']}, {item['ilce']}, {item['mahalle']}. " \
                       f"Oda Sayısı: {item['oda_sayisi']}, Net Metrekare: {item['net_m2']} m2. " \
                       f"Özellikler: {', '.join(item['ozellikler'])}. Açıklama: {item['aciklama']}"
        
        print(f"Vektörleştiriliyor: {item['id']} - {item['baslik']}")
        embedding = get_embedding(text_content)
        
        # Meta veriler (Filtreleme için eklenebilir)
        metadata = {
            "baslik": item['baslik'],
            "tip": item['tip'],
            "durum": item['durum'],
            "fiyat_tl": item['fiyat_tl'],
            "il": item['il'],
            "ilce": item['ilce'],
            "oda_sayisi": item['oda_sayisi']
        }
        
        vectors_to_upsert.append((item['id'], embedding, metadata))
        
    # Toplu olarak yükle
    print(f"Toplam {len(vectors_to_upsert)} ilan Pinecone'a yükleniyor...")
    index.upsert(vectors=vectors_to_upsert)
    print("Yükleme tamamlandı.")

def search_listings(query, top_k=3):
    """Kullanıcının sorgusuna en uygun ilanları getirir."""
    index = init_pinecone_index()
    query_embedding = get_embedding(query)
    
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )
    
    matched_listings = []
    for match in results['matches']:
        matched_listings.append({
            "id": match['id'],
            "score": match['score'],
            "metadata": match['metadata']
        })
        
    return matched_listings
