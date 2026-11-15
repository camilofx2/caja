const wp=figma.root.children.find(p=>p.name.startsWith('Pantallas en alta'));await wp.loadAsync();await figma.setCurrentPageAsync(wp);
const screens=[];for(const sec of wp.children){if(sec.type!=='SECTION')continue;for(const f of sec.children){if(f.type==='FRAME'&&/^[A-I]\d\d/.test(f.name))screens.push(f);}}
const byId={};screens.forEach(s=>byId[s.id]=s);const code=s=>s.name.split(' ')[0];
const out={n:screens.length,flows:wp.flowStartingPoints.map(f=>f.name+'|'+(byId[f.nodeId]?code(byId[f.nodeId]):'??'+f.nodeId)),screens:{},issues:[]};
const incoming={};const edges={};
async function compName(n){if(n.type!=='INSTANCE')return null;const m=await n.getMainComponentAsync();if(!m)return null;return (m.parent&&m.parent.type==='COMPONENT_SET'?m.parent.name:m.name)+'|'+m.name;}
for(const s of screens){const c=code(s);edges[c]=[];const rs=[];const nodes=[s,...s.findAll(()=>true)];
 for(const n of nodes){if(!n.reactions||!n.reactions.length)continue;for(const r of n.reactions){const acts=r.actions||(r.action?[r.action]:[]);for(const a of acts){let d='';if(a.type==='NODE'){const t=byId[a.destinationId];if(!t){d='ROTO:'+a.destinationId;out.issues.push(c+' '+n.name+' destino roto '+a.destinationId);}else{d=code(t);edges[c].push(d);incoming[d]=(incoming[d]||0)+1;}d=(a.navigation==='NAVIGATE'?'':a.navigation+':')+d;}else d=a.type;
   let label=n.name;if(n.type==='INSTANCE'||n.type==='FRAME'){const t=n.findOne?n.findOne(x=>x.type==='TEXT'&&x.visible):null;if(t)label=n.name+'«'+t.characters.slice(0,22)+'»';}
   rs.push((r.trigger.type==='AFTER_TIMEOUT'?'⏱'+r.trigger.timeout+' ':'')+label+'→'+d);}}}
 // botones sin enlace
 const noLink=[];const insts=s.findAll(n=>n.type==='INSTANCE');
 for(const i of insts){const cn=await compName(i);if(!cn)continue;const set=cn.split('|')[0];if(set!=='Botón')continue;let has=i.reactions&&i.reactions.length>0;let p=i.parent;while(!has&&p&&p.id!==s.id){if(p.reactions&&p.reactions.length)has=true;p=p.parent;}
  if(!has){const t=i.findOne(x=>x.type==='TEXT'&&x.visible);noLink.push((t?t.characters:'?')+(cn.includes('Disabled')?'(dis)':''));}}
 out.screens[c]={name:s.name.slice(0,40),r:rs,noLink};}
// alcanzabilidad
const starts=wp.flowStartingPoints.map(f=>byId[f.nodeId]?code(byId[f.nodeId]):null).filter(Boolean);const seen=new Set(starts);const q=[...starts];while(q.length){const c=q.shift();for(const d of edges[c]||[])if(!seen.has(d)){seen.add(d);q.push(d);}}
out.unreachable=screens.map(code).filter(c=>!seen.has(c));out.noIncoming=screens.map(code).filter(c=>!incoming[c]&&!starts.includes(c));out.deadEnds=screens.map(code).filter(c=>out.screens[c].r.filter(x=>!x.endsWith('→BACK')).length===0);
return out;
