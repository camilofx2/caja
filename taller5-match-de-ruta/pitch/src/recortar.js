// Recorta las capturas de Figma al marco de la pantalla (412x917) y las pasa a WebP.
const {chromium}=require('playwright');const fs=require('fs');
const [,, outDir, ...pairs]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const pair of pairs){const [name,file,mode]=pair.split('=');const data='data:image/png;base64,'+fs.readFileSync(file).toString('base64');
 const res=await p.evaluate(async({data,mode})=>{const im=new Image();im.src=data;await im.decode();const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const x=c.getContext('2d');x.drawImage(im,0,0);
  let x0=0,y0=0,w=im.width,h=im.height;
  if(mode==='screen'){const d=x.getImageData(0,0,w,h).data;let minx=w,miny=h,maxx=0,maxy=0;for(let j=0;j<h;j++)for(let i=0;i<w;i++){if(d[(j*w+i)*4+3]>=252){if(i<minx)minx=i;if(i>maxx)maxx=i;if(j<miny)miny=j;if(j>maxy)maxy=j;}}
   x0=minx;y0=miny;w=maxx-minx+1;h=maxy-miny+1;}
  const o=document.createElement('canvas');o.width=w;o.height=h;o.getContext('2d').drawImage(c,x0,y0,w,h,0,0,w,h);return {url:o.toDataURL('image/webp',mode==='screen'?0.92:0.82),w,h,x0,y0};},{data,mode});
 fs.writeFileSync(`${outDir}/${name}.webp`,Buffer.from(res.url.split(',')[1],'base64'));console.log(name,res.w+'x'+res.h,'@',res.x0,res.y0,fs.statSync(`${outDir}/${name}.webp`).size);}
await b.close();})();
