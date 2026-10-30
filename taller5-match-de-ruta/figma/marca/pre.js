const hex=h=>({r:parseInt(h.slice(0,2),16)/255,g:parseInt(h.slice(2,4),16)/255,b:parseInt(h.slice(4,6),16)/255});
async function lf(f,ss){for(const s of ss){try{await figma.loadFontAsync({family:f,style:s});return s;}catch(e){}}throw new Error('font '+f+' '+ss);}
const FB=await lf('Figtree',['Bold']),FS=await lf('Figtree',['SemiBold','Semi Bold']),FM=await lf('Figtree',['Medium']),FR=await lf('Figtree',['Regular']);
let page=figma.root.children.find(p=>p.name==='Identidad · Mini manual v0.1');
if(!page){page=figma.createPage();page.name='Identidad · Mini manual v0.1';}
await figma.setCurrentPageAsync(page);
const cols=await figma.variables.getLocalVariableCollectionsAsync();
let col=cols.find(c=>c.name==='Match · Marca');if(!col)col=figma.variables.createVariableCollection('Match · Marca');
const mode=col.modes[0].modeId;const allV=await figma.variables.getLocalVariablesAsync('COLOR');const V={};
function cv(name,h,a=1){let v=allV.find(x=>x.name===name&&x.variableCollectionId===col.id);if(!v)v=figma.variables.createVariable(name,col,'COLOR');const c=hex(h);v.setValueForMode(mode,{r:c.r,g:c.g,b:c.b,a});V[name]=v;return v;}
const TOK=[['neutro/negro','0A0A0A'],['neutro/gris-800','27272A'],['neutro/gris-600','5E5E66'],['neutro/gris-400','A1A1AA'],['neutro/gris-200','E4E4E7'],['neutro/gris-100','F4F4F5'],['neutro/blanco','FFFFFF'],['acento/principal','5B3DF5'],['acento/suave','EEEBFE'],['acento/sobre-acento','FFFFFF'],['semantico/exito','15803D'],['semantico/alerta','B45309'],['semantico/peligro','D92D20'],['candidata/a-violeta','5B3DF5'],['candidata/b-lima','C8F560'],['candidata/c-coral','E8461E'],['mapa/fondo','ECECEF'],['mapa/calle','FFFFFF'],['mapa/manzana','E2E2E6']];
for(const [n,h] of TOK)cv(n,h);
const P=(n,op)=>{let p={type:'SOLID',color:{r:0,g:0,b:0},opacity:op===undefined?1:op};p=figma.variables.setBoundVariableForPaint(p,'color',V[n]);return [p];};
const exTS=await figma.getLocalTextStylesAsync();const S={};
const TSD={disp:['Marca/Display 48',FB,48,56,-1.5],h1:['Marca/Título 32',FB,32,40,-1],h2:['Marca/H2 20',FS,20,28,-0.5],base:['Marca/Base 16',FR,16,20,0],strong:['Marca/Base fuerte 16',FS,16,20,0],label:['Marca/Label 14',FM,14,18,0],hint:['Marca/Pista 12',FR,12,16,0],mt:['Manual/Título 64',FB,64,72,-2],mk:['Manual/Sección 14',FS,14,18,0],mhero:['Manual/Marca 160',FB,160,160,-4],mp:['Manual/Texto 20',FR,20,28,0]};
for(const k in TSD){const [n,st,sz,lh,ls]=TSD[k];let s=exTS.find(x=>x.name===n);if(!s){s=figma.createTextStyle();s.name=n;}s.fontName={family:'Figtree',style:st};s.fontSize=sz;s.lineHeight={unit:'PIXELS',value:lh};s.letterSpacing={unit:'PERCENT',value:ls};S[k]=s;}
const isAL=n=>n&&'layoutMode' in n&&n.layoutMode!=='NONE';
async function T(p,str,k,cn='neutro/negro',o={}){const t=figma.createText();p.appendChild(t);await t.setTextStyleIdAsync(S[k].id);t.characters=str;t.fills=P(cn,o.op);if(o.align)t.textAlignHorizontal=o.align;if(o.w){t.resize(o.w,t.height);t.textAutoResize='HEIGHT';}else if(isAL(p)&&!o.hug){t.textAutoResize='HEIGHT';t.layoutSizingHorizontal='FILL';}if(o.x!==undefined){t.x=o.x;t.y=o.y;}return t;}
function AL(p,dir,props={},hug){const f=figma.createAutoLayout(dir,Object.assign({fills:[]},props));if(p){p.appendChild(f);if(isAL(p)&&!hug)f.layoutSizingHorizontal='FILL';}return f;}
function FR_(p,w,h,x=0,y=0,name='Capa'){const f=figma.createFrame();p.appendChild(f);f.name=name;f.resize(w,h);f.x=x;f.y=y;f.fills=[];f.clipsContent=false;return f;}
function rect(p,w,h,x,y,cn,r=0,op){const s=figma.createRectangle();p.appendChild(s);s.resize(w,h);s.x=x;s.y=y;s.fills=P(cn,op);s.cornerRadius=r;return s;}
function circ(p,d,x,y,cn,op){const s=figma.createEllipse();p.appendChild(s);s.resize(d,d);s.x=x;s.y=y;s.fills=cn?P(cn,op):[];return s;}
function stroke(n,cn,w,al='INSIDE',op){n.strokes=P(cn,op);n.strokeWeight=w;n.strokeAlign=al;}
async function line(p,pts,x,y,cn,w,name='Trazo'){const v=figma.createVector();p.appendChild(v);const net={vertices:pts.map(([a,b])=>({x:a,y:b,strokeCap:'ROUND'})),segments:pts.slice(1).map((_,i)=>({start:i,end:i+1})),regions:[]};await v.setVectorNetworkAsync(net);v.x=x;v.y=y;v.strokes=P(cn);v.strokeWeight=w;v.strokeJoin='ROUND';v.strokeCap='ROUND';v.fills=[];v.name=name;return v;}
async function symbol(p,size,ink,acc,bg,name='Símbolo'){const s=size/80;const f=FR_(p,size,size,0,0,name);
await line(f,[[0,0],[24*s,28*s],[48*s,0]],16*s,14*s,ink,12*s,'Rutas');
await line(f,[[0,0],[0,20*s]],40*s,42*s,acc,12*s,'Tramo compartido');
circ(f,22*s,5*s,3*s,ink).name='Origen 1';circ(f,22*s,53*s,3*s,ink).name='Origen 2';
const d=circ(f,24*s,28*s,52*s,bg);stroke(d,acc,6*s,'CENTER');d.name='Llegada';return f;}
async function lockup(p,size,ink,acc,bg){const r=AL(p,'HORIZONTAL',{name:'Logo horizontal',itemSpacing:Math.round(size*0.22),counterAxisAlignItems:'CENTER'},true);await symbol(r,size,ink,acc,bg);const t=figma.createText();r.appendChild(t);t.fontName={family:'Figtree',style:FB};t.fontSize=Math.round(size*0.9);t.letterSpacing={unit:'PERCENT',value:-4};t.lineHeight={unit:'PERCENT',value:100};t.characters='match';t.fills=P(ink);return r;}
function glass(n,fillOp=0.22,frost=16){n.fills=P('neutro/blanco',fillOp);n.effects=[{type:'GLASS',visible:true,radius:frost,refraction:0.5,depth:16,dispersion:0.2,lightAngle:-45,lightIntensity:0.6},{type:'DROP_SHADOW',visible:true,blendMode:'NORMAL',color:{r:0,g:0,b:0,a:0.10},offset:{x:0,y:8},radius:24,spread:0}];stroke(n,'neutro/blanco',1,'INSIDE',0.7);}
async function board(i,kicker,title,dark){const name=kicker;const old=page.children.find(n=>n.name===name);if(old)old.remove();
const b=figma.createAutoLayout('VERTICAL',{name,itemSpacing:48,paddingLeft:80,paddingRight:80,paddingTop:64,paddingBottom:80});page.appendChild(b);b.fills=P(dark?'neutro/negro':'neutro/blanco');b.resize(i===9?1480:1440,100);b.counterAxisSizingMode='FIXED';b.primaryAxisSizingMode='AUTO';b.cornerRadius=32;
const c=(i-1)%3,r=Math.floor((i-1)/3);b.x=c*1560;b.y=r*1560;
const hd=AL(b,'HORIZONTAL',{primaryAxisAlignItems:'SPACE_BETWEEN'});await T(hd,kicker,'mk',dark?'neutro/gris-400':'neutro/gris-600',{hug:true});await T(hd,'match · mini manual de marca v0.1','mk',dark?'neutro/gris-400':'neutro/gris-600',{hug:true});
if(title)await T(b,title,'mt',dark?'neutro/blanco':'neutro/negro');return b;}
function colsRow(b,n,gap=48){const r=AL(b,'HORIZONTAL',{itemSpacing:gap,name:'Columnas'});const cs=[];for(let i=0;i<n;i++){const c=AL(r,'VERTICAL',{itemSpacing:16,name:'Columna'});c.layoutSizingHorizontal='FILL';cs.push(c);}return cs;}
async function bullets(p,items,k='base',cn='neutro/gris-600'){const w=AL(p,'VERTICAL',{itemSpacing:8});for(const it of items)await T(w,'— '+it,k,cn);return w;}
const out=[];
