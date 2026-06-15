---
title: CEO Intelligence Cockpit
type: dashboard
created: 2026-06-13
updated: 2026-06-15
tags:
  - dashboard
  - executive
  - meta-intelligence
---

# 🧠 CEO Intelligence Cockpit

> [!NOTE]
> This is your interactive Decision Intelligence OS workspace. Use the tabs to switch layers, search or filter items, resolve forecasts, or spawn new strategic notes from templates.

```dataviewjs
// State management
if (!window.diOSState) {
  window.diOSState = {
    activeTab: 'summary', // 'summary', 'intelligence', 'decisions', 'execution', 'learning'
    opportunityFilter: 'all',
    signalSearch: '',
    forecastFilter: 'active',
    riskFilter: 'all'
  };
}
const state = window.diOSState;

// Container setup
const mainContainer = dv.container.createEl('div', { cls: 'di-dashboard' });

// Style fallback injection
const styleId = 'di-dashboard-injected-styles';
if (!document.getElementById(styleId)) {
  const styleEl = document.createElement('style');
  styleEl.id = styleId;
  styleEl.textContent = `
    .di-dashboard {
      --di-success: #10b981;
      --di-success-bg: rgba(16, 185, 129, 0.12);
      --di-warning: #f59e0b;
      --di-warning-bg: rgba(245, 158, 11, 0.12);
      --di-danger: #ef4444;
      --di-danger-bg: rgba(239, 68, 68, 0.12);
      --di-info: #3b82f6;
      --di-info-bg: rgba(59, 130, 246, 0.12);
      --di-purple: #8b5cf6;
      --di-purple-bg: rgba(139, 92, 246, 0.12);
      
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-top: 1rem;
    }
    
    .theme-dark .di-dashboard {
      --di-card-bg: rgba(30, 30, 35, 0.6);
      --di-card-border: rgba(255, 255, 255, 0.08);
      --di-card-shadow: 0 8px 24px 0 rgba(0, 0, 0, 0.3);
      --di-card-hover-bg: rgba(35, 35, 42, 0.8);
      --di-header-bg: linear-gradient(135deg, #1e1e24, #121214);
    }
    
    .theme-light .di-dashboard {
      --di-card-bg: rgba(248, 249, 250, 0.8);
      --di-card-border: rgba(0, 0, 0, 0.08);
      --di-card-shadow: 0 8px 24px 0 rgba(31, 38, 135, 0.04);
      --di-card-hover-bg: rgba(240, 242, 245, 0.9);
      --di-header-bg: linear-gradient(135deg, #ffffff, #f1f3f5);
    }
    
    .di-header {
      padding: 1.5rem;
      border-radius: 12px;
      background: var(--di-header-bg);
      border: 1px solid var(--di-card-border);
      box-shadow: var(--di-card-shadow);
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }
    
    .di-header h1 {
      margin: 0 !important;
      font-size: 1.8rem;
      font-weight: 700;
      letter-spacing: -0.025em;
      background: linear-gradient(90deg, var(--text-normal), var(--text-accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    
    .di-subtitle {
      font-size: 0.95rem;
      color: var(--text-muted);
      margin: 0;
    }
    
    .di-tabs {
      display: flex;
      gap: 0.5rem;
      padding: 0.25rem;
      background: rgba(var(--mono-rgb-200), 0.03);
      border-radius: 8px;
      border: 1px solid var(--di-card-border);
      overflow-x: auto;
      margin-top: 0.5rem;
    }
    
    .di-tab {
      padding: 0.5rem 1rem;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 500;
      color: var(--text-muted);
      transition: all 0.2s ease-in-out;
      border: none;
      background: transparent;
      white-space: nowrap;
    }
    
    .di-tab:hover {
      color: var(--text-normal);
      background: rgba(var(--mono-rgb-200), 0.08);
    }
    
    .di-tab.is-active {
      color: var(--text-on-accent, white);
      background: var(--interactive-accent);
      box-shadow: 0 4px 12px rgba(var(--accent-rgb), 0.3);
    }
    
    .di-metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
    }
    
    .di-metric-card {
      padding: 1.25rem;
      border-radius: 10px;
      background: var(--di-card-bg);
      border: 1px solid var(--di-card-border);
      box-shadow: var(--di-card-shadow);
      transition: transform 0.2s ease, background-color 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    
    .di-metric-card:hover {
      transform: translateY(-2px);
      background: var(--di-card-hover-bg);
    }
    
    .di-metric-title {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      font-weight: 600;
    }
    
    .di-metric-value {
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--text-normal);
      line-height: 1;
    }
    
    .di-metric-sub {
      font-size: 0.8rem;
      color: var(--text-muted);
    }
    
    .di-metric-card.brier-excellent { border-left: 4px solid var(--di-success); }
    .di-metric-card.brier-good { border-left: 4px solid var(--di-info); }
    .di-metric-card.brier-moderate { border-left: 4px solid var(--di-warning); }
    .di-metric-card.brier-poor { border-left: 4px solid var(--di-danger); }
    
    .di-alert-banner {
      padding: 1rem 1.25rem;
      border-radius: 10px;
      border-left: 4px solid var(--di-danger);
      background: var(--di-danger-bg);
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }
    
    .di-alert-header {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--di-danger);
      font-weight: 700;
      font-size: 0.95rem;
    }
    
    .di-alert-item {
      font-size: 0.85rem;
      margin-left: 1.25rem;
      color: var(--text-normal);
    }
    
    .di-alert-empty {
      padding: 1rem 1.25rem;
      border-radius: 10px;
      border-left: 4px solid var(--di-success);
      background: var(--di-success-bg);
      color: var(--di-success);
      font-weight: 500;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    
    .di-panel {
      padding: 1.5rem;
      border-radius: 12px;
      background: var(--di-card-bg);
      border: 1px solid var(--di-card-border);
      box-shadow: var(--di-card-shadow);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    
    .di-panel-title {
      font-size: 1.15rem;
      font-weight: 600;
      margin: 0 0 0.5rem 0 !important;
      color: var(--text-normal);
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--di-card-border);
      padding-bottom: 0.5rem;
    }
    
    .di-panel-title span {
      font-size: 0.8rem;
      font-weight: 400;
      color: var(--text-muted);
    }
    
    .di-table-wrapper {
      overflow-x: auto;
      width: 100%;
    }
    
    .di-table {
      width: 100%;
      border-collapse: collapse !important;
      font-size: 0.9rem;
      text-align: left;
    }
    
    .di-table th {
      padding: 0.75rem 0.5rem;
      border-bottom: 2px solid var(--di-card-border) !important;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }
    
    .di-table td {
      padding: 0.75rem 0.5rem;
      border-bottom: 1px solid var(--di-card-border) !important;
      vertical-align: middle;
    }
    
    .di-table tr:hover {
      background: rgba(var(--mono-rgb-200), 0.02);
    }
    
    .di-badge {
      display: inline-flex;
      align-items: center;
      padding: 0.2rem 0.5rem;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 600;
      text-transform: capitalize;
      line-height: 1;
    }
    
    .di-badge-success { color: var(--di-success); background: var(--di-success-bg); }
    .di-badge-warning { color: var(--di-warning); background: var(--di-warning-bg); }
    .di-badge-danger { color: var(--di-danger); background: var(--di-danger-bg); }
    .di-badge-info { color: var(--di-info); background: var(--di-info-bg); }
    .di-badge-purple { color: var(--di-purple); background: var(--di-purple-bg); }
    
    .di-progress-container {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      width: 100%;
      min-width: 80px;
    }
    
    .di-progress {
      flex-grow: 1;
      height: 6px;
      background: rgba(var(--mono-rgb-200), 0.1);
      border-radius: 9999px;
      overflow: hidden;
    }
    
    .di-progress-bar {
      height: 100%;
      background: var(--interactive-accent);
      border-radius: 9999px;
      transition: width 0.3s ease;
    }
    
    .di-progress-label {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      min-width: 28px;
      text-align: right;
    }
    
    .di-filter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      align-items: center;
      margin-bottom: 0.5rem;
      padding: 0.75rem;
      background: rgba(var(--mono-rgb-200), 0.02);
      border-radius: 8px;
      border: 1px solid var(--di-card-border);
    }
    
    .di-filter-label {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 500;
    }
    
    .di-select {
      padding: 0.4rem 1.8rem 0.4rem 0.75rem;
      font-size: 0.85rem;
      border-radius: 6px;
      border: 1px solid var(--di-card-border);
      background: var(--background-primary);
      color: var(--text-normal);
      cursor: pointer;
    }
    
    .di-input {
      padding: 0.4rem 0.75rem;
      font-size: 0.85rem;
      border-radius: 6px;
      border: 1px solid var(--di-card-border);
      background: var(--background-primary);
      color: var(--text-normal);
      min-width: 180px;
    }
    
    .di-btn {
      padding: 0.4rem 0.85rem;
      font-size: 0.85rem;
      border-radius: 6px;
      border: 1px solid var(--di-card-border);
      background: var(--background-primary);
      color: var(--text-normal);
      cursor: pointer;
      transition: all 0.15s ease;
      font-weight: 500;
    }
    
    .di-btn:hover {
      background: var(--di-card-hover-bg);
      border-color: var(--text-muted);
    }
    
    .di-btn-primary {
      background: var(--interactive-accent);
      color: var(--text-on-accent, white);
      border: none;
    }
    
    .di-btn-primary:hover {
      background: var(--interactive-accent-hover);
      color: var(--text-on-accent, white);
    }
    
    .di-risk-matrix-panel {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    
    .di-risk-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.5rem;
      margin-top: 0.5rem;
    }
    
    .di-risk-cell {
      aspect-ratio: 1.4;
      border-radius: 6px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-size: 0.8rem;
      font-weight: 600;
      border: 1px solid var(--di-card-border);
      position: relative;
    }
    
    .di-risk-cell-red { background: rgba(239, 68, 68, 0.12); color: var(--di-danger); border-color: rgba(239, 68, 68, 0.25); }
    .di-risk-cell-orange { background: rgba(245, 158, 11, 0.12); color: var(--di-warning); border-color: rgba(245, 158, 11, 0.25); }
    .di-risk-cell-green { background: rgba(16, 185, 129, 0.12); color: var(--di-success); border-color: rgba(16, 185, 129, 0.25); }
    
    .di-risk-cell-count {
      font-size: 1.3rem;
      font-weight: 700;
    }
    
    .di-risk-cell-label {
      font-size: 0.65rem;
      text-transform: uppercase;
      opacity: 0.8;
    }
    
    .di-calibration-svg {
      background: rgba(var(--mono-rgb-200), 0.01);
      border-radius: 8px;
      border: 1px solid var(--di-card-border);
      max-width: 100%;
    }
    
    .di-calibration-point {
      fill: var(--interactive-accent);
      stroke: var(--background-primary);
      stroke-width: 1.5;
    }
    
    .di-calibration-line {
      stroke: var(--interactive-accent);
      stroke-width: 2px;
      fill: none;
    }
    
    .di-calibration-diagonal {
      stroke: var(--text-muted);
      stroke-width: 1px;
      stroke-dasharray: 4;
      opacity: 0.5;
    }
    
    .di-calibration-axis {
      stroke: var(--di-card-border);
      stroke-width: 1px;
    }
    
    .di-calibration-text {
      font-size: 9px;
      fill: var(--text-muted);
    }
    
    .di-prompt-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.5);
      z-index: 1000;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .di-prompt-modal {
      background: var(--background-primary);
      border-radius: 12px;
      padding: 1.5rem;
      min-width: 360px;
      max-width: 500px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    .di-prompt-title {
      font-weight: 600;
      font-size: 1rem;
      margin-bottom: 0.75rem;
    }
    .di-prompt-input {
      width: 100%;
      box-sizing: border-box;
      margin-bottom: 1rem;
    }
    .di-prompt-actions {
      display: flex;
      gap: 0.5rem;
      justify-content: flex-end;
    }
  `;
  document.head.appendChild(styleEl);
}

// Custom prompt (replaces window.prompt which is often blocked in Obsidian)
function showPrompt(message, defaultValue) {
  return new Promise((resolve) => {
    const overlay = mainContainer.createEl('div', { cls: 'di-prompt-overlay' });
    overlay.innerHTML =
      '<div class="di-prompt-modal">' +
        '<div class="di-prompt-title">' + message + '</div>' +
        '<input type="text" class="di-input di-prompt-input" value="' + (defaultValue || '') + '" autofocus>' +
        '<div class="di-prompt-actions">' +
          '<button class="di-btn" id="di-prompt-cancel">Cancel</button>' +
          '<button class="di-btn di-btn-primary" id="di-prompt-submit">OK</button>' +
        '</div>' +
      '</div>';
    
    const input = overlay.querySelector('.di-prompt-input');
    input.focus();
    input.select();
    
    const cleanup = () => { if (overlay.isConnected) overlay.remove(); };
    
    overlay.querySelector('#di-prompt-submit').addEventListener('click', () => {
      cleanup();
      resolve(input.value);
    });
    overlay.querySelector('#di-prompt-cancel').addEventListener('click', () => {
      cleanup();
      resolve(null);
    });
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') { cleanup(); resolve(input.value); }
      if (e.key === 'Escape') { cleanup(); resolve(null); }
    });
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) { cleanup(); resolve(null); }
    });
  });
}

// Global renderer function
async function render() {
  mainContainer.innerHTML = '';
  
  // Fetch lists
  const signals = dv.pages('"01-intelligence/signals"');
  const trends = dv.pages('"01-intelligence/trends"');
  const competitors = dv.pages('"01-intelligence/competitors"');
  const opportunities = dv.pages('"01-intelligence/opportunities"') || dv.pages('"05-strategy/portfolio"');
  const assumptions = dv.pages('"02-decisions/assumptions"');
  const memos = dv.pages('"02-decisions/memos"');
  const forecasts = dv.pages('"02-decisions/forecasts"');
  const initiatives = dv.pages('"03-execution/initiatives"');
  const kpis = dv.pages('"03-execution/kpis"');
  const risks = dv.pages('"03-execution/risks"');
  const outcomes = dv.pages('"04-learning/outcomes"');
  const lessons = dv.pages('"04-learning/lessons"');
  
  // Helpers
  const getBadge = (text, status) => {
    if (!text) return `<span class="di-badge di-badge-info">N/A</span>`;
    if (!status) status = text;
    status = status.toLowerCase();
    
    let type = 'info';
    if (['approved', 'validated', 'success', 'active', 'high-quality', 'complete', 'improving', 'high'].includes(status)) type = 'success';
    else if (['draft', 'unvalidated', 'paused', 'medium', 'researching', 'reversible', 'stable'].includes(status)) type = 'warning';
    else if (['rejected', 'critical', 'high', 'failed', 'declining', 'unprocessed'].includes(status)) type = 'danger';
    else if (['irreversible', 'planned', 'strategic'].includes(status)) type = 'purple';
    
    return `<span class="di-badge di-badge-${type}">${text}</span>`;
  };
  
  const getProgressBar = (val, max = 10) => {
    const pct = Math.min(Math.max((parseFloat(val) / max) * 100, 0), 100);
    return `
      <div class="di-progress-container">
        <div class="di-progress">
          <div class="di-progress-bar" style="width: ${pct}%"></div>
        </div>
        <div class="di-progress-label">${parseFloat(val).toFixed(1)}</div>
      </div>
    `;
  };
  
  // 1. Header and tab setup
  const headerEl = mainContainer.createEl('div', { cls: 'di-header' });
  headerEl.innerHTML = `
    <h1>🧠 CEO Decision Intelligence OS</h1>
    <p class="di-subtitle">Single-pane-of-glass executive cockpit. Live-updated from vault metadata.</p>
    <div class="di-tabs">
      <button class="di-tab ${state.activeTab === 'summary' ? 'is-active' : ''}" data-tab="summary">📊 Executive Overview</button>
      <button class="di-tab ${state.activeTab === 'intelligence' ? 'is-active' : ''}" data-tab="intelligence">📡 Intelligence Hub</button>
      <button class="di-tab ${state.activeTab === 'decisions' ? 'is-active' : ''}" data-tab="decisions">📋 Decisions &amp; Forecasts</button>
      <button class="di-tab ${state.activeTab === 'execution' ? 'is-active' : ''}" data-tab="execution">🚀 Execution &amp; Risks</button>
      <button class="di-tab ${state.activeTab === 'learning' ? 'is-active' : ''}" data-tab="learning">🧠 Learning &amp; Calibration</button>
    </div>
  `;
  
  headerEl.querySelectorAll('.di-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      state.activeTab = btn.getAttribute('data-tab');
      render();
    });
  });
  
  // 2. Active Tab Renders
  const contentEl = mainContainer.createEl('div', { cls: 'di-content' });
  
  if (state.activeTab === 'summary') {
    // Action Required / Alert Banner
    const today = new Date().toISOString().split('T')[0];
    const alerts = [];
    
    forecasts.forEach(f => {
      if (f.status === 'active' && f.deadline && f.deadline < today) {
        alerts.push(`Overdue Forecast: <a class="internal-link" href="${f.file.path}">${f.file.name}</a> deadline was ${f.deadline}`);
      }
    });
    
    assumptions.forEach(a => {
      if (a.status === 'unvalidated' && a.confidence_score <= 4 && (a.invalidation_risk === 'critical' || a.invalidation_risk === 'high')) {
        alerts.push(`Critical Weak Assumption: <a class="internal-link" href="${a.file.path}">${a.file.name}</a> confidence is ${a.confidence_score}`);
      }
      if (a.status === 'unvalidated' && a.validation_deadline && a.validation_deadline < today) {
        alerts.push(`Overdue Assumption Validation: <a class="internal-link" href="${a.file.path}">${a.file.name}</a> deadline was ${a.validation_deadline}`);
      }
    });
    
    memos.forEach(m => {
      if ((m.status === 'draft' || m.status === 'ready-for-review') && m.review_date && m.review_date < today) {
        alerts.push(`Overdue Memo Review: <a class="internal-link" href="${m.file.path}">${m.file.name}</a> review date was ${m.review_date}`);
      }
    });
    
    if (alerts.length > 0) {
      const banner = contentEl.createEl('div', { cls: 'di-alert-banner' });
      banner.innerHTML = `
        <div class="di-alert-header">🚨 Action Required (Alert Center)</div>
        ${alerts.map(a => `<div class="di-alert-item">${a}</div>`).join('')}
      `;
    } else {
      const banner = contentEl.createEl('div', { cls: 'di-alert-empty' });
      banner.innerHTML = `<div>✅ All systems operational. No critical risk triggers active.</div>`;
    }
    
    // Metrics Grid
    const gridEl = contentEl.createEl('div', { cls: 'di-metrics-grid', style: 'margin-top: 1rem;' });
    
    // Brier score calculation
    const resolvedForecasts = forecasts.filter(f => f.status === 'resolved');
    let avgBrier = null;
    let brierClass = 'brier-excellent';
    let brierText = 'N/A';
    
    if (resolvedForecasts.length > 0) {
      const brierScores = resolvedForecasts.map(f => f.brier_score).filter(s => s !== null && s !== undefined);
      if (brierScores.length > 0) {
        avgBrier = brierScores.reduce((a, b) => a + b, 0) / brierScores.length;
        brierText = avgBrier.toFixed(3);
        if (avgBrier <= 0.05) brierClass = 'brier-excellent';
        else if (avgBrier <= 0.10) brierClass = 'brier-good';
        else if (avgBrier <= 0.20) brierClass = 'brier-moderate';
        else brierClass = 'brier-poor';
      }
    }
    
    gridEl.createEl('div', { cls: `di-metric-card ${brierClass}` }).innerHTML = `
      <div class="di-metric-title">Forecasting Brier</div>
      <div class="di-metric-value">${brierText}</div>
      <div class="di-metric-sub">${resolvedForecasts.length} Resolved Forecasts</div>
    `;
    
    const openDecs = memos.filter(m => m.status === 'draft' || m.status === 'ready-for-review');
    gridEl.createEl('div', { cls: 'di-metric-card' }).innerHTML = `
      <div class="di-metric-title">Open Decisions</div>
      <div class="di-metric-value">${openDecs.length}</div>
      <div class="di-metric-sub">${memos.filter(m => m.status === 'approved').length} Active (Approved)</div>
    `;
    
    const unvalAsm = assumptions.filter(a => a.status === 'unvalidated');
    gridEl.createEl('div', { cls: 'di-metric-card' }).innerHTML = `
      <div class="di-metric-title">Unvalidated Assumptions</div>
      <div class="di-metric-value">${unvalAsm.length}</div>
      <div class="di-metric-sub">${assumptions.filter(a => a.status === 'validated').length} Validated</div>
    `;
    
    gridEl.createEl('div', { cls: 'di-metric-card' }).innerHTML = `
      <div class="di-metric-title">Active Forecasts</div>
      <div class="di-metric-value">${forecasts.filter(f => f.status === 'active').length}</div>
      <div class="di-metric-sub">Brier Target &lt; 0.10</div>
    `;
    
    gridEl.createEl('div', { cls: 'di-metric-card' }).innerHTML = `
      <div class="di-metric-title">Active Initiatives</div>
      <div class="di-metric-value">${initiatives.filter(i => i.status === 'active').length}</div>
      <div class="di-metric-sub">${kpis.filter(k => k.status === 'active').length} KPIs Tracked</div>
    `;
    
    // Top Opportunities Panel
    const oppPanel = contentEl.createEl('div', { cls: 'di-panel', style: 'margin-top: 1rem;' });
    
    const sortedOpps = [...opportunities].map(o => {
      let score = parseFloat(o.composite_score || 0);
      if (score === 0) {
        score = (o.score_expected_return || 0) * 0.25 + 
                (o.score_probability || 0) * 0.20 + 
                (o.score_strategic_fit || 0) * 0.20 - 
                (o.score_execution_complexity || 0) * 0.15 - 
                (o.score_resource_requirement || 0) * 0.10 - 
                (o.score_risk || 0) * 0.10;
      }
      return { note: o, score: score };
    }).sort((a, b) => b.score - a.score);
    
    oppPanel.innerHTML = `
      <div class="di-panel-title">🏆 Top Strategic Opportunities <span>Composite score auto-calculated</span></div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>Opportunity</th>
              <th>Category</th>
              <th>Est. Value</th>
              <th>Composite Score</th>
              <th>Readiness</th>
            </tr>
          </thead>
          <tbody>
            ${sortedOpps.length === 0 ? '<tr><td colspan="5">No opportunities registered.</td></tr>' :
              sortedOpps.map(item => {
                const o = item.note;
                const formattedVal = typeof o.estimated_value === 'number' ? 
                  '$' + o.estimated_value.toLocaleString() : (o.estimated_value || '$0');
                return `
                  <tr>
                    <td><a class="internal-link" href="${o.file.path}">${o.file.name}</a></td>
                    <td>${getBadge(o.category || 'General')}</td>
                    <td>${formattedVal}</td>
                    <td>${getProgressBar(item.score, 10)}</td>
                    <td>${getBadge(o.decision_readiness || 'Research Needed')}</td>
                  </tr>
                `;
              }).join('')
            }
          </tbody>
        </table>
      </div>
    `;
  }
  
  else if (state.activeTab === 'intelligence') {
    // Filters Panel
    const filters = contentEl.createEl('div', { cls: 'di-filter-bar' });
    filters.innerHTML = `
      <span class="di-filter-label">🔍 Search Signals:</span>
      <input type="text" class="di-input sig-search-input" placeholder="Type to filter..." value="${state.signalSearch}">
      
      <span class="di-filter-label" style="margin-left:auto;">🎯 Opp Status:</span>
      <select class="di-select opp-status-select">
        <option value="all" ${state.opportunityFilter === 'all' ? 'selected' : ''}>All Statuses</option>
        <option value="researching" ${state.opportunityFilter === 'researching' ? 'selected' : ''}>Researching</option>
        <option value="ready-for-review" ${state.opportunityFilter === 'ready-for-review' ? 'selected' : ''}>Ready for Review</option>
        <option value="approved" ${state.opportunityFilter === 'approved' ? 'selected' : ''}>Approved</option>
      </select>
      
      <button class="di-btn di-btn-primary" id="btn-new-signal">📡 Ingest Signal</button>
      <button class="di-btn" id="btn-new-opp">🏆 Add Opportunity</button>
    `;
    
    const intelGrid = contentEl.createEl('div');
    
    // Define updateIntelGrid first so event handlers can reference it
    const updateIntelGrid = () => {
      intelGrid.innerHTML = '';
      
      const searchLower = state.signalSearch.toLowerCase();
      const filteredSignals = signals.filter(s => {
        const text = (s.title + ' ' + (s.source || '')).toLowerCase();
        return text.includes(searchLower);
      });
      
      const filteredOpps = opportunities.filter(o => {
        if (state.opportunityFilter === 'all') return true;
        return o.status === state.opportunityFilter;
      });
      
      const layout = intelGrid.createEl('div', { style: 'display:grid; grid-template-columns: 1.1fr 0.9fr; gap:1.5rem; margin-top:1rem;' });
      
      // Signals
      const sigPanel = layout.createEl('div', { cls: 'di-panel' });
      sigPanel.innerHTML = `
        <div class="di-panel-title">📡 Captured Signals (Matching: ${filteredSignals.length})</div>
        <div class="di-table-wrapper">
          <table class="di-table">
            <thead>
              <tr>
                <th>Signal</th>
                <th>Strength</th>
                <th>Confidence</th>
                <th>Source</th>
              </tr>
            </thead>
            <tbody>
              ${filteredSignals.length === 0 ? '<tr><td colspan="4">No matching signals.</td></tr>' :
                filteredSignals.slice(0, 10).map(s => `
                  <tr>
                    <td><a class="internal-link" href="${s.file.path}">${s.file.name}</a></td>
                    <td>${getBadge(s.strength || 'Medium')}</td>
                    <td>${getProgressBar(s.confidence_score || 5, 10)}</td>
                    <td>${s.source ? `<a href="${s.source}" target="_blank">${s.source_quality || 'Link'}</a>` : 'N/A'}</td>
                  </tr>
                `).join('')
              }
            </tbody>
          </table>
        </div>
      `;
      
      // Trends
      const trendPanel = layout.createEl('div', { cls: 'di-panel' });
      trendPanel.innerHTML = `
        <div class="di-panel-title">📈 Active Trends</div>
        <div class="di-table-wrapper">
          <table class="di-table">
            <thead>
              <tr>
                <th>Trend</th>
                <th>Confidence</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              ${trends.length === 0 ? '<tr><td colspan="3">No active trends.</td></tr>' :
                trends.map(t => `
                  <tr>
                    <td><a class="internal-link" href="${t.file.path}">${t.file.name}</a></td>
                    <td>${getProgressBar(t.confidence_score || 5, 10)}</td>
                    <td>${getBadge(t.status || 'Active')}</td>
                  </tr>
                `).join('')
              }
            </tbody>
          </table>
        </div>
      `;
      
      // Opportunity scoring portfolio matrix
      const matrixPanel = intelGrid.createEl('div', { cls: 'di-panel', style: 'margin-top:1.5rem;' });
      matrixPanel.innerHTML = `
        <div class="di-panel-title">🏆 Opportunity Scoring Matrix <span>Filters applied</span></div>
        <div class="di-table-wrapper">
          <table class="di-table">
            <thead>
              <tr>
                <th>Opportunity</th>
                <th>Return</th>
                <th>Probability</th>
                <th>Fit</th>
                <th>Complexity</th>
                <th>Resource</th>
                <th>Risk</th>
                <th>Composite Score</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              ${filteredOpps.length === 0 ? '<tr><td colspan="9">No opportunities matching filter.</td></tr>' :
                filteredOpps.map(o => {
                  let comp = parseFloat(o.composite_score || 0);
                  if (comp === 0) {
                    comp = (o.score_expected_return || 0) * 0.25 + 
                           (o.score_probability || 0) * 0.20 + 
                           (o.score_strategic_fit || 0) * 0.20 - 
                           (o.score_execution_complexity || 0) * 0.15 - 
                           (o.score_resource_requirement || 0) * 0.10 - 
                           (o.score_risk || 0) * 0.10;
                  }
                  return `
                    <tr>
                      <td><a class="internal-link" href="${o.file.path}">${o.file.name}</a></td>
                      <td>${o.score_expected_return || 5}/10</td>
                      <td>${o.score_probability || 5}/10</td>
                      <td>${o.score_strategic_fit || 5}/10</td>
                      <td>${o.score_execution_complexity || 5}/10</td>
                      <td>${o.score_resource_requirement || 5}/10</td>
                      <td>${o.score_risk || 5}/10</td>
                      <td>${getProgressBar(comp, 10)}</td>
                      <td>${getBadge(o.status || 'Draft')}</td>
                    </tr>
                  `;
                }).join('')
              }
            </tbody>
          </table>
        </div>
      `;
    };
    
    // Add filter events (after updateIntelGrid is defined)
    filters.querySelector('.sig-search-input').addEventListener('input', (e) => {
      try {
        state.signalSearch = e.target.value;
        updateIntelGrid();
      } catch (err) { console.error('Signal search error', err); }
    });
    filters.querySelector('.opp-status-select').addEventListener('change', (e) => {
      try {
        state.opportunityFilter = e.target.value;
        render();
      } catch (err) { console.error('Opp filter error', err); }
    });
    filters.querySelector('#btn-new-signal').addEventListener('click', async () => {
      try { await createEntity('01-intelligence/signals', 'SIG', 'Market Signal', 'signal.md'); }
      catch (err) { console.error('Signal creation error', err); }
    });
    filters.querySelector('#btn-new-opp').addEventListener('click', async () => {
      try { await createEntity('01-intelligence/opportunities', 'OPP', 'Strategic Opportunity', 'opportunity-v2.md'); }
      catch (err) { console.error('Opp creation error', err); }
    });
    
    updateIntelGrid();
  }
  
  else if (state.activeTab === 'decisions') {
    // Actions Panel
    const filters = contentEl.createEl('div', { cls: 'di-filter-bar' });
    filters.innerHTML = `
      <span class="di-filter-label">📋 Decisions &amp; Forecasting Registry</span>
      <button class="di-btn di-btn-primary" style="margin-left:auto;" id="btn-new-dec">📋 Draft Decision Memo</button>
      <button class="di-btn" id="btn-new-forecast">🎯 Add Forecast</button>
      <button class="di-btn" id="btn-new-assumption">🧩 Register Assumption</button>
    `;
    
    filters.querySelector('#btn-new-dec').addEventListener('click', async () => {
      try { await createEntity('02-decisions/memos', 'DEC', 'Decision Memo', 'decision-memo.md'); }
      catch (err) { console.error('Memo creation error', err); }
    });
    filters.querySelector('#btn-new-forecast').addEventListener('click', async () => {
      try { await createEntity('02-decisions/forecasts', 'FRC', 'Forecast Question', 'forecast-v2.md'); }
      catch (err) { console.error('Forecast creation error', err); }
    });
    filters.querySelector('#btn-new-assumption').addEventListener('click', async () => {
      try { await createEntity('02-decisions/assumptions', 'ASM', 'Hypothesis Statement', 'assumption-v2.md'); }
      catch (err) { console.error('Assumption creation error', err); }
    });
    
    const layout = contentEl.createEl('div', { style: 'display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem;' });
    
    // Memos
    const memoPanel = layout.createEl('div', { cls: 'di-panel' });
    memoPanel.innerHTML = `
      <div class="di-panel-title">📋 Decision Pipeline</div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>Memo</th>
              <th>Reversibility</th>
              <th>Confidence</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            ${memos.length === 0 ? '<tr><td colspan="4">No decision memos drafted.</td></tr>' :
              memos.map(m => `
                <tr>
                  <td><a class="internal-link" href="${m.file.path}">${m.file.name}</a></td>
                  <td>${getBadge(m.reversibility || 'Reversible')}</td>
                  <td>${getProgressBar(m.confidence_at_decision || 5, 10)}</td>
                  <td>${getBadge(m.status || 'Draft')}</td>
                </tr>
              `).join('')
            }
          </tbody>
        </table>
      </div>
    `;
    
    // Active Forecasts
    const activeF = forecasts.filter(f => f.status === 'active');
    const forePanel = layout.createEl('div', { cls: 'di-panel' });
    forePanel.innerHTML = `
      <div class="di-panel-title">🎯 Active Forecasts (${activeF.length})</div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>Question</th>
              <th>Prediction</th>
              <th>Deadline</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            ${activeF.length === 0 ? '<tr><td colspan="4">No active forecasts.</td></tr>' :
              activeF.map(f => `
                <tr>
                  <td><a class="internal-link" href="${f.file.path}">${f.file.name}</a></td>
                  <td><span style="font-weight:600;">${((f.predicted_probability || 0.5) * 100).toFixed(0)}%</span></td>
                  <td>${f.deadline || 'N/A'}</td>
                  <td><button class="di-btn btn-resolve" data-path="${f.file.path}">Resolve</button></td>
                </tr>
              `).join('')
            }
          </tbody>
        </table>
      </div>
    `;
    
    forePanel.querySelectorAll('.btn-resolve').forEach(btn => {
      btn.addEventListener('click', async () => {
        try {
          const path = btn.getAttribute('data-path');
          await resolveForecast(path);
        } catch (err) { console.error('Forecast resolution error', err); }
      });
    });
    
    // Assumptions Health Registry
    const asmPanel = contentEl.createEl('div', { cls: 'di-panel', style: 'margin-top:1.5rem;' });
    asmPanel.innerHTML = `
      <div class="di-panel-title">🧩 Assumption Intelligence Registry</div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>Assumption</th>
              <th>Category</th>
              <th>Risk Level</th>
              <th>Evidence</th>
              <th>Confidence</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            ${assumptions.length === 0 ? '<tr><td colspan="6">No assumptions recorded.</td></tr>' :
              assumptions.map(a => `
                <tr>
                  <td><a class="internal-link" href="${a.file.path}">${a.file.name}</a></td>
                  <td>${a.category || 'General'}</td>
                  <td>${getBadge(a.invalidation_risk || 'Medium')}</td>
                  <td>${getBadge(a.evidence_status || 'None')}</td>
                  <td>${getProgressBar(a.confidence_score || 5, 10)}</td>
                  <td>${getBadge(a.status || 'Unvalidated')}</td>
                </tr>
              `).join('')
            }
          </tbody>
        </table>
      </div>
    `;
  }
  
  else if (state.activeTab === 'execution') {
    // Actions Panel
    const filters = contentEl.createEl('div', { cls: 'di-filter-bar' });
    filters.innerHTML = `
      <span class="di-filter-label">🚀 Execution &amp; Risk Board</span>
      <button class="di-btn di-btn-primary" style="margin-left:auto;" id="btn-new-ini">🚀 Launch Initiative</button>
      <button class="di-btn" id="btn-new-kpi">📏 Add KPI Target</button>
      <button class="di-btn" id="btn-new-risk">🚨 Flag Risk</button>
    `;
    
    filters.querySelector('#btn-new-ini').addEventListener('click', async () => {
      try { await createEntity('03-execution/initiatives', 'INI', 'Initiative Name', 'initiative.md'); }
      catch (err) { console.error('Initiative creation error', err); }
    });
    filters.querySelector('#btn-new-kpi').addEventListener('click', async () => {
      try { await createEntity('03-execution/kpis', 'KPI', 'KPI Target', 'kpi.md'); }
      catch (err) { console.error('KPI creation error', err); }
    });
    filters.querySelector('#btn-new-risk').addEventListener('click', async () => {
      try { await createEntity('03-execution/risks', 'RSK', 'Risk Threat', 'risk.md'); }
      catch (err) { console.error('Risk creation error', err); }
    });
    
    const layout = contentEl.createEl('div', { style: 'display:grid; grid-template-columns: 1.1fr 0.9fr; gap:1.5rem;' });
    
    // Left side: Initiatives & KPIs
    const leftPane = layout.createEl('div', { style: 'display:flex; flex-direction:column; gap:1.5rem;' });
    
    leftPane.createEl('div', { cls: 'di-panel' }).innerHTML = `
      <div class="di-panel-title">🚀 Active Initiatives</div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>Initiative</th>
              <th>Budget</th>
              <th>Expected Impact</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            ${initiatives.length === 0 ? '<tr><td colspan="4">No initiatives running.</td></tr>' :
              initiatives.map(i => `
                <tr>
                  <td><a class="internal-link" href="${i.file.path}">${i.file.name}</a></td>
                  <td>$${(i.budget || 0).toLocaleString()}</td>
                  <td>${getBadge(i.expected_impact || 'Medium')}</td>
                  <td>${getBadge(i.status || 'Active')}</td>
                </tr>
              `).join('')
            }
          </tbody>
        </table>
      </div>
    `;
    
    leftPane.createEl('div', { cls: 'di-panel' }).innerHTML = `
      <div class="di-panel-title">📏 Key Performance Indicators (KPIs)</div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>KPI</th>
              <th>Target</th>
              <th>Actual</th>
              <th>Trend</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            ${kpis.length === 0 ? '<tr><td colspan="5">No KPIs configured.</td></tr>' :
              kpis.map(k => {
                let trendIcon = '→';
                if (k.trend === 'improving') trendIcon = '↑';
                if (k.trend === 'declining') trendIcon = '↓';
                return `
                  <tr>
                    <td><a class="internal-link" href="${k.file.path}">${k.file.name}</a></td>
                    <td>${k.target || 0}</td>
                    <td>${k.actual || 0}</td>
                    <td><span style="font-weight:700;">${trendIcon} ${k.trend || 'stable'}</span></td>
                    <td>${getBadge(k.status || 'Active')}</td>
                  </tr>
                `;
              }).join('')
            }
          </tbody>
        </table>
      </div>
    `;
    
    // Right side: Risk matrix & lists
    const rightPane = layout.createEl('div', { style: 'display:flex; flex-direction:column; gap:1.5rem;' });
    
    // Risk Heatmap
    let riskCounts = {
      'high-high': 0, 'high-medium': 0, 'high-low': 0,
      'medium-high': 0, 'medium-medium': 0, 'medium-low': 0,
      'low-high': 0, 'low-medium': 0, 'low-low': 0
    };
    risks.forEach(r => {
      if (r.status === 'active') {
        const impact = (r.impact || 'medium').toLowerCase();
        const prob = (r.probability || 'medium').toLowerCase();
        const key = `${prob}-${impact}`;
        if (riskCounts[key] !== undefined) riskCounts[key]++;
      }
    });
    
    rightPane.createEl('div', { cls: 'di-panel' }).innerHTML = `
      <div class="di-panel-title">🚨 Active Risk Heatmap</div>
      <div class="di-risk-matrix-panel">
        <div style="font-size:0.75rem; text-align:center; color:var(--text-muted);">Impact (Low → Med → High)</div>
        <div class="di-risk-grid">
          <div class="di-risk-cell di-risk-cell-orange"><span class="di-risk-cell-count">${riskCounts['high-low']}</span><span class="di-risk-cell-label">H/L</span></div>
          <div class="di-risk-cell di-risk-cell-red"><span class="di-risk-cell-count">${riskCounts['high-medium']}</span><span class="di-risk-cell-label">H/M</span></div>
          <div class="di-risk-cell di-risk-cell-red" style="box-shadow: 0 0 10px rgba(239,68,68,0.3);"><span class="di-risk-cell-count">${riskCounts['high-high']}</span><span class="di-risk-cell-label">H/H</span></div>
          
          <div class="di-risk-cell di-risk-cell-green"><span class="di-risk-cell-count">${riskCounts['medium-low']}</span><span class="di-risk-cell-label">M/L</span></div>
          <div class="di-risk-cell di-risk-cell-orange"><span class="di-risk-cell-count">${riskCounts['medium-medium']}</span><span class="di-risk-cell-label">M/M</span></div>
          <div class="di-risk-cell di-risk-cell-red"><span class="di-risk-cell-count">${riskCounts['medium-high']}</span><span class="di-risk-cell-label">M/H</span></div>
          
          <div class="di-risk-cell di-risk-cell-green"><span class="di-risk-cell-count">${riskCounts['low-low']}</span><span class="di-risk-cell-label">L/L</span></div>
          <div class="di-risk-cell di-risk-cell-green"><span class="di-risk-cell-count">${riskCounts['low-medium']}</span><span class="di-risk-cell-label">L/M</span></div>
          <div class="di-risk-cell di-risk-cell-orange"><span class="di-risk-cell-count">${riskCounts['low-high']}</span><span class="di-risk-cell-label">L/H</span></div>
        </div>
        <div style="font-size:0.75rem; text-align:center; color:var(--text-muted); margin-top:-0.5rem;">Probability (High at Top)</div>
      </div>
    `;
    
    rightPane.createEl('div', { cls: 'di-panel' }).innerHTML = `
      <div class="di-panel-title">🚨 Active Risks Registry</div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>Risk Note</th>
              <th>Probability</th>
              <th>Impact</th>
            </tr>
          </thead>
          <tbody>
            ${risks.length === 0 ? '<tr><td colspan="3">No active risks.</td></tr>' :
              risks.map(r => `
                <tr>
                  <td><a class="internal-link" href="${r.file.path}">${r.file.name}</a></td>
                  <td>${getBadge(r.probability || 'Medium')}</td>
                  <td>${getBadge(r.impact || 'Medium')}</td>
                </tr>
              `).join('')
            }
          </tbody>
        </table>
      </div>
    `;
  }
  
  else if (state.activeTab === 'learning') {
    const filters = contentEl.createEl('div', { cls: 'di-filter-bar' });
    filters.innerHTML = `
      <span class="di-filter-label">🧠 Learning &amp; Calibration</span>
      <button class="di-btn di-btn-primary" style="margin-left:auto;" id="btn-new-review">📝 Record Outcome Review</button>
      <button class="di-btn" id="btn-new-lesson">💡 Extract Lesson</button>
    `;
    
    filters.querySelector('#btn-new-review').addEventListener('click', async () => {
      try { await createEntity('04-learning/outcome-reviews', 'REV', 'Outcome Review', 'outcome-review.md'); }
      catch (err) { console.error('Review creation error', err); }
    });
    filters.querySelector('#btn-new-lesson').addEventListener('click', async () => {
      try { await createEntity('04-learning/lessons', 'LSN', 'Lesson Learned', 'lesson.md'); }
      catch (err) { console.error('Lesson creation error', err); }
    });
    
    const layout = contentEl.createEl('div', { style: 'display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem;' });
    
    // Left Pane: Stats & SVG Calibration Chart
    const leftPane = layout.createEl('div', { style: 'display:flex; flex-direction:column; gap:1.5rem;' });
    
    const resolvedForecasts = forecasts.filter(f => f.status === 'resolved');
    let brierText = 'N/A';
    let errText = 'N/A';
    let brierCardClass = 'brier-excellent';
    
    // Group resolved forecasts into probability bins for SVG graph
    let bins = [
      { name: '0-20%', min: 0.0, max: 0.20, count: 0, successes: 0, avgPred: 0 },
      { name: '21-40%', min: 0.21, max: 0.40, count: 0, successes: 0, avgPred: 0 },
      { name: '41-60%', min: 0.41, max: 0.60, count: 0, successes: 0, avgPred: 0 },
      { name: '61-80%', min: 0.61, max: 0.80, count: 0, successes: 0, avgPred: 0 },
      { name: '81-100%', min: 0.81, max: 1.0, count: 0, successes: 0, avgPred: 0 }
    ];
    
    if (resolvedForecasts.length > 0) {
      const scores = resolvedForecasts.map(f => f.brier_score).filter(s => s !== null && s !== undefined);
      const errors = resolvedForecasts.map(f => f.calibration_error).filter(e => e !== null && e !== undefined);
      
      if (scores.length > 0) {
        const avg = scores.reduce((a, b) => a + b, 0) / scores.length;
        brierText = avg.toFixed(3);
        if (avg <= 0.05) brierCardClass = 'brier-excellent';
        else if (avg <= 0.10) brierCardClass = 'brier-good';
        else if (avg <= 0.20) brierCardClass = 'brier-moderate';
        else brierCardClass = 'brier-poor';
      }
      
      if (errors.length > 0) {
        errText = (errors.reduce((a, b) => a + b, 0) / errors.length).toFixed(3);
      }
      
      // Compute bin values
      resolvedForecasts.forEach(f => {
        const pred = f.predicted_probability || 0;
        const actual = f.actual_probability || 0;
        for (let bin of bins) {
          if (pred >= bin.min && pred <= bin.max) {
            bin.count++;
            bin.avgPred += pred;
            if (actual === 1.0) bin.successes++;
            break;
          }
        }
      });
      bins.forEach(bin => {
        if (bin.count > 0) bin.avgPred = bin.avgPred / bin.count;
      });
    }
    
    // Draw SVG Calibration Chart
    const w = 300, h = 300, padding = 40;
    const chartW = w - 2 * padding;
    const chartH = h - 2 * padding;
    const getX = (val) => padding + val * chartW;
    const getY = (val) => padding + (1 - val) * chartH;
    
    let svg = `
      <svg class="di-calibration-svg" width="100%" height="240" viewBox="0 0 ${w} ${h}">
        <line class="di-calibration-diagonal" x1="${getX(0)}" y1="${getY(0)}" x2="${getX(1)}" y2="${getY(1)}" />
        <line class="di-calibration-axis" x1="${padding}" y1="${padding}" x2="${padding}" y2="${h - padding}" />
        <line class="di-calibration-axis" x1="${padding}" y1="${h - padding}" x2="${w - padding}" y2="${h - padding}" />
        
        <text class="di-calibration-text" x="${w / 2}" y="${h - 8}" text-anchor="middle">Predicted Probability</text>
        <text class="di-calibration-text" x="12" y="${h / 2}" text-anchor="middle" transform="rotate(-90 12 ${h / 2})">Actual Rate</text>
        
        <text class="di-calibration-text" x="${getX(0)}" y="${h - padding + 15}" text-anchor="middle">0%</text>
        <text class="di-calibration-text" x="${getX(0.5)}" y="${h - padding + 15}" text-anchor="middle">50%</text>
        <text class="di-calibration-text" x="${getX(1)}" y="${h - padding + 15}" text-anchor="middle">100%</text>
        
        <text class="di-calibration-text" x="${padding - 6}" y="${getY(0) + 3}" text-anchor="end">0%</text>
        <text class="di-calibration-text" x="${padding - 6}" y="${getY(0.5) + 3}" text-anchor="end">50%</text>
        <text class="di-calibration-text" x="${padding - 6}" y="${getY(1) + 3}" text-anchor="end">100%</text>
    `;
    
    let pts = [];
    bins.forEach(bin => {
      if (bin.count > 0) {
        pts.push({ x: bin.avgPred, y: bin.successes / bin.count, count: bin.count });
      }
    });
    
    if (pts.length > 0) {
      let pathD = `M ${getX(pts[0].x)} ${getY(pts[0].y)}`;
      for (let i = 1; i < pts.length; i++) {
        pathD += ` L ${getX(pts[i].x)} ${getY(pts[i].y)}`;
      }
      svg += `<path class="di-calibration-line" d="${pathD}" />`;
      pts.forEach(p => {
        svg += `<circle class="di-calibration-point" cx="${getX(p.x)}" cy="${getY(p.y)}" r="4"><title>Pred: ${(p.x*100).toFixed(0)}%, Actual: ${(p.y*100).toFixed(0)}% (${p.count} forecasts)</title></circle>`;
      });
    } else {
      svg += `
        <text class="di-calibration-text" x="${w / 2}" y="${h / 2 - 10}" text-anchor="middle" style="fill: var(--text-muted); font-style: italic;">No resolved forecasts</text>
        <text class="di-calibration-text" x="${w / 2}" y="${h / 2 + 10}" text-anchor="middle" style="fill: var(--text-muted); font-size: 8px;">Calibration curve plots here</text>
      `;
    }
    svg += `</svg>`;
    
    const stats = leftPane.createEl('div', { cls: 'di-panel' });
    stats.innerHTML = `
      <div class="di-panel-title">🎯 Live Forecast Calibration</div>
      <div style="display:flex; gap:1rem; margin-bottom:0.5rem;">
        <div class="di-metric-card ${brierCardClass}" style="flex-grow:1;">
          <div class="di-metric-title">Average Brier Score</div>
          <div class="di-metric-value">${brierText}</div>
          <div class="di-metric-sub">Ideal: 0.00 (Low = Better)</div>
        </div>
        <div class="di-metric-card" style="flex-grow:1;">
          <div class="di-metric-title">Calibration Error</div>
          <div class="di-metric-value">${errText}</div>
          <div class="di-metric-sub">&lt; 0 means underconfident</div>
        </div>
      </div>
      <div style="text-align:center; padding-top:0.5rem;">
        ${svg}
      </div>
    `;
    
    // Outcomes List
    leftPane.createEl('div', { cls: 'di-panel' }).innerHTML = `
      <div class="di-panel-title">📝 Outcome Reviews</div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>Outcome Note</th>
              <th>Result</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            ${outcomes.length === 0 ? '<tr><td colspan="3">No outcome reviews recorded.</td></tr>' :
              outcomes.map(o => `
                <tr>
                  <td><a class="internal-link" href="${o.file.path}">${o.file.name}</a></td>
                  <td>${getBadge(o.result || 'Success')}</td>
                  <td>${o.resolution_date || o.created || 'N/A'}</td>
                </tr>
              `).join('')
            }
          </tbody>
        </table>
      </div>
    `;
    
    // Right Pane: Lessons & Failures
    const rightPane = layout.createEl('div', { style: 'display:flex; flex-direction:column; gap:1.5rem;' });
    
    // Lessons
    rightPane.createEl('div', { cls: 'di-panel' }).innerHTML = `
      <div class="di-panel-title">💡 Recent Lessons Learned</div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>Lesson Note</th>
              <th>Category</th>
              <th>Trigger</th>
            </tr>
          </thead>
          <tbody>
            ${lessons.length === 0 ? '<tr><td colspan="3">No lessons logged.</td></tr>' :
              lessons.slice(0, 8).map(l => `
                <tr>
                  <td><a class="internal-link" href="${l.file.path}">${l.file.name}</a></td>
                  <td>${getBadge(l.category || 'Forecasting')}</td>
                  <td>${l.trigger || 'N/A'}</td>
                </tr>
              `).join('')
            }
          </tbody>
        </table>
      </div>
    `;
    
    // Failure Loops
    const failureLoops = lessons.filter(l => l.recurrence_count > 1);
    rightPane.createEl('div', { cls: 'di-panel' }).innerHTML = `
      <div class="di-panel-title">🔁 Repeated Failure Loops</div>
      <div class="di-table-wrapper">
        <table class="di-table">
          <thead>
            <tr>
              <th>Pattern / Lesson</th>
              <th>Recurrences</th>
              <th>Category</th>
            </tr>
          </thead>
          <tbody>
            ${failureLoops.length === 0 ? '<tr><td colspan="3">No repeated failure patterns logged (recurrence &gt; 1).</td></tr>' :
              failureLoops.map(f => `
                <tr>
                  <td><a class="internal-link" href="${f.file.path}">${f.file.name}</a></td>
                  <td><span style="color:var(--di-danger); font-weight:700;">${f.recurrence_count} times</span></td>
                  <td>${getBadge(f.category || 'Operational')}</td>
                </tr>
              `).join('')
            }
          </tbody>
        </table>
      </div>
    `;
  }
}

// Interactive Forecast Resolution Helper
async function resolveForecast(filePath) {
  const file = app.vault.getAbstractFileByPath(filePath);
  if (!file) {
    new Notice("Could not load forecast note: " + filePath);
    return;
  }
  
  const content = await app.vault.read(file);
  const outcomeDesc = await showPrompt("Describe the actual outcome that occurred:");
  if (!outcomeDesc || outcomeDesc.trim() === '') {
    new Notice("Resolution cancelled.");
    return;
  }
  
  const outcomeProb = await showPrompt("Set actual outcome probability (1 = Occurred, 0 = Did not occur):", "1");
  if (outcomeProb === null) return;
  
  const actualProb = parseFloat(outcomeProb);
  if (actualProb !== 0 && actualProb !== 1) {
    new Notice("Probability must be 0 or 1!");
    return;
  }
  
  // Extract predicted probability
  const predMatch = content.match(/predicted_probability:\s*([\d.]+)/);
  if (!predMatch) {
    new Notice("Could not find predicted_probability in forecast note!");
    return;
  }
  const predicted = parseFloat(predMatch[1]);
  const brier = Math.pow(predicted - actualProb, 2);
  const error = predicted - actualProb;
  const todayStr = new Date().toISOString().split('T')[0];
  
  // Update frontmatter values
  const updates = {
    status: 'resolved',
    actual_outcome: `"${outcomeDesc.replace(/"/g, '\\"')}"`,
    actual_probability: actualProb,
    brier_score: brier.toFixed(4),
    calibration_error: error.toFixed(4),
    resolution_date: todayStr
  };
  
  let newContent = updateFrontmatter(content, updates);
  
  // Update body with outcome resolution details
  const divider = "\n---\n";
  const parts = newContent.split(divider);
  if (parts.length >= 2) {
    let body = parts.slice(2).join(divider);
    if (!body.includes('## Actual Outcome Resolution')) {
      body += `\n\n## Actual Outcome Resolution\n- **Resolved Date:** ${todayStr}\n- **Outcome Details:** ${outcomeDesc}\n- **Brier Score Contribution:** ${brier.toFixed(4)} (Error: ${error.toFixed(4)})\n`;
    }
    newContent = parts[0] + divider + parts[1] + divider + body;
  }
  
  try {
    await app.vault.modify(file, newContent);
    new Notice("✅ Forecast resolved — Brier: " + brier.toFixed(4));
    render();
  } catch (e) {
    console.error("Error saving forecast", e);
    new Notice("❌ Error modifying forecast note: " + e.message);
  }
}

