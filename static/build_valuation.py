import os

html_code = """
<section id="valuation" style="padding: 80px 40px; background: var(--surface); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); text-align: center;">
    <div style="max-width: 800px; margin: 0 auto;">
        <span class="hero-badge" style="margin-bottom: 16px;"><div class="dot"></div> Ücretsiz Değerleme Aracı</span>
        <h2 style="font-size: 36px; margin-bottom: 16px;">Evinizin Değerini Yapay Zeka İle Öğrenin</h2>
        <p style="color: var(--text-muted); margin-bottom: 40px; font-size: 16px;">Evinizin temel özelliklerini girin, piyasa verilerine dayalı tahmini değerini saniyeler içinde ücretsiz öğrenin. Sizi en doğru fiyatla alıcılarla buluşturalım.</p>
        
        <div style="background: var(--bg); padding: 32px; border-radius: 16px; border: 1px solid var(--border); text-align: left;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                <div>
                    <label style="display: block; margin-bottom: 8px; color: var(--text-muted); font-size: 14px;">Şehir</label>
                    <input type="text" id="val-city" placeholder="Örn: İstanbul" style="width: 100%; padding: 12px 16px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: white;">
                </div>
                <div>
                    <label style="display: block; margin-bottom: 8px; color: var(--text-muted); font-size: 14px;">İlçe / Semt</label>
                    <input type="text" id="val-district" placeholder="Örn: Kadıköy" style="width: 100%; padding: 12px 16px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: white;">
                </div>
                <div>
                    <label style="display: block; margin-bottom: 8px; color: var(--text-muted); font-size: 14px;">Oda Sayısı</label>
                    <input type="text" id="val-rooms" placeholder="Örn: 3+1" style="width: 100%; padding: 12px 16px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: white;">
                </div>
                <div>
                    <label style="display: block; margin-bottom: 8px; color: var(--text-muted); font-size: 14px;">Metrekare (m²)</label>
                    <input type="number" id="val-m2" placeholder="Örn: 120" style="width: 100%; padding: 12px 16px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: white;">
                </div>
            </div>
            <div style="margin-bottom: 24px;">
                <label style="display: block; margin-bottom: 8px; color: var(--text-muted); font-size: 14px;">Telefon Numaranız (Sonucu iletmek için)</label>
                <input type="text" id="val-phone" placeholder="Örn: 0555 123 45 67" style="width: 100%; padding: 12px 16px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: white;">
            </div>
            
            <button onclick="getValuation()" id="val-btn" style="width: 100%; background: var(--accent); color: black; font-weight: 700; border: none; padding: 16px; border-radius: 8px; font-size: 16px; cursor: pointer; transition: 0.2s;">
                <i class="fa-solid fa-calculator" style="margin-right: 8px;"></i> Değerlemeyi Hesapla
            </button>
            
            <div id="val-result" style="display: none; margin-top: 24px; padding: 24px; background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); border-radius: 8px; text-align: center;">
                <p style="color: #4ade80; font-weight: 600; margin-bottom: 8px;">Tahmini Piyasa Değeri</p>
                <h3 id="val-price-range" style="font-size: 28px; color: white;">...</h3>
                <p style="color: var(--text-muted); font-size: 13px; margin-top: 12px;">Bir uzmanımız detaylı analiz için sizi en kısa sürede arayacaktır.</p>
            </div>
        </div>
    </div>
</section>

<script>
async function getValuation() {
    const city = document.getElementById('val-city').value;
    const district = document.getElementById('val-district').value;
    const rooms = document.getElementById('val-rooms').value;
    const m2 = document.getElementById('val-m2').value;
    const phone = document.getElementById('val-phone').value;
    
    if(!city || !district || !rooms || !m2 || !phone) {
        alert("Lütfen tüm alanları doldurun.");
        return;
    }
    
    const btn = document.getElementById('val-btn');
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Hesaplanıyor...';
    btn.disabled = true;
    
    try {
        const res = await fetch('/api/valuation', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ city, district, rooms, m2: parseInt(m2), phone })
        });
        const data = await res.json();
        
        if(data.status === 'success') {
            document.getElementById('val-price-range').innerText = data.min_price + " - " + data.max_price;
            document.getElementById('val-result').style.display = 'block';
        }
    } catch (e) {
        alert("Hesaplama sırasında bir hata oluştu.");
    }
    
    btn.innerHTML = '<i class="fa-solid fa-check"></i> Hesaplandı';
}
</script>
"""

with open("static/index.html", "a", encoding="utf-8") as f:
    f.write(html_code)

print("build_valuation.py çalıştı, değerleme aracı eklendi.")
