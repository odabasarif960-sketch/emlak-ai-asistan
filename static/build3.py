
import os, json

p = os.path.join(os.path.dirname(__file__), 'index.html')
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_listings.json')
listings = json.load(open(data_path, encoding='utf-8'))

def fmt_price(listing):
    p = listing['fiyat_tl']
    durum = listing['durum']
    if p >= 1_000_000:
        return f"{p/1_000_000:.1f}M ₺"
    elif p >= 1000:
        return f"{p//1000}K ₺"
    return f"{p:,} ₺"

def card_html(l):
    badge_cls = "badge-s" if l["durum"] == "Satılık" else "badge-k"
    tags = "".join(f'<span class="tag">{t}</span>' for t in l["ozellikler"][:3])
    foto = l.get("foto_url", "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800")
    price = fmt_price(l)
    suffix = "/ay" if l["durum"] == "Kiralık" else ""
    data = json.dumps(l, ensure_ascii=False).replace('"', '&quot;')
    return f"""
<div class="card" data-tip="{l['tip']}" onclick='openModal({data})'>
  <div class="card-img">
    <img src="{foto}" alt="{l['baslik']}" loading="lazy"/>
    <span class="badge {badge_cls}">{l['durum']}</span>
    <button class="fav-btn" onclick="event.stopPropagation();this.style.background='var(--red)';this.innerHTML='<i class=\\'fas fa-heart\\'></i>'">
      <i class="far fa-heart"></i>
    </button>
  </div>
  <div class="card-body">
    <div class="card-price">{price}{suffix}</div>
    <div class="card-title">{l['baslik']}</div>
    <div class="card-loc"><i class="fas fa-location-dot"></i> {l['ilce']}, {l['il']}</div>
    <div class="card-specs">
      <span class="spec"><i class="fas fa-expand"></i> {l['net_m2']} m²</span>
      <span class="spec"><i class="fas fa-door-open"></i> {l['oda_sayisi']}</span>
      <span class="spec"><i class="fas fa-building"></i> Kat {l['kat']}</span>
      <span class="spec"><i class="fas fa-calendar"></i> {l['bina_yasi']} yıl</span>
    </div>
    <div class="card-tags">{tags}</div>
  </div>
</div>"""

cards_html = "\n".join(card_html(l) for l in listings)

with open(p, 'a', encoding='utf-8') as f:
    f.write(f"""
<!-- LISTINGS -->
<section id="ilanlar">
  <div class="container">
    <div class="listings-header">
      <div>
        <div class="section-tag">Örnek Demo</div>
        <h2 class="section-title">Sizin <span class="gold">İlanlarınız</span></h2>
        <p class="section-sub">Mevcut sisteminize veya CRM'inize entegre olduğunda ilanlarınız sistemde bu şekilde sergilenir.</p>
        <div class="filter-row">
          <button class="ftab active" onclick="filterCards('Tümü',this)">Tümü</button>
          <button class="ftab" onclick="filterCards('Daire',this)">Daire</button>
          <button class="ftab" onclick="filterCards('Villa',this)">Villa</button>
          <button class="ftab" onclick="filterCards('Ofis',this)">Ofis</button>
          <button class="ftab" onclick="filterCards('Müstakil Ev',this)">Müstakil</button>
          <button class="ftab" onclick="filterCards('Çiftlik Evi',this)">Çiftlik</button>
        </div>
      </div>
      <div style="font-size:13px;color:var(--text2)"><i class="fas fa-filter" style="color:var(--accent);margin-right:5px"></i><span id="count-lbl">22 ilan gösteriliyor</span></div>
    </div>
    <div class="grid" id="listings-grid">
      {cards_html}
    </div>
  </div>
</section>
""")
print("Part 3 done")
