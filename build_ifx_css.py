CSS = r'''
:root{
  --ink:#14213d; --ink-soft:#3d6080; --muted:#68788f;
  --ground:#fafbfc; --card:#ffffff; --line:#dde3ec; --tint:#eef3f8;
  --accent:#00aeef; --accent-ink:#0079a8; --navy:#0f1f44; --navy-text:#ffffff;
  --pass:#1e7a45; --pass-tint:#e4f6ea; --pass-edge:#8ccaa6;
  --fail:#9a3f36; --fail-tint:#fbeae7; --fail-edge:#d4a49d;
  --warn:#b45309; --warn-tint:#fdf3e3; --warn-edge:#e0b877;
  --chip:#e7f6fd;
  --f-disp:"Montserrat",system-ui,sans-serif;
  --f-body:"Open Sans",system-ui,sans-serif;
  --f-mono:ui-monospace,"SFMono-Regular",Menlo,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ink:#e8edf5; --ink-soft:#9fb4cc; --muted:#8496ad;
  --ground:#0d1830; --card:#152342; --line:#2a3a5c; --tint:#1a2a4d;
  --accent:#3cc5f5; --accent-ink:#5fd0f7; --navy:#0a142e; --navy-text:#e8edf5;
  --pass:#5fc98a; --pass-tint:#12301e; --pass-edge:#2f6344;
  --fail:#e39288; --fail-tint:#2e1815; --fail-edge:#6d3a33;
  --warn:#e8a24b; --warn-tint:#3a2c12; --warn-edge:#7a5c22;
  --chip:#123a52;
}}
:root[data-theme="dark"]{
  --ink:#e8edf5; --ink-soft:#9fb4cc; --muted:#8496ad;
  --ground:#0d1830; --card:#152342; --line:#2a3a5c; --tint:#1a2a4d;
  --accent:#3cc5f5; --accent-ink:#5fd0f7; --navy:#0a142e; --navy-text:#e8edf5;
  --pass:#5fc98a; --pass-tint:#12301e; --pass-edge:#2f6344;
  --fail:#e39288; --fail-tint:#2e1815; --fail-edge:#6d3a33;
  --warn:#e8a24b; --warn-tint:#3a2c12; --warn-edge:#7a5c22;
  --chip:#123a52;
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
body{background:var(--ground);color:var(--ink);font:16px/1.65 var(--f-body);margin:0}
.wrap{max-width:880px;margin:0 auto;padding:0 22px}
h1,h2,h3,h4{font-family:var(--f-disp);text-wrap:balance;line-height:1.2;margin:0}
h1{font-size:2.1rem;font-weight:800;letter-spacing:-.02em}
h2{font-size:1.45rem;font-weight:700;margin:0 0 .5rem}
h3{font-size:1.05rem;font-weight:700}
p{margin:.55rem 0;max-width:68ch}
a{color:var(--accent-ink)}
strong{font-weight:700}
code{font-family:var(--f-mono);font-size:.85em;background:var(--tint);padding:1px 5px;
  border-radius:3px;border:1px solid var(--line)}
.eyebrow{font-family:var(--f-disp);font-weight:700;font-size:.7rem;letter-spacing:.18em;
  color:var(--accent);text-transform:uppercase;margin:0 0 .6rem}

/* ── hero with live progress ─────────────────────────────────────────────── */
header.hero{background:var(--navy);color:var(--navy-text);padding:38px 0 30px;
  border-bottom:4px solid var(--accent)}
header.hero .eyebrow{color:#7fd6f5}
header.hero p.stand{color:#c3d3e8;font-size:1.05rem;margin-top:.6rem}
.prog{margin:26px 0 0;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);
  border-radius:8px;padding:16px 18px}
.prog .top{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
.prog .lbl{font-family:var(--f-disp);font-weight:700;font-size:.72rem;letter-spacing:.14em;
  text-transform:uppercase;color:#8fd9f7}
.prog .count{font-family:var(--f-disp);font-weight:800;font-size:1.5rem;
  font-variant-numeric:tabular-nums}
.prog .bar{height:9px;background:rgba(255,255,255,.14);border-radius:99px;margin:12px 0 10px;
  overflow:hidden}
.prog .bar i{display:block;height:100%;background:var(--accent);border-radius:99px;
  transition:width .35s ease;width:0}
.prog .row{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:.86rem;color:#c3d3e8}
.prog input{width:64px;font:inherit;font-family:var(--f-mono);padding:4px 7px;border-radius:5px;
  border:1px solid rgba(255,255,255,.25);background:rgba(0,0,0,.2);color:#fff;text-align:center}
.prog button{font:inherit;font-family:var(--f-disp);font-weight:700;font-size:.82rem;cursor:pointer;
  border-radius:6px;padding:6px 13px;border:1px solid var(--accent);background:var(--accent);
  color:#05263a}
.prog button.ghost{background:transparent;color:#8fd9f7}
.prog button:hover{filter:brightness(1.08)}
.prog button:focus-visible,.prog input:focus-visible{outline:2px solid #fff;outline-offset:2px}

/* ── nav ─────────────────────────────────────────────────────────────────── */
nav.jump{background:var(--card);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:20}
nav.jump .wrap{display:flex;gap:6px;flex-wrap:wrap;padding:10px 22px}
nav.jump a{font-family:var(--f-disp);font-weight:600;font-size:.8rem;text-decoration:none;
  color:var(--ink-soft);background:var(--tint);border:1px solid var(--line);
  padding:5px 11px;border-radius:99px}
nav.jump a:hover{background:var(--chip);color:var(--accent-ink);border-color:var(--accent)}
nav.jump a:focus-visible{outline:2px solid var(--accent);outline-offset:1px}

main{padding:34px 0 90px}
section{margin:0 0 52px;scroll-margin-top:64px}
.dek{color:var(--ink-soft);max-width:66ch;margin:0 0 18px}

/* ── click-path steps ────────────────────────────────────────────────────── */
.steps{list-style:none;margin:0;padding:0;counter-reset:s}
.steps > li{counter-increment:s;background:var(--card);border:1px solid var(--line);
  border-radius:9px;margin-bottom:10px;overflow:hidden}
.steps > li.done{border-color:var(--pass-edge)}
.steps .head{display:flex;gap:13px;align-items:flex-start;padding:15px 17px;cursor:pointer;
  user-select:none}
.steps .head:hover{background:var(--tint)}
.steps .num{flex:0 0 27px;height:27px;border-radius:50%;background:var(--chip);
  color:var(--accent-ink);font-family:var(--f-disp);font-weight:800;font-size:.85rem;
  display:grid;place-items:center}
.steps li.done .num{background:var(--pass);color:#fff}
.steps li.done .num::after{content:"✓"}
.steps li.done .num span{display:none}
.steps .ttl{flex:1 1 auto}
.steps .ttl b{font-family:var(--f-disp);font-size:1.02rem;display:block}
.steps .ttl em{font-style:normal;color:var(--muted);font-size:.88rem}
.steps .tick{flex:0 0 auto;font-size:.75rem;font-family:var(--f-disp);font-weight:700;
  color:var(--muted);letter-spacing:.08em;text-transform:uppercase;padding-top:5px}
/* Without an affordance nobody discovers these open -- the audience has never used the app. */
.steps .chev{flex:0 0 auto;color:var(--accent);font-size:1.15rem;line-height:1;padding-top:4px;
  transition:transform .18s ease}
.steps li.open .chev{transform:rotate(90deg)}
.steps .head:hover .chev{color:var(--accent-ink)}
.steps li.done .tick{color:var(--pass)}
.steps .body{padding:0 17px 17px 57px;display:none}
.steps li.open .body{display:block}
.steps .body p{margin:.4rem 0}
.steps .body ul{margin:.4rem 0 .6rem;padding-left:20px}
.steps .body li{margin-bottom:4px}

/* click path breadcrumb */
.path{display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin:.6rem 0 .8rem;
  font-family:var(--f-mono);font-size:.82rem}
.path span{background:var(--navy);color:#fff;padding:3px 9px;border-radius:5px;white-space:nowrap}
.path i{color:var(--muted);font-style:normal}
.path span.btn{background:var(--accent);color:#05263a;font-weight:600}

/* ── stage explorer ─────────────────────────────────────────────────────── */
.stagepick{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 16px}
.stagepick button{font:inherit;font-family:var(--f-disp);font-weight:600;font-size:.84rem;
  cursor:pointer;background:var(--card);color:var(--ink-soft);border:1px solid var(--line);
  padding:8px 13px;border-radius:7px}
.stagepick button[aria-pressed="true"]{background:var(--navy);color:#fff;border-color:var(--navy)}
.stagepick button:hover{border-color:var(--accent)}
.stagepick button:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.stagebox{background:var(--card);border:1px solid var(--line);border-radius:9px;overflow:hidden}
.stagebox .sb-head{padding:15px 18px;background:var(--tint);border-bottom:1px solid var(--line)}
.stagebox .sb-head h3{margin:0}
.stagebox .sb-head p{margin:.3rem 0 0;font-size:.9rem;color:var(--ink-soft)}
.stagebox .sb-body{padding:16px 18px}
.req{list-style:none;margin:0;padding:0}
.req li{padding:11px 0;border-bottom:1px solid var(--line)}
.req li:last-child{border-bottom:none}
.req .f{font-family:var(--f-disp);font-weight:700;font-size:.96rem}
.req .w{display:block;color:var(--ink-soft);font-size:.9rem;margin-top:2px}
.opts{display:flex;gap:5px;flex-wrap:wrap;margin-top:7px}
.opt{font-family:var(--f-mono);font-size:.76rem;padding:3px 8px;border-radius:4px;border:1px solid}
.opt.y{background:var(--pass-tint);color:var(--pass);border-color:var(--pass-edge);font-weight:600}
.opt.n{background:var(--ground);color:var(--muted);border-color:var(--line)}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:.85rem;color:var(--ink-soft);
  margin:0 0 14px;align-items:center}
.legend span{display:inline-flex;gap:6px;align-items:center}

/* ── callouts ───────────────────────────────────────────────────────────── */
.note{border-left:4px solid var(--accent);background:var(--card);border-top:1px solid var(--line);
  border-right:1px solid var(--line);border-bottom:1px solid var(--line);
  padding:14px 17px;border-radius:0 8px 8px 0;margin:0 0 16px}
.note.warn{border-left-color:var(--warn-edge);background:var(--warn-tint)}
.note.stop{border-left-color:var(--fail-edge);background:var(--fail-tint)}
.note > :last-child{margin-bottom:0}
.note .tag{display:block;font-family:var(--f-disp);font-weight:700;font-size:.68rem;
  letter-spacing:.14em;text-transform:uppercase;color:var(--accent-ink);margin-bottom:5px}
.note.warn .tag{color:var(--warn)}
.note.stop .tag{color:var(--fail)}

/* ── error decoder ──────────────────────────────────────────────────────── */
.errs{display:grid;gap:10px}
.err{background:var(--card);border:1px solid var(--line);border-radius:9px;padding:14px 17px}
.err .msg{font-family:var(--f-mono);font-size:.84rem;background:var(--fail-tint);
  color:var(--fail);padding:8px 11px;border-radius:6px;border:1px solid var(--fail-edge);
  margin-bottom:9px}
.err p{margin:0;font-size:.94rem}

/* ── screenshots ────────────────────────────────────────────────────────── */
figure{margin:14px 0;background:var(--card);border:1px solid var(--line);border-radius:9px;
  overflow:hidden}
figure img{display:block;width:100%;height:auto}
figcaption{padding:9px 14px;font-size:.85rem;color:var(--muted);border-top:1px solid var(--line)}

/* ── tracker ────────────────────────────────────────────────────────────── */
.deals{margin:0 0 14px}
.deal{display:flex;gap:11px;align-items:center;background:var(--card);border:1px solid var(--line);
  border-radius:8px;padding:10px 13px;margin-bottom:7px}
.deal.done{border-color:var(--pass-edge);background:var(--pass-tint)}
.deal input[type=checkbox]{width:19px;height:19px;accent-color:var(--pass);flex:0 0 auto;cursor:pointer}
.deal input[type=text]{flex:1 1 auto;font:inherit;font-size:.94rem;border:none;background:none;
  color:var(--ink);padding:2px 0}
.deal input[type=text]:focus-visible{outline:none;border-bottom:1px solid var(--accent)}
.deal.done input[type=text]{text-decoration:line-through;color:var(--muted)}
.deal button{font:inherit;background:none;border:none;color:var(--muted);cursor:pointer;
  font-size:1.1rem;line-height:1;padding:0 4px}
.deal button:hover{color:var(--fail)}
.addrow{display:flex;gap:8px;flex-wrap:wrap}
.addrow input{flex:1 1 220px;font:inherit;padding:9px 12px;border-radius:7px;
  border:1px solid var(--line);background:var(--card);color:var(--ink)}
.addrow button{font:inherit;font-family:var(--f-disp);font-weight:700;cursor:pointer;
  border-radius:7px;padding:9px 16px;border:1px solid var(--accent);background:var(--accent);
  color:#05263a}
.addrow input:focus-visible,.addrow button:focus-visible{outline:2px solid var(--accent);
  outline-offset:1px}
.empty{color:var(--muted);font-size:.92rem;font-style:italic;margin:.4rem 0 .8rem}

footer{border-top:1px solid var(--line);background:var(--card)}
footer .wrap{padding:22px 22px 56px;color:var(--muted);font-size:.86rem}
'''
