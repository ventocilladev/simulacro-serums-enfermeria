"""Build a case comparison bank from the user-provided study outline.

The existing, independently written 300 cases are the factual starting point.
Each new item asks for two interpretations; distractors differ by one decision.
The official exams are used to judge style, never copied into this bank.
"""
from __future__ import annotations

import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ['questions.js', 'questions-extra.js', 'questions-banco-1.js',
         'questions-banco-2.js', 'questions-banco-3.js',
         'questions-banco-4.js', 'questions-coverage.js']
script = "const fs=require('fs'),vm=require('vm');const c={window:{}};for(const f of " + json.dumps(FILES) + ")vm.runInNewContext(fs.readFileSync(f,'utf8'),c);console.log(JSON.stringify(c.window.QUESTIONS));"
source = json.loads(subprocess.check_output(['node', '-e', script], cwd=ROOT).decode('utf-8'))
assert len(source) == 300

CASE_OVERRIDES = {
    2: 'Una municipalidad desarrolla espacios y capacidades para que los vecinos decidan sobre hábitos y entornos saludables.',
    3: 'Los vecinos identifican un problema sanitario, eligen prioridades y participan en la ejecución de las medidas.',
    7: 'Una prueba de tamizaje detecta a casi todas las personas que realmente padecen la enfermedad.',
    8: 'Entre quienes obtuvieron un resultado positivo, se estima qué proporción verdaderamente tiene la enfermedad.',
    13: 'Se vacuna a población susceptible antes de que aparezcan casos de la enfermedad.',
    18: 'En una vivienda se observa humedad, hacinamiento y falta de agua segura.',
    19: 'Dos grupos tienen oportunidades educativas muy distintas por su posición social.',
    26: 'Antes de administrar un fármaco, la enfermera coteja el identificador de la persona con la orden y el brazalete.',
    27: 'Una enfermera detecta que documentó un procedimiento en el registro equivocado y deja constancia de la corrección.',
    32: 'En una campaña infantil se mide hemoglobina para identificar anemia no diagnosticada.',
    35: 'El equipo incorpora los tamizajes de infecciones y el seguimiento de la gestante en cada control prenatal.',
    38: 'Una paciente que habla otra lengua explica una práctica cultural segura que desea mantener durante su atención.',
    50: 'Un estudio encuentra asociación entre exposición y daño; se comprueba que la exposición ocurrió antes del daño.',
    56: 'Después de retirarse los guantes, una enfermera realiza la medida de prevención que sigue siendo indispensable.',
    63: 'Durante una campaña se entrega un folleto con signos de alarma del dengue.',
    72: 'El registrador muestra una excursión térmica de vacunas y el equipo inmoviliza los frascos hasta evaluarlos.',
    86: 'Una gestante solicita parto vertical y el equipo valora sus preferencias y las condiciones de seguridad.',
    87: 'Una usuaria emplea una práctica tradicional junto con su tratamiento y pide orientación para continuarla con seguridad.',
    100: 'Un contacto domiciliario de tuberculosis no tiene enfermedad activa y cumple criterios de terapia preventiva.',
    102: 'En una localidad amazónica con malaria se organiza vigilancia del mosquito transmisor.',
    103: 'El tamizaje neonatal sugiere una enfermedad congénita rara y tratable antes de que el niño presente síntomas.',
    117: 'En una comunidad no hay casos de leptospirosis, pero existen roedores y agua contaminada.',
    123: 'Una dirección revisa las normas y objetivos nacionales antes de formular el plan estratégico de su entidad.',
    128: 'Un paciente con resfriado no complicado solicita antibióticos, aunque no existe indicación clínica.',
    139: 'Una persona con enfermedad avanzada tiene dolor persistente y angustia que afectan su calidad de vida.',
    143: 'Una adolescente refiere tristeza persistente e insomnio y acepta conversar sobre su seguridad y apoyos.',
    145: 'La enfermera termina una inyección y descarta la aguja usada sin volver a encapucharla.',
    165: 'Una persona sin síntomas participa en una estrategia de tamizaje colorrectal que busca sangre no visible en heces.',
    166: 'Un varón sin síntomas pregunta por el tamizaje de próstata y por los beneficios y límites de las pruebas.',
    169: 'Una lesión pigmentada cambia de forma y color en pocos meses y requiere valoración clínica.',
    182: 'Durante una curación hay riesgo de salpicadura de fluidos hacia la cara de la enfermera.',
    196: 'Al preguntar por sus molestias, el paciente dice que siente dolor de cabeza desde la mañana.',
    199: 'En consejería bucal, una madre pregunta por la frecuencia mínima de cepillado con pasta fluorada.',
    202: 'En el plan de atención de enfermería se consignan los resultados que se espera alcanzar.',
    203: 'La enfermera selecciona acciones estandarizadas para resolver una necesidad de cuidado.',
    204: 'El profesional necesita nombrar de manera estandarizada la respuesta humana identificada en su valoración.',
    213: 'Una alarma confirma que varias vacunas estuvieron fuera del intervalo térmico previsto.',
    217: 'Una madre pregunta cuándo ofrecer alimentos complementarios además de la lactancia.',
    221: 'Una gestante presenta sangrado vaginal durante una visita domiciliaria.',
    232: 'En un puesto de salud, una gestante tiene sangrado abundante, palidez y signos de choque.',
    241: 'En el control posparto se vigilan el descenso del fondo uterino y las características de los loquios.',
    242: 'Un establecimiento aplica pruebas rápidas para detectar una infección de transmisión sexual en una usuaria sin síntomas.',
    256: 'Una persona sin VIH recibe PrEP, consejería y controles para disminuir su riesgo de adquirir el virus.',
    261: 'Una mujer quechuahablante no comprende las indicaciones explicadas solo en castellano.',
    263: 'Una gestante solicita conocer las condiciones en que puede atenderse un parto vertical.',
    275: 'Una mujer busca reducir su riesgo de cáncer de cuello uterino y detectar lesiones tempranas.',
    276: 'Una persona quiere reducir factores modificables asociados con distintos cánceres.',
    279: 'El personal realiza una medida antes y después del contacto con cada paciente para limitar IAAS.'
}
ANSWER_OVERRIDES = {
    2:'Empoderamiento para mejorar la salud', 27:'Corrección documentada del registro',
    38:'Comunicación culturalmente pertinente', 72:'Evaluación de cadena de frío',
    86:'Respetar la elección y verificar seguridad', 87:'Diálogo sobre seguridad y compatibilidad',
    100:'Prevenir tuberculosis activa', 103:'Confirmación y referencia oportuna',
    123:'Alineamiento con el marco normativo', 128:'Evitar antibiótico sin indicación',
    139:'Cuidado paliativo integral', 143:'Valoración inicial de salud mental',
    166:'Decisión informada según riesgo', 169:'Evaluación y referencia de la lesión',
    199:'Dos veces al día',
    232:'Estabilización y referencia inmediata',
    256:'Tamizaje y seguimiento periódicos',
    261:'Comunicación en su lengua', 263:'Informar opciones y valorar seguridad',
    275:'Vacuna VPH y tamizaje cervical',
    276:'Evitar tabaco y mantener hábitos saludables'
    ,76:'Cuidado integral del niño',77:'Cuidado integral del adolescente',
    78:'Cuidado integral del adulto',79:'Valoración funcional geriátrica',
    226:'Cuidado integral del adolescente',227:'Cuidado integral del joven',
    50:'Temporalidad',191:'Agente comunitario',192:'Determinante ambiental'
}

