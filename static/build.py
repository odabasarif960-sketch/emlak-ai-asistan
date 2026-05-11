
import os
p = os.path.join(os.path.dirname(__file__), 'index.html')
with open(p, 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Emlak AI — Emlak Ofisleri İçin Yapay Zeka</title>
<meta name="description" content="Emlak ofisleri için 7/24 çalışan, ilan sunan ve randevu alan AI asistan altyapısı."/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#080c14;--surface:#0f1623;--surface2:#17202e;--surface3:#1e2a3a;
  --border:rgba(255,255,255,0.06);--border2:rgba(255,255,255,0.1);
  --accent:#f59e0b;--accent2:#fbbf24;--accent3:#fde68a;
  --blue:#3b82f6;--text:#f1f5f9;--text2:#94a3b8;--text3:#64748b;
  --green:#22c55e;--red:#ef4444;
  --radius:16px;--radius2:12px;--radius3:8px;
  --shadow:0 25px 50px rgba(0,0,0,0.5);
  --glow:0 0 40px rgba(245,158,11,0.15);
}
html{scroll-behavior:smooth}
body{font-family:"Inter",sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden}
a{text-decoration:none;color:inherit}
button{cursor:pointer;font-family:inherit}
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:var(--surface)}
::-webkit-scrollbar-thumb{background:var(--surface3);border-radius:4px}
nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:16px 40px;display:flex;align-items:center;justify-content:space-between;background:rgba(8,12,20,0.88);backdrop-filter:blur(20px);border-bottom:1px solid var(--border)}
.nav-logo{display:flex;align-items:center;gap:10px;font-size:20px;font-weight:700}
.nav-logo .logo-text{background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nav-logo i{color:var(--accent);font-size:22px}
.nav-links{display:flex;align-items:center;gap:32px}
.nav-links a{font-size:14px;color:var(--text2);transition:.2s}
.nav-links a:hover{color:var(--text)}
.nav-cta{padding:10px 22px;border-radius:8px;background:var(--accent);color:#000;font-weight:600;font-size:14px;transition:.2s;border:none}
.nav-cta:hover{background:var(--accent2);transform:translateY(-1px)}
.hero{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:120px 40px 80px;text-align:center;position:relative;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 80% 50% at 50% 0%,rgba(245,158,11,0.08),transparent 60%)}
.hero::after{content:"";position:absolute;bottom:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent)}
.hero-badge{display:inline-flex;align-items:center;gap:8px;padding:8px 18px;border-radius:100px;border:1px solid rgba(245,158,11,0.3);background:rgba(245,158,11,0.08);font-size:13px;color:var(--accent2);margin-bottom:28px;animation:fadeUp .6s ease}
.hero-badge .dot{width:6px;height:6px;background:var(--green);border-radius:50%;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
.hero h1{font-size:clamp(38px,6vw,74px);font-weight:800;line-height:1.08;letter-spacing:-2.5px;max-width:900px;margin-bottom:22px;animation:fadeUp .7s ease .1s both}
.gold{background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent3));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{font-size:18px;color:var(--text2);max-width:580px;line-height:1.7;margin-bottom:40px;animation:fadeUp .7s ease .2s both}
.hero-btns{display:flex;gap:16px;flex-wrap:wrap;justify-content:center;animation:fadeUp .7s ease .3s both}
.btn-primary{padding:16px 32px;border-radius:12px;background:var(--accent);color:#000;font-weight:700;font-size:15px;border:none;transition:.3s;display:flex;align-items:center;gap:8px}
.btn-primary:hover{background:var(--accent2);transform:translateY(-2px);box-shadow:0 8px 30px rgba(245,158,11,0.4)}
.btn-secondary{padding:16px 32px;border-radius:12px;background:transparent;color:var(--text);font-weight:600;font-size:15px;border:1px solid var(--border2);transition:.3s;display:flex;align-items:center;gap:8px}
.btn-secondary:hover{border-color:var(--accent);color:var(--accent);background:rgba(245,158,11,0.05)}
.stats-bar{display:flex;margin-top:64px;border:1px solid var(--border);border-radius:16px;overflow:hidden;background:var(--surface);animation:fadeUp .7s ease .4s both;max-width:700px;width:100%}
.stat{flex:1;padding:24px 20px;text-align:center;border-right:1px solid var(--border)}
.stat:last-child{border-right:none}
.stat-num{font-size:30px;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stat-lbl{font-size:12px;color:var(--text2);margin-top:4px}
section{padding:100px 40px}
.container{max-width:1200px;margin:0 auto}
.section-tag{display:inline-block;padding:6px 14px;border-radius:100px;background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.2);font-size:12px;color:var(--accent2);font-weight:600;letter-spacing:.5px;text-transform:uppercase;margin-bottom:16px}
.section-title{font-size:clamp(28px,4vw,46px);font-weight:800;letter-spacing:-1px;margin-bottom:14px}
.section-sub{font-size:17px;color:var(--text2);max-width:540px;line-height:1.6}
.features-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px;margin-top:56px}
.fc{padding:30px;border-radius:16px;border:1px solid var(--border);background:var(--surface);transition:.3s;position:relative;overflow:hidden}
.fc::before{content:"";position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--accent),var(--accent2));opacity:0;transition:.3s}
.fc:hover{border-color:rgba(245,158,11,0.2);transform:translateY(-4px);box-shadow:var(--glow)}
.fc:hover::before{opacity:1}
.fc-icon{width:50px;height:50px;border-radius:12px;background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.2);display:flex;align-items:center;justify-content:center;font-size:20px;color:var(--accent);margin-bottom:18px}
.fc h3{font-size:17px;font-weight:700;margin-bottom:8px}
.fc p{font-size:13px;color:var(--text2);line-height:1.6}
#ilanlar{background:linear-gradient(180deg,var(--bg) 0%,rgba(15,22,35,0.5) 100%)}
.listings-header{display:flex;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;gap:20px;margin-bottom:40px}
.filter-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.ftab{padding:8px 18px;border-radius:100px;border:1px solid var(--border);background:transparent;color:var(--text2);font-size:13px;transition:.2s;font-family:inherit}
.ftab.active,.ftab:hover{border-color:var(--accent);color:var(--accent);background:rgba(245,158,11,0.08)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:24px}
.card{border-radius:16px;border:1px solid var(--border);background:var(--surface);overflow:hidden;transition:.3s;cursor:pointer}
.card:hover{border-color:rgba(245,158,11,0.25);transform:translateY(-6px);box-shadow:0 20px 60px rgba(0,0,0,0.4),var(--glow)}
.card-img{position:relative;height:210px;overflow:hidden}
.card-img img{width:100%;height:100%;object-fit:cover;transition:.5s}
.card:hover .card-img img{transform:scale(1.07)}
.badge{position:absolute;top:12px;left:12px;padding:4px 11px;border-radius:100px;font-size:11px;font-weight:700}
.badge-s{background:rgba(245,158,11,.92);color:#000}
.badge-k{background:rgba(59,130,246,.92);color:#fff}
.fav-btn{position:absolute;top:12px;right:12px;width:34px;height:34px;border-radius:50%;background:rgba(0,0,0,.5);border:none;color:#fff;font-size:14px;display:flex;align-items:center;justify-content:center;transition:.2s;backdrop-filter:blur(4px)}
.fav-btn:hover{background:var(--red);transform:scale(1.12)}
.card-body{padding:18px}
.card-price{font-size:20px;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:5px}
.card-title{font-size:14px;font-weight:600;line-height:1.4;color:var(--text);margin-bottom:7px}
.card-loc{font-size:12px;color:var(--text2);display:flex;align-items:center;gap:4px;margin-bottom:14px}
.card-specs{display:flex;gap:14px;padding-top:14px;border-top:1px solid var(--border)}
.spec{display:flex;align-items:center;gap:4px;font-size:11px;color:var(--text2)}
.spec i{color:var(--text3);font-size:10px}
.card-tags{display:flex;flex-wrap:wrap;gap:5px;margin-top:12px}
.tag{padding:3px 9px;border-radius:100px;background:var(--surface2);border:1px solid var(--border);font-size:10px;color:var(--text3)}
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:200;display:none;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(10px)}
.modal-overlay.open{display:flex}
.modal{background:var(--surface);border:1px solid var(--border2);border-radius:16px;max-width:680px;width:100%;max-height:90vh;overflow-y:auto;animation:fadeUp .3s ease;position:relative}
.modal-img{height:260px;object-fit:cover;width:100%;display:block}
.modal-body{padding:26px}
.modal-price{font-size:26px;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.modal-title{font-size:19px;font-weight:700;margin:6px 0 16px}
.modal-specs{display:flex;gap:20px;flex-wrap:wrap;padding:14px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border);margin-bottom:16px}
.mspec span:first-child{font-size:10px;color:var(--text3);text-transform:uppercase;letter-spacing:.5px;display:block}
.mspec span:last-child{font-size:14px;font-weight:600}
.modal-desc{font-size:13px;color:var(--text2);line-height:1.7;margin-bottom:14px}
.modal-tags{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:20px}
.mtag{padding:4px 11px;border-radius:100px;background:var(--surface2);border:1px solid var(--border);font-size:11px;color:var(--text2)}
.mtag i{color:var(--accent);margin-right:3px}
.modal-footer{display:flex;gap:10px}
.mbtn{flex:1;padding:13px;border-radius:8px;border:none;font-weight:700;font-size:14px;transition:.2s}
.mbtn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000}
.mbtn-primary:hover{transform:translateY(-1px);box-shadow:0 6px 20px rgba(245,158,11,.3)}
.mbtn-secondary{background:var(--surface2);color:var(--text);border:1px solid var(--border2)}
.mbtn-secondary:hover{border-color:var(--accent);color:var(--accent)}
.mclose{position:absolute;top:14px;right:14px;width:34px;height:34px;border-radius:50%;background:rgba(0,0,0,.6);border:none;color:#fff;font-size:14px;display:flex;align-items:center;justify-content:center;cursor:pointer;backdrop-filter:blur(4px);transition:.2s;z-index:1}
.mclose:hover{background:var(--red)}
#asistan{background:var(--bg)}
.chat-layout{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;margin-top:56px}
.chat-info h3{font-size:24px;font-weight:700;margin-bottom:14px}
.chat-info p{color:var(--text2);line-height:1.7;margin-bottom:20px;font-size:15px}
.cfeats{display:flex;flex-direction:column;gap:12px}
.cfeat{display:flex;align-items:center;gap:12px;font-size:14px}
.cfeat i{width:30px;height:30px;border-radius:8px;background:rgba(245,158,11,.1);display:flex;align-items:center;justify-content:center;color:var(--accent);font-size:12px;flex-shrink:0}
.chat-win{border-radius:16px;border:1px solid var(--border);background:var(--surface);overflow:hidden;box-shadow:var(--shadow)}
.chat-head{padding:14px 18px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:12px;background:var(--surface2)}
.ch-av{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:16px;box-shadow:0 0 14px rgba(245,158,11,.3)}
.ch-info h4{font-size:14px;font-weight:600}
.ch-info p{font-size:11px;color:var(--text2);display:flex;align-items:center;gap:4px}
.odot{width:6px;height:6px;background:var(--green);border-radius:50%;animation:pulse 2s infinite}
#chat-box{height:300px;overflow-y:auto;padding:18px;display:flex;flex-direction:column;gap:12px}
.msg{display:flex;gap:8px;animation:fadeUp .3s ease}
.msg.user{flex-direction:row-reverse}
.mav{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0;align-self:flex-end}
.msg.bot .mav{background:var(--surface3)}
.msg.user .mav{background:linear-gradient(135deg,var(--accent),var(--accent2))}
.bbl{max-width:78%;padding:10px 13px;border-radius:13px;font-size:13px;line-height:1.6}
.msg.bot .bbl{background:var(--surface2);border:1px solid var(--border);border-bottom-left-radius:3px}
.msg.user .bbl{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000;border-bottom-right-radius:3px;font-weight:500}
.bbl .tm{font-size:10px;margin-top:4px;opacity:.45}
.typing{display:flex;align-items:center;gap:4px;padding:11px 13px}
.typing span{width:6px;height:6px;background:var(--accent);border-radius:50%;animation:bnc 1.2s infinite}
.typing span:nth-child(2){animation-delay:.2s}
.typing span:nth-child(3){animation-delay:.4s}
@keyframes bnc{0%,80%,100%{transform:translateY(0)}40%{transform:translateY(-7px)}}
.chips{display:flex;flex-wrap:wrap;gap:6px;padding:0 14px 10px}
.chip{padding:5px 12px;border-radius:100px;border:1px solid var(--border);background:var(--surface2);font-size:11px;color:var(--text2);cursor:pointer;transition:.2s}
.chip:hover{border-color:var(--accent);color:var(--accent);background:rgba(245,158,11,.07)}
.cin{padding:12px 14px;border-top:1px solid var(--border);display:flex;gap:8px}
#user-input{flex:1;background:var(--surface2);border:1px solid var(--border);border-radius:9px;padding:9px 13px;font-size:13px;color:var(--text);font-family:inherit;outline:none;resize:none;min-height:40px;max-height:110px;transition:.2s}
#user-input:focus{border-color:var(--accent)}
#user-input::placeholder{color:var(--text3)}
#sbtn{width:40px;height:40px;border-radius:9px;border:none;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000;font-size:15px;display:flex;align-items:center;justify-content:center;transition:.2s;flex-shrink:0}
#sbtn:hover{transform:scale(1.07);box-shadow:0 4px 18px rgba(245,158,11,.4)}
#sbtn:disabled{opacity:.4;cursor:not-allowed;transform:none}
footer{padding:60px 40px 28px;border-top:1px solid var(--border);background:var(--surface)}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:36px;margin-bottom:36px}
.fbrand p{font-size:13px;color:var(--text2);margin-top:10px;line-height:1.7;max-width:280px}
.fcol h4{font-size:13px;font-weight:600;margin-bottom:14px}
.fcol a{display:block;font-size:13px;color:var(--text2);margin-bottom:9px;transition:.2s}
.fcol a:hover{color:var(--accent)}
.fbot{padding-top:22px;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px}
.fbot p{font-size:12px;color:var(--text3)}
.hidden{display:none}
@media(max-width:900px){
  .nav-links{display:none}
  nav{padding:14px 20px}
  section{padding:70px 20px}
  .hero{padding:100px 20px 60px}
  .stats-bar{flex-wrap:wrap}
  .stat{border-right:none;border-bottom:1px solid var(--border)}
  .chat-layout{grid-template-columns:1fr}
  .footer-grid{grid-template-columns:1fr 1fr}
  .grid{grid-template-columns:1fr}
}
/* PRICING */
#fiyatlandirma { background: var(--surface); position: relative; }
.pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 50px; }
.p-card { background: var(--bg); border: 1px solid var(--border); border-radius: 16px; padding: 40px 30px; transition: .3s; position: relative; overflow: hidden; }
.p-card:hover { transform: translateY(-8px); border-color: rgba(245,158,11,.3); box-shadow: var(--shadow); }
.p-card.popular { border-color: var(--accent); background: linear-gradient(180deg, rgba(245,158,11,.05) 0%, var(--bg) 100%); }
.pop-badge { position: absolute; top: 16px; right: 16px; padding: 6px 12px; background: linear-gradient(135deg, var(--accent), var(--accent2)); color: #000; font-size: 11px; font-weight: 700; border-radius: 100px; }
.p-name { font-size: 20px; font-weight: 700; margin-bottom: 12px; }
.p-price { font-size: 38px; font-weight: 800; margin-bottom: 24px; color: var(--text); }
.p-price span { font-size: 14px; font-weight: 500; color: var(--text2); }
.p-features { list-style: none; margin-bottom: 30px; }
.p-features li { display: flex; align-items: flex-start; gap: 10px; font-size: 14px; color: var(--text2); margin-bottom: 12px; line-height: 1.5; }
.p-features li i { color: var(--accent); margin-top: 3px; font-size: 13px; }
.p-btn { width: 100%; padding: 14px; border-radius: 12px; font-weight: 700; font-size: 15px; border: 1px solid var(--border2); background: transparent; color: var(--text); transition: .3s; display: block; text-align: center; }
.p-card.popular .p-btn { background: var(--accent); color: #000; border: none; }
.p-btn:hover { background: var(--accent2); color: #000; border-color: transparent; }
</style>
</head>
""")
print("Part 1 done")
