const col=(await figma.variables.getLocalVariableCollectionsAsync()).find(c=>c.name==='Match · Marca');const V={};for(const v of await figma.variables.getLocalVariablesAsync('COLOR'))if(v.variableCollectionId===col.id)V[v.name]=v;
const P=n=>[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',V[n])];
const vn=async n=>{const f=n.fills&&n.fills[0];const b=f&&f.boundVariables&&f.boundVariables.color;if(!b)return null;const v=await figma.variables.getVariableByIdAsync(b.id);return v&&v.name;};
const res={sections:0,screens:0,soft:0,cards:0};
// 1) Aviso Info: tinte primario
const cp=figma.root.children.find(p=>(p.name==='Sistema de diseño · Componentes'||p.name==='Componentes · Match'));await cp.loadAsync();
const av=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Aviso');const info=av.children.find(c=>c.name==='Tipo=Info');info.fills=P('primario/100');for(const ic of info.findAll(n=>n.type==='VECTOR'))ic.fills=P('primario/500');
// Persona Tarjeta: borde más visible
const pe=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Persona');const pt=pe.children.find(c=>c.name==='Tipo=Tarjeta');pt.strokes=P('neutral/300');
const wp=figma.root.children.find(p=>(p.name==='Pantallas en alta · v3 (con prototipo)'||p.name==='Wireframes v3 · alta'));await wp.loadAsync();
for(const s of wp.children.filter(n=>n.type==='SECTION')){s.fills=P('neutral/200');res.sections++;
 for(const t of s.children.filter(n=>n.type==='TEXT')){if(await vn(t)==='neutral/600')t.fills=P('neutral/700');}
 for(const f of s.children.filter(n=>n.type==='FRAME'&&/^[A-I]\d/.test(n.name))){res.screens++;f.strokes=P('neutral/300');f.strokeWeight=1;f.strokeAlign='OUTSIDE';f.effects=[{type:'DROP_SHADOW',visible:true,blendMode:'NORMAL',color:{r:0,g:0,b:0,a:0.08},offset:{x:0,y:8},radius:32,spread:0}];
  if(await vn(f)!=='neutral/0')continue;
  const ct=f.children.find(c=>c.name==='Contenido');if(!ct)continue;
  const whiteCards=[...ct.findAll(n=>n.type==='FRAME'&&(n.name==='Tarjeta'||n.name==='Tarjeta de persona'))].filter(Boolean);let hasWhite=false;for(const c of whiteCards)if(await vn(c)==='neutral/0')hasWhite=true;
  const hasPT=ct.findAll(n=>n.type==='INSTANCE'&&n.mainComponent&&n.mainComponent.name==='Tipo=Tarjeta').length>0;
  const hasOpt=ct.findAll(n=>n.type==='INSTANCE'&&n.mainComponent&&n.mainComponent.parent&&n.mainComponent.parent.name==='Opción').length>0;
  if(hasWhite||hasPT||hasOpt){f.fills=P('neutral/100');res.soft++;
   for(const c of ct.findAll(n=>n.type==='FRAME'&&n.name==='Tarjeta')){if(await vn(c)==='neutral/100'){c.fills=P('neutral/0');c.strokes=P('neutral/200');c.strokeWeight=1;c.strokeAlign='INSIDE';res.cards++;}}
   for(const c of ct.findAll(n=>n.type==='FRAME'&&n.name==='Tarjeta de persona'))c.strokes=P('neutral/300');}
 }}
return res;