# Each pool keeps all alternatives within the same decision family.
POOLS = [
    ([0,1,2,3,74,75,104,105,108,109,110,111,112,113,114], ['Monitoreo y evaluación de la salud','Vigilancia y control de riesgos','Intervención sobre determinantes sociales','Participación y movilización social','Promoción de la salud','Acceso a servicios integrales','Desarrollo de recursos humanos','Financiamiento de la salud']),
    ([4,5,6,120,53,272], ['Incidencia','Prevalencia','Letalidad','Tasa de mortalidad','Riesgo relativo','Riesgo atribuible poblacional']),
    ([7,8], ['Sensibilidad','Especificidad','Valor predictivo positivo','Valor predictivo negativo']),
    ([9,54,133,134,135,136], ['Vigilancia activa','Vigilancia pasiva','Vigilancia centinela','Vigilancia basada en laboratorio','Difusión de información','Notificación epidemiológica']),
    ([10,11,12,13,154], ['Primaria','Secundaria','Terciaria','Cuaternaria']),
    ([14,15,16,155,156,158,159,160,161,162,163,193,194,195], ['Sectorización','Ficha familiar','Plan de salud local','Vigilancia comunitaria','Priorización','Cronograma','Seguimiento y evaluación','Trabajo intersectorial']),
    ([17,186,187,188,189], ['Barrera geográfica','Barrera económica','Barrera cultural','Barrera organizacional','Accesibilidad efectiva']),
    ([18,19,146,147,148,149,150,151,152,153], ['Determinante estructural','Condición material intermedia','Circunstancia psicosocial','Condición laboral','Posición socioeconómica','Acceso a servicios','Discriminación social']),
    ([20,69,171,172], ['Peligro físico','Peligro químico','Peligro biológico','Contaminación cruzada']),
    ([21,55,57,140,141,142,144,185,279], ['Control de infecciones','Vigilancia epidemiológica','Asepsia','Antisepsia','Desinfección','Esterilización','Precauciones estándar','Higiene de manos']),
    ([22,176,177,181], ['Riesgo psicosocial','Riesgo ergonómico','Riesgo biológico','Riesgo físico']),
    ([23,180], ['Identificación de amenazas','Evaluación del riesgo','Preparación','Respuesta','Recuperación','Mitigación']),
    ([24,25,198,199,200,201,202,203,204,205], ['Valoración','Diagnóstico de enfermería','Planificación','Ejecución','Evaluación','NANDA-I','NOC','NIC']),
    ([26,27,196,197], ['Verificación de identidad','Validación de la orden','Registro y corrección documentada','Valoración de datos subjetivos','Valoración de datos objetivos']),
    ([28,31,76,77,78,79,216,226,227,228,229,230], ['Cuidado integral del niño','Cuidado integral del adolescente','Cuidado integral del joven','Cuidado integral del adulto','Cuidado integral del adulto mayor','Evaluación de funcionalidad']),
    ([29,30,35,220,221,222,223,224,225,232,235,239,241,244,245,270], ['Plan de parto','Consejería prenatal','Signos de alarma obstétrica','Estabilización y referencia inmediata','Tamizaje prenatal','Vigilancia del puerperio','Alumbramiento','Prevención de transmisión maternoinfantil']),
    ([32,33,238,240], ['Tamizaje de anemia','Suplementación preventiva','Tratamiento de anemia','Seguimiento de adherencia','Consejería nutricional']),
    ([34,80,100,101,231,233,234,236,237], ['Búsqueda activa de tuberculosis','Baciloscopía','Prueba molecular','Cultivo','Estudio de contactos','Terapia preventiva','Control ambiental','Protección respiratoria','Canasta PANTBC']),
    ([36,37,39,84,85,93,251,252,253,255,257,258,259,260], ['Autonomía','Beneficencia','No maleficencia','Justicia','Confidencialidad','Consentimiento informado','Probidad','Transparencia','Discreción']),
    ([38,86,87,88,261,262,263,264,265,266], ['Diálogo intercultural','Comunicación en lengua materna','Pertinencia cultural','Práctica complementaria','Práctica alternativa','Parto vertical seguro','Prevención del estigma']),
    ([40,41,89,90,91,267,268,269,271,273], ['Cuantitativo','Cualitativo','Mixto','Descriptivo','Analítico','Experimental','Transversal','Longitudinal','Investigación básica','Investigación aplicada']),
    ([42,43,92,274,275,276,277,278,280,281], ['Lista de cotejo','Ficha de observación','Validez de contenido','Validez de criterio','Validez de constructo','Confiabilidad','Procesamiento de datos','Resultados','Discusión']),
    ([44,45,46,47,49,94,98,106,107,121,122,123,254,282,283,284,285,286,287,288,289,290,291,292,296,297,298,299], ['PEI','POI','ROF','MOP','Misión','Visión','Fortaleza','Debilidad','Oportunidad','Amenaza','Clima organizacional','Cultura organizacional','Liderazgo','Trabajo colaborativo','Contrarreferencia']),
    ([48,95,96,97,137,138,254,290,291,292,293,294,295], ['I-3','I-4','UPSS de atención directa','UPSS de soporte','Cartera de servicios','Referencia','Contrarreferencia','Red integrada de salud','Teleorientación','Teleinterconsulta','Telemedicina','Telecapacitación']),
    ([56,61,145,182,183,279], ['Higiene de manos','Guantes según riesgo','Protección ocular','Mascarilla según riesgo','Descarte inmediato de punzocortantes','Precauciones estándar']),
    ([58,59,60,168,170,173,175], ['Eliminación de criaderos','Control físico de vectores','Segregación de residuos','Minimización de residuos','Almacenamiento temporal','Transporte interno']),
    ([62,63,64,65,167], ['Información','Educación','Comunicación','Consejería','Seguimiento del plan local']),
    ([66,143,247,248,249,250], ['Salud mental comunitaria','Centro de Salud Mental Comunitaria','Atención interdisciplinaria','Rehabilitación psicosocial','Continuidad de cuidados','Valoración de riesgo individual']),
    ([67,68,106,107,137,138], ['HIS','Historia clínica electrónica','Receta electrónica','Seguro Integral de Salud','Cartera de servicios']),
    ([70,71,72,73,206,207,208,209,210,213,214,215,218], ['Revisión previa a la vacunación','Error programático','ESAVI','ESAVI grave','Excursión térmica','Inmovilización de biológicos','Data logger','Verificación de dosis y vía']),
    ([81,82,242,243,245,256,270], ['Abordaje sindrómico','Consejería preprueba','Consejería posprueba','Tamizaje de ITS','PrEP con seguimiento','Prevención maternoinfantil']),
    ([83,154,157,164,165,166,169,275,276], ['Prevención primaria','Tamizaje cervical','Mamografía','Sangre oculta en heces','Evaluación de riesgo prostático','Evaluación de lesión cutánea']),
    ([102,212,224], ['Dengue por Aedes aegypti','Malaria por Anopheles','Leptospirosis por contacto con orina animal','Enfermedad de Chagas por triatominos']),
    ([103,174,178], ['Tamizaje neonatal en sangre de talón','Oximetría de pulso neonatal','Confirmación diagnóstica','Referencia especializada']),
    ([117,118,119,115,116,127], ['Período prepatogénico','Período patogénico','Tríada epidemiológica','Brote','Endemia','Epizootia','Pandemia']),
    ([124,125,126,128], ['Temporalidad','Consistencia','Gradiente biológico','Confusión','Plausibilidad biológica']),
    ([129,130,131,132], ['ASIS','Transición demográfica','Transición epidemiológica','Crecimiento poblacional']),
    ([139,143], ['Control de síntomas','Apoyo emocional','Valoración de riesgo','Referencia especializada']),
    ([157,164,165,166,169,275,276], ['Tamizaje cervical','Mamografía','Prueba de sangre oculta en heces','Evaluación de riesgo prostático','Valoración de lesión cutánea','Vacunación contra VPH']),
    ([179,184], ['Exposición a plomo','Exposición a mercurio','Exposición a arsénico','Exposición a cadmio']),
    ([199,211], ['Cepillado con pasta fluorada','Uso de hilo dental','Enjuague bucal como único método','Limpieza interdental']),
]
POOL_FOR_ID = {}
for ids, options in POOLS:
    for index in ids:
        POOL_FOR_ID[index] = options
