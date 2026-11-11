"""Build the single-question bank with editorial aliases and distinct choices."""
import json
import math
import re
import runpy
import subprocess
import unicodedata
from pathlib import Path
from question_families import FAMILIES
from editorial_review import REVIEW

ROOT = Path(__file__).resolve().parents[1]
legacy = runpy.run_path(str(ROOT / 'scripts/build_advanced_bank.py'))
script = "const fs=require('fs'),vm=require('vm');const c={window:{}};for(const f of ['questions-advanced.js','questions-clinical.js'])vm.runInNewContext(fs.readFileSync(f,'utf8'),c);console.log(JSON.stringify(c.window.QUESTIONS));"
base = json.loads(subprocess.check_output(['node','-e',script],cwd=ROOT).decode('utf-8'))

def normalize(s):
    s = ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c) != 'Mn')
    return ' '.join(re.findall(r'[a-z0-9]+',s))

ALIASES = {}
def alias(*values):
    key = normalize(values[0])
    for value in values:
        ALIASES[normalize(value)] = key

for i,q in enumerate(legacy['source']):
    alias(q[2][q[3]], legacy['answer'](q))
for values in [
    ['ASIS','Análisis de situación de salud','Análisis de situación de salud (ASIS)','Análisis situacional de salud'],
    ['POI','Plan Operativo Institucional'],['PEI','Plan Estratégico Institucional'],
    ['ROF','Reglamento de Organización y Funciones'],['MOP','Manual de Operaciones'],
    ['HIS','Sistema de información HIS'],['Historia clínica electrónica','HCE','SIHCE'],
    ['SIS','Seguro Integral de Salud','Seguro Integral de Salud (SIS)'],
    ['PVPS o FEFO','FEFO o PVPS'],['Estructural','Estructurales','Determinante estructural'],
    ['Condición material intermedia','Condiciones materiales intermedias'],
    ['Físico','Peligro físico','Riesgo físico'],['Biológico','Peligro biológico','Riesgo biológico'],
    ['Químico','Peligro químico','Riesgo químico'],['Ergonómico','Riesgo ergonómico'],
    ['Psicosocial','Riesgo psicosocial'],['Activa','Vigilancia activa'],['Pasiva','Vigilancia pasiva'],
    ['Centinela','Vigilancia centinela'],['Basada en laboratorio','Vigilancia basada en laboratorio'],
    ['Cultural','Barrera cultural'],['Geográfica','Barrera geográfica'],['Organizacional','Barrera organizacional'],
    ['De soporte','UPSS de soporte'],['De atención directa','UPSS de atención directa'],
    ['Clima organizacional','Clima laboral'],['NANDA-I','Diagnósticos NANDA-I'],
    ['NOC','Resultados NOC'],['NIC','Intervenciones NIC'],
    ['Prepatogénico','Período prepatogénico'],['Primaria','Prevención primaria'],
    ['Secundaria','Prevención secundaria'],['Terciaria','Prevención terciaria'],['Cuaternaria','Prevención cuaternaria'],
    ['Anopheles','Mosquito Anopheles'],['Aedes aegypti','Mosquito Aedes aegypti'],
    ['Dos veces al día','Cepillado dos veces al día con pasta fluorada'],
    ['Tamizaje de anemia','Medición de hemoglobina según grupo de edad'],
    ['Funcionalidad','Valoración funcional geriátrica','Funcional y de síndromes geriátricos'],
    ['Corrección documentada del registro','Registro y corrección documentada'],
    ['Medición de hemoglobina según grupo de edad','Tamizaje de hemoglobina'],
    ['Estudio de contactos','Estudio y control de contactos'],
    ['Alineamiento con el marco normativo','Alineamiento normativo'],
    ['Circunstancias psicosociales','Circunstancia psicosocial'],
    ['Prueba molecular','Prueba de diagnóstico rápido molecular'],
    ['Comunicación en su lengua','Comunicación en lengua materna'],
    ['Búsqueda activa de casos','Búsqueda activa de tuberculosis'],
    ['Contacto con fuentes de plomo en el ambiente','Exposición a plomo'],
]: alias(*values)

