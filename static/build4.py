
import os
p = os.path.join(os.path.dirname(__file__), 'index.html')
with open(p, 'a', encoding='utf-8') as f:
    f.write("""
<!-- CHAT / AI SECTION -->
<section id="asistan">
  <div class="container">
    <div style="text-align:center;margin-bottom:0">
      <div class="section-tag">AI Danışman</div>
      <h2 class="section-title">Hayalinizdeki Evi <span class="gold">Bize Anlatın</span></h2>
      <p class="section-sub" style="margin:0 auto">GPT-4o destekli asistanımız bütçenize ve tercihlerinize göre size özel ilanları getirir, randevu ayarlar.</p>
    </div>
    <div class="chat-layout">
      <div class="chat-info">
        <h3>Akıllı Danışmanınız<br>7/24 Yanınızda</h3>
        <p>Sohbet tarzında arama yapın. "5 milyon TL bütçem var, Kadıköy'de deniz manzaralı daire istiyorum" demeniz yeterli.</p>
        <div class="cfeats">
          <div class="cfeat"><i class="fas fa-search"></i> Semantik ilan arama (RAG + Pinecone)</div>
          <div class="cfeat"><i class="fas fa-calendar"></i> Otomatik randevu oluşturma</div>
          <div class="cfeat"><i class="fas fa-camera"></i> Fotoğraf analizi (GPT-4o Vision)</div>
          <div class="cfeat"><i class="fas fa-user-check"></i> CRM'e otomatik kayıt</div>
          <div class="cfeat"><i class="fas fa-language"></i> Türkçe doğal dil anlayışı</div>
        </div>
      </div>
      <div class="chat-win">
        <div class="chat-head">
          <div class="ch-av">🏠</div>
          <div class="ch-info">
            <h4>Emlak AI Danışmanı</h4>
            <p><span class="odot"></span> Çevrimiçi — Hizmetinizde</p>
          </div>
        </div>
        <div id="chat-box">
          <div class="msg bot">
            <div class="mav">🤖</div>
            <div class="bbl">
              Merhaba! Ben Emlak AI danışmanınızım. 🏡<br><br>
              Portföyümüzde İstanbul, Bodrum, İzmir, Antalya ve daha birçok şehirde lüks villalardan uygun fiyatlı dairelere kadar 22+ ilan var.<br><br>
              Bütçenizi ve lokasyon tercihinizi söyleyin!
              <div class="tm" id="bot-time"></div>
            </div>
          </div>
        </div>
        <div class="chips" id="chips">
          <span class="chip" onclick="useChip(this)">🏙️ İstanbul'da 3+1 daire</span>
          <span class="chip" onclick="useChip(this)">🌊 Bodrum'da lüks villa</span>
          <span class="chip" onclick="useChip(this)">💼 Kiralık ofis Levent</span>
          <span class="chip" onclick="useChip(this)">📅 Randevu almak istiyorum</span>
          <span class="chip" onclick="useChip(this)">💰 5M TL bütçem var</span>
        </div>
        <div class="cin">
          <textarea id="user-input" placeholder="Bir şey yazın... örn: deniz manzaralı 3+1 arıyorum" rows="1"></textarea>
          <button id="sbtn" onclick="sendMessage()" title="Gönder"><i class="fas fa-paper-plane"></i></button>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- MODAL -->
<div class="modal-overlay" id="modal-overlay" onclick="closeModal(event)">
  <div class="modal" id="modal">
    <button class="mclose" onclick="closeModalBtn()"><i class="fas fa-times"></i></button>
    <img class="modal-img" id="m-img" src="" alt=""/>
    <div class="modal-body">
      <div class="modal-price" id="m-price"></div>
      <div class="modal-title" id="m-title"></div>
      <div class="modal-specs" id="m-specs"></div>
      <div class="modal-desc" id="m-desc"></div>
      <div class="modal-tags" id="m-tags"></div>
      <div class="modal-footer">
        <button class="mbtn mbtn-primary" id="m-chat-btn"><i class="fas fa-robot"></i> AI'ya Sor</button>
        <button class="mbtn mbtn-secondary" onclick="closeModalBtn()"><i class="fas fa-times"></i> Kapat</button>
      </div>
    </div>
  </div>
</div>

<!-- FOOTER -->
<footer id="iletisim">
  <div class="container">
    <div class="footer-grid">
      <div class="fbrand">
        <div class="nav-logo"><i class="fas fa-building"></i> <span class="logo-text">Emlak AI</span></div>
        <p>Yapay zeka destekli gayrimenkul platformu. GPT-4o ve Pinecone teknolojisiyle hayalinizdeki mülkü bulun.</p>
      </div>
      <div class="fcol">
        <h4>Hızlı Bağlantı</h4>
        <a href="#ozellikler">Özellikler</a>
        <a href="#ilanlar">İlanlar</a>
        <a href="#asistan">AI Asistan</a>
      </div>
      <div class="fcol">
        <h4>Lokasyonlar</h4>
        <a href="#">İstanbul</a>
        <a href="#">Bodrum</a>
        <a href="#">İzmir</a>
        <a href="#">Antalya</a>
        <a href="#">Ankara</a>
      </div>
      <div class="fcol">
        <h4>İletişim</h4>
        <a href="#"><i class="fas fa-envelope" style="margin-right:6px;color:var(--accent)"></i> info@emlakAI.com</a>
        <a href="#"><i class="fas fa-phone" style="margin-right:6px;color:var(--accent)"></i> +90 212 000 00 00</a>
        <a href="#"><i class="fab fa-whatsapp" style="margin-right:6px;color:var(--accent)"></i> WhatsApp</a>
      </div>
    </div>
    <div class="fbot">
      <p>© 2026 Emlak AI — Tüm hakları saklıdır. Antigravity altyapısı ile güçlendirilmiştir.</p>
      <p style="color:var(--accent)">GPT-4o + Pinecone + FastAPI</p>
    </div>
  </div>
</footer>
""")
print("Part 4 done")