for ids, options in [
    ([44,45,287], ['POI','PEI','Plan de salud local','Plan estratégico sectorial']),
    ([46,284,285,286], ['Fortaleza','Debilidad','Oportunidad','Amenaza']),
    ([47], ['FEFO o PVPS','PEPS','Punto de pedido','Inventario periódico']),
    ([48], ['I-1','I-2','I-3','I-4']),
    ([49], ['Asistencia','Permanencia','Rendimiento','Productividad']),
    ([67,68,106,137,138], ['HIS','Historia clínica electrónica','Receta electrónica','Seguro Integral de Salud']),
    ([94,288,289], ['ROF','MOP','PEI','POI']),
    ([95,290,291], ['UPSS de atención directa','UPSS de soporte','Servicio administrativo','Cartera de servicios']),
    ([96,292], ['Red integrada de salud','Microred','Unidad prestadora','Referencia individual']),
    ([97,293,294,295], ['Telemedicina','Teleorientación','Teleinterconsulta','Telecapacitación']),
    ([98,296], ['Planificar','Hacer','Verificar','Actuar']),
    ([99,297], ['Cuasi incidente','Evento adverso','Evento centinela','Incidente sin daño']),
    ([107], ['Cartera de servicios','UPSS','Categoría del establecimiento','Plan operativo']),
    ([121,122], ['Liderazgo','Trabajo colaborativo','Coordinación intersectorial','Delegación de funciones']),
    ([123], ['Alineamiento normativo','Planificación operativa','Evaluación institucional','Priorización local']),
    ([254], ['Referencia','Contrarreferencia','Interconsulta','Transferencia asistencial']),
    ([282,283], ['Misión','Visión','Objetivo estratégico','Valor institucional']),
    ([298,299], ['Clima organizacional','Cultura organizacional','Satisfacción individual','Identidad institucional']),
    ([6,120], ['Incidencia','Prevalencia','Mortalidad','Letalidad']),
    ([21], ['Vigilancia en salud pública','Control de brotes','Investigación epidemiológica','Monitoreo sanitario']),
    ([23,180], ['Evaluación del riesgo','Preparación','Respuesta','Recuperación','Mitigación']),
    ([32], ['Tamizaje de hemoglobina','Tratamiento con hierro','Prevención nutricional','Seguimiento de adherencia']),
    ([34], ['Búsqueda activa de casos','Estudio de contactos','Terapia preventiva','Seguimiento del tratamiento']),
    ([43,277,278], ['Validez de contenido','Validez de criterio','Validez de constructo','Confiabilidad']),
    ([52,132], ['Transición demográfica','Transición epidemiológica','Cambio de estructura etaria','Aumento de incidencia']),
    ([80,233,234], ['Baciloscopía','Cultivo','Prueba molecular','Prueba de sensibilidad']),
    ([81,82,242,243,256], ['Abordaje sindrómico','Tamizaje de ITS','Consejería preprueba','Consejería posprueba','PrEP con seguimiento']),
    ([102,212], ['Aedes aegypti','Anopheles','Culex quinquefasciatus','Triatoma infestans']),
    ([224], ['Leptospirosis','Hantavirosis','Rickettsiosis','Brucelosis']),
    ([117], ['Prepatogénico','Subclínico','Clínico','Resolutivo']),
    ([118], ['Tríada agente, huésped y ambiente','Cadena epidemiológica','Red de causalidad','Historia natural de la enfermedad']),
    ([124,125,126], ['Temporalidad','Consistencia','Gradiente biológico','Confusión']),
    ([128], ['Prescripción según necesidad clínica','Tratamiento empírico innecesario','Optimización de dosis','Seguimiento de adherencia']),
    ([139], ['Cuidado paliativo integral','Tratamiento curativo exclusivo','Control del dolor aislado','Apoyo emocional sin control de síntomas']),
    ([143], ['Valoración inicial de salud mental','Consejería sin valorar riesgo','Derivación sin escucha inicial','Seguimiento sin evaluación']),
    ([185], ['Infección comunitaria','Infección presente al ingreso','Colonización sin infección','Infección asociada a la atención de salud']),
    ([154], ['Primaria','Secundaria','Terciaria','Cuaternaria']),
    ([157], ['Prueba de VPH o Papanicolaou','Colposcopía','Biopsia cervical','Ecografía transvaginal']),
    ([275], ['Vacuna VPH y tamizaje cervical','Vacuna VPH sin controles posteriores','Tamizaje sin vacunación cuando corresponde','Tratamiento de lesiones sin prevención']),
    ([164], ['Mamografía','Ecografía mamaria','Resonancia magnética de mama','Exploración clínica mamaria']),
    ([165], ['Prueba de sangre oculta en heces','Colonoscopía','Sigmoidoscopía','Prueba inmunoquímica fecal']),
    ([166], ['Decisión informada según riesgo','PSA sin consejería','Biopsia a todo varón','Seguimiento de síntomas únicamente']),
    ([169], ['Evaluación y referencia de la lesión','Control rutinario diferido','Tratamiento tópico empírico','Fotografía sin valoración clínica']),
    ([276], ['Evitar tabaco y mantener hábitos saludables','Tamizaje en población elegible','Vacunación contra VPH','Consulta por síntomas de alarma']),
    ([179,184], ['Exposición a plomo','Exposición a mercurio','Exposición a arsénico','Exposición a cadmio']),
    ([199], ['Una vez al día','Dos veces al día','Tres veces al día','Solo cuando hay dolor']),
    ([211], ['Uso cuidadoso de hilo dental','Cepillado de superficies externas','Enjuague con flúor','Limpieza de la lengua']),
    ([36,93], ['Consentimiento informado','Asentimiento informado','Autorización por representación','Información sin decisión voluntaria']),
    ([70], ['Antes de administrar la vacuna','Durante la administración','Después de la vacunación','Durante el seguimiento de ESAVI']),
    ([71,208,209], ['ESAVI leve','ESAVI grave','Error programático','Evento coincidente']),
    ([72,213,214,215], ['Evaluación de cadena de frío','Inmovilización de biológicos','Monitoreo de temperatura','Reacondicionamiento de paquetes fríos']),
    ([76,77,78,79,226,227,228,229,230], ['Cuidado integral del niño','Cuidado integral del adolescente','Cuidado integral del joven','Cuidado integral del adulto','Cuidado integral del adulto mayor','Valoración funcional geriátrica']),
    ([142], ['Limitar la propagación','Detectar precozmente nuevos casos','Evitar la exposición inicial','Reducir secuelas después de la infección']),
    ([57], ['Esterilización','Antisepsia','Limpieza mecánica','Desinfección de alto nivel']),
    ([141], ['Desinfección','Esterilización','Antisepsia','Limpieza mecánica']),
    ([218], ['Inmunizaciones','Evaluación del desarrollo','Consejería nutricional','Tamizaje de anemia']),
    ([50], ['Temporalidad de la exposición','Consistencia entre estudios','Gradiente biológico','Plausibilidad biológica']),
    ([51], ['Transición demográfica','Transición epidemiológica','Envejecimiento individual','Migración neta']),
    ([190], ['Atención integral familiar','Atención individual episódica','Vigilancia comunitaria','Intervención intersectorial']),
    ([191], ['Agente comunitario','Profesional de salud','Autoridad municipal','Representante institucional']),
    ([192], ['Determinante ambiental','Determinante estructural','Factor psicosocial','Barrera organizacional']),
    ([217], ['Desde los cuatro meses','Desde los seis meses de edad','Desde los ocho meses','Desde los doce meses']),
    ([219], ['Derivación y seguimiento oportunos','Observación sin seguimiento','Repetir control sin evaluación','Alta de CRED sin plan']),
    ([246], ['Enfermedades no transmisibles','Enfermedades metaxénicas','Enfermedades zoonóticas','Infecciones oportunistas']),
]:
    for index in ids:
        POOL_FOR_ID[index] = options

