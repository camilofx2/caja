const wp=figma.root.children.find(p=>p.name.startsWith('Pantallas en alta'));await wp.loadAsync();await figma.setCurrentPageAsync(wp);
const screens={};for(const sec of wp.children){if(sec.type!=='SECTION')continue;for(const f of sec.children){if(f.type==='FRAME'&&/^[A-I]\d\d/.test(f.name))screens[f.name.split(' ')[0]]=f;}}
// transición de referencia
let TR=null;{const b=screens.A01.findOne(n=>n.reactions&&n.reactions.length>0);const a=(b.reactions[0].actions||[b.reactions[0].action])[0];TR=a.transition||null;}
const nav=d=>({trigger:{type:'ON_CLICK'},actions:[{type:'NODE',destinationId:screens[d].id,navigation:'NAVIGATE',transition:TR,preserveScrollPosition:false}]});
const back=()=>({trigger:{type:'ON_CLICK'},actions:[{type:'BACK'}]});
const log=[];
async function setOf(i){const m=await i.getMainComponentAsync();if(!m)return '';return m.parent&&m.parent.type==='COMPONENT_SET'?m.parent.name:m.name;}
async function inst(sc,set,txt){const s=screens[sc];for(const i of s.findAll(n=>n.type==='INSTANCE')){if(await setOf(i)!==set)continue;const t=i.findAll(x=>x.type==='TEXT'&&x.visible).map(x=>x.characters);if(t.some(c=>c.startsWith(txt)))return i;}return null;}
async function wire(sc,set,txt,dest){const n=await inst(sc,set,txt);if(!n){log.push('NO ENCONTRADO '+sc+' '+set+' '+txt);return;}await n.setReactionsAsync([dest==='BACK'?back():nav(dest)]);log.push(sc+' '+set+'«'+txt+'»→'+dest);}
await wire('B01','Opción','Correo institucional','B02');
await wire('C02','Botón','Enviar un enlace','C03');
await wire('D06','Tarjeta de match','Laura M.','E04');await wire('D06','Tarjeta de match','Sara P.','E04');
await wire('E02','Tarjeta de match','Sara P.','E04');await wire('E10','Tarjeta de match','Sara P.','E04');
await wire('D08','Tarjeta','Del trabajo a la U','D09');
await wire('E01','Tarjeta','Hoy · de la U','E02');
await wire('H05','Botón','Elegir de mi agenda','H05b');
await wire('C06','Botón','Volver al inicio','E01');
await wire('I07','Botón','Llamar a Daniela','BACK');await wire('I11','Botón','Llamar a Daniela','BACK');await wire('I11','Botón','Llamar al 123','BACK');
// filas con › sin enlace
function linked(n,s){let p=n;while(p&&p.id!==s.id){if(p.reactions&&p.reactions.length)return true;p=p.parent;}return false;}
const ROWS={'D09|Pausar la ruta':'D08','D09|Eliminar la ruta':'D08'};const rowsLeft=[];
for(const [c,s] of Object.entries(screens)){for(const t of s.findAll(n=>n.type==='TEXT'&&n.characters==='›'&&n.visible)){const row=t.parent;if(linked(row,s))continue;const lab=row.findOne(x=>x.type==='TEXT'&&x.characters!=='›');const key=c+'|'+(lab?lab.characters:'');if(ROWS[key]){await row.setReactionsAsync([nav(ROWS[key])]);log.push(key+'→'+ROWS[key]);}else rowsLeft.push(key);}}
// final del recorrido de Gloria: tocar la pantalla vuelve al chat
{const c=screens.I09.children.find(k=>k.name==='Contenido');await c.setReactionsAsync([back()]);log.push('I09 Contenido→BACK');}
return {log,rowsLeft,TR};