// Frontmatter Helper
function updateFrontmatter(content, updates) {
  const parts = content.split('---\n');
  if (parts.length < 3) return content;
  
  let frontmatterText = parts[1];
  const lines = frontmatterText.split('\n');
  const fmData = {};
  
  lines.forEach(line => {
    const colonIdx = line.indexOf(':');
    if (colonIdx > 0) {
      const key = line.substring(0, colonIdx).trim();
      const val = line.substring(colonIdx + 1).trim();
      fmData[key] = val;
    }
  });
  
  Object.keys(updates).forEach(key => {
    fmData[key] = updates[key];
  });
  
  const newLines = [];
  const updatedKeys = new Set(Object.keys(updates));
  
  lines.forEach(line => {
    const colonIdx = line.indexOf(':');
    if (colonIdx > 0) {
      const key = line.substring(0, colonIdx).trim();
      if (updatedKeys.has(key)) {
        newLines.push(`${key}: ${updates[key]}`);
        updatedKeys.delete(key);
      } else {
        newLines.push(line);
      }
    } else if (line.trim() !== '') {
      newLines.push(line);
    }
  });
  
  updatedKeys.forEach(key => {
    newLines.push(`${key}: ${updates[key]}`);
  });
  
  parts[1] = newLines.join('\n') + '\n';
  return parts.join('---\n');
}