STOP = set('para como esta este estas estos cuál cual debe durante entre desde sobre según luego porque caso grupo tipo persona paciente equipo salud atención una uno unos unas del las los con que sus por ante tras forma cuál'.split())
def words(s: str) -> set[str]:
    return set(re.findall(r'[a-záéíóúñ]{4,}', s.lower())) - STOP

def answer(q):
    index = source.index(q)
    return ANSWER_OVERRIDES.get(index, q[2][q[3]].strip())

def case(q):
    index = source.index(q)
    head = CASE_OVERRIDES.get(index, q[1].split('¿', 1)[0].strip())
    return head if len(head) >= 45 and len(head) < 200 and head.endswith('.') and len(answer(q)) < 52 else None

eligible = [i for i, q in enumerate(source) if case(q)]
by_cat = defaultdict(list)
for i in eligible:
    by_cat[source[i][0]].append(i)

def score(i, j):
    a, b = source[i], source[j]
    common = len(words(a[1] + ' ' + a[4]) & words(b[1] + ' ' + b[4]))
    # Prefer nearby concepts while retaining some variety of cases.
    return (common, -abs(len(answer(a)) - len(answer(b))), -abs(i-j))

def neighbors(i):
    a = answer(source[i]).lower()
    options = [j for j in by_cat[source[i][0]] if j != i and answer(source[j]).lower() != a
               and not (len(a) >= 5 and (a in answer(source[j]).lower() or answer(source[j]).lower() in a))]
    return sorted(options, key=lambda j: score(i,j), reverse=True)

