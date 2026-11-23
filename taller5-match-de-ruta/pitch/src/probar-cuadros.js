// Captura el comercial en los segundos indicados: node src/probar-cuadros.js archivo.html carpeta 8 30 57
const {chromium}=require('playwright');const path=require('path');
(async()=>{const [,,file,out,...ts]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:780}});
await p.goto('file://'+path.resolve(file));await p.waitForTimeout(500);
for(const t of ts){await p.evaluate(()=>adStart());await p.evaluate(x=>{AD.t=x;},Number(t)-3);await p.waitForTimeout(3000);await p.screenshot({path:`${out}/q${t}.png`});await p.evaluate(()=>adStop());}
await b.close();})();
