"""Original single-case items. One family is sampled at most once per exam."""
FAMILIES = []
def add(category, topic, question, options, rules, rows):
    cases = []
    for line in rows.strip().splitlines():
        key, case = line.strip().split('|', 1)
        cases.append((case.strip(), int(key)))
    assert len(cases) == 10, (topic, len(cases))
    assert len(options) == len(rules) == 4
    FAMILIES.append((category, topic, question, options, rules, cases))

add('Epidemiología','Eventos poblacionales','¿Cómo se denomina el evento descrito?',
['Brote o epidemia local','Endemia','Epizootia','Pandemia'],
['Un aumento sobre lo esperado en lugar y período definidos indica brote o epidemia.','La endemia implica presencia habitual en una zona.','La epizootia afecta de forma inusual a una población animal.','La pandemia implica extensión internacional o intercontinental.'],'''
0|Una localidad notifica en una semana un número de casos humanos claramente superior a lo esperado para ese período.
1|Una enfermedad mantiene presencia habitual y persistente en un territorio a lo largo de varios años.
2|Los vecinos comunican enfermedad y muerte inusuales entre animales de crianza de una misma región.
3|Una epidemia se extiende a numerosos países de varios continentes.
0|El equipo compara el nivel esperado con los casos actuales y encuentra un incremento localizado que requiere investigación.
1|La presencia sostenida del evento forma parte del patrón habitual de la zona y no constituye por sí sola un aumento inesperado.
2|La alerta describe una propagación extraordinaria de enfermedad entre poblaciones de animales.
3|El evento epidémico sobrepasa fronteras y presenta una expansión extensa internacional.
0|Varias personas del mismo distrito enferman en un intervalo corto y la frecuencia supera el patrón esperado.
2|La notificación inicial se origina por mortalidad animal inusual, antes de confirmar enfermedad en seres humanos.
''')
add('Determinantes','Determinantes de salud','¿Qué componente explica más directamente el hallazgo destacado?',
['Posición socioeconómica estructural','Condiciones materiales de vida','Circunstancias psicosociales','Acceso y organización de servicios'],
['La posición social se relaciona con distribución de educación, ingreso y oportunidades.','Las condiciones materiales incluyen vivienda, agua y ambiente físico.','Las circunstancias psicosociales comprenden estrés y apoyos.','El acceso depende también de barreras y organización de la atención.'],'''
0|Dos grupos tienen oportunidades educativas y laborales desiguales que condicionan sus posibilidades de alcanzar salud.
1|Una familia vive en hacinamiento y no dispone de agua segura ni saneamiento.
2|La violencia persistente y la falta de apoyo generan estrés sostenido en una usuaria.
3|El horario del establecimiento impide acudir a controles a quienes trabajan durante toda la jornada de atención.
0|La investigación relaciona desigualdades sanitarias con la distribución del ingreso y la posición de los grupos sociales.
1|La exposición destacada es una vivienda húmeda y sin condiciones adecuadas de ventilación.
2|El problema descrito es aislamiento social y tensión continua, sin que el caso se centre en ingreso o vivienda.
3|Una comunidad encuentra barreras para recibir atención por la forma en que se programan las citas.
1|El equipo interviene sobre agua, residuos y características físicas del entorno donde viven las familias.
0|Se estudia cómo la ubicación en la estructura social distribuye recursos y oportunidades de forma desigual.
''')
add('Comunidad','ASIS y planificación local','¿Qué herramienta o componente corresponde?',
['Análisis de situación de salud','Plan de salud local','Cronograma de actividades','Seguimiento y evaluación del plan'],
['El ASIS integra daños, determinantes y necesidades para orientar prioridades.','El plan organiza objetivos, intervenciones, actores y recursos.','El cronograma establece cuándo se realizan las actividades.','El seguimiento contrasta avance y resultados con metas.'],'''
0|El equipo integra mortalidad, morbilidad, demografía y determinantes con participación local para comprender las necesidades del distrito.
1|Tras el diagnóstico, se acuerdan objetivos, acciones, responsables y recursos para atender las prioridades del territorio.
2|El documento indica en qué meses se ejecutará cada intervención ya aprobada.
3|Se comparan coberturas alcanzadas con metas y se analizan las causas de retraso.
0|La actividad se centra en caracterizar la situación sanitaria y sus desigualdades antes de seleccionar intervenciones.
1|La autoridad y los actores locales organizan una respuesta territorial con objetivos y responsabilidades definidos.
2|El equipo necesita distribuir las tareas del plan a lo largo del año y fijar fechas de ejecución.
3|Una reunión revisa si las acciones realizadas produjeron los cambios previstos y acuerda ajustes.
0|La herramienta solicitada sintetiza daños y determinantes de la jurisdicción; todavía no establece un calendario de ejecución.
1|La comunidad ya priorizó problemas y ahora concreta qué hará cada actor y con qué recursos.
''')
add('Comunidad','Educación y participación','¿Qué estrategia predomina en la actividad?',
['Información','Educación mediante aprendizaje práctico','Comunicación y diálogo','Participación comunitaria en decisiones'],
['La información transmite contenidos relevantes.','La educación desarrolla conocimientos y habilidades y comprueba aprendizaje.','La comunicación incorpora intercambio y adaptación del mensaje.','La participación implica intervenir en decisiones y acciones colectivas.'],'''
0|El establecimiento entrega un afiche con horarios y signos de alarma, sin interacción posterior en esa actividad.
1|La madre practica la preparación de un alimento y la enfermera verifica cómo aplica lo aprendido.
2|Durante la consejería, el personal escucha dudas y adapta sus explicaciones para llegar a un acuerdo comprensible.
3|Los vecinos eligen prioridades sanitarias y deciden junto al equipo cómo usar recursos comunitarios.
0|Se difunde un aviso sobre una jornada sanitaria para que la población conozca lugar y fecha.
1|Los agentes comunitarios realizan una demostración y reciben retroalimentación hasta dominar la habilidad.
2|El profesional identifica qué comprendió la familia y responde a sus preocupaciones mediante intercambio de mensajes.
3|La comunidad interviene en el diseño y evaluación de un proyecto, además de recibir sus beneficios.
1|Se observa al usuario ejecutar una técnica de autocuidado para corregir errores y comprobar aprendizaje.
3|Representantes vecinales participan en la selección de las acciones que se implementarán en su sector.
''')
add('Ambiente y seguridad','Residuos sanitarios','¿Qué etapa del manejo de residuos se describe?',
['Minimización','Segregación','Almacenamiento temporal','Transporte interno'],
['La minimización reduce generación de residuos.','La segregación separa por tipo en el punto de generación.','El almacenamiento conserva temporalmente en condiciones previstas.','El transporte interno desplaza residuos dentro del establecimiento.'],'''
0|El servicio ajusta el consumo para generar menos residuos sin comprometer los cuidados necesarios.
1|Al terminar un procedimiento se deposita cada residuo en el recipiente que corresponde a su tipo.
2|Los residuos permanecen en un lugar previsto y acondicionado antes de su siguiente traslado.
3|El personal moviliza los residuos por la ruta definida desde las áreas de generación al punto de almacenamiento.
0|La intervención busca evitar materiales y empaques innecesarios desde el momento de la adquisición y uso.
1|La separación se realiza inmediatamente donde se produce el residuo, evitando mezclas posteriores.
2|La supervisión verifica las condiciones del espacio en que los residuos esperan su recolección.
3|Se revisan carros, horarios y recorridos utilizados para desplazar residuos dentro del establecimiento.
1|Una enfermera identifica el tipo de residuo antes de descartarlo en el recipiente correspondiente de la unidad.
0|El indicador evalúa reducción de la cantidad de residuos generados por una práctica sin perder seguridad asistencial.
''')
add('Ética e interculturalidad','Principios bioéticos','¿Qué principio se aplica de manera más directa?',
['Autonomía','Beneficencia','No maleficencia','Justicia'],
['La autonomía protege decisiones informadas y libres.','La beneficencia busca el bienestar de la persona.','La no maleficencia exige evitar daño prevenible.','La justicia implica distribución y trato equitativos según necesidades.'],'''
0|Una persona capaz rechaza un procedimiento después de comprender alternativas y consecuencias; el equipo respeta su decisión.
1|Se elige el cuidado que ofrece mayor bienestar esperado a la paciente, considerando sus necesidades.
2|Se retira una intervención innecesaria para evitar un daño prevenible que supera su posible beneficio.
3|Los recursos escasos se asignan con criterios clínicos transparentes y sin favoritismo.
0|El profesional proporciona información comprensible para que la usuaria decida sin presión.
1|La intervención se fundamenta en el beneficio que puede aportar al bienestar de la persona.
2|El equipo identifica y elimina un riesgo evitable que podría lesionar a la paciente durante el procedimiento.
3|Se garantiza la misma calidad de atención a personas con necesidades equivalentes, sin discriminar por origen.
0|La usuaria participa en la elección entre opciones válidas de cuidado de acuerdo con sus preferencias informadas.
3|Una programación prioriza a quienes tienen mayor necesidad clínica con reglas aplicables a todos los usuarios.
''')
add('Ética e interculturalidad','Interculturalidad y prácticas','¿Qué concepto describe con precisión la situación?',
['Pertinencia cultural del cuidado','Medicina complementaria','Medicina alternativa','Estigma'],
['La pertinencia adapta la comunicación y la atención al contexto cultural con seguridad.','Una práctica complementaria se utiliza junto a la atención convencional.','Una práctica alternativa sustituye a la atención convencional.','El estigma atribuye etiquetas negativas a un grupo o persona.'],'''
0|Una mujer quechuahablante recibe explicación comprensible en su lengua y participa en acuerdos de cuidado compatibles con su contexto.
1|Una persona utiliza una práctica tradicional junto con su tratamiento convencional y consulta sobre su compatibilidad.
2|La usuaria decide reemplazar por completo el tratamiento convencional por una terapia no convencional.
3|Se asignan características negativas a una población por su origen cultural, antes de valorar a sus integrantes individualmente.
0|El establecimiento incorpora prácticas culturales seguras y una comunicación que permita comprender las decisiones de atención.
1|La intervención no convencional se suma al tratamiento habitual, sin sustituirlo.
2|La familia propone abandonar la atención convencional y utilizar exclusivamente otro sistema terapéutico.
3|Un grupo es etiquetado como incapaz de seguir tratamientos únicamente por su pertenencia étnica.
0|La gestante participa en decisiones sobre una atención con adecuación cultural y condiciones de seguridad.
1|El equipo evalúa una práctica que se mantiene como apoyo junto con la atención médica convencional.
''')
add('Investigación','Diseños de investigación','¿Qué diseño se describe?',
['Descriptivo transversal','Observacional analítico','Experimental','Cualitativo'],
['El descriptivo transversal caracteriza una población en un corte temporal.','El observacional analítico compara grupos para estudiar asociaciones sin asignar exposición.','El experimental introduce una intervención para evaluar sus efectos.','El cualitativo explora experiencias y significados.'],'''
0|Se encuesta una vez a la población para describir sus hábitos, sin comparar factores de riesgo ni asignar intervenciones.
1|Se comparan personas expuestas y no expuestas para estudiar asociación con enfermedad, sin que el investigador asigne la exposición.
2|El investigador asigna una intervención educativa y evalúa su efecto frente a una condición de comparación.
3|Se realizan entrevistas para comprender qué significa para las familias convivir con una enfermedad.
0|El objetivo es estimar la frecuencia de una característica en una fecha definida, sin seguimiento posterior.
1|El análisis contrasta grupos para explorar una asociación entre exposición y daño observados en la práctica.
2|La característica central es que el investigador introduce deliberadamente la intervención que desea evaluar.
3|El estudio interpreta relatos y experiencias para comprender barreras percibidas por los usuarios.
1|Se busca explicar diferencias de enfermedad entre grupos mediante comparación, sin manipular la exposición.
0|El informe describe prevalencias en un único corte y no pretende demostrar causalidad.
''')
add('Investigación','Calidad de instrumentos','¿Qué propiedad se está evaluando?',
['Validez de contenido','Validez de criterio','Validez de constructo','Confiabilidad'],
['El contenido se evalúa verificando representación de los aspectos relevantes del tema.','La de criterio compara con una referencia pertinente.','La de constructo examina coherencia con el concepto teórico.','La confiabilidad evalúa consistencia o reproducibilidad de la medición.'],'''
0|Expertos revisan si un cuestionario cubre los componentes importantes del tema que pretende medir.
1|Una nueva medición se compara con una referencia aceptada para valorar su correspondencia.
2|Se estudia si la estructura de una escala se comporta como predice la teoría del concepto de ansiedad.
3|Se comprueba si el instrumento produce resultados semejantes en condiciones equivalentes de medición.
0|La revisión identifica que faltan preguntas sobre una dimensión esencial del conocimiento evaluado.
1|El desempeño de la prueba se contrasta con un estándar externo relevante para el mismo fenómeno.
2|Se analiza la relación entre dimensiones de una escala para comprobar que representa el concepto teórico previsto.
3|Dos mediciones repetidas del mismo fenómeno en condiciones estables muestran alta concordancia.
0|La pregunta editorial es si los ítems representan adecuadamente el universo de contenidos, no si repiten el mismo valor.
3|El equipo evalúa estabilidad y consistencia de los resultados, sin afirmar por ello que se mida el concepto correcto.
''')
add('Gestión','Planeamiento institucional','¿Qué instrumento corresponde a la necesidad descrita?',
['Plan Estratégico Institucional','Plan Operativo Institucional','Reglamento de Organización y Funciones','Manual de Operaciones'],
['El PEI define la orientación y objetivos estratégicos institucionales.','El POI organiza actividades operativas, metas y recursos.','El ROF formaliza estructura y funciones de la entidad.','El MOP desarrolla organización y operaciones en los ámbitos a los que corresponde.'],'''
0|La entidad necesita establecer sus objetivos estratégicos y la orientación institucional de mediano plazo.
1|El establecimiento programa actividades del año, metas físicas y recursos para ejecutar los objetivos institucionales.
2|Se solicita el documento que define formalmente la estructura orgánica y funciones de la entidad pública.
3|Un programa o proyecto requiere ordenar unidades, funciones y procesos propios mediante el instrumento de gestión aplicable.
0|La discusión se centra en resultados estratégicos institucionales y no en el calendario de actividades anuales.
1|La jefatura convierte objetivos institucionales en acciones operativas con metas y asignación de recursos.
2|La entidad revisa qué órgano tiene una competencia formal dentro de su estructura organizacional.
3|Se necesita un instrumento de organización y operación para un programa en el ámbito que requiere manual de operaciones.
1|El seguimiento evalúa el cumplimiento de actividades operativas programadas y sus metas del período.
0|La planificación define la dirección estratégica que guiará la posterior programación operativa.
''')
add('Gestión','Mejora continua','¿Qué fase del ciclo PHVA predomina?',
['Planificar','Hacer','Verificar','Actuar'],
['Se analiza el problema y se diseña la mejora.','Se implementa la intervención prevista.','Se comparan resultados con las metas.','Se estandariza la mejora útil o se ajusta según lo aprendido.'],'''
0|El servicio analiza por qué ocurren errores y define una intervención y un indicador antes de aplicarla.
1|Se ejecuta a pequeña escala la intervención diseñada para mejorar la identificación de pacientes.
2|El equipo compara el indicador posterior con la meta establecida para conocer si la intervención funcionó.
3|Al comprobar beneficio, se incorpora la práctica a la rutina institucional y se organiza su sostenimiento.
0|Se establecen objetivos, responsables y forma de medir una mejora todavía no implementada.
1|La unidad pone en práctica el cambio acordado y registra su ejecución.
2|La reunión analiza resultados y determina si el cambio produjo la mejoría esperada.
3|Se modifican procedimientos y se estandariza el cambio efectivo después de revisar sus resultados.
0|La fase se concentra en diseñar cómo se resolverá el problema y cómo se comprobará el resultado.
2|La actividad central es contrastar lo obtenido con lo previsto, antes de decidir la estandarización.
''')