forms = [
    'En la primera situación, {a} En la segunda, {b} ¿Qué par de interpretaciones corresponde, en ese orden?',
    'Una supervisora revisa dos situaciones. Primero: {a} Después: {b} ¿Cuál es la clasificación correcta de ambas?',
    'En dos actividades del establecimiento se observa lo siguiente: (1) {a} (2) {b} ¿Qué conceptos explican, respectivamente, cada situación?',
    'El equipo compara dos hallazgos: {a} Por otro lado, {b} ¿Cuál alternativa interpreta correctamente ambos hallazgos?'
]

def distractor(i, excluded):
    target = answer(source[i])
    def distinct(candidate):
        candidate = candidate.lower().strip()
        return all(candidate != other and not (len(candidate) >= 5 and (candidate in other or other in candidate)) for other in excluded)
    if i in POOL_FOR_ID:
        for candidate in POOL_FOR_ID[i]:
            if distinct(candidate) and candidate.lower() != target.lower():
                return candidate
    for j in neighbors(i):
        if score(i, j)[0] < 1:
            continue
        candidate = answer(source[j])
        if distinct(candidate) and 0.35 <= len(candidate)/len(target) <= 2.6:
            return candidate
    for j in neighbors(i):
        candidate = answer(source[j])
        if distinct(candidate):
            return candidate
    raise RuntimeError(f'No distractor for {i}')

