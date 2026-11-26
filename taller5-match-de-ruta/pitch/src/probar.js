const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:780}});const errs=[];p.on('pageerror',e=>errs.push(String(e)));p.on('console',m=>{if(m.type()==='error')errs.push(m.text());});
await p.goto('file://'+path.resolve(process.argv[2]));await p.waitForTimeout(800);
const mode=process.argv[3];const out=process.argv[4];
if(mode==='slides'){for(let i=1;i<=20;i++){await p.keyboard.press('ArrowRight');await p.waitForTimeout(3300);await p.screenshot({path:`${out}/s${String(i).padStart(2,'0')}.png`});}}
else{await p.screenshot({path:`${out}/ad00.png`});await p.click('#adPlay');const T=[2,5,9,12,14.5,18.5,22,25.5,29,33,37,41,46,51,55,59.5,61];let t=0;for(const x of T){await p.waitForTimeout((x-t)*1000);t=x;await p.screenshot({path:`${out}/ad${String(x).replace('.','_')}.png`});}}
const ov=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);console.log('errores',errs,'desborde',ov);await b.close();})();