add('Epidemiología','Medidas epidemiológicas','¿Qué medida responde a la información solicitada?',
['Incidencia','Prevalencia','Mortalidad','Letalidad'],
['La incidencia considera casos nuevos entre población en riesgo durante un período.','La prevalencia considera casos existentes en una población.','La mortalidad relaciona defunciones con población.','La letalidad relaciona muertes por una enfermedad con quienes la padecen.'],'''
0|La microred quiere estimar la aparición de casos nuevos de dengue durante el mes entre las personas que podían enfermar.
1|Se necesita conocer qué proporción de la población vive actualmente con diabetes, incluidos diagnósticos anteriores.
2|El informe compara defunciones por tuberculosis con la población total del distrito durante el año.
3|El equipo quiere conocer qué proporción de quienes enfermaron de una infección falleció por esa enfermedad.
0|Se sigue a personas inicialmente sin el daño para registrar cuántas lo desarrollan durante el período.
1|Un corte poblacional cuenta todos los casos que existen en una fecha, sin distinguir cuándo comenzaron.
2|La dirección calcula el impacto de las muertes en la población de su jurisdicción, no solo entre los casos enfermos.
3|Se evalúa gravedad comparando fallecimientos con el total de personas diagnosticadas con el mismo evento.
1|La pregunta es cuántas personas requieren hoy atención por una enfermedad persistente, incluyendo casos nuevos y antiguos.
0|El denominador del estudio está formado por quienes podían desarrollar el evento al comenzar la observación.
''')
add('Epidemiología','Validez diagnóstica','¿Qué propiedad de la prueba se está estimando?',
['Sensibilidad','Especificidad','Valor predictivo positivo','Valor predictivo negativo'],
['La sensibilidad se calcula entre quienes tienen la enfermedad.','La especificidad se calcula entre quienes no tienen la enfermedad.','El valor predictivo positivo se calcula entre resultados positivos.','El valor predictivo negativo se calcula entre resultados negativos.'],'''
0|Entre las personas con enfermedad confirmada se calcula qué proporción obtuvo un resultado positivo.
1|Entre quienes no tienen la enfermedad se determina cuántos fueron correctamente identificados como negativos.
2|La prueba salió positiva y se desea conocer la probabilidad de que ese resultado corresponda a enfermedad real.
3|La prueba salió negativa y la persona pregunta qué probabilidad existe de que realmente no tenga la enfermedad.
0|La validación se centra en la capacidad de reconocer enfermos y reducir falsos negativos.
1|El objetivo es identificar correctamente a los sanos y reducir falsos positivos.
2|Se divide el número de verdaderos positivos entre todos los resultados positivos del tamizaje.
3|Se divide el número de verdaderos negativos entre todas las pruebas que resultaron negativas.
0|El denominador está compuesto por todos los enfermos, con independencia del resultado de su prueba.
1|El denominador incluye únicamente a quienes la referencia diagnóstica clasificó sin enfermedad.
''')
add('Epidemiología','Causalidad','¿Qué criterio de causalidad se ilustra?',
['Temporalidad','Consistencia','Gradiente biológico','Plausibilidad biológica'],
['La exposición debe preceder al efecto.','La consistencia se apoya en hallazgos semejantes en distintos estudios.','El gradiente describe cambios de riesgo según magnitud de exposición.','La plausibilidad considera un mecanismo biológico compatible.'],'''
0|Antes de sostener causalidad se comprueba que la exposición ocurrió antes del comienzo de la enfermedad.
1|Investigaciones independientes en poblaciones diferentes encuentran una asociación semejante.
2|A medida que aumenta la intensidad de la exposición, aumenta también el riesgo observado del daño.
3|La asociación puede explicarse por un mecanismo compatible con el conocimiento biológico disponible.
0|Se descarta una interpretación causal cuando el supuesto factor apareció después del evento estudiado.
1|El resultado inicial vuelve a observarse al repetir el estudio en otras localidades y con otros equipos.
2|Las categorías de mayor dosis acumulada presentan un riesgo progresivamente mayor.
3|La discusión analiza si existe una vía fisiopatológica razonable que conecte el factor con el efecto.
1|Una sola investigación no se toma como suficiente y se compara su resultado con evidencia de otros contextos.
0|El aspecto decisivo es establecer la secuencia entre exposición y aparición del evento, no solo su coexistencia.
''')
add('Epidemiología','Historia natural','¿Qué período de la historia natural se describe?',
['Prepatogénico','Patogénico subclínico','Clínico','Desenlace'],
['En el prepatogénico interactúan riesgos antes del inicio de enfermedad.','En el subclínico el proceso comenzó sin manifestaciones clínicas reconocibles.','En el clínico aparecen signos o síntomas.','El desenlace comprende recuperación, secuelas o muerte.'],'''
0|Una comunidad susceptible convive con factores de riesgo, pero el proceso de enfermedad todavía no se ha iniciado.
1|El agente ya actúa en el organismo, aunque aún no se presentan signos ni síntomas identificables.
2|La persona desarrolla fiebre y otros hallazgos reconocibles que expresan la enfermedad.
3|El proceso termina con recuperación, persistencia de secuelas o fallecimiento.
0|Se analiza la interacción de agente, huésped y ambiente antes de que la persona enferme.
1|Una alteración puede detectarse mediante una prueba antes de que la persona perciba manifestaciones.
2|Una lesión sintomática motiva consulta y marca la fase manifiesta de la enfermedad.
3|El seguimiento documenta la recuperación y la presencia o ausencia de discapacidad residual.
1|La enfermedad está en curso, pero el caso aún no ha cruzado el horizonte de manifestaciones clínicas.
0|El objeto de estudio es la susceptibilidad y la exposición previas al comienzo del proceso patológico.
''')
add('Prevención','Niveles de prevención','¿Qué nivel de prevención predomina?',
['Primaria','Secundaria','Terciaria','Cuaternaria'],
['La primaria reduce aparición del daño antes de enfermedad.','La secundaria detecta y atiende tempranamente.','La terciaria reduce secuelas y discapacidad.','La cuaternaria previene daño por intervenciones innecesarias.'],'''
0|Se mejora una fuente de agua para reducir la exposición de una comunidad antes de que aparezcan nuevos casos.
1|Se realiza un tamizaje en personas sin síntomas para detectar tempranamente un problema de salud.
2|Una persona con secuelas de un accidente cerebrovascular recibe rehabilitación para recuperar autonomía.
3|Se evita un medicamento sin indicación después de valorar sus riesgos y ausencia de beneficio esperado.
0|Una población susceptible recibe vacunación para evitar una enfermedad específica.
1|La campaña busca identificar enfermedad todavía no conocida y asegurar su evaluación oportuna.
2|El cuidado de una enfermedad establecida incluye acciones para reducir discapacidad y complicaciones funcionales.
3|Se decide no repetir un examen innecesario que podría generar procedimientos y diagnósticos evitables.
1|La intervención se dirige a personas asintomáticas con el propósito de reconocer un daño en una etapa temprana.
0|La actividad modifica un riesgo ambiental antes de la aparición de la enfermedad que se busca prevenir.
''')
add('Epidemiología','Vigilancia','¿Qué modalidad de vigilancia se describe?',
['Activa','Pasiva','Centinela','Basada en laboratorio'],
['La activa busca deliberadamente casos.','La pasiva recibe reportes del sistema habitual.','La centinela utiliza establecimientos o unidades seleccionadas para seguir tendencias.','La basada en laboratorio utiliza resultados laboratoriales para detectar y seguir eventos.'],'''
0|El personal sale a los domicilios para buscar casos compatibles con una alerta epidemiológica.
1|La unidad recibe los reportes regulares que envían los establecimientos, sin salir a buscar los casos.
2|Se selecciona un conjunto de servicios que aporta información sistemática para seguir tendencias del evento.
3|El sistema utiliza resultados de pruebas para detectar cambios en la circulación de un agente.
0|Ante un incremento sospechoso, el equipo revisa registros y visita familias para encontrar casos no notificados.
1|La vigilancia depende de las comunicaciones habituales que generan los servicios al identificar casos.
2|No participan todos los establecimientos; unidades elegidas aportan datos continuos bajo un esquema definido.
3|El análisis destaca los reportes de confirmación y caracterización producidos por laboratorios.
0|Se entrevista deliberadamente a contactos para identificar personas que no habían acudido a consulta.
1|El establecimiento comunica los casos que identifica durante su atención rutinaria al sistema de vigilancia.
''')

