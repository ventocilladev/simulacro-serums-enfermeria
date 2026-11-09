(function () {
  'use strict';
  const KEY = 'serums-simulacro-v1';
  const LETTERS = ['A', 'B', 'C', 'D'];
  const app = document.getElementById('app');
  const bank = window.QUESTIONS.map((q, id) => ({ id, category: q[0], stem: q[1], choices: q[2], correct: q[3], why: q[4] }));
  let state = read();
  let current = 0;
  let tick;

  function read() {
    try {
      const s = JSON.parse(localStorage.getItem(KEY));
      if (!s || !Array.isArray(s.ids) || !s.ids.every(id => Number.isInteger(id) && id >= 0 && id < bank.length)) return null;
      if (!Array.isArray(s.answers) || s.answers.length !== s.ids.length) return null;
      return s;
    } catch { return null; }
  }
  function save() { localStorage.setItem(KEY, JSON.stringify(state)); }
  function escape(s) { return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]); }
  function shuffle(values) {
    const a = [...values];
    for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
    return a;
  }
  function formatTime(seconds) { const m = Math.floor(Math.max(0, seconds) / 60); return `${String(m).padStart(2, '0')}:${String(Math.max(0, seconds) % 60).padStart(2, '0')}`; }
  function remaining() { return state && state.minutes ? Math.max(0, state.minutes * 60 - Math.floor((Date.now() - state.started) / 1000)) : null; }
  function stopClock() { if (tick) clearInterval(tick); tick = null; }
  function clock() {
    stopClock();
    if (!state || state.finished || !state.minutes) return;
    tick = setInterval(() => {
      const seconds = remaining();
      const el = document.getElementById('clock');
      if (el) el.textContent = formatTime(seconds);
      if (seconds === 0) finish(true);
    }, 1000);
  }
  function start(count, minutes, category) {
    const eligible = bank.filter(q => category === 'Todas' || q.category === category);
    const ids = shuffle(eligible.map(q => q.id)).slice(0, Math.min(count, eligible.length));
    state = { ids, answers: ids.map(() => null), flagged: ids.map(() => false), started: Date.now(), minutes, finished: false, category };
    current = 0; save(); renderExam();
  }
  function home() {
    stopClock();
    const categories = [...new Set(bank.map(q => q.category))];
    const resume = state && !state.finished;
    const completed = state && state.finished;
    app.innerHTML = `<section class="hero"><div class="hero-copy"><span class="eyebrow">PREPARACIÓN SERUMS · ENFERMERÍA</span><h1>Practica a tu ritmo.<br><em>Responde con confianza.</em></h1><p>Preguntas tipo examen, cuatro alternativas y revisión al terminar. Funciona en celular y laptop.</p><div class="hero-stats"><span><strong>${bank.length}</strong> preguntas</span><span><strong>${categories.length}</strong> áreas</span><span><strong>4</strong> alternativas</span></div></div><div class="hero-art" aria-hidden="true"><div class="art-card"><span class="art-kicker">SIMULACRO</span><div class="art-number">01<span>/ 20</span></div><div class="art-lines"><i></i><i></i><i></i></div><div class="art-choice selected">A <span></span></div><div class="art-choice">B <span></span></div><div class="art-choice">C <span></span></div></div></div></section>
    <section class="setup card"><div class="section-title"><div><span class="eyebrow dark">TU PRÓXIMA PRÁCTICA</span><h2>Configura tu simulacro</h2></div><span class="sparkle" aria-hidden="true">✦</span></div><div class="setup-grid"><label>Área<select id="category"><option>Todas</option>${categories.map(c => `<option>${escape(c)}</option>`).join('')}</select></label><label>Cantidad<select id="count"><option value="20">20 preguntas · práctica rápida</option><option value="50">50 preguntas · simulacro completo</option></select></label><label>Tiempo<select id="minutes"><option value="0">Sin límite</option><option value="30">30 minutos</option><option value="60">60 minutos</option><option value="90">90 minutos</option></select></label></div><div class="setup-actions"><button class="primary" id="start">Comenzar simulacro <span>→</span></button>${resume ? '<button class="secondary" id="resume">Continuar práctica guardada</button>' : ''}${completed ? '<button class="secondary" id="last">Ver último resultado</button>' : ''}</div><p class="helper">Tu avance se guarda en este navegador. No necesitas crear una cuenta.</p></section>
    <section class="info-grid"><div class="mini-card"><span class="mini-icon">◉</span><h3>Como en un examen</h3><p>Marca una alternativa, salta entre preguntas y señala las que quieras revisar.</p></div><div class="mini-card"><span class="mini-icon">↗</span><h3>Aprende al terminar</h3><p>Consulta tu puntaje, las respuestas correctas y una explicación breve.</p></div><div class="mini-card"><span class="mini-icon">▣</span><h3>Donde prefieras</h3><p>Diseñado para responder cómodamente desde una pantalla pequeña o grande.</p></div></section>`;
    document.getElementById('start').onclick = () => {
      if (resume && !confirm('Hay una práctica en curso. ¿Empezar una nueva y reemplazarla?')) return;
      start(Number(document.getElementById('count').value), Number(document.getElementById('minutes').value), document.getElementById('category').value);
    };
    if (resume) document.getElementById('resume').onclick = () => { current = Math.max(0, state.answers.findIndex(a => a === null)); renderExam(); };
    if (completed) document.getElementById('last').onclick = renderResults;
  }
  function renderExam() {
    if (!state) return home();
    if (state.finished) return renderResults();
    if (remaining() === 0) return finish(true);
    const total = state.ids.length;
    current = Math.max(0, Math.min(current, total - 1));
    const q = bank[state.ids[current]];
    const answered = state.answers.filter(a => a !== null).length;
    const selected = state.answers[current];
    app.innerHTML = `<div class="exam-layout"><section class="exam-main"><div class="exam-head"><button class="text-button" id="exit">← Inicio</button><span class="exam-label">SIMULACRO EN CURSO</span>${state.minutes ? `<span class="timer" aria-label="Tiempo restante">◷ <span id="clock">${formatTime(remaining())}</span></span>` : '<span class="timer">Sin límite</span>'}</div><div class="progress-line"><span style="width:${answered / total * 100}%"></span></div><div class="question-meta"><span class="eyebrow dark">PREGUNTA ${current + 1} DE ${total}</span><span class="pill">${escape(q.category)}</span></div><h1 class="question-stem">${escape(q.stem)}</h1><fieldset class="options"><legend class="sr-only">Selecciona una respuesta</legend>${q.choices.map((choice, i) => `<button type="button" class="option ${selected === i ? 'chosen' : ''}" data-answer="${i}" aria-pressed="${selected === i}"><span class="option-letter">${LETTERS[i]}</span><span>${escape(choice)}</span><span class="option-check">✓</span></button>`).join('')}</fieldset><div class="exam-actions"><button class="flag-button ${state.flagged[current] ? 'active' : ''}" id="flag">${state.flagged[current] ? '⚑ Marcada para revisar' : '⚑ Marcar para revisar'}</button><div class="step-actions"><button class="secondary" id="prev" ${current === 0 ? 'disabled' : ''}>Anterior</button><button class="primary" id="next">${current === total - 1 ? 'Revisar avance' : 'Siguiente →'}</button></div></div></section><aside class="exam-side"><div class="side-heading"><h2>Tu avance</h2><span>${answered}/${total}</span></div><p>Elige un número para ir a esa pregunta.</p><div class="question-grid">${state.ids.map((_, i) => `<button class="number ${i === current ? 'current' : ''} ${state.answers[i] !== null ? 'answered' : ''} ${state.flagged[i] ? 'flagged' : ''}" data-jump="${i}" aria-label="Pregunta ${i + 1}${state.answers[i] !== null ? ', respondida' : ''}">${i + 1}</button>`).join('')}</div><div class="legend"><span><i class="legend-answered"></i>Respondida</span><span><i class="legend-flagged"></i>Por revisar</span></div><button class="finish-link" id="finish">Finalizar simulacro →</button></aside></div>`;
    document.querySelectorAll('[data-answer]').forEach(el => el.onclick = () => { state.answers[current] = Number(el.dataset.answer); save(); renderExam(); });
    document.querySelectorAll('[data-jump]').forEach(el => el.onclick = () => { current = Number(el.dataset.jump); renderExam(); window.scrollTo(0, 0); });
    document.getElementById('flag').onclick = () => { state.flagged[current] = !state.flagged[current]; save(); renderExam(); };
    document.getElementById('prev').onclick = () => { current--; renderExam(); window.scrollTo(0, 0); };
    document.getElementById('next').onclick = () => { if (current < total - 1) { current++; renderExam(); window.scrollTo(0, 0); } else review(); };
    document.getElementById('finish').onclick = review;
    document.getElementById('exit').onclick = home;
    clock();
  }
  function review() {
    stopClock();
    const missing = state.answers.filter(a => a === null).length;
    const flagged = state.flagged.filter(Boolean).length;
    app.innerHTML = `<section class="review card"><span class="eyebrow dark">ANTES DE ENTREGAR</span><h1>Revisa tu avance</h1><p>Has respondido <strong>${state.ids.length - missing} de ${state.ids.length}</strong> preguntas.${missing ? ` Te faltan <strong>${missing}</strong>.` : ' Ya completaste todas.'}${flagged ? ` Tienes <strong>${flagged}</strong> marcadas para revisar.` : ''}</p><div class="review-actions"><button class="secondary" id="back">Volver al examen</button><button class="primary" id="submit">Entregar respuestas →</button></div></section>`;
    document.getElementById('back').onclick = renderExam;
    document.getElementById('submit').onclick = () => { if (missing && !confirm(`Quedan ${missing} preguntas sin responder. ¿Entregar de todos modos?`)) return; finish(false); };
    clock();
  }
  function finish(timedOut) { if (!state || state.finished) return; stopClock(); state.finished = true; state.timedOut = timedOut; state.ended = Date.now(); save(); renderResults(); }
  function renderResults() {
    if (!state) return home();
    stopClock();
    const total = state.ids.length;
    const correct = state.answers.reduce((n, a, i) => n + Number(a === bank[state.ids[i]].correct), 0);
    const percent = Math.round(correct / total * 100);
    const skipped = state.answers.filter(a => a === null).length;
    app.innerHTML = `<section class="results-hero"><span class="eyebrow">SIMULACRO FINALIZADO</span><h1>${state.timedOut ? 'Se terminó el tiempo.' : '¡Terminaste tu práctica!'}</h1><p>Revisa cada respuesta y vuelve a intentarlo cuando quieras.</p><div class="score"><strong>${percent}<small>%</small></strong><span>${correct} correctas de ${total}</span></div><div class="result-stats"><span>${total - correct - skipped} incorrectas</span><span>${skipped} sin responder</span></div></section><div class="result-top"><h2>Revisión de preguntas</h2><button class="primary" id="again">Nuevo simulacro →</button></div><div class="result-list">${state.ids.map((id, i) => { const q = bank[id], answer = state.answers[i], ok = answer === q.correct; return `<article class="result-card"><div class="result-card-head"><span class="result-status ${ok ? 'ok' : 'bad'}">${ok ? '✓ Correcta' : answer === null ? '— Sin responder' : '× Incorrecta'}</span><span>Pregunta ${i + 1} · ${escape(q.category)}</span></div><h3>${escape(q.stem)}</h3><p>Tu respuesta: <strong>${answer === null ? 'Sin responder' : `${LETTERS[answer]}. ${escape(q.choices[answer])}`}</strong></p>${!ok ? `<p>Respuesta correcta: <strong>${LETTERS[q.correct]}. ${escape(q.choices[q.correct])}</strong></p>` : ''}<div class="explanation">${escape(q.why)}</div></article>`; }).join('')}</div>`;
    document.getElementById('again').onclick = home;
  }
  if (state && !state.finished && remaining() === 0) finish(true); else home();
})();
