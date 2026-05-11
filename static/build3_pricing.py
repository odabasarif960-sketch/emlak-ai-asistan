import os

p = os.path.join(os.path.dirname(__file__), 'index.html')

with open(p, 'a', encoding='utf-8') as f:
    f.write("""
<!-- PRICING -->
<section id="fiyatlandirma">
  <div class="container">
    <div style="text-align:center;margin-bottom:20px">
      <div class="section-tag">Fiyatlandırma</div>
      <h2 class="section-title">Yatırımınızın <span class="gold">Karşılığını Alın</span></h2>
      <p class="section-sub" style="margin:0 auto">İşletmenizin büyüklüğüne göre ölçeklenebilen, şeffaf ve taahhütsüz fiyatlandırma modelleri.</p>
    </div>
    
    <div class="pricing-grid">
      <!-- Paket 1 -->
      <div class="p-card">
        <h3 class="p-name">Başlangıç</h3>
        <div class="p-price">2.500₺ <span>/ ay</span></div>
        <ul class="p-features">
          <li><i class="fas fa-check"></i> Maksimum 50 İlan Entegrasyonu</li>
          <li><i class="fas fa-check"></i> AI Chatbot (GPT-3.5 altyapısı)</li>
          <li><i class="fas fa-check"></i> Standart Web Arayüzü</li>
          <li><i class="fas fa-check"></i> E-posta ile Destek</li>
          <li><i class="fas fa-check"></i> WhatsApp Entegrasyonu</li>
        </ul>
        <button class="p-btn">Hemen Başla</button>
      </div>

      <!-- Paket 2 -->
      <div class="p-card popular">
        <div class="pop-badge">EN ÇOK TERCİH EDİLEN</div>
        <h3 class="p-name">Profesyonel</h3>
        <div class="p-price">5.000₺ <span>/ ay</span></div>
        <ul class="p-features">
          <li><i class="fas fa-check"></i> Limitsiz İlan Entegrasyonu</li>
          <li><i class="fas fa-check"></i> Gelişmiş AI Asistan (GPT-4o)</li>
          <li><i class="fas fa-check"></i> Otomatik Randevu Sistemi (Takvim)</li>
          <li><i class="fas fa-check"></i> Kendi Domaininize Kurulum</li>
          <li><i class="fas fa-check"></i> Sahibinden / Hepsiemlak Botu</li>
        </ul>
        <button class="p-btn">Ücretsiz Demo İste</button>
      </div>

      <!-- Paket 3 -->
      <div class="p-card">
        <h3 class="p-name">Kurumsal</h3>
        <div class="p-price">12.000₺ <span>/ ay</span></div>
        <ul class="p-features">
          <li><i class="fas fa-check"></i> Çoklu Ofis / Acente Yönetimi</li>
          <li><i class="fas fa-check"></i> WhatsApp Cloud API Entegrasyonu</li>
          <li><i class="fas fa-check"></i> CRM Sistemine (Salesforce vb.) Veri Aktarımı</li>
          <li><i class="fas fa-check"></i> Görsel Analiz (GPT-4o Vision)</li>
          <li><i class="fas fa-check"></i> 7/24 Özel Temsilci</li>
        </ul>
        <button class="p-btn">Bize Ulaşın</button>
      </div>
    </div>
  </div>
</section>
""")
print("Part 3 Pricing done")
