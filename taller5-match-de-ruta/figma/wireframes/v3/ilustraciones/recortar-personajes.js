const {chromium}=require('playwright');const fs=require('fs');
const src=fs.readFileSync(process.argv[2],'utf8');
const V={n900:'#0a0a0a',n800:'#27272a',n700:'#3f3f46',n0:'#ffffff',p500:'#5b3df5',p700:'#3f22c9',p100:'#eeebfe',lima:'#c8f560',piel2:'#8d5524',piel3:'#e0ac69'};
const DROP=['#ff6584','#f2f2f2','#f0f0f0','#ccc','#3f3d56'];
const MAP={'currentcolor':V.p500,'#2f2e41':V.n900,'#9e616a':V.piel2,'#ffb6b6':V.piel3};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:520}});
await p.setContent('<body>'+src+'</body>');
const svg=await p.evaluate(({DROP,MAP})=>{const s=document.querySelector('svg');const t=s.querySelector('title');if(t)t.remove();
 for(const e of [...s.querySelectorAll('*')]){const f=(e.getAttribute('fill')||'').toLowerCase();if(DROP.includes(f)){e.remove();continue;}if(MAP[f])e.setAttribute('fill',MAP[f]);else if(f&&f!=='none')e.setAttribute('data-miss',f);}
 s.removeAttribute('id');s.removeAttribute('data-name');for(const e of s.querySelectorAll('[id]'))e.removeAttribute('id');
 const bb=s.getBBox();s.setAttribute('viewBox',[bb.x,bb.y,bb.width,bb.height].map(v=>v.toFixed(2)).join(' '));s.removeAttribute('width');s.removeAttribute('height');
 return {svg:s.outerHTML,miss:[...s.querySelectorAll('[data-miss]')].map(e=>e.getAttribute('data-miss')),bb:[bb.width,bb.height]};},{DROP,MAP});
console.log(svg.miss,svg.bb);let out=svg.svg.replace(/\sdata-miss="[^"]*"/g,'').replace(/\s+/g,' ').replace(/> </g,'><').replace(/(\d+\.\d{2})\d+/g,'$1');
fs.writeFileSync('hero.svg',out);console.log(out.length);
const d=Buffer.from(out).toString('base64');const ar=svg.bb[0]/svg.bb[1];
// escena
const W=412,H=456,g=80,gy=H-g;const D=364;const fh=292,fw=fh*ar;
const B=[[0,34,96],[30,44,150],[70,30,70],[96,40,118],[300,36,104],[332,30,160],[358,34,84],[388,24,128]];
const stars=[[40,84,2],[92,58,1.5],[150,40,1.5],[262,44,2],[330,70,1.5],[378,104,2],[24,150,1.5],[392,52,1.5],[60,118,1],[350,34,1]];
function scene(sky,moon,bld,win){let h=`<div style="position:relative;width:${W}px;height:${H}px;background:${sky};overflow:hidden">`;
 for(const [x,y,r] of stars)h+=`<div style="position:absolute;left:${x}px;top:${y}px;width:${r*2}px;height:${r*2}px;border-radius:50%;background:#fff;opacity:.8"></div>`;
 for(const [x,w,bh] of B){h+=`<div style="position:absolute;left:${x}px;top:${gy-bh}px;width:${w}px;height:${bh}px;background:${bld}"></div>`;for(let r=0;r<Math.floor((bh-14)/18);r++)for(let c=0;c<Math.floor((w-8)/12);c++)if((r*3+c*5+x)%4===0)h+=`<div style="position:absolute;left:${x+6+c*12}px;top:${gy-bh+10+r*18}px;width:5px;height:7px;background:${win}"></div>`;}
 h+=`<div style="position:absolute;left:${W/2-D/2}px;top:${gy+40-D}px;width:${D}px;height:${D}px;border-radius:50%;background:${moon}"></div>`;
 h+=`<div style="position:absolute;left:0;top:${gy}px;width:${W}px;height:${g}px;background:#0a0a0a"></div>`;
 h+=`<img src="data:image/svg+xml;base64,${d}" style="position:absolute;left:${W/2-fw/2}px;top:${gy-fh+3}px;width:${fw}px;height:${fh}px"></div>`;return h;}
const text='<div style="background:#0a0a0a;color:#fff;font:700 34px sans-serif;padding:60px 20px 40px;width:372px">Nadie espera<br>solo.</div>';
await p.setContent('<body style="margin:0;background:#888;display:flex;gap:16px;padding:16px">'+[scene(V.p500,V.p100,V.p700,V.lima),scene(V.n800,V.lima,V.n700,V.p100),scene(V.n900,V.p500,V.n800,V.lima)].map(s=>'<div>'+s+text+'</div>').join('')+'</body>');
await p.screenshot({path:'hero.png',fullPage:true});await b.close();})();