def canonical(s):
    n = normalize(s)
    # Explicitly recognize a known acronym embedded in a full label.
    match = re.search(r'\((ASIS|POI|PEI|HIS|SIS|ROF|MOP|NOC|NIC|HCE)\)',s)
    if match: return ALIASES.get(normalize(match[1]), normalize(match[1]))
    return ALIASES.get(n,n)

FIXES = {
 129: ['Análisis de situación de salud (ASIS)','Plan de salud local','Plan Operativo Institucional','Análisis FODA institucional'],
 7:['Sensibilidad','Especificidad','Valor predictivo positivo','Valor predictivo negativo'],
 8:['Valor predictivo positivo','Sensibilidad','Especificidad','Valor predictivo negativo'],
 26:['Verificar los identificadores personales con la orden','Usar el número de cama como identificador','Confirmar la identidad solo por el apellido','Aceptar como identificador el diagnóstico de ingreso'],
 43:['Validez de contenido','Validez de criterio','Validez de constructo','Confiabilidad'],
 57:['Esterilización','Desinfección de alto nivel','Antisepsia','Limpieza mecánica'],
 93:['Consentimiento informado','Asentimiento informado','Autorización por representación','Comunicación de resultados'],
 117:['Prepatogénico','Subclínico','Clínico','Resolutivo'],
 118:['Tríada agente, huésped y ambiente','Cadena epidemiológica','Red de causalidad','Historia natural de la enfermedad'],
 128:['Evitar prescribir un antibiótico sin indicación','Iniciar un antibiótico para prevenir complicaciones sin valorar indicación','Reducir la dosis habitual para justificar el uso innecesario','Elegir otro antibiótico sin establecer necesidad clínica'],
 140:['Asepsia','Antisepsia','Desinfección','Esterilización'],
 141:['Desinfección','Esterilización','Antisepsia','Limpieza mecánica'],
 174:['Tamizaje neonatal','Confirmación diagnóstica','Evaluación clínica integral','Vigilancia de cardiopatías por oximetría'],
 185:['Infección asociada a la atención de salud','Infección presente al ingreso','Colonización sin infección','Infección adquirida en la comunidad'],
 196:['Dato subjetivo actual','Dato objetivo actual','Antecedente personal','Antecedente familiar'],
 197:['Dato objetivo actual','Dato subjetivo actual','Antecedente personal','Antecedente familiar'],
 202:['NOC','NIC','NANDA-I','Clasificación Internacional de Enfermedades'],
 203:['NIC','NOC','NANDA-I','Clasificación Internacional de Enfermedades'],
 204:['NANDA-I','NOC','NIC','Clasificación Internacional de Enfermedades'],
 210:['Error de preparación','Error de administración','Error de conservación','Error de registro'],
 214:['Data logger','Termómetro de lectura puntual','Registro de dosis aplicadas','Indicador de vencimiento del producto'],
 217:['Desde los seis meses de edad','Desde los cuatro meses de edad','Desde los ocho meses de edad','Desde los doce meses de edad'],
 235:['Eclampsia','Preeclampsia sin convulsiones','Hipertensión gestacional sin complicación neurológica','Hipertensión crónica estable'],
 239:['Después de 12 meses consecutivos sin menstruación y sin otra causa','Después de seis meses sin menstruación','Después de tres ciclos irregulares','Al aparecer bochornos, sin considerar la historia menstrual'],
 242:['Sífilis','Gonorrea por cultivo','Clamidiasis mediante examen clínico','Herpes genital por serología aislada'],
 244:['Alumbramiento','Dilatación','Expulsivo fetal','Puerperio tardío'],
 277:['Validez de criterio','Validez de contenido','Validez de constructo','Confiabilidad'],
 278:['Confiabilidad','Validez de contenido','Validez de criterio','Validez de constructo'],
 298:['Clima organizacional','Cultura organizacional','Satisfacción individual','Identidad institucional'],
 299:['Cultura organizacional','Clima organizacional','Liderazgo formal','Satisfacción individual'],
}
STEMS = {
 26:'Antes de administrar un medicamento, se detectan dos pacientes con el mismo apellido. ¿Qué verificación permite evitar confundir a las personas?',
 129:'El equipo integra morbilidad, mortalidad, demografía y determinantes, con participación comunitaria, para caracterizar las necesidades del distrito antes de planificar intervenciones. ¿Qué herramienta está elaborando?',
 196:'Un paciente dice «me duele la cabeza desde esta mañana». ¿Cómo se clasifica este dato de valoración?',
 197:'La enfermera mide y registra una temperatura de 38,5 °C en la valoración actual. ¿Cómo se clasifica este dato?',
}
items=[]
repairs=[]
for i,q in enumerate(base):
    preferred=REVIEW[i][1] if i in REVIEW else FIXES.get(i,q[2])
    correct=preferred[0] if i in FIXES or i in REVIEW else q[2][q[3]]
    choices=[correct]
    candidates=list(preferred)
    if i<300:
        candidates += list(legacy['POOL_FOR_ID'].get(i,[])) + legacy['source'][i][2]
    for candidate in candidates:
        if canonical(candidate) in {canonical(x) for x in choices}: continue
        choices.append(candidate)
        if len(choices)==4: break
    if len(choices)!=4: raise ValueError(('Insufficient distinct choices',i,choices))
    if choices!=q[2]: repairs.append(i)
    stem=REVIEW[i][0] if i in REVIEW and REVIEW[i][0] else STEMS.get(i,q[1])
    items.append([q[0],stem,choices,0,q[4],i,'case','Fuente temática proporcionada'])