items = []
seen_pairs = set()
for rank in range(20):
    for i in eligible:
        for j in neighbors(i)[rank:]:
            if score(i,j)[0] >= 1 and (i,j) not in seen_pairs:
                break
        else:
            continue
        seen_pairs.add((i,j))
        a, b = answer(source[i]), answer(source[j])
        c = distractor(i, {a.lower(),b.lower()})
        d = distractor(j, {a.lower(),b.lower(),c.lower()})
        choices = [f'{a} / {b}', f'{c} / {b}', f'{a} / {d}', f'{c} / {d}']
        if len(set(choices)) < 4:
            continue
        a_case = case(source[i]); b_case = case(source[j]); assert a_case and b_case
        stem = forms[rank % len(forms)].format(a=a_case[0].lower()+a_case[1:], b=b_case[0].lower()+b_case[1:])
        explanation = f'Primera situación: {source[i][4]} Segunda situación: {source[j][4]}'
        items.append([source[i][0], stem, choices, 0, explanation, i, j])
        if len(items) == 1000:
            break
    if len(items) == 1000:
        break

assert len(items) == 1000, len(items)
assert len(set(q[1] for q in items)) == 1000
assert all(len(set(q[2])) == 4 for q in items)
assert len(set(q[5] for q in items)) == len(eligible)
out = ROOT / 'questions-advanced.js'
out.write_text('window.QUESTIONS = ' + json.dumps(items, ensure_ascii=False, separators=(',', ':')) + ';\n', encoding='utf-8')
print(f'{len(items)} questions, {len(eligible)} focal concepts, {len(by_cat)} areas, {out.stat().st_size} bytes')
