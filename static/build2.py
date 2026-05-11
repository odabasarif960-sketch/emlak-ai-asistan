
import os
p = os.path.join(os.path.dirname(__file__), 'index.html')
with open(p, 'a', encoding='utf-8') as f:
    f.write("""<body>

<!-- NAV -->
<nav>
  <div class="nav-logo">
    <i class="fas fa-building"></i>
    <span class="logo-text">Emlak AI</span>
  </div>
  <div class="nav-links">
    <a href="#ozellikler">Özellikler</a>
    <a href="#ilanlar">İlanlar</a>
    <a href="#asistan">AI Asistan</a>
    <a href="#iletisim">İletişim</a>
  </div>
  <button class="nav-cta" onclick="document.getElementById('demo-modal').classList.add('open')">
    <i class="fas fa-calendar-check"></i> Demo Talep Et
  </button>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-badge"><span class="dot"></span> Emlak Ofislerine Özel B2B SaaS — Aktif</div>
  <h1>Emlak Ofisinizi<br><span class="gold">Yapay Zeka ile Büyütün</span></h1>
  <p>Kendi ilanlarınızı müşterilerinize saniyeler içinde sunan, 7/24 soruları yanıtlayan ve otomatik randevu toplayan yapay zeka asistanınız.</p>
  <div class="hero-btns">
    <button class="btn-primary" onclick="document.getElementById('fiyatlandirma').scrollIntoView({behavior:'smooth'})">
      <i class="fas fa-rocket"></i> Paketleri İncele
    </button>
    <button class="btn-secondary" onclick="document.getElementById('asistan').scrollIntoView({behavior:'smooth'})">
      <i class="fas fa-comments"></i> Demosunu Deneyin
    </button>
  </div>
  <div class="stats-bar">
    <div class="stat"><div class="stat-num">22+</div><div class="stat-lbl">Aktif İlan</div></div>
    <div class="stat"><div class="stat-num">7</div><div class="stat-lbl">Şehir</div></div>
    <div class="stat"><div class="stat-num">GPT-4o</div><div class="stat-lbl">AI Motoru</div></div>
    <div class="stat"><div class="stat-num">7/24</div><div class="stat-lbl">Çevrimiçi</div></div>
  </div>
</section>

<!-- FEATURES -->
<section id="ozellikler">
  <div class="container">
    <div class="section-tag">Neden Emlak AI?</div>
    <h2 class="section-title">Ofisiniz İçin <span class="gold">Yapay Zeka</span> Devrimi</h2>
    <p class="section-sub">Müşterilerinizi portföyünüzle 7/24 buluşturan, tamamen size özel (White-label) akıllı asistan altyapısı.</p>
    <div class="features-grid">
      <div class="fc">
        <div class="fc-icon"><i class="fas fa-brain"></i></div>
        <h3>Semantik Arama (RAG)</h3>
        <p>Pinecone vektör veritabanıyla doğal dil sorgularını anlayan akıllı arama. "Deniz manzaralı, köpeğe uygun 3+1" gibi sorgular bile çalışır.</p>
      </div>
      <div class="fc">
        <div class="fc-icon"><i class="fas fa-calendar-check"></i></div>
        <h3>Otomatik Randevu</h3>
        <p>Beğendiğiniz evi görmek için AI asistanınız müsait saatleri gösterir ve randevunuzu anında oluşturur. Telefon beklemenize gerek yok.</p>
      </div>
      <div class="fc">
        <div class="fc-icon"><i class="fas fa-eye"></i></div>
        <h3>Fotoğraf Analizi</h3>
        <p>GPT-4o Vision ile ev fotoğraflarını analiz edin. Fotoğraf linkini paylaşın, AI tadilat durumu, oda büyüklüğü ve potansiyeli değerlendirsin.</p>
      </div>
      <div class="fc">
        <div class="fc-icon"><i class="fas fa-database"></i></div>
        <h3>CRM Entegrasyonu</h3>
        <p>Potansiyel alıcı bilgileriniz otomatik sisteme kaydedilir. Bütçe, tercih ve iletişim bilgileri eksiksiz takip edilir.</p>
      </div>
      <div class="fc">
        <div class="fc-icon"><i class="fas fa-chart-line"></i></div>
        <h3>Piyasa Analizi</h3>
        <p>İstanbul'dan Bodrum'a, Alanya'dan İzmir'e geniş portföyde fiyat karşılaştırması ve yatırım getirisi değerlendirmesi.</p>
      </div>
      <div class="fc">
        <div class="fc-icon"><i class="fas fa-shield-halved"></i></div>
        <h3>Güvenli & Hızlı</h3>
        <p>FastAPI backend, SSL şifreleme ve Railway cloud altyapısı ile verileriniz güvende. 7/24 kesintisiz hizmet garantisi.</p>
      </div>
    </div>
  </div>
</section>
""")
print("Part 2 done")