assert len(FAMILIES)==47
for family_id,(category,topic,question,options,rules,cases) in enumerate(FAMILIES):
    for case,correct in cases:
        explanation=rules[correct]
        items.append([category,case+' '+question,options,correct,explanation,1000+family_id,'case',topic])

def fmt(x):
    return f'{x:.2f}'.rstrip('0').rstrip('.').replace('.',',')
def numeric(category,group,stem,correct,alternatives,why,topic):
    values=[]
    for value in [correct]+alternatives:
        label=fmt(value)
        if label not in values: values.append(label)
    assert len(values)==4,(stem,values)
    items.append([category,stem,values,0,why,2000+group,'numeric',topic])

for k in range(25):
    concentration=[25,40,50,80,100][k%5]; volume=1+(k//5)*.5
    dose=concentration*volume
    numeric('Enfermería',0,f'Una prescripción ya validada indica {fmt(dose)} mg de un medicamento. La solución disponible contiene {concentration} mg por mL. Considerando solo el cálculo indicado, ¿qué volumen en mL corresponde administrar?',volume,[volume/2,volume*2,volume+.25],f'Volumen = dosis indicada / concentración = {fmt(dose)} / {concentration} = {fmt(volume)} mL.','Cálculo de volumen prescrito')
    weight=8+k; rate=[4,6,8,10,12][k%5]; conc=[20,30,40,50,60][k%5]; result=weight*rate/conc
    numeric('Enfermería',1,f'La orden validada para una persona de {weight} kg es de {rate} mg/kg por dosis. El preparado contiene {conc} mg/mL. Sin modificar la prescripción, ¿cuántos mL corresponden a una dosis?',result,[result/2,result*2,result+.5],f'Dosis = {weight} × {rate} mg; volumen = dosis / {conc} mg/mL = {fmt(result)} mL.','Cálculo de dosis por peso')
    total=[300,450,600,750,900][k%5]; hours=3+k//5; result=total/hours
    numeric('Enfermería',2,f'Una infusión prescrita de {total} mL debe pasar en {hours} horas mediante una bomba. ¿Qué velocidad en mL/h cumple la orden?',result,[total/(hours+1),total/(hours-1),result*.9],f'Velocidad = volumen / tiempo = {total} / {hours} = {fmt(result)} mL/h.','Cálculo de velocidad de infusión')
    total=[240,360,480,600,720][k%5]; hours=4+k//5; factor=[15,20,60,15,20][k%5]; raw=total*factor/(hours*60); result=math.floor(raw+.5)
    numeric('Enfermería',3,f'Una orden indica infundir {total} mL en {hours} horas. El equipo entrega {factor} gotas/mL. ¿Qué goteo en gotas/min corresponde, redondeado al entero más cercano?',result,[result+5,max(1,result-5),result+10],f'Gotas/min = {total} × {factor} / ({hours} × 60) = {fmt(raw)}; redondeado: {result}.','Cálculo de goteo prescrito')
    population=1000+k*100; existing=40+k*2; new=20+k; susceptible=population-existing; result=new/susceptible*100
    numeric('Epidemiología',4,f'Una población cerrada tiene {population} personas; {existing} ya presentan la enfermedad al inicio. Durante el seguimiento aparecen {new} casos nuevos entre quienes estaban libres del daño. Sin pérdidas, ¿cuál es la incidencia acumulada porcentual?',result,[new/population*100,(existing+new)/population*100,new/(susceptible-new)*100],f'Población en riesgo inicial = {population} − {existing} = {susceptible}; incidencia = {new}/{susceptible} × 100 = {fmt(result)} %.','Incidencia acumulada')
    cases=80+k*4; deaths=4+k%7; pop=3000+k*200; result=deaths/cases*100
    numeric('Epidemiología',5,f'Un distrito de {pop} habitantes registró {cases} casos de una enfermedad; {deaths} fallecieron por ella. ¿Cuál es la letalidad porcentual entre los casos?',result,[deaths/pop*100,deaths/(cases-deaths)*100,cases/pop*100],f'Letalidad = muertes entre los casos / total de casos × 100 = {deaths}/{cases} × 100 = {fmt(result)} %.','Letalidad y denominadores')
    ne=200+k*10; nu=400+k*10; ce=40+k*2; cu=20+k; result=(ce/ne)/(cu/nu)
    numeric('Epidemiología',6,f'En una cohorte, enferman {ce} de {ne} personas expuestas y {cu} de {nu} no expuestas. ¿Cuál es el riesgo relativo de los expuestos, expresado como razón?',result,[ce/cu,cu/ce,1/result],f'RR = ({ce}/{ne}) / ({cu}/{nu}) = {fmt(result)}. Se comparan riesgos, no solo cantidades de casos.','Riesgo relativo')
    tp=50+k*2; fn=5+k%6; tn=120+k*3; fp=13+k%8
    metrics=[tp/(tp+fn)*100,tn/(tn+fp)*100,tp/(tp+fp)*100,tn/(tn+fn)*100]
    # Deterministic adjustment if a table accidentally gives two equal displayed percentages.
    while len({fmt(v) for v in metrics})<4:
        fp+=1; metrics=[tp/(tp+fn)*100,tn/(tn+fp)*100,tp/(tp+fp)*100,tn/(tn+fn)*100]
    target=k%4; names=['sensibilidad','especificidad','valor predictivo positivo','valor predictivo negativo']; denoms=[tp+fn,tn+fp,tp+fp,tn+fn]; nums=[tp,tn,tp,tn]
    numeric('Epidemiología',7,f'Una prueba produce {tp} verdaderos positivos, {fn} falsos negativos, {tn} verdaderos negativos y {fp} falsos positivos. ¿Cuál es su {names[target]}, en porcentaje?',metrics[target],[metrics[i] for i in range(4) if i!=target],f'{names[target].capitalize()} = {nums[target]}/{denoms[target]} × 100 = {fmt(metrics[target])} %.','Interpretación de tabla diagnóstica')

assert len(items)==1000,len(items)
# The published edition retains every source topic and reduces repeated variants.
base_items=items[:330]
case_items=items[330:800]
first_cases=[]
seen_families=set()
for q in case_items:
    if q[5] not in seen_families:
        first_cases.append(q)
        seen_families.add(q[5])
clinical={'Enfermería','Curso de vida','Problemas prioritarios'}
second_cases=[]
second_families=set()
for q in case_items:
    if q[0] in clinical and q not in first_cases and q[5] not in second_families:
        second_cases.append(q)
        second_families.add(q[5])
        if len(second_cases)==23: break
items=base_items+first_cases+second_cases
assert len(items)==400,len(items)
assert len({q[1] for q in items})==400,'Repeated stems'
for i,q in enumerate(items):
    assert len(q[2])==4 and len({canonical(x) for x in q[2]})==4,('Equivalent choices',i,q[2])
    assert q[3] in range(4) and q[4]
    assert not re.search('primera situación|segunda situación|par de interpretaciones',q[1],re.I)
out=ROOT/'questions-master.js'
out.write_text('window.QUESTIONS = '+json.dumps(items,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
(ROOT/'scripts/option-aliases.json').write_text(json.dumps(ALIASES,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'400 single questions: 330 revised and 70 additional cases. Revised choice sets: {len(repairs)}. Bank: {out.stat().st_size} bytes')