add('Enfermería','Administración segura','¿Qué acción debe priorizar enfermería?',
['Verificar la identidad antes de administrar','Interrumpir la administración y valorar una posible reacción','Restablecer la técnica aséptica comprometida','Documentar y comunicar el error identificado'],
['La discrepancia de identidad debe resolverse antes de administrar.','Una posible reacción durante la administración requiere valoración inmediata y respuesta según protocolo.','El contacto contaminante obliga a corregir la técnica antes de continuar.','Un error identificado requiere registro y comunicación por el procedimiento institucional.'],'''
0|La orden corresponde a una persona con el mismo apellido, pero el identificador del brazalete no coincide.
1|Durante la administración de un medicamento aparece una manifestación súbita compatible con reacción adversa y la infusión continúa.
2|Un material estéril cae sobre una superficie no estéril antes de utilizarse en el procedimiento.
3|Se descubre un error ya interceptado; la persona no recibió el medicamento, pero falta registrarlo y comunicarlo.
0|El número de cama coincide con la hoja, pero nombre y otro identificador no corresponden al paciente presente.
1|La paciente desarrolla síntomas inesperados mientras recibe el fármaco y requiere evaluación de seguridad en ese momento.
2|La enfermera toca con guantes estériles un objeto no estéril y se dispone a continuar la curación.
3|Una discrepancia de registro fue corregida; aún debe quedar constancia trazable del error y de la conducta adoptada.
0|Dos pacientes tienen nombres similares y todavía no se ha contrastado la orden con los identificadores establecidos.
2|El campo estéril perdió su integridad y el equipo considera continuar porque no observa suciedad.
''')
add('Enfermería','Uso racional de medicamentos','¿Qué dimensión del uso racional debe revisarse de manera principal?',
['Pertinencia de la indicación','Adecuación de la dosis individual','Duración y frecuencia prescritas','Adherencia y forma de administración'],
['El medicamento debe responder a una necesidad clínica.','La dosis se ajusta a características individuales relevantes.','La pauta debe respetar intervalos y duración indicados.','La adherencia exige comprobar cómo se sigue realmente la pauta.'],'''
0|Una persona con cuadro viral no complicado solicita antibióticos, sin evidencia de una indicación que los justifique.
1|Antes de administrar, se observa que la dosis no fue contrastada con el peso y las condiciones clínicas relevantes de la persona.
2|La familia cambia por cuenta propia los intervalos y acorta el tiempo de tratamiento indicado.
3|El paciente afirma cumplir el tratamiento, pero al explicar su rutina reconoce olvidos frecuentes.
0|Se plantea añadir un fármaco sin identificar qué problema clínico trataría ni qué beneficio se espera.
1|La prescripción necesita revisión porque un dato individual relevante para la dosificación cambió desde el control anterior.
2|El usuario agrupa todas las dosis del día en una sola toma pese a una pauta con intervalos definidos.
3|La enfermera utiliza preguntas y demostración para comprobar si la persona entiende y aplica las instrucciones.
0|El equipo revisa una prescripción innecesaria que aumenta riesgos y costos sin una necesidad clínica identificada.
3|La falta de mejoría obliga a explorar si el medicamento se tomó realmente como fue indicado antes de atribuir fracaso terapéutico.
''')
add('Enfermería','Finalidades del cuidado','¿Cuál es la finalidad principal de la intervención descrita?',
['Prevención','Recuperación','Rehabilitación','Cuidado paliativo'],
['La prevención busca evitar enfermedad o complicaciones.','La recuperación acompaña la mejoría durante la enfermedad.','La rehabilitación busca recuperar o mantener funcionalidad.','El cuidado paliativo alivia sufrimiento y mejora calidad de vida ante enfermedad grave.'],'''
0|Una persona susceptible recibe inmunización antes de desarrollar la enfermedad que se desea evitar.
1|Durante una infección, enfermería vigila síntomas y respuesta al manejo indicado para favorecer la mejoría.
2|Después de un accidente cerebrovascular se entrenan actividades para recuperar movilidad y autonomía.
3|Una persona con enfermedad avanzada recibe control de dolor y apoyo emocional centrados en su calidad de vida.
0|Se educa a una familia sobre medidas que disminuyan el riesgo de aparición de un daño todavía no presente.
1|La enfermera controla hidratación y evolución clínica de una persona durante su enfermedad aguda.
2|Tras una lesión se practican tareas que permitan recuperar el autocuidado cotidiano.
3|El plan prioriza aliviar síntomas y sufrimiento, además de respetar las preferencias de una persona con enfermedad grave.
2|Una adulta con secuelas recibe ejercicios y adaptación de actividades para mantener la mayor independencia posible.
1|El cuidado se centra en vigilar la evolución de una herida tratada y prevenir complicaciones durante su mejoría.
''')
add('Problemas prioritarios','Transmisión en atención de salud','¿Qué mecanismo de transmisión se describe?',
['Contacto directo','Contacto indirecto','Gotas respiratorias','Vía aérea'],
['El contacto directo ocurre por transferencia sin un objeto intermediario.','El contacto indirecto incorpora manos u objetos contaminados como intermediarios.','Las gotas respiratorias alcanzan mucosas a corta distancia según el contexto de exposición.','La vía aérea implica partículas infecciosas que pueden permanecer suspendidas.'],'''
0|La exposición descrita ocurre por contacto físico entre una zona infectada de una persona y otra susceptible, sin objeto intermediario.
1|Un equipo contaminado no se procesa entre pacientes y actúa como vehículo para transferir microorganismos.
2|La situación describe secreciones respiratorias expulsadas a corta distancia que alcanzan las mucosas de otra persona.
3|El riesgo señalado proviene de partículas infecciosas suspendidas en un ambiente mal ventilado.
1|Las manos del personal trasladan microorganismos desde una superficie contaminada hacia otra paciente.
0|La transferencia ocurre entre personas mediante contacto físico inmediato con la zona contaminada.
2|Una persona susceptible recibe gotas respiratorias sobre mucosas durante un contacto cercano con alguien que tose.
3|El análisis de tuberculosis en una sala cerrada enfatiza la inhalación de partículas infecciosas suspendidas.
1|Un dispositivo reutilizado sin el procesamiento requerido constituye el intermediario de la transmisión.
0|En la exposición evaluada no participan instrumental, superficies ni otro objeto que sirva de vehículo.
''')
add('Problemas prioritarios','Enfermedades metaxénicas y zoonóticas','¿Qué asociación entre exposición y enfermedad es la más pertinente?',
['Dengue: mosquito Aedes','Malaria: mosquito Anopheles','Leptospirosis: agua contaminada con orina animal','Rabia: exposición a saliva de animal infectado'],
['Aedes es el principal vector del dengue.','Anopheles transmite malaria.','La leptospirosis puede transmitirse por agua o suelo contaminados con orina de animales infectados.','La exposición a saliva de un animal potencialmente infectado requiere evaluación por riesgo de rabia.'],'''
0|El equipo de una localidad con dengue elimina recipientes que acumulan agua y sirven de criaderos del vector.
1|En una zona con malaria se organiza vigilancia específica del mosquito transmisor de esa enfermedad.
2|Después de una inundación, la persona caminó por agua contaminada con orina de roedores y ahora requiere evaluación por fiebre.
3|Una mordedura de un mamífero potencialmente infectado expuso la herida a su saliva y requiere valoración inmediata.
0|La intervención busca reducir la reproducción de Aedes en depósitos domiciliarios de una localidad con transmisión viral.
1|La investigación relaciona casos de malaria con exposición al vector Anopheles en el territorio.
2|La exposición destacada es contacto de piel lesionada con agua de inundación contaminada por animales.
3|Se evalúa una exposición de mucosa a saliva de un animal con sospecha de rabia.
0|La pregunta requiere identificar el vector de dengue, diferenciándolo del transmisor de malaria.
2|La familia comparte una fuente de agua posiblemente contaminada con orina animal; el equipo investiga una zoonosis asociada a esa vía.
''')
add('Curso de vida','Parto y puerperio','¿A qué período corresponde la situación?',
['Dilatación','Expulsivo','Alumbramiento','Puerperio'],
['La dilatación comprende los cambios cervicales previos al nacimiento.','El expulsivo culmina con el nacimiento del bebé.','El alumbramiento corresponde a la expulsión de la placenta.','El puerperio es el período de recuperación posterior al parto.'],'''
0|Durante el trabajo de parto se vigilan los cambios cervicales y aún no se ha producido el nacimiento.
1|El cuello está completamente dilatado y el proceso se dirige al nacimiento del bebé.
2|El bebé ya nació y se espera la expulsión de la placenta, verificando luego su integridad.
3|En las semanas posteriores al parto se sigue la recuperación de la madre, incluida la involución uterina.
0|La valoración registra progresión cervical durante la primera etapa del trabajo de parto.
1|La etapa observada termina cuando nace el bebé, antes de la salida de la placenta.
2|La atención se concentra en la salida de los anexos placentarios después del nacimiento.
3|La madre acude al control posparto para vigilancia de loquios, involución y recuperación general.
2|El nacimiento ya ocurrió, pero la placenta todavía no ha sido expulsada.
3|La consulta corresponde al seguimiento materno después de finalizado el parto, no a una etapa de dilatación.
''')
add('Curso de vida','Climaterio y salud integral','¿Qué afirmación es la más adecuada?',
['Aún no se confirma menopausia por ese tiempo de amenorrea','La menopausia requiere 12 meses de amenorrea sin otra causa','Los síntomas requieren valoración integral individual','La irregularidad menstrual por sí sola no confirma menopausia'],
['Un período menor al criterio de 12 meses no basta para confirmación retrospectiva.','El criterio temporal se interpreta después de excluir otras causas de amenorrea.','El cuidado integra síntomas, riesgos, necesidades y preferencias de la mujer.','Las variaciones del ciclo necesitan interpretación clínica y no equivalen por sí solas a menopausia.'],'''
0|Una mujer lleva cuatro meses sin menstruar y pregunta si ese tiempo basta para afirmar que ya ocurrió la menopausia.
1|La consulta solicita el criterio retrospectivo que permite reconocer menopausia cuando se descartaron otras causas de amenorrea.
2|Una mujer con bochornos y dificultades de sueño solicita ayuda para decidir cómo afrontar sus molestias y riesgos personales.
3|La usuaria presenta ciclos de duración variable, pero continúa menstruando y pregunta si la irregularidad confirma menopausia.
0|Después de siete meses de amenorrea, una mujer considera que el dato temporal ya confirma por sí solo menopausia.
1|El equipo debe explicar el período consecutivo sin menstruación necesario para reconocer retrospectivamente menopausia.
2|El cuidado debe abordar molestias, salud mental y riesgos de la mujer en su contexto, evitando una indicación igual para todas.
3|Una persona asocia un solo ciclo menstrual irregular con el diagnóstico definitivo de menopausia.
0|La amenorrea lleva nueve meses y todavía se investigan otras causas posibles; la usuaria pide una conclusión definitiva.
2|Dos mujeres de edad semejante tienen síntomas y necesidades diferentes y solicitan un plan adaptado a cada una.
''')
add('Curso de vida','Cuidado integral y etapa de vida','¿Qué paquete o enfoque corresponde de forma más específica?',
['Atención integral del adolescente','Atención integral del joven','Atención integral del adulto','Atención integral del adulto mayor'],
['El adolescente requiere cuidado adaptado a su etapa, privacidad y valoración integral.','La atención del joven integra necesidades y riesgos propios de su etapa.','El adulto requiere evaluación integral de riesgos y autocuidado.','El adulto mayor requiere además valoración funcional, mental, nutricional y sociofamiliar.'],'''
0|Una persona de 15 años recibe evaluación de nutrición, salud mental, vacunas y necesidades sexuales en un espacio privado.
1|Una persona de 22 años acude para valoración integral y consejería adaptada a su etapa de vida.
2|Un hombre de 46 años recibe evaluación de presión arterial, riesgos metabólicos, hábitos y tamizajes indicados.
3|Una mujer de 72 años necesita valoración de autonomía, caídas, memoria, nutrición y red de apoyo.
0|El plan de una usuaria de 16 años incorpora prevención de violencia, salud mental y orientación sexual con privacidad.
1|Un usuario de 24 años consulta por riesgos laborales, salud sexual y hábitos dentro de su cuidado integral.
2|La persona de 50 años requiere seguimiento de factores de riesgo cardiovascular y prevención según sus necesidades.
3|El usuario de 78 años presenta dependencia para actividades cotidianas y necesita un plan con su familia.
0|El equipo adapta la atención de una persona de 14 años, incluyendo su desarrollo y necesidades psicosociales.
3|En una mujer de 69 años se revisa el estado cognitivo y funcional además de las enfermedades conocidas.
''')
add('Enfermería','Continuidad asistencial','¿Qué acción o proceso corresponde?',
['Referencia','Contrarreferencia','Interconsulta','Estabilización inicial'],
['La referencia deriva a un establecimiento con capacidad requerida.','La contrarreferencia devuelve información y continuidad al origen.','La interconsulta solicita valoración de otro profesional sobre un caso.','La estabilización atiende necesidades urgentes antes o durante la coordinación del traslado.'],'''
0|Un puesto no dispone de la capacidad necesaria y coordina que la paciente sea atendida en un establecimiento de mayor resolución.
1|Después de la atención hospitalaria, se envían indicaciones y resumen al establecimiento de origen para seguimiento.
2|El profesional solicita la opinión de otra especialidad para orientar un caso, manteniendo la atención en el mismo servicio.
3|Una persona inestable requiere medidas inmediatas disponibles mientras se organiza su traslado a otro establecimiento.
0|El equipo documenta el motivo y coordina el envío de una paciente cuyo problema supera sus recursos locales.
1|El hospital retorna la información y el plan para que el primer nivel continúe los controles.
2|Una enfermera coordina una valoración especializada que complemente el manejo sin que se describa un retorno al origen.
3|Ante una emergencia, no se espera completar todos los documentos para comenzar las medidas iniciales de soporte disponibles.
0|La decisión se basa en la capacidad resolutiva insuficiente del establecimiento de procedencia.
1|Se evalúa la llegada oportuna del informe posterior a la atención de la paciente en el nivel de mayor complejidad.
''')
add('Problemas prioritarios','Prevención de enfermedades crónicas','¿Qué intervención responde de forma más específica al objetivo?',
['Identificación y reducción de factores de riesgo','Detección temprana de enfermedad no conocida','Seguimiento de adherencia y autocuidado','Valoración de complicaciones y necesidad de referencia'],
['Se actúa sobre exposiciones modificables antes del daño.','Se busca identificar enfermedad en personas sin diagnóstico previo.','Se acompaña el cumplimiento del plan y las habilidades de autocuidado.','Los hallazgos de posible complicación requieren evaluación y decisión oportuna.'],'''
0|Una persona sin diagnóstico recibe apoyo para actividad física, alimentación y abandono de tabaco según sus riesgos.
1|En una campaña se mide presión arterial para identificar posibles casos de hipertensión no conocida.
2|Una paciente con diabetes explica cómo sigue su tratamiento y cuida sus pies; se resuelven barreras para cumplir el plan.
3|Una persona con enfermedad crónica presenta un cambio clínico preocupante y el equipo valora si necesita atención de mayor capacidad.
0|El equipo trabaja con población sedentaria para disminuir exposiciones asociadas a diabetes y enfermedad cardiovascular.
1|La intervención ofrece evaluación a personas sin diagnóstico para reconocer tempranamente un problema metabólico.
2|En un control se revisan conocimientos, práctica y dificultades para mantener el cuidado acordado de una enfermedad ya conocida.
3|Se identifica una lesión en una persona con diabetes y se organiza evaluación de su gravedad y manejo oportuno.
0|La actividad se centra en modificar hábitos de riesgo antes de confirmar una enfermedad crónica.
2|La persona ya tiene diagnóstico y el objetivo es sostener el tratamiento y las medidas de autocuidado indicadas.
''')

