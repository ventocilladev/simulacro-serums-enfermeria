(function () {
  'use strict';
  const KEY = 'serums-simulacro-v5';
  const LETTERS = ['A', 'B', 'C', 'D'];
  const app = document.getElementById('app');
  const bank = window.QUESTIONS.map((q, id) => ({ id, category: q[0], stem: q[1], choices: q[2], correct: q[3], why: q[4] }));
  let state = read();
  let current = 0;
  let tick;

  function escape(s) { return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]); }
  function shuffle(values) { const a = [...values]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  function read() {
    try {
      const s = JSON.parse(localStorage.getItem(KEY));
      if (!s || ![60, 100].includes(s.ids?.length) || s.minutes !== (s.ids.length === 60 ? 30 : 90)) return null;
      if (s.ids.some(id => !Number.isInteger(id) || id < 0 || id >= bank.length) || new Set(s.ids).size !== s.ids.length) return null;
      if (s.answers?.length !== s.ids.length || s.flagged?.length !== s.ids.length || s.orders?.length !== s.ids.length) return null;
      if (s.orders.some(o => !Array.isArray(o) || o.length !== 4 || new Set(o).size !== 4 || o.some(n => ![0, 1, 2, 3].includes(n)))) return null;
      return s;
    } catch { return null; }
  }
  function save() { localStorage.setItem(KEY, JSON.stringify(state)); }
  function formatTime(seconds) { const m = Math.floor(Math.max(0, seconds) / 60); return `${String(m).padStart(2, '0')}:${String(Math.max(0, seconds) % 60).padStart(2, '0')}`; }
  function remaining() { return Math.max(0, state.minutes * 60 - Math.floor((Date.now() - state.started) / 1000)); }
  function stopClock() { if (tick) clearInterval(tick); tick = null; }
  function clock() {
    stopClock(); if (!state || state.finished) return;
    tick = setInterval(() => { const seconds = remaining(); const el = document.getElementById('clock'); if (el) el.textContent = formatTime(seconds); if (seconds === 0) finish(true); }, 1000);
  }
  function selectedIds(count) {
    const groups = new Map();
    const previous = new Set(state?.ids || []);
    bank.forEach(q => { if (!groups.has(q.category)) groups.set(q.category, []); if (!previous.has(q.id)) groups.get(q.category).push(q.id); });
    for (const [key, ids] of groups) groups.set(key, shuffle(ids));
    const chosen = [];
    while (chosen.length < count) {
      let added = false;
      for (const category of shuffle([...groups.keys()])) {
        if (chosen.length === count) break;
        const id = groups.get(category).pop();
        if (id !== undefined) { chosen.push(id); added = true; }
      }
      if (!added) break;
    }
    return shuffle(chosen);
  }
  function start(count) {
    if (![60, 100].includes(count) || bank.length < count) return;
    const ids = selectedIds(count);
    state = { ids, answers: ids.map(() => null), flagged: ids.map(() => false), orders: ids.map(() => shuffle([0, 1, 2, 3])), started: Date.now(), minutes: count === 60 ? 30 : 90, finished: false };
    current = 0; save(); renderExam(); window.scrollTo(0, 0);
  }
  function home() {
    stopClock();
    const resume = state && !state.finished;
    const completed = state && state.finished;
    app.innerHTML = `<section class="hero"><div class="hero-copy"><span class="eyebrow">SIMULACRO SERUMS · ENFERMERÍA</span><h1>De tu amorshito<br><em>para ti.</em></h1><p class="dedication">Tú puedes. Vamos por ese 20 de nota.</p></div><div class="hero-art" aria-hidden="true"><div class="art-card"><span class="art-kicker">SIMULACRO</span><div class="art-number">01<span>/ 60</span></div><div class="art-lines"><i></i><i></i><i></i></div><div class="art-choice selected">A <span></span></div><div class="art-choice">B <span></span></div><div class="art-choice">C <span></span></div></div></div></section>
    <section class="setup card"><div class="section-title"><div><span class="eyebrow dark">ELIGE TU EXAMEN</span><h2>Simulacro</h2></div><span class="sparkle" aria-hidden="true">✦</span></div><div class="exam-choices"><button class="exam-choice" data-count="60"><span class="choice-number">60</span><span class="choice-copy"><strong>60 preguntas</strong><small>30 minutos</small></span><span class="choice-arrow">→</span></button><button class="exam-choice" data-count="100"><span class="choice-number">100</span><span class="choice-copy"><strong>100 preguntas</strong><small>90 minutos</small></span><span class="choice-arrow">→</span></button></div>${resume ? '<button class="secondary resume-button" id="resume">Continuar examen guardado</button>' : ''}${completed ? '<button class="secondary resume-button" id="last">Ver último resultado</button>' : ''}<p class="helper">El tiempo comienza al iniciar. Tus respuestas se guardan en este navegador.</p></section>`;
    document.querySelectorAll('[data-count]').forEach(el => el.onclick = () => { if (resume && !confirm('Hay un examen en curso. ¿Empezar otro y reemplazarlo?')) return; start(Number(el.dataset.count)); });
    if (resume) document.getElementById('resume').onclick = () => { current = Math.max(0, state.answers.findIndex(a => a === null)); renderExam(); };
    if (completed) document.getElementById('last').onclick = renderResults;
  }
  function renderExam() {
    if (!state) return home(); if (state.finished) return renderResults(); if (remaining() === 0) return finish(true);
    const total = state.ids.length; current = Math.max(0, Math.min(current, total - 1));
    const q = bank[state.ids[current]]; const order = state.orders[current];
    const answered = state.answers.filter(a => a !== null).length; const selected = state.answers[current];
    app.innerHTML = `<div class="exam-layout"><section class="exam-main"><div class="exam-head"><button class="text-button" id="exit">← Inicio</button><span class="exam-label">EXAMEN DE ${total} PREGUNTAS</span><span class="timer" aria-label="Tiempo restante">◷ <span id="clock">${formatTime(remaining())}</span></span></div><div class="progress-line"><span style="width:${answered / total * 100}%"></span></div><div class="question-meta"><span class="eyebrow dark">PREGUNTA ${current + 1} DE ${total}</span></div><h1 class="question-stem">${escape(q.stem)}</h1><fieldset class="options"><legend class="sr-only">Selecciona una respuesta</legend>${order.map((choiceIndex, displayIndex) => `<button type="button" class="option ${selected === choiceIndex ? 'chosen' : ''}" data-answer="${choiceIndex}" aria-pressed="${selected === choiceIndex}"><span class="option-letter">${LETTERS[displayIndex]}</span><span>${escape(q.choices[choiceIndex])}</span><span class="option-check">✓</span></button>`).join('')}</fieldset><div class="exam-actions"><button class="flag-button ${state.flagged[current] ? 'active' : ''}" id="flag">${state.flagged[current] ? '⚑ Marcada para revisar' : '⚑ Marcar para revisar'}</button><div class="step-actions"><button class="secondary" id="prev" ${current === 0 ? 'disabled' : ''}>Anterior</button><button class="primary" id="next">${current === total - 1 ? 'Revisar avance' : 'Siguiente →'}</button></div></div></section><aside class="exam-side"><div class="side-heading"><h2>Tu avance</h2><span>${answered}/${total}</span></div><p>Elige un número para ir a esa pregunta.</p><div class="question-grid">${state.ids.map((_, i) => `<button class="number ${i === current ? 'current' : ''} ${state.answers[i] !== null ? 'answered' : ''} ${state.flagged[i] ? 'flagged' : ''}" data-jump="${i}" aria-label="Pregunta ${i + 1}${state.answers[i] !== null ? ', respondida' : ''}">${i + 1}</button>`).join('')}</div><div class="legend"><span><i class="legend-answered"></i>Respondida</span><span><i class="legend-flagged"></i>Por revisar</span></div><button class="finish-link" id="finish">Finalizar simulacro →</button></aside></div>`;
    document.querySelectorAll('[data-answer]').forEach(el => el.onclick = () => { state.answers[current] = Number(el.dataset.answer); save(); renderExam(); });
    document.querySelectorAll('[data-jump]').forEach(el => el.onclick = () => { current = Number(el.dataset.jump); renderExam(); window.scrollTo(0, 0); });
    document.getElementById('flag').onclick = () => { state.flagged[current] = !state.flagged[current]; save(); renderExam(); };
    document.getElementById('prev').onclick = () => { current--; renderExam(); window.scrollTo(0, 0); };
    document.getElementById('next').onclick = () => { if (current < total - 1) { current++; renderExam(); window.scrollTo(0, 0); } else review(); };
    document.getElementById('finish').onclick = review; document.getElementById('exit').onclick = home; clock();
  }
  function review() {
    stopClock(); const missing = state.answers.filter(a => a === null).length; const flagged = state.flagged.filter(Boolean).length;
    app.innerHTML = `<section class="review card"><span class="eyebrow dark">ANTES DE ENTREGAR</span><h1>Revisa tu avance</h1><p>Has respondido <strong>${state.ids.length - missing} de ${state.ids.length}</strong> preguntas.${missing ? ` Te faltan <strong>${missing}</strong>.` : ' Ya completaste todas.'}${flagged ? ` Tienes <strong>${flagged}</strong> marcadas para revisar.` : ''}</p><p class="review-clock">Tiempo restante: <strong id="clock">${formatTime(remaining())}</strong></p><div class="review-actions"><button class="secondary" id="back">Volver al examen</button><button class="primary" id="submit">Entregar respuestas →</button></div></section>`;
    document.getElementById('back').onclick = renderExam;
    document.getElementById('submit').onclick = () => { if (remaining() === 0) return finish(true); if (missing && !confirm(`Quedan ${missing} preguntas sin responder. ¿Entregar de todos modos?`)) return; finish(false); };
    clock();
  }
  function finish(timedOut) { if (!state || state.finished) return; stopClock(); state.finished = true; state.timedOut = timedOut; state.ended = Date.now(); save(); renderResults(); }
  function renderResults() {
    if (!state) return home(); stopClock();
    const total = state.ids.length; const correct = state.answers.reduce((n, a, i) => n + Number(a === bank[state.ids[i]].correct), 0);
    const grade = (correct / total * 20).toFixed(1); const skipped = state.answers.filter(a => a === null).length;
    app.innerHTML = `<section class="results-hero"><span class="eyebrow">SIMULACRO FINALIZADO</span><h1>${state.timedOut ? 'Se terminó el tiempo.' : 'Terminaste el examen.'}</h1><div class="score"><strong>${grade}<small>/20</small></strong><span>Nota referencial · ${correct} correctas de ${total}</span></div><div class="result-stats"><span>${total - correct - skipped} incorrectas</span><span>${skipped} sin responder</span></div></section><div class="result-top"><h2>Revisión de respuestas</h2><button class="primary" id="again">Nuevo simulacro →</button></div><div class="result-list">${state.ids.map((id, i) => { const q = bank[id], answer = state.answers[i], ok = answer === q.correct, order = state.orders[i]; return `<article class="result-card"><div class="result-card-head"><span class="result-status ${ok ? 'ok' : 'bad'}">${ok ? '✓ Correcta' : answer === null ? '— Sin responder' : '× Incorrecta'}</span><span>Pregunta ${i + 1}</span></div><h3>${escape(q.stem)}</h3><p>Tu respuesta: <strong>${answer === null ? 'Sin responder' : `${LETTERS[order.indexOf(answer)]}. ${escape(q.choices[answer])}`}</strong></p>${!ok ? `<p>Respuesta correcta: <strong>${LETTERS[order.indexOf(q.correct)]}. ${escape(q.choices[q.correct])}</strong></p>` : ''}<div class="explanation">${escape(q.why)}</div></article>`; }).join('')}</div>`;
    document.getElementById('again').onclick = home;
  }
  if (state && !state.finished && remaining() === 0) finish(true); else home();
})();
