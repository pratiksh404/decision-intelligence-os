---
title: CEO Intelligence Cockpit
type: dashboard
created: 2026-06-13
updated: 2026-06-13
tags:
  - dashboard
  - executive
  - meta-intelligence
---
# 🧠 CEO Intelligence Cockpit

> Single-pane-of-glass view across all 6 intelligence layers.
> Refresh by reopening this note in Obsidian (Dataview auto-updates).

---

## 🔔 Action Required

```dataview
TABLE
  file.link AS "Item",
  type AS "Type",
  status AS "Status",
  review_date AS "Due"
FROM "vault"
WHERE review_date <= date(today) + dur(3 days)
  AND review_date >= date(today) - dur(7 days)
  AND status != "resolved" AND status != "archived" AND status != "rejected"
SORT review_date ASC
LIMIT 15
```

---

## 1. Intelligence Layer

### 📡 Signals (Last 7 Days)
```dataview
TABLE
  title AS "Signal",
  confidence_score AS "Confidence",
  file.ctime AS "Captured"
FROM "vault/01-intelligence/signals"
WHERE type = "signal" AND file.ctime >= date(today) - dur(7 days)
SORT file.ctime DESC
LIMIT 8
```

### 📈 Active Trends
```dataview
TABLE title AS "Trend", confidence_score AS "Confidence", status AS "Status"
FROM "vault/01-intelligence/trends"
WHERE type = "trend" AND status = "active"
SORT confidence_score DESC
LIMIT 5
```

### ⚔️ Competitor Moves (Updated This Month)
```dataview
TABLE title AS "Competitor", file.mtime AS "Last Updated"
FROM "vault/01-intelligence/competitors"
WHERE type = "competitor" AND file.mtime >= date(today) - dur(30 days)
SORT file.mtime DESC
```

---

## 2. Decision Layer

### 📋 Open Decisions
```dataview
TABLE
  title AS "Decision",
  status AS "Status",
  confidence_score AS "Confidence",
  review_date AS "Review Due"
FROM "vault/02-decisions/memos"
WHERE type = "decision" AND (status = "draft" OR status = "ready-for-review")
SORT review_date ASC
```

### ⚡ Decision Velocity (Last 90 Days)
```dataview
TABLE
  title AS "Decision",
  status AS "Status",
  created AS "Created",
  updated AS "Last Updated"
FROM "vault/02-decisions/memos"
WHERE type = "decision" AND file.ctime >= date(today) - dur(90 days)
SORT file.ctime DESC
```

---

## 3. Forecasting Layer

### 🎯 Forecasts Due (Next 30 Days)
```dataview
TABLE
  question AS "Question",
  predicted_probability AS "Probability",
  deadline AS "Deadline",
  category AS "Category"
FROM "vault/02-decisions/forecasts"
WHERE type = "forecast" AND status = "active"
  AND deadline <= date(today) + dur(30 days)
SORT deadline ASC
```

### 📊 Calibration Score (Recent)
```dataview
TABLE
  brier_score_period AS "Period",
  number_of_forecasts AS "Forecasts",
  average_brier_score AS "Avg Brier"
FROM "vault/04-learning/calibration"
WHERE type = "calibration"
SORT file.ctime DESC
LIMIT 3
```

---

## 4. Execution Layer

### 🚀 Active Initiatives
```dataview
TABLE
  title AS "Initiative",
  status AS "Status",
  review_date AS "Review Due"
FROM "vault/03-execution/initiatives"
WHERE type = "initiative" AND status = "active"
SORT review_date ASC
```

### 📏 Active KPIs
```dataview
TABLE title AS "KPI", status AS "Status", file.mtime AS "Updated"
FROM "vault/03-execution/kpis"
WHERE type = "kpi" AND status = "active"
SORT file.mtime ASC
```

### 🚨 High Impact Risks
```dataview
TABLE title AS "Risk", impact AS "Impact", probability AS "Probability"
FROM "vault/03-execution/risks"
WHERE type = "risk" AND status = "active" AND impact = "high"
SORT probability DESC
```

---

## 5. Learning Layer

### 💡 Recent Lessons
```dataview
TABLE title AS "Lesson", category AS "Category", file.ctime AS "Created"
FROM "vault/04-learning/lessons"
WHERE type = "lesson" AND file.ctime >= date(today) - dur(30 days)
SORT file.ctime DESC
LIMIT 5
```

### 🔁 Repeated Failures
```dataview
TABLE title AS "Pattern", recurrence_count AS "Times", category AS "Category"
FROM "vault/04-learning/lessons"
WHERE type = "lesson" AND recurrence_count > 1
SORT recurrence_count DESC
LIMIT 5
```

---

## 6. Strategy Layer

### 🏆 Top Opportunities
```dataview
TABLE
  title AS "Opportunity",
  composite_score AS "Score",
  market AS "Market",
  decision_readiness AS "Readiness"
FROM "vault/01-intelligence/opportunities" OR "vault/05-strategy/portfolio"
WHERE type = "opportunity" AND status != "rejected"
SORT composite_score DESC
LIMIT 8
```

### 🎲 Strategic Bets
```dataview
TABLE title AS "Bet", status AS "Status", confidence_score AS "Conviction"
FROM "vault/05-strategy/bets"
WHERE type = "strategic-bet" AND status = "active"
SORT confidence_score DESC
```

### 🗂️ Portfolio Distribution
```dataview
TABLE
  rows.file.name AS "Opportunities",
  length(rows) AS "Count",
  average(rows.composite_score) AS "Avg Score"
FROM "vault/01-intelligence/opportunities"
WHERE type = "opportunity" AND status != "rejected"
GROUP BY status
```

---

## System Health

```dataview
TABLE
  length(rows) AS "Count",
  rows.type AS "Types"
FROM "vault"
WHERE file.ctime >= date(today) - dur(7 days)
  AND type != null
GROUP BY type
SORT length(rows) DESC
```

_→ [[Forecast Calibration Dashboard]] | [[Assumption Intelligence Dashboard]] | [[Opportunity Scoring Engine]]_