add('Problemas prioritarios','Tuberculosis: métodos','¿Qué método o resultado se describe?',
['Baciloscopía','Cultivo','Prueba molecular','Prueba de sensibilidad a medicamentos'],
['La baciloscopía busca bacilos mediante microscopía.','El cultivo identifica crecimiento del microorganismo en medios apropiados.','La prueba molecular detecta material genético y, según el ensayo, resistencia específica.','La sensibilidad evalúa la respuesta del bacilo a medicamentos.'],'''
0|El laboratorio examina una muestra de esputo al microscopio para identificar bacilos ácido-alcohol resistentes.
1|La confirmación se obtiene por crecimiento del bacilo en un medio de laboratorio, no solo por observación directa.
2|Se detecta ADN del bacilo y una señal de posible resistencia a rifampicina en una misma prueba rápida.
3|El equipo necesita conocer a qué medicamentos es susceptible el microorganismo para orientar el manejo especializado.
0|El informe describe búsqueda microscópica de bacilos en la muestra respiratoria recibida.
1|Un resultado confirma la multiplicación del microorganismo en un medio utilizado por el laboratorio.
2|La técnica amplifica secuencias genéticas del agente a partir de una muestra clínica.
3|Tras identificar tuberculosis, se estudia el comportamiento del bacilo frente a fármacos antituberculosos.
2|La pregunta clínica requiere una prueba que aporte detección genética del bacilo y resistencia específica según su plataforma.
0|El procedimiento destacado es una lectura microscópica de esputo, sin amplificación genética ni crecimiento en medio.
''')
add('Problemas prioritarios','Tuberculosis: controles','¿Qué tipo de medida predomina?',
['Control administrativo','Control ambiental','Protección respiratoria personal','Apoyo social durante el tratamiento'],
['La organización de la atención reduce exposición y demoras.','La ventilación y otras medidas del ambiente reducen el riesgo.','El respirador indicado protege al trabajador expuesto.','El apoyo alimentario y social ayuda al cuidado integral.'],'''
0|El establecimiento reorganiza el flujo para identificar y atender oportunamente a personas con sospecha de tuberculosis.
1|Se mejora la ventilación de una sala para reducir la concentración de partículas infecciosas en el aire.
2|La enfermera utiliza el respirador indicado para ingresar a un área de riesgo de tuberculosis.
3|Se orienta a una familia afectada por tuberculosis sobre el apoyo alimentario PANTBC y la continuidad del tratamiento.
0|Se establece un circuito para evitar que personas con sospecha permanezcan largo tiempo en una sala de espera cerrada.
1|El equipo revisa el flujo de aire y las condiciones físicas de los ambientes donde se atienden casos respiratorios.
2|Se verifica el uso adecuado del equipo de protección respiratoria del personal según el riesgo de exposición.
3|La visita identifica inseguridad alimentaria y se coordina apoyo disponible para la persona en tratamiento.
0|La jefatura define responsabilidades y procedimientos de identificación oportuna de sintomáticos en el servicio.
1|Se acondiciona una zona de atención para favorecer renovación del aire, además de mantener los otros controles.
''')
add('Problemas prioritarios','Seguimiento de anemia','¿Qué actividad corresponde principalmente al caso?',
['Tamizaje','Suplementación preventiva','Seguimiento de adherencia','Reevaluación de respuesta al tratamiento'],
['El tamizaje identifica anemia no conocida.','La suplementación preventiva se dirige a personas elegibles sin anemia diagnosticada.','La adherencia comprende cumplimiento y forma de administración.','La respuesta se valora comparando la evolución con los objetivos de tratamiento.'],'''
0|Un niño sin diagnóstico previo participa en una medición de hemoglobina para detectar anemia.
1|Un niño sin anemia recibe hierro porque cumple los criterios de prevención correspondientes a su etapa.
2|La enfermera pide a la madre explicar cómo ofrece el suplemento y cuántas dosis logró administrar.
3|En el control se compara la evolución de hemoglobina con la respuesta esperada tras el tratamiento indicado.
0|La actividad busca identificar casos nuevos de anemia entre niños que todavía no tienen ese diagnóstico.
1|Se organiza una intervención con hierro antes de la aparición de anemia en población elegible.
2|La familia refiere olvidos y se acuerdan medidas para cumplir la pauta, sin modificarla por cuenta propia.
3|El equipo integra la evolución clínica y el resultado de control para decidir si requiere otra evaluación.
2|Antes de atribuir un resultado insuficiente a fracaso terapéutico, se verifica si la pauta realmente se cumplió.
0|Una campaña obtiene hemoglobina para distinguir a quienes requieren evaluación por posible anemia.
''')
add('Problemas prioritarios','Consejería VIH','¿Qué intervención se describe?',
['Consejería preprueba','Consejería posprueba','Consejería para reducción de riesgos','Prevención maternoinfantil'],
['La preprueba prepara una decisión informada sobre el tamizaje.','La posprueba acompaña la comunicación del resultado y los pasos siguientes.','La reducción de riesgos identifica exposiciones y acuerda medidas de protección.','La prevención maternoinfantil articula la atención de madre y niño.'],'''
0|Antes del tamizaje, el profesional explica su finalidad, confidencialidad y posibles resultados para una decisión informada.
1|Al entregar un resultado de VIH, se explora la comprensión y se acuerdan los siguientes pasos de atención.
2|Durante el seguimiento se identifican exposiciones recientes y barreras para usar medidas de protección.
3|El control prenatal identifica una infección y organiza acciones de atención de la gestante y del recién nacido.
0|Una persona aún no se ha realizado la prueba y solicita conocer qué significa un resultado reactivo o no reactivo.
1|La usuaria recibe el resultado del tamizaje y necesita apoyo individual para comprenderlo y continuar la evaluación.
2|Se acuerda un plan para disminuir exposiciones sexuales de riesgo, adaptado a la situación de la persona.
3|El equipo articula el tamizaje prenatal y el seguimiento del bebé para reducir transmisión de la madre al hijo.
1|La conversación se realiza inmediatamente después de comunicar un resultado no reactivo, sin suspender la orientación preventiva.
2|Un usuario con PrEP mantiene seguimiento para revisar su situación de riesgo y las medidas complementarias de protección.
''')
add('Problemas prioritarios','Prevención oncológica','¿Qué nivel de prevención predomina?',
['Primaria','Secundaria','Terciaria','Cuaternaria'],
['La primaria actúa antes de la enfermedad para reducir su aparición.','La secundaria busca detección temprana.','La terciaria reduce discapacidad o secuelas de una enfermedad establecida.','La cuaternaria evita intervenciones innecesarias y daño por sobremedicalización.'],'''
0|Una escuela organiza vacunación contra VPH en población elegible para prevenir la infección asociada a cáncer.
1|Una mujer sin síntomas accede al tamizaje cervical indicado para identificar lesiones tempranas.
2|Tras tratamiento oncológico, una paciente realiza rehabilitación para recuperar funcionalidad y reducir secuelas.
3|Se evita una prueba sin indicación después de valorar que sus daños potenciales superan el beneficio esperado.
0|El equipo trabaja para reducir el consumo de tabaco en personas sin enfermedad oncológica diagnosticada.
1|Una estrategia invita a población elegible asintomática a realizar tamizaje colorrectal.
2|Una persona con secuelas de un tratamiento recibe cuidados para mejorar autonomía y prevenir complicaciones funcionales.
3|Se explica por qué repetir un examen sin indicación puede causar sobrediagnóstico y procedimientos evitables.
1|La actividad detecta posibles lesiones antes de que se manifieste enfermedad avanzada.
0|Se promueven hábitos saludables y reducción de factores modificables antes de la aparición del daño.
''')
add('Problemas prioritarios','Tamizajes de cáncer','¿Qué examen corresponde al objetivo señalado?',
['Mamografía','Prueba de VPH','Prueba de sangre oculta en heces','Evaluación de PSA según decisión informada'],
['La mamografía es una modalidad de tamizaje mamario en población indicada.','La prueba de VPH se emplea en estrategias de tamizaje cervical.','La sangre oculta en heces se utiliza en estrategias de tamizaje colorrectal.','La evaluación prostática requiere considerar riesgo, beneficios y límites de las pruebas.'],'''
0|Una mujer asintomática participa en una estrategia de tamizaje de cáncer de mama mediante un examen de imagen indicado.
1|La estrategia cervical busca detectar infección por el virus relacionado con lesiones de cuello uterino mediante una prueba molecular.
2|Un programa colorrectal busca sangre no visible en deposiciones de una persona sin síntomas.
3|Un varón consulta sobre detección prostática y acuerda con el profesional valorar una prueba después de revisar sus beneficios y límites.
0|El examen solicitado corresponde a imágenes de mama con finalidad de detección temprana, según elegibilidad.
1|El programa de cuello uterino utiliza detección del material genético viral como parte de su estrategia.
2|La persona recibe instrucciones para recoger una muestra de heces destinada a buscar un sangrado no visible.
3|La consulta se centra en una prueba sanguínea prostática cuyo resultado requiere interpretación y no confirma por sí solo cáncer.
0|La solicitud de tamizaje mamario requiere distinguir el método de imagen de las pruebas cervicales o digestivas.
2|El resultado de un tamizaje fecal es positivo y el equipo organiza evaluación posterior, sin asumir diagnóstico de cáncer.
''')
add('Curso de vida','Tamizaje neonatal','¿Qué interpretación o conducta es correcta?',
['Sospecha que requiere confirmación oportuna','Oximetría para detectar cardiopatía crítica','Muestra de talón para enfermedades congénitas','Continuidad del seguimiento aunque no existan síntomas'],
['Un tamizaje alterado no constituye por sí solo diagnóstico definitivo.','La oximetría neonatal ayuda a detectar cardiopatías congénitas críticas.','La muestra de talón permite buscar determinadas enfermedades congénitas tratables.','La ausencia de síntomas no elimina la necesidad de completar el seguimiento indicado.'],'''
0|El laboratorio informa un tamizaje neonatal alterado y la familia pregunta si ya se confirmó la enfermedad.
1|Antes del alta se mide saturación en puntos indicados para identificar cardiopatías congénitas críticas.
2|Se obtiene una muestra de sangre del recién nacido destinada a detectar hipotiroidismo congénito y otras enfermedades del programa.
3|Un bebé con resultado de tamizaje pendiente se ve sano y su familia considera innecesario volver a buscar el informe.
0|Una prueba de pesquisa resulta positiva; el equipo organiza evaluación diagnóstica en lugar de etiquetar una enfermedad definitiva.
1|La actividad de detección temprana neonatal utiliza un sensor de saturación para buscar alteraciones cardiacas críticas.
2|La familia pregunta la finalidad de recoger sangre del talón antes de que aparezcan signos de enfermedad congénita.
3|Aunque el recién nacido se alimenta bien, corresponde asegurar la entrega del resultado y las acciones posteriores del programa.
0|La consejería distingue claramente entre un resultado de pesquisa sospechoso y la confirmación por estudios posteriores.
2|La prueba neonatal señalada busca enfermedades metabólicas o endocrinas mediante una muestra sanguínea, no mediante saturación.
''')
add('Problemas prioritarios','Exposición ambiental','¿Qué conclusión orienta mejor el cuidado?',
['Investigar exposición crónica aunque no haya episodio agudo','Priorizar evaluación por sospecha de exposición a plomo','Considerar la fuente común y evaluar al grupo expuesto','Reducir contacto con la fuente y facilitar atención de salud'],
['La exposición repetida puede producir daño sin una intoxicación aguda identificable.','El plomo puede asociarse con anemia y alteraciones del aprendizaje, que requieren evaluación.','Compartir una fuente contaminada justifica valorar a otras personas expuestas.','La atención integra evaluación de salud y reducción de la exposición.'],'''
0|Una familia consume agua de una fuente potencialmente contaminada por actividad minera desde hace meses, sin recordar un episodio de intoxicación.
1|Un niño de una zona con fuente de plomo presenta anemia y dificultades de aprendizaje que requieren evaluación.
2|Varios integrantes de una vivienda utilizan la misma agua posiblemente contaminada y solo uno ha consultado hasta ahora.
3|La comunidad solicita orientación mientras se investiga una fuente química de riesgo que continúa utilizándose.
0|El trabajador tuvo contacto repetido con sustancias químicas y atribuye el riesgo únicamente a accidentes de gran magnitud.
1|La valoración debe explorar fuentes ambientales de plomo en un niño con manifestaciones compatibles, sin asumir diagnóstico solo por síntomas.
2|La pesquisa identifica un problema posiblemente vinculado al agua que comparten varias familias del mismo sector.
3|Ante sospecha de exposición a metales se necesita articular la evaluación de salud con medidas para evitar nuevos contactos.
0|No hubo un evento tóxico único, pero la exposición cotidiana persiste y la familia cree que ello descarta riesgo.
2|El equipo evalúa si otras personas que comparten la fuente requieren valoración, aunque todavía no refieran molestias.
''')
add('Curso de vida','Salud bucal','¿Qué medida responde al problema señalado?',
['Cepillado con pasta fluorada al menos dos veces al día','Hilo dental para espacios interdentales','Evaluación odontológica de un problema identificado','Educación demostrativa para mejorar la técnica'],
['El cepillado regular con pasta fluorada es una medida básica preventiva.','El hilo complementa la limpieza de zonas interdentales.','Un problema clínico identificado requiere evaluación, no solo educación.','La demostración y práctica verifican una habilidad de autocuidado.'],'''
0|Una madre pregunta por la frecuencia mínima de cepillado preventivo de su hijo y cree suficiente hacerlo solo por la mañana.
1|Una persona mantiene cepillado, pero pregunta cómo limpiar las superficies entre dientes que el cepillo no alcanza bien.
2|Durante una consejería se identifica dolor dental persistente y una lesión que necesita valoración profesional.
3|El usuario conoce la recomendación, pero al practicar se observa que no alcanza varias superficies dentarias.
0|La familia propone reemplazar el cepillado nocturno por enjuague como única acción habitual de higiene.
1|La dificultad principal es retirar placa de espacios interdentales sin sustituir el cepillado de otras superficies.
2|Una persona tiene sangrado y dolor recurrentes; la enfermera debe organizar valoración y no limitarse a entregar un folleto.
3|La madre pide aprender la técnica y la profesional demuestra, observa la práctica y corrige errores.
1|El usuario solicita un complemento específico para limpiar entre dientes, además de mantener el cepillado habitual.
0|El consejo preventivo debe incluir pasta fluorada y cepillado regular, especialmente antes de dormir.
''')
add('Curso de vida','Salud mental y continuidad','¿Qué intervención se ajusta mejor al objetivo?',
['Valoración inicial de necesidades y riesgo','Atención comunitaria con apoyo de la red cercana','Rehabilitación psicosocial','Continuidad de cuidados'],
['La valoración inicial identifica necesidades y riesgos para decidir la atención.','El modelo comunitario articula cuidado próximo y apoyos.','La rehabilitación favorece habilidades y participación social.','La continuidad evita interrupciones entre etapas y servicios.'],'''
0|Una adolescente consulta por tristeza e insomnio; primero se explora cómo se encuentra y qué riesgos o apoyos tiene.
1|Una persona con trastorno mental recibe atención cerca de su domicilio y trabajo coordinado con su familia y comunidad.
2|El plan se centra en recuperar habilidades cotidianas y retomar participación social después de una crisis.
3|Tras un alta, el equipo enlaza el control especializado con el seguimiento del primer nivel para evitar abandono.
0|Antes de decidir una derivación, la enfermera escucha el malestar, explora su impacto y valora la seguridad de la persona.
1|Se organiza un cuidado ambulatorio que incluye apoyos de la vida cotidiana y participación de la red local.
2|Una usuaria practica habilidades para manejar actividades diarias y reintegrarse a espacios comunitarios.
3|Se coordinan controles sucesivos y comunicación entre profesionales durante la evolución de un problema mental.
1|El objetivo es acercar la atención al lugar donde vive la persona y articular su red de apoyo.
2|La mejoría clínica ya se acompaña de actividades para recuperar autonomía y participación fuera del establecimiento.
''')