// Create Note Helper
async function createEntity(folder, prefix, defaultName, templateName) {
  const title = await showPrompt(`Enter title for the new ${prefix}:`, defaultName);
  if (!title || title.trim() === '') {
    new Notice("Cancelled — no title entered.");
    return;
  }
  title = title.trim();
  
  const formattedTitle = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
  
  const files = app.vault.getMarkdownFiles().filter(f => f.path.startsWith(folder + "/"));
  let nextId = 1;
  const idRegex = new RegExp(prefix + "-(\\d+)");
  files.forEach(f => {
    const match = f.name.match(idRegex);
    if (match) {
      const num = parseInt(match[1]);
      if (num >= nextId) nextId = num + 1;
    }
  });
  
  const idString = `${prefix}-${String(nextId).padStart(3, '0')}`;
  const filename = `${folder}/${idString} — ${formattedTitle}.md`;
  
  let content = "";
  try {
    const templateFile = app.vault.getAbstractFileByPath(`templates/${templateName}`);
    if (templateFile) {
      content = await app.vault.read(templateFile);
      content = processTemplate(content, title, idString);
    } else {
      content = `---\nentity_id: ${idString}\nentity_type: ${prefix.toLowerCase()}\ntitle: "${title}"\ncreated: ${new Date().toISOString().split('T')[0]}\n---\n# ${title}\n`;
    }
  } catch (e) {
    console.error("Template read error", e);
    new Notice("Template read failed — using fallback.");
    content = `---\nentity_id: ${idString}\nentity_type: ${prefix.toLowerCase()}\ntitle: "${title}"\ncreated: ${new Date().toISOString().split('T')[0]}\n---\n# ${title}\n`;
  }
  
  try {
    const newFile = await app.vault.create(filename, content);
    await app.workspace.getLeaf().openFile(newFile);
    new Notice(`✅ Created: ${idString}`);
  } catch (e) {
    console.error("File creation error", e);
    new Notice("❌ Error creating note: " + e.message);
  }
}

function processTemplate(content, title, idString) {
  const today = new Date();
  const getFutureDate = (days) => {
    const d = new Date();
    d.setDate(d.getDate() + parseInt(days));
    return d.toISOString().split('T')[0];
  };
  
  return content
    .replace(/<%\s*tp\.file\.title\s*%>/g, title)
    .replace(/<%\s*tp\.file\.creation_date\([^)]*\)\s*%>/g, today.toISOString().split('T')[0])
    .replace(/<%\s*tp\.file\.last_modified_date\([^)]*\)\s*%>/g, today.toISOString().split('T')[0])
    .replace(/<%\s*tp\.date\.now\("YYYY-MM-DD",\s*(\d+)\)\s*%>/g, (match, days) => getFutureDate(days))
    .replace(/<%\s*tp\.date\.now\("YYYY-MM-DD"\)\s*%>/g, today.toISOString().split('T')[0])
    .replace(/{{title}}/g, title)
    .replace(/{{name}}/g, title)
    .replace(/entity_id:\s*""/g, `entity_id: ${idString}`)
    .replace(/entity_id:\s*null/g, `entity_id: ${idString}`)
    .replace(/entity_id:\s*\n/g, `entity_id: ${idString}\n`);
}

// Initial render
render();
```
