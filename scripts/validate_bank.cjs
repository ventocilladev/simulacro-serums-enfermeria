const fs = require('fs');
const vm = require('vm');
const path = require('path');
const assert = require('assert/strict');
const root = path.resolve(__dirname,'..');
const context = {window:{}, document:{getElementById:()=>({})}, localStorage:{getItem:()=>null},console};
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root,'questions-master.js'),'utf8'),context);
const questions=context.window.QUESTIONS;
const aliases=JSON.parse(fs.readFileSync(path.join(root,'scripts/option-aliases.json'),'utf8'));
function normalize(s){return s.toLowerCase().normalize('NFD').replace(/\p{M}/gu,'').match(/[a-z0-9]+/g)?.join(' ') || '';}
function canonical(s){
  const acronym=s.match(/\((ASIS|POI|PEI|HIS|SIS|ROF|MOP|NOC|NIC|HCE)\)/)?.[1];
  const value=normalize(acronym || s);
  return aliases[value] || value;
}
assert.equal(canonical('ASIS'),canonical('Análisis de situación de salud (ASIS)'));
assert.equal(canonical('POI'),canonical('Plan Operativo Institucional'));
assert.equal(canonical('Prueba molecular'),canonical('Prueba de diagnóstico rápido molecular'));
assert.equal(questions.length,400);
assert.equal(new Set(questions.map(q=>q[1])).size,400);
for(const [i,q] of questions.entries()){
  assert.equal(q[2].length,4,`choice count ${i}`);
  assert.equal(new Set(q[2].map(canonical)).size,4,`equivalent choices ${i}`);
  assert(q[3]>=0 && q[3]<4 && q[4],`answer/explanation ${i}`);
  assert((q[1].match(/¿/g)||[]).length<=1,`single prompt ${i}`);
  assert(!/primera situación|segunda situación|par de interpretaciones/.test(q[1]),`double case ${i}`);
}
const asis=questions[129];
assert.equal(asis[2].filter(x=>canonical(x)===canonical('ASIS')).length,1,'ASIS screenshot regression');
assert.equal(questions.filter(q=>q[6]==='numeric').length,0);
let app=fs.readFileSync(path.join(root,'app.js'),'utf8');
app=app.replace(/if \(state && !state\.finished && remaining\(\) === 0\) finish\(true\); else home\(\);/,
 'globalThis.testApi={selectedIds,bank,setState:s=>state=s,setHistory:ids=>history=ids};');
vm.runInContext(app,context);
const api=context.testApi;
function block(q){
 if(['Enfermería','Curso de vida','Problemas prioritarios'].includes(q.category))return 'clinical';
 if(q.category==='Gestión')return 'management';
 if(q.category==='Investigación')return 'research';
 if(q.category==='Ética e interculturalidad')return 'ethics';
 return 'public';
}
for(const count of [60,100]){
  for(let trial=0;trial<50;trial++){
    api.setState(null);api.setHistory([]);
    const first=api.selectedIds(count);
    assert.equal(first.length,count);
    assert.equal(new Set(first.map(id=>api.bank[id].concept)).size,count,'one question per family');
    for(const [b,share] of Object.entries({clinical:.6,public:.2,management:.1,ethics:.05,research:.05}))
      assert.equal(first.filter(id=>block(api.bank[id])===b).length,count*share,`${b} quota`);
    assert(first.filter(id=>questions[id][6]==='numeric').length<=8,'numeric applications cannot dominate');
    api.setState({ids:first});api.setHistory(first);
    const second=api.selectedIds(count);
    const prior=new Set(first.map(id=>api.bank[id].concept));
    assert.equal(second.length,count);
    assert(!second.some(id=>prior.has(api.bank[id].concept)),'avoid previous family');
    api.setState(null);
    const unseen=api.selectedIds(count);
    assert(!unseen.some(id=>first.includes(id)),'prefer unseen questions');
  }
  console.log(`${count}: correct quotas, distinct families, no immediate family repeat; 50 trials`);
}
console.log('400 items: alias regression, unique options and single prompts passed');