add('Enfermería','PAE','¿Qué etapa del proceso de atención de enfermería se evidencia?',
['Valoración','Diagnóstico de enfermería','Planificación','Evaluación'],
['Se reúnen datos relevantes de la persona.','Se interpreta la información para identificar una respuesta humana.','Se fijan resultados y se seleccionan intervenciones.','Se compara la respuesta obtenida con el resultado esperado.'],'''
0|Una enfermera entrevista a una persona con disnea y registra frecuencia respiratoria, saturación y molestias antes de formular un juicio clínico.
1|Tras reunir datos, la enfermera identifica que la paciente no tolera la actividad habitual y nombra la respuesta humana que requiere cuidado.
2|El equipo acuerda con el paciente una meta de movilidad y selecciona las actividades para alcanzarla durante el turno.
3|Después del cuidado, se contrasta la intensidad del dolor con la meta prevista y se decide modificar el plan.
0|En una visita domiciliaria se exploran hábitos, apoyos familiares y barreras para seguir el tratamiento, sin establecer aún un diagnóstico.
1|La enfermera agrupa los hallazgos de una persona con movilidad reducida e identifica un riesgo de lesión que debe abordar.
2|Antes de realizar las acciones de cuidado se definen prioridades, resultados medibles y responsables.
3|Al finalizar el turno se determina si la paciente logró la autonomía prevista y se fundamenta la continuidad de las intervenciones.
1|El profesional interpreta los datos objetivos y subjetivos y formula un juicio sobre una necesidad de cuidado de la familia.
2|Una paciente y su enfermera acuerdan qué mejoría esperan observar y qué cuidados se aplicarán para conseguirla.
''')
add('Enfermería','Datos de valoración','¿Cómo se clasifica el dato que se destaca?',
['Dato subjetivo actual','Dato objetivo actual','Antecedente personal','Antecedente familiar'],
['Es una experiencia actual referida por la persona.','Es un hallazgo actual observado o medido.','Corresponde a un evento previo de la propia persona.','Corresponde a la historia de salud de un familiar.'],'''
0|Al valorar a una paciente, esta expresa que siente un dolor opresivo y que le cuesta conciliar el sueño.
1|La enfermera registra una temperatura medida de 38,4 °C durante el examen actual.
2|Durante la entrevista, el paciente informa que fue operado de apéndice hace seis años.
3|La usuaria señala que su madre y su hermana tienen diabetes; ella no tiene ese diagnóstico.
0|Una persona afirma que siente náuseas desde la madrugada, aunque todavía no ha vomitado durante la atención.
1|En el examen se observa una herida con secreción y se registra su tamaño con una regla.
2|Una adulta cuenta que tuvo una reacción alérgica documentada a un medicamento durante una hospitalización anterior.
3|En la ficha se consigna que el padre del paciente falleció por enfermedad cardiovascular.
1|Durante el control se mide una frecuencia respiratoria elevada y se documenta el valor obtenido.
0|La paciente describe hormigueo y sensación de frío en los pies; esos síntomas son el dato consultado.
''')
add('Enfermería','Lenguajes del cuidado','¿Qué componente estandarizado necesita utilizar?',
['Diagnósticos NANDA-I','Resultados NOC','Intervenciones NIC','Indicador de evaluación del resultado'],
['NANDA-I organiza diagnósticos de enfermería.','NOC organiza resultados esperados del cuidado.','NIC organiza intervenciones de enfermería.','Un indicador permite observar y medir el logro de un resultado.'],'''
0|La enfermera ya interpretó los hallazgos y busca una denominación estandarizada para la respuesta humana identificada.
1|El plan requiere seleccionar el estado que se espera mejorar con el cuidado, antes de elegir las actividades.
2|El diagnóstico y el resultado ya están definidos; falta seleccionar las acciones estandarizadas que realizará enfermería.
3|Para comprobar un resultado de movilidad se elige la capacidad observable de caminar con el apoyo acordado.
1|El equipo necesita expresar de forma estandarizada la mejoría esperada en el autocuidado de una persona.
0|Se solicita clasificar un juicio clínico sobre la respuesta de la familia frente a un problema de salud.
2|Se busca una clasificación para organizar el conjunto de cuidados que se aplicará durante la hospitalización.
3|La enfermera elige una conducta concreta y medible que mostrará si se consiguió el resultado previsto.
0|El profesional desea nombrar el problema de cuidado con una etiqueta diagnóstica y no con el nombre de una enfermedad médica.
1|La discusión del equipo se centra en qué cambio favorable debe lograr la persona, no todavía en las actividades para obtenerlo.
''')
add('Enfermería','Procesamiento y asepsia','¿Qué proceso se describe con mayor precisión?',
['Limpieza','Antisepsia','Desinfección','Esterilización'],
['La limpieza remueve suciedad y materia orgánica.','La antisepsia se aplica a tejido vivo.','La desinfección reduce o elimina microorganismos de objetos sin garantizar todas las esporas.','La esterilización elimina microorganismos, incluidas esporas, mediante un proceso validado.'],'''
0|Antes del procesamiento de un instrumental se remueve físicamente la materia orgánica adherida mediante agua y detergente.
1|Se aplica un producto indicado sobre la piel de la paciente antes de una punción.
2|Una superficie inanimada se trata con un agente que reduce microorganismos, pero el procedimiento no garantiza eliminación de esporas.
3|Se somete material compatible a un ciclo validado para eliminar toda forma microbiana, incluidas esporas.
0|El personal retira suciedad visible de una camilla como paso previo al uso del desinfectante.
1|Para preparar la piel antes de un procedimiento se utiliza un agente antimicrobiano apto para tejido vivo.
2|Tras la limpieza, el equipo aplica sobre una mesa un producto destinado a reducir la contaminación microbiana del objeto.
3|Se requiere que un instrumento crítico quede libre de microorganismos viables y esporas antes de utilizarlo.
0|La acción evaluada consiste exclusivamente en retirar restos de sangre de un objeto antes de su procesamiento posterior.
1|Durante la preparación de una zona de punción, la intervención antimicrobiana se realiza sobre piel íntegra.
''')
add('Enfermería','Momentos de inmunización','¿En qué momento corresponde la actividad descrita?',
['Preparación previa de la sesión','Evaluación individual antes de aplicar','Administración del biológico','Observación y orientación posterior'],
['Se organizan termo, registros e insumos de la sesión.','Se verifica la elegibilidad y antecedentes de la persona.','Se controla la técnica durante la aplicación.','Se vigila y se orienta después de aplicar la vacuna.'],'''
0|Antes de recibir usuarios, el personal acondiciona el termo, verifica el registro térmico y dispone los insumos de la jornada.
1|Frente a una niña que ya llegó al consultorio, la enfermera revisa carné, antecedentes y posibles contraindicaciones.
2|La enfermera comprueba sitio anatómico, vía y dosis en el momento de aplicar el biológico indicado.
3|Una vez aplicada la vacuna, se informa a la familia sobre reacciones esperables y signos que requieren atención.
0|El equipo revisa fechas de vencimiento y disponibilidad de diluyentes al organizar la campaña del día.
1|Una gestante acude a vacunación y se contrasta su historia de dosis antes de decidir qué aplicación corresponde.
2|Durante la inyección se verifica que la técnica corresponda a la vía indicada para ese producto.
3|Tras la aplicación, se organiza la vigilancia inmediata de la persona y se resuelven dudas sobre cuándo consultar.
1|La madre refiere una reacción previa; el dato se valora antes de autorizar la dosis de su hijo.
0|El responsable comprueba que el equipo de transporte y los insumos estén listos antes de iniciar el desplazamiento extramural.
''')
add('Enfermería','Conservación y vacunación segura','¿Cuál es la decisión más adecuada en este momento?',
['Inmovilizar y evaluar los biológicos afectados','Obtener el diluyente específico antes de reconstituir','Atender y notificar el evento grave','Verificar carné y antecedentes antes de decidir la dosis'],
['Una excursión térmica exige suspender el uso y evaluar la exposición.','El diluyente debe corresponder al producto indicado.','La atención y notificación no esperan una confirmación causal.','La decisión de vacunar depende de la evaluación individual y del esquema.'],'''
0|El registrador confirma temperaturas fuera del intervalo de conservación y se desconoce la duración de la exposición de varios frascos.
1|La vacuna requiere reconstitución y el único diluyente disponible pertenece a otra vacuna, aunque ambos están vigentes.
2|Después de una vacunación aparece un evento que exige hospitalización y su relación causal aún no ha sido establecida.
3|Una persona desconoce sus dosis previas y lleva un carné incompleto; todavía no se ha indicado el biológico de hoy.
0|Durante el transporte se identifica una ruptura de cadena de frío y todavía no existe evaluación técnica de los frascos afectados.
1|La enfermera detecta que el diluyente fue separado de su vacuna y no puede comprobar que corresponda al mismo producto.
2|Un evento posterior a la vacuna cumple criterio de gravedad, aunque la técnica de aplicación aparentemente fue correcta.
3|Antes de vacunar, un familiar comunica una reacción previa importante que no estaba registrada en la ficha.
0|Un termo llega con una alarma térmica activada; el equipo considera que enfriar nuevamente los frascos sería suficiente para usarlos.
1|Se propone usar agua estéril para reemplazar un diluyente específico no disponible en la sesión.
''')
add('Curso de vida','Cuidado infantil','¿Qué componente del paquete infantil se está realizando?',
['Evaluación del crecimiento','Evaluación del desarrollo','Inmunizaciones','Tamizaje de anemia'],
['El crecimiento se valora con medidas antropométricas y su interpretación.','El desarrollo se valora por adquisiciones y capacidades.','Las inmunizaciones previenen enfermedades mediante vacunación.','El tamizaje busca detectar anemia mediante la evaluación indicada, incluida hemoglobina.'],'''
0|En CRED se miden peso y longitud y se interpreta su evolución en los controles registrados.
1|La enfermera explora cómo el niño se comunica, juega y realiza actividades acordes con su edad.
2|El carné muestra dosis pendientes y se organiza su aplicación conforme al esquema vigente.
3|Se mide hemoglobina en un niño sin diagnóstico previo para identificar si presenta anemia.
0|El profesional analiza una desviación en la trayectoria de peso y talla, junto con el contexto de alimentación.
1|Una madre refiere pérdida de una habilidad adquirida y el equipo la evalúa dentro de las capacidades del niño.
2|Durante el control se revisa el registro de biológicos y se determina la continuidad de las dosis indicadas.
3|En una actividad preventiva se obtiene el dato de hemoglobina para detectar anemia no conocida.
1|Se identifican dificultades persistentes de lenguaje y se programa evaluación y seguimiento del desarrollo.
0|La visita se centra en comparar medidas antropométricas sucesivas, evitando interpretar un valor aislado sin contexto.
''')
add('Curso de vida','Valoración geriátrica','¿Qué dimensión de la valoración integral está principalmente comprometida?',
['Funcional','Mental','Nutricional','Sociofamiliar'],
['La funcionalidad comprende autonomía en actividades cotidianas.','La dimensión mental incluye cognición y estado afectivo.','La nutricional integra ingesta, peso y riesgos de malnutrición.','La sociofamiliar incluye apoyos, convivencia y condiciones sociales.'],'''
0|Una adulta mayor que antes se vestía sola ahora necesita ayuda para bañarse y cambiarse de ropa.
1|Un hombre mayor presenta cambios de memoria y desorientación que afectan su participación en la consulta.
2|Se detecta pérdida de peso no intencional y una ingesta cada vez más limitada por problemas al comer.
3|Una mujer mayor vive sola, carece de apoyo para acudir a controles y no tiene quién la ayude en una emergencia.
0|Después de una caída, una persona dejó de desplazarse y usar el baño sin asistencia.
1|La familia consulta por tristeza persistente, desinterés y cambios afectivos de la persona mayor.
2|En el control se identifica que la persona omite comidas y ha perdido masa corporal en los últimos meses.
3|El problema destacado es la ausencia de red de apoyo y conflictos con quienes comparten su vivienda.
0|Se evalúa específicamente si la persona puede realizar actividades diarias sin depender de un cuidador.
1|La enfermera explora orientación, memoria y estado de ánimo durante la valoración del adulto mayor.
''')
add('Curso de vida','Atención prenatal','¿Qué componente se desarrolla de manera principal?',
['Identificación de riesgos obstétricos','Plan de parto y emergencias','Consejería nutricional','Tamizajes y exámenes auxiliares'],
['Se reconocen antecedentes y hallazgos que modifican el riesgo.','Se acuerdan lugar, transporte, acompañamiento y respuesta ante emergencias.','Se orienta alimentación y necesidades nutricionales.','Se realizan pruebas indicadas para detectar condiciones relevantes.'],'''
0|En el primer contacto se investigan antecedentes de complicaciones gestacionales y enfermedades que puedan afectar el embarazo.
1|La gestante acuerda dónde acudir, quién la acompañará y cómo se trasladará si comienza el parto o aparece una alarma.
2|La enfermera orienta sobre fuentes de hierro, alimentación y ganancia de peso, según las necesidades de la gestante.
3|Se solicitan las pruebas prenatales indicadas para detectar anemia e infecciones y conocer el grupo sanguíneo.
0|El profesional integra antecedentes y hallazgos clínicos para decidir si la gestante requiere una atención de mayor capacidad.
1|La familia identifica un transporte alternativo porque el camino suele quedar bloqueado durante lluvias.
2|La consulta se dedica a revisar la ingesta y acordar ajustes alimentarios que favorezcan el estado nutricional materno.
3|La gestante acude a completar el tamizaje de VIH y sífilis previsto dentro de su cuidado prenatal.
1|Se registra el establecimiento de destino y la persona que ayudará a movilizar a la gestante ante una urgencia.
0|Se revisa una historia de enfermedad hipertensiva en un embarazo anterior para orientar la vigilancia actual.
''')
add('Curso de vida','Urgencia obstétrica','¿Cuál es la prioridad de atención?',
['Valoración urgente por posible trastorno hipertensivo','Respuesta inmediata ante hemorragia y estabilización','Reconocimiento de eclampsia y respuesta de emergencia','Vigilancia del puerperio normal'],
['Cefalea intensa y alteraciones visuales requieren evaluación inmediata.','El sangrado con compromiso circulatorio exige estabilización y referencia según capacidad.','Convulsiones en contexto hipertensivo del embarazo orientan a eclampsia.','La recuperación posparto requiere vigilar involución y loquios cuando no hay alarmas.'],'''
0|Una gestante refiere cefalea intensa y visión borrosa; la familia propone esperar hasta su control programado.
1|Una gestante llega con hemorragia abundante, palidez y signos de choque a un puesto de baja capacidad resolutiva.
2|Una embarazada con hipertensión presenta una convulsión durante la valoración del equipo.
3|En una puérpera sin signos de alarma se controlan la involución uterina y las características de los loquios.
0|Durante una visita, la gestante comunica dolor de cabeza intenso acompañado de cambios visuales de aparición reciente.
1|Después del parto, una mujer presenta sangrado importante y deterioro circulatorio; aún no se dispone del diagnóstico etiológico.
2|El equipo atiende a una gestante con enfermedad hipertensiva que inicia movimientos convulsivos y pérdida de conciencia.
3|La consulta posparto se realiza para seguir la recuperación fisiológica de una mujer clínicamente estable.
1|El personal considera esperar resultados de rutina antes de actuar frente a una hemorragia obstétrica con inestabilidad.
0|La paciente embarazada describe síntomas neurológicos de alarma en una localidad donde el siguiente control será dentro de varios días.
''')
