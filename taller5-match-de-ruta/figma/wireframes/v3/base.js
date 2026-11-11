const hex=h=>({r:parseInt(h.slice(0,2),16)/255,g:parseInt(h.slice(2,4),16)/255,b:parseInt(h.slice(4,6),16)/255});
async function lf(f,ss){for(const s of ss){try{await figma.loadFontAsync({family:f,style:s});return s;}catch(e){}}throw new Error('font');}
const FB=await lf('Figtree',['Bold']),FS=await lf('Figtree',['SemiBold','Semi Bold']),FM=await lf('Figtree',['Medium']),FR=await lf('Figtree',['Regular']);
const col=(await figma.variables.getLocalVariableCollectionsAsync()).find(c=>c.name==='Match · Marca');const V={};
for(const v of await figma.variables.getLocalVariablesAsync('COLOR'))if(v.variableCollectionId===col.id)V[v.name]=v;
const P=(n,op)=>{if(!V[n])throw new Error('var '+n);let p={type:'SOLID',color:{r:0,g:0,b:0}};p=figma.variables.setBoundVariableForPaint(p,'color',V[n]);if(op!==undefined)p=Object.assign({},p,{opacity:op});return [p];};
const exTS=await figma.getLocalTextStylesAsync();const S={};
for(const [k,n] of [['disp','Marca/Display 48'],['h1','Marca/Título 32'],['h2','Marca/H2 20'],['code','Marca/Código 24'],['base','Marca/Base 16'],['strong','Marca/Base fuerte 16'],['label','Marca/Label 14'],['hint','Marca/Pista 12']])S[k]=exTS.find(x=>x.name===n);
const isAL=n=>n&&'layoutMode' in n&&n.layoutMode!=='NONE';
async function T(p,str,k,cn='neutral/900',o={}){const t=figma.createText();p.appendChild(t);await t.setTextStyleIdAsync(S[k].id);t.characters=str;t.fills=P(cn,o.op);if(o.align)t.textAlignHorizontal=o.align;if(o.name)t.name=o.name;if(o.w){t.resize(o.w,t.height);t.textAutoResize='HEIGHT';}else if(isAL(p)&&!o.hug){t.textAutoResize='HEIGHT';t.layoutSizingHorizontal='FILL';}return t;}
function AL(p,dir,props={},hug){const f=figma.createAutoLayout(dir,Object.assign({fills:[]},props));if(p){p.appendChild(f);if(isAL(p)&&!hug)f.layoutSizingHorizontal='FILL';}return f;}
function FR_(p,w,h,x=0,y=0,name='Capa'){const f=figma.createFrame();p.appendChild(f);f.name=name;f.resize(w,h);f.x=x;f.y=y;f.fills=[];f.clipsContent=false;return f;}
function rect(p,w,h,x,y,cn,r=0,op){const s=figma.createRectangle();p.appendChild(s);s.resize(w,h);s.x=x;s.y=y;s.fills=P(cn,op);s.cornerRadius=r;return s;}
function circ(p,d,x,y,cn,op){const s=figma.createEllipse();p.appendChild(s);s.resize(d,d);s.x=x;s.y=y;s.fills=cn?P(cn,op):[];return s;}
function stroke(n,cn,w,al='INSIDE',op){n.strokes=P(cn,op);n.strokeWeight=w;n.strokeAlign=al;}
const shadow=(a=0.08)=>[{type:'DROP_SHADOW',visible:true,blendMode:'NORMAL',color:{r:0,g:0,b:0,a},offset:{x:0,y:8},radius:24,spread:0}];
const ring=(n,vn)=>{const e={type:'DROP_SHADOW',visible:true,blendMode:'NORMAL',color:{r:0,g:0,b:0,a:1},offset:{x:0,y:0},radius:0,spread:4};n.effects=[figma.variables.setBoundVariableForEffect(e,'color',V[vn])];};
function glass(n,fillOp=0.22,frost=16){n.fills=P('neutral/0',fillOp);n.effects=[{type:'GLASS',visible:true,radius:frost,refraction:0.5,depth:16,dispersion:0.2,lightAngle:-45,lightIntensity:0.6},shadow(0.1)[0]];stroke(n,'neutral/0',1,'INSIDE',0.7);}
let cp=figma.root.children.find(p=>p.name==='Componentes · Match');
