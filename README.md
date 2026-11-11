# Simulacro SERUMS de enfermería

Aplicación para celular y laptop con 400 preguntas individuales. Modalidades: 60 preguntas en 30 minutos y 100 en 90 minutos. Cuatro alternativas, marcado para revisión, guardado local y explicación al finalizar.

## Contenido y distribución

El temario SERUMS 2026-II de enfermería proporcionado define los apartados; el balotario Word desarrolla el contenido. Los exámenes oficiales enviados y el examen MINSA 2025-II se consultaron como referencia de redacción. Las preguntas publicadas son elaboradas para este banco.

Cada intento contiene 60 % de enfermería y cuidado integral, 20 % de salud pública/comunitaria, 10 % de gestión, 5 % de ética/interculturalidad y 5 % de investigación, mezclados.

La edición ligera contiene 330 preguntas de la base revisada y 70 casos adicionales. Se conservan todos los apartados del temario y se reduce la cantidad de variantes por familia. El navegador descarga un único archivo de preguntas de aproximadamente 162 kB.

Se evita repetir la familia del intento inmediatamente anterior. El historial local prioriza preguntas todavía no utilizadas antes de volver a las ya vistas. El avance y el historial se guardan en el navegador; no se sincronizan entre dispositivos.

Los 92 apartados del temario están representados en el banco completo. Un intento de 60 o 100 toma una muestra. Véase [SOURCES.md](SOURCES.md). La dificultad se ha aumentado mediante casos y distractores relacionados; todavía no está calibrada psicométricamente con resultados de estudiantes.

## Edición y controles

El navegador carga únicamente `questions-master.js` y `app.js`. Los archivos anteriores se conservan como fuente editorial y no se cargan en la aplicación.

Para reconstruir y verificar el banco:

```text
python scripts/build_master_bank.py
node scripts/validate_bank.cjs
python scripts/coverage_audit.py
```

`editorial_review.py` contiene decisiones por pregunta. `question_families.py` contiene los casos nuevos. `option-aliases.json` permite detectar siglas y nombres equivalentes; no sustituye la revisión del significado clínico. El control incluye el caso de regresión ASIS, opciones distintas, una sola pregunta por ítem, cuotas de selección.
