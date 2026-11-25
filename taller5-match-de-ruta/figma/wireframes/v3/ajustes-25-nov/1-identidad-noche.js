const vars=await figma.variables.getLocalVariablesAsync('COLOR');const V=n=>vars.find(x=>x.name===n);
const h2c=h=>({r:parseInt(h.slice(1,3),16)/255,g:parseInt(h.slice(3,5),16)/255,b:parseInt(h.slice(5,7),16)/255,a:1});
const NEW={'neutral/900':'#14112b','neutral/800':'#252140','neutral/700':'#3b3658','neutral/600':'#5a5577','neutral/500':'#6f6a8a','neutral/400':'#a29dba','neutral/300':'#d5d2e5','neutral/200':'#e7e4f2','neutral/100':'#f5f3fb','mapa/fondo':'#eceaf4','mapa/manzana':'#e0ddee'};
const log=[];
for(const [n,h] of Object.entries(NEW)){const v=V(n);const mode=Object.keys(v.valuesByMode)[0];v.setValueForMode(mode,h2c(h));v.description='Neutro con tinte noche (ajuste 25 nov)';log.push(n+'→'+h);}
// tipografía de títulos
const ts=await figma.getLocalTextStylesAsync();
for(const st of ['ExtraBold','Bold','SemiBold'])await figma.loadFontAsync({family:'Bricolage Grotesque',style:st});
const T={'Marca/Display 48':['ExtraBold',-2],'Marca/Título 32':['ExtraBold',-1.5],'Marca/Código 24':['Bold',0],'Marca/H2 20':['Bold',-0.5],'Manual/Título 64':['ExtraBold',-2.5],'Manual/Marca 160':['ExtraBold',-4]};
for(const s of ts){if(!T[s.name])continue;const [style,ls]=T[s.name];s.fontName={family:'Bricolage Grotesque',style};s.letterSpacing={unit:'PERCENT',value:ls};log.push(s.name+'→Bricolage '+style);}
// línea de tramos en Tarjeta de match
const cp=figma.root.children.find(p=>p.name==='Sistema de diseño · Componentes');await cp.loadAsync();
const tm=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Tarjeta de match');
const paint=(name,op)=>{const q=figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',V(name));return Object.assign({},q,{opacity:op===undefined?1:op});};
const SH={'1 y 2':[1,1,0],'2 y 3':[0,1,1],'3':[0,0,1],'1':[1,0,0]};
for(const v of tm.children){const key=v.name.replace('Tramos=','');const sh=SH[key];if(!sh){log.push('?? '+v.name);continue;}
 const grp=v.findOne(n=>n.name==='Tramos en común');const bar=grp.children.find(c=>c.type==='FRAME');const idx=grp.children.indexOf(bar);const W=bar.width;
 const nf=figma.createFrame();nf.name='Línea de tramos';nf.fills=[];nf.clipsContent=false;nf.resize(W,14);grp.insertChild(idx,nf);if(grp.layoutMode!=='NONE'){nf.layoutAlign='STRETCH';}
 const xs=[7,W/3,2*W/3,W-7];
 for(let i=0;i<3;i++){const on=sh[i]===1;const r=figma.createRectangle();nf.appendChild(r);const x0=xs[i],x1=xs[i+1];r.resize(x1-x0,on?6:2);r.x=x0;r.y=on?4:6;r.cornerRadius=on?3:1;r.fills=[paint(on?'primario/500':'neutral/300')];r.name=on?'Tramo en común':'Tramo propio';r.constraints={horizontal:'SCALE',vertical:'CENTER'};}
 for(let i=0;i<4;i++){const touches=(i>0&&sh[i-1])||(i<3&&sh[i]);const e=figma.createEllipse();nf.appendChild(e);const d=touches?12:10;e.resize(d,d);e.x=xs[i]-d/2;e.y=7-d/2;e.name=touches?'Parada compartida':'Parada';
  if(touches){e.fills=[paint('neutral/900')];}else{e.fills=[paint('neutral/0')];e.strokes=[paint('neutral/300')];e.strokeWeight=2;}
  e.constraints={horizontal:i===0?'MIN':(i===3?'MAX':'SCALE'),vertical:'CENTER'};}
 bar.remove();log.push(v.name+' línea OK');}
return log;
