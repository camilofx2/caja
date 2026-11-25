const ip=figma.root.children.find(p=>p.name.includes('Identidad'));await ip.loadAsync();
const F=await figma.getNodeByIdAsync('221:2');
for(const card of F.findAll(n=>n.type==='FRAME'&&n.parent&&n.parent.parent===F&&n.cornerRadius===24)){card.layoutGrow=1;card.counterAxisSizingMode='FIXED';
 for(const ch of card.children){if(ch.type==='TEXT'){ch.layoutAlign='STRETCH';ch.textAutoResize='HEIGHT';}else if(ch.type==='INSTANCE'){ch.layoutAlign='STRETCH';}else if(ch.type==='FRAME'){ch.layoutAlign='STRETCH';ch.primaryAxisSizingMode='FIXED';ch.layoutWrap='WRAP';ch.counterAxisSpacing=10;ch.counterAxisSizingMode='AUTO';}}}
const wp=figma.root.children.find(p=>p.name.startsWith('Pantallas en alta'));await wp.loadAsync();
let e05;for(const sec of wp.children){if(sec.type!=='SECTION')continue;for(const f of sec.children)if(f.name.startsWith('E05'))e05=f;}
const sh=e05.findOne(n=>n.name==='Hoja inferior');sh.y=e05.height-sh.height;
return {h:Math.round(F.height),sheet:[Math.round(sh.y),Math.round(sh.height)],clip:e05.clipsContent};
