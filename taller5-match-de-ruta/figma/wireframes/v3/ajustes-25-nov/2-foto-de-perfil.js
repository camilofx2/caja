const AV=__AV__; // sale de fotos-preparar.py (SVG de unDraw recoloreados, no se guardan aquí)
const vars=await figma.variables.getLocalVariablesAsync('COLOR');const V=n=>vars.find(x=>x.name===n);
const hex=c=>'#'+[c.r,c.g,c.b].map(x=>Math.round(x*255).toString(16).padStart(2,'0')).join('');
const MAP={'#eeebfe':'primario/100','#14112b':'neutral/900','#3b3658':'neutral/700','#5b3df5':'primario/500','#d5d2e5':'neutral/300','#ffffff':'neutral/0','#c68642':'ilustracion/piel-1','#8d5524':'ilustracion/piel-2','#e0ac69':'ilustracion/piel-3','#000000':'neutral/900'};
const miss={};
function bind(n){for(const prop of ['fills','strokes']){if(!(prop in n)||n[prop]===figma.mixed||!n[prop].length)continue;n[prop]=n[prop].map(p=>{if(p.type!=='SOLID')return p;const k=MAP[hex(p.color)];if(!k){miss[hex(p.color)]=1;return p;}const q=figma.variables.setBoundVariableForPaint(p,'color',V(k));return Object.assign({},q,{opacity:p.opacity===undefined?1:p.opacity});});}}
const paint=(n)=>figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:1,g:1,b:1}},'color',V(n));
const cp=figma.root.children.find(p=>p.name==='Sistema de diseño · Componentes');await cp.loadAsync();await figma.setCurrentPageAsync(cp);
let maxY=0;for(const n of cp.children)maxY=Math.max(maxY,n.y+n.height);
const comps=[];
for(const [who,svg] of Object.entries(AV)){const c=figma.createComponent();c.name='Persona='+who;c.resize(96,96);c.cornerRadius=48;c.clipsContent=true;c.fills=[paint('primario/100')];
 const s=figma.createNodeFromSvg(svg);s.name='Ilustración de '+who;s.fills=[];c.appendChild(s);s.rescale(96/s.width);s.x=0;s.y=0;
 [s,...s.findAll(()=>true)].forEach(bind);
 s.constraints={horizontal:'SCALE',vertical:'SCALE'};for(const k of s.findAll(()=>true)){if('constraints' in k)k.constraints={horizontal:'SCALE',vertical:'SCALE'};}comps.push(c);}
const set=figma.combineAsVariants(comps,cp);set.name='Foto de perfil';
set.layoutMode='HORIZONTAL';set.itemSpacing=24;set.paddingLeft=set.paddingRight=set.paddingTop=set.paddingBottom=24;set.primaryAxisSizingMode='AUTO';set.counterAxisSizingMode='AUTO';
set.x=0;set.y=maxY+240;set.description='Foto verificada de cada persona. Se usa con el intercambio de instancia «Foto» del componente Persona.';
const lbl=figma.createText();await figma.loadFontAsync({family:'Figtree',style:'SemiBold'});lbl.fontName={family:'Figtree',style:'SemiBold'};lbl.characters='Foto de perfil · 6 personas · se cambia con el intercambio de instancia de Persona';lbl.fontSize=20;cp.appendChild(lbl);lbl.x=0;lbl.y=set.y-44;lbl.fills=[paint('neutral/900')];
const pset=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Persona');const laura=comps.find(c=>c.name==='Persona=Laura');
const key=pset.addComponentProperty('Foto','INSTANCE_SWAP',laura.id,{preferredValues:comps.map(c=>({type:'COMPONENT',key:c.key}))});
const log=[];
for(const v of pset.children){const e=v.findOne(n=>n.name==='Foto');const d=Math.round(e.width);const par=e.parent;const idx=par.children.indexOf(e);const i=laura.createInstance();i.name='Foto';par.insertChild(idx,i);i.resize(d,d);e.remove();i.componentPropertyReferences={mainComponent:key};log.push(v.name+' foto '+d);}
return {set:set.id,key,log,miss,ids:comps.map(c=>c.name+'|'+c.id)};
