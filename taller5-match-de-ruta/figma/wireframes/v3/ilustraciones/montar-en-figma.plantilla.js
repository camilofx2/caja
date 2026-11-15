const SVGS=__SVGS__;const MODE=__MODE__;
const cp=figma.root.children.find(p=>p.name==='Sistema de diseño · Componentes'||p.name==='Componentes · Match');await cp.loadAsync();await figma.setCurrentPageAsync(cp);
const set=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Ilustración');
const vars=await figma.variables.getLocalVariablesAsync('COLOR');
const hex=c=>'#'+[c.r,c.g,c.b].map(x=>Math.round(x*255).toString(16).padStart(2,'0')).join('');
const NAMES=['neutral/900','neutral/800','neutral/700','neutral/600','neutral/500','neutral/400','neutral/300','neutral/200','neutral/100','neutral/0','primario/500','primario/700','primario/100','candidata/c-coral','candidata/b-lima','ilustracion/piel-1','ilustracion/piel-2','ilustracion/piel-3'];
const byHex={},byName={};for(const n of NAMES){const v=vars.find(x=>x.name===n);byName[n]=v;byHex[hex(Object.values(v.valuesByMode)[0])]=v;}
byHex["#000000"]=byName["neutral/900"];
const miss={};let bound=0;
function bind(node){for(const prop of ['fills','strokes']){if(!(prop in node)||node[prop]===figma.mixed)continue;const ps=node[prop];if(!ps||!ps.length)continue;node[prop]=ps.map(p=>{if(p.type!=='SOLID')return p;const v=byHex[hex(p.color)];if(!v){miss[hex(p.color)]=(miss[hex(p.color)]||0)+1;return p;}bound++;const q=figma.variables.setBoundVariableForPaint(p,'color',v);return Object.assign({},q,{opacity:p.opacity===undefined?1:p.opacity});});}}
const SZ={Grande:[456,80,340,110,270],Mediana:[340,60,250,80,200],Compacta:[220,44,170,56,140]};const log=[];
for(const t of Object.keys(SVGS)){const base=figma.createNodeFromSvg(SVGS[t]);base.name='Sujeto';base.fills=[];base.clipsContent=false;bind(base);base.findAll(()=>true).forEach(bind);const ar=base.width/base.height;const mode=MODE[t];
 for(const sz of Object.keys(SZ)){const v=set.children.find(c=>c.name==='Tema='+t+', Tamaño='+sz);if(!v){log.push('NO '+t+' '+sz);continue;}
  const [H,g,D,sink,fh0]=SZ[sz];const gy=H-g;const keepLuna=(t==='Paradero vacío');const rem=[];
  for(const c of [...v.children]){if(c.name==='Suelo')continue;if(keepLuna&&c.name==='Luna')continue;rem.push(c.name);c.remove();}
  let suelo=v.children.find(c=>c.name==='Suelo');if(!suelo){suelo=figma.createRectangle();suelo.name='Suelo';v.appendChild(suelo);suelo.resize(412,g);suelo.x=0;suelo.y=gy;suelo.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',byName['neutral/900'])];suelo.constraints={horizontal:'STRETCH',vertical:'MAX'};}
  let fw,fh;
  if(mode==='light'){const m=figma.createEllipse();m.name='Luna';v.insertChild(0,m);m.resize(D,D);m.x=206-D/2;m.y=Math.round(gy+sink*0.35-D);m.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:1,g:1,b:1}},'color',byName['primario/100'])];m.constraints={horizontal:'CENTER',vertical:'MAX'};
   fh=fh0;fw=fh*ar;if(fw>380){fw=380;fh=fw/ar;}}
  else{fw=380;fh=fw/ar;if(fh>gy-30){fh=gy-30;fw=fh*ar;}}
  const s=base.clone();v.appendChild(s);s.rescale(fw/s.width);s.x=Math.round(206-fw/2);s.y=Math.round(gy-fh+(mode==='light'?4:2));s.constraints={horizontal:'CENTER',vertical:'MAX'};
  log.push(t+' '+sz+' rem['+rem.join(',')+'] kids['+v.children.map(c=>c.name).join(',')+'] subj '+Math.round(s.width)+'x'+Math.round(s.height));}
 base.remove();}
return {log,miss,bound};
