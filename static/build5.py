
import os
p = os.path.join(os.path.dirname(__file__), 'index.html')
with open(p, 'a', encoding='utf-8') as f:
    f.write("""
<div class="modal-overlay" id="demo-modal" onclick="if(event.target.id==='demo-modal') this.classList.remove('open')">
  <div class="modal" style="max-width: 500px; padding: 30px;">
    <button class="mclose" onclick="document.getElementById('demo-modal').classList.remove('open')"><i class="fas fa-times"></i></button>
    <div style="text-align:center; margin-bottom: 24px;">
      <i class="fas fa-rocket" style="font-size: 40px; color: var(--accent); margin-bottom: 16px;"></i>
      <h2 style="font-size: 24px; margin-bottom: 8px;">Demo Talep Et</h2>
      <p style="color: var(--text-muted); font-size: 14px;">Emlak ofisinize özel yapay zeka asistanını ücretsiz deneyin.</p>
    </div>
    
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <div>
        <label style="font-size: 13px; color: var(--text-muted); margin-bottom: 6px; display: block;">Ad Soyad</label>
        <input type="text" id="demo-name" style="width: 100%; padding: 12px; background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; color: white;" placeholder="Örn: Ahmet Yılmaz">
      </div>
      <div>
        <label style="font-size: 13px; color: var(--text-muted); margin-bottom: 6px; display: block;">Emlak Ofisi Adı</label>
        <input type="text" id="demo-agency" style="width: 100%; padding: 12px; background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; color: white;" placeholder="Örn: Yılmaz Emlak">
      </div>
      <div>
        <label style="font-size: 13px; color: var(--text-muted); margin-bottom: 6px; display: block;">E-posta Adresi</label>
        <input type="email" id="demo-email" style="width: 100%; padding: 12px; background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; color: white;" placeholder="Örn: ahmet@ajans.com">
      </div>
      <button onclick="submitDemo()" id="demo-btn" style="width: 100%; padding: 14px; background: var(--accent); color: black; border: none; border-radius: 8px; font-weight: 700; font-size: 15px; margin-top: 10px; cursor: pointer; transition: 0.2s;">
        <i class="fas fa-paper-plane"></i> Talebi Gönder
      </button>
      <div id="demo-result" style="display: none; text-align: center; color: #4ade80; font-weight: 600; font-size: 14px; margin-top: 10px;"></div>
    </div>
  </div>
</div>

<script>
async function submitDemo() {
    const name = document.getElementById('demo-name').value;
    const agency = document.getElementById('demo-agency').value;
    const email = document.getElementById('demo-email').value;
    if(!name || !email) return alert('Lütfen zorunlu alanları doldurun.');
    
    document.getElementById('demo-btn').innerHTML = '<i class="fas fa-spinner fa-spin"></i> Gönderiliyor...';
    
    try {
        await fetch('/api/request-demo', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ name, agency, email })
        });
        document.getElementById('demo-btn').style.display = 'none';
        document.getElementById('demo-result').innerHTML = '<i class="fas fa-check-circle"></i> Talebiniz alındı! Sizi en kısa sürede arayacağız.';
        document.getElementById('demo-result').style.display = 'block';
    } catch(e) {
        alert('Hata oluştu!');
        document.getElementById('demo-btn').innerHTML = '<i class="fas fa-paper-plane"></i> Talebi Gönder';
    }
}
// Zaman
function now(){return new Date().toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})}
document.getElementById('bot-time').textContent = now();

const chatBox = document.getElementById('chat-box');
const inputEl = document.getElementById('user-input');
const sbtn    = document.getElementById('sbtn');
const API_URL = '/chat';
const SID     = 'user-' + Math.random().toString(36).slice(2,9);

function addMsg(role, text){
  const d = document.createElement('div');
  d.className = 'msg ' + role;
  const av = document.createElement('div'); av.className='mav';
  av.textContent = role==='user' ? '👤' : '🤖';
  const b = document.createElement('div'); b.className='bbl';
  b.innerHTML = text.replace(/\\n/g,'<br>') + '<div class="tm">' + now() + '</div>';
  d.appendChild(av); d.appendChild(b);
  chatBox.appendChild(d);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function showTyping(){
  const d = document.createElement('div');
  d.className='msg bot'; d.id='typing';
  d.innerHTML='<div class="mav">🤖</div><div class="bbl typing"><span></span><span></span><span></span></div>';
  chatBox.appendChild(d); chatBox.scrollTop=chatBox.scrollHeight;
}
function hideTyping(){ const t=document.getElementById('typing'); if(t) t.remove(); }

async function sendMessage(){
  const txt = inputEl.value.trim(); if(!txt) return;
  document.getElementById('chips').style.display='none';
  addMsg('user', txt);
  inputEl.value=''; inputEl.style.height='auto';
  sbtn.disabled=true; showTyping();
  try{
    const r = await fetch(API_URL,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({user_id:SID,message:txt})});
    const data = await r.json();
    hideTyping(); addMsg('bot', data.response||'Bir hata oluştu.');
  }catch(e){
    hideTyping(); addMsg('bot','⚠️ Sunucuya bağlanılamadı.\\n\\nAPI sunucusunu başlatın:\\n`python -m uvicorn api.main:app --reload`');
  }finally{ sbtn.disabled=false; }
}

function useChip(el){
  inputEl.value = el.textContent.replace(/^.{2}/,'').trim();
  sendMessage();
}

inputEl.addEventListener('keydown', e=>{
  if(e.key==='Enter' && !e.shiftKey){ e.preventDefault(); sendMessage(); }
});
inputEl.addEventListener('input', ()=>{
  inputEl.style.height='auto';
  inputEl.style.height = Math.min(inputEl.scrollHeight,110)+'px';
});

// FILTER
function filterCards(tip, btn){
  document.querySelectorAll('.ftab').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  const cards = document.querySelectorAll('.card');
  let count=0;
  cards.forEach(c=>{
    const show = tip==='Tümü' || c.dataset.tip===tip;
    c.style.display = show ? '' : 'none';
    if(show) count++;
  });
  document.getElementById('count-lbl').textContent = count + ' ilan gösteriliyor';
}

// MODAL
function fmtPrice(l){
  const p = l.fiyat_tl;
  if(p>=1000000) return (p/1000000).toFixed(1)+'M ₺';
  if(p>=1000) return Math.floor(p/1000)+'K ₺';
  return p.toLocaleString('tr-TR')+' ₺';
}

function openModal(l){
  const suf = l.durum==='Kiralık' ? '/ay' : '';
  document.getElementById('m-img').src = l.foto_url || '';
  document.getElementById('m-img').alt = l.baslik;
  document.getElementById('m-price').textContent = fmtPrice(l) + suf;
  document.getElementById('m-title').textContent = l.baslik;
  document.getElementById('m-desc').textContent = l.aciklama;

  document.getElementById('m-specs').innerHTML =
    '<div class="mspec"><span>Tip</span><span>'+l.tip+'</span></div>' +
    '<div class="mspec"><span>Durum</span><span>'+l.durum+'</span></div>' +
    '<div class="mspec"><span>Net m²</span><span>'+l.net_m2+' m²</span></div>' +
    '<div class="mspec"><span>Brüt m²</span><span>'+l.brut_m2+' m²</span></div>' +
    '<div class="mspec"><span>Oda</span><span>'+l.oda_sayisi+'</span></div>' +
    '<div class="mspec"><span>Kat</span><span>'+l.kat+'</span></div>' +
    '<div class="mspec"><span>Bina Yaşı</span><span>'+l.bina_yasi+' yıl</span></div>' +
    '<div class="mspec"><span>İlçe</span><span>'+l.ilce+', '+l.il+'</span></div>';

  document.getElementById('m-tags').innerHTML =
    l.ozellikler.map(t=>'<span class="mtag"><i class="fas fa-check"></i>'+t+'</span>').join('');

  document.getElementById('m-chat-btn').onclick = ()=>{
    closeModalBtn();
    inputEl.value = l.baslik + ' hakkında bilgi almak istiyorum';
    document.getElementById('asistan').scrollIntoView({behavior:'smooth'});
    setTimeout(sendMessage, 600);
  };

  document.getElementById('modal-overlay').classList.add('open');
  document.body.style.overflow='hidden';
}

function closeModal(e){ if(e.target.id==='modal-overlay') closeModalBtn(); }
function closeModalBtn(){ document.getElementById('modal-overlay').classList.remove('open'); document.body.style.overflow=''; }
document.addEventListener('keydown', e=>{ if(e.key==='Escape') closeModalBtn(); });

// Scroll reveal
const observer = new IntersectionObserver(entries=>{
  entries.forEach(e=>{ if(e.isIntersecting) e.target.style.opacity='1'; });
},{threshold:0.1});
document.querySelectorAll('.fc,.card').forEach(el=>{
  el.style.opacity='0';
  el.style.transition='opacity .5s ease, transform .3s ease';
  observer.observe(el);
});
</script>
</body>
</html>
""")
print("Part 5 done — Build complete!")
