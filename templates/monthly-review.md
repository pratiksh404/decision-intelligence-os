---
title: Monthly Review — <% tp.date.now("YYYY-MM") %>
type: monthly-review
status: draft
created: <% tp.file.creation_date("YYYY-MM-DD") %>
month: <% tp.date.now("YYYY-MM") %>
owner: Founder/CEO
tags:
  - monthly-review
  - calibration
  - review
---
# Monthly Review — <% tp.date.now("MMMM YYYY") %>

## 1. Forecast Calibration

### Forecasts Resolved This Month
```dataview
TABLE
  question AS "Question",
  predicted_probability AS "Predicted",
  actual_probability AS "Actual",
  brier_score AS "Brier Score"
FROM "vault/02-decisions/forecasts"
WHERE type = "forecast"
  AND status = "resolved"
  AND resolution_date >= date(this.month) - dur(0 days)
  AND resolution_date < date(this.month) + dur(31 days)
SORT brier_score DESC
```

**Monthly average Brier score:**
**Calibration trend vs last month:**
**Bias detected:** Overconfident / Underconfident / Well-calibrated

### Forecasts Overdue (never resolved)
```dataview
TABLE question AS "Question", deadline AS "Deadline", predicted_probability AS "Predicted"
FROM "vault/02-decisions/forecasts"
WHERE type = "forecast" AND status = "active" AND deadline < date(today)
```

---

## 2. Bias Detection

### Bias Audit Triggers
Check each item — mark ✅ if clean, ⚠️ if detected:

- [ ] **Confirmation bias** — Did we update forecasts when disconfirming evidence appeared?
- [ ] **Overconfidence** — Average calibration_error > +0.15 this month?
- [ ] **Anchoring** — Any forecast unchanged for > 60 days despite new evidence?
- [ ] **Availability bias** — Were we overweighting recent dramatic events?
- [ ] **Sunk cost** — Any decisions continued despite negative signals?

**If biases detected:** Create a `bias-audit` note in `vault/04-learning/bias-audits/`

---

## 3. Portfolio Review

### Current Opportunity Rankings
```dataview
TABLE
  title AS "Opportunity",
  composite_score AS "Score",
  status AS "Status",
  decision_readiness AS "Readiness"
FROM "vault/01-intelligence/opportunities" OR "vault/05-strategy/portfolio"
WHERE type = "opportunity" AND status != "rejected"
SORT composite_score DESC
LIMIT 10
```

**Portfolio decisions this month:**
- New opportunities added:
- Opportunities rejected:
- Opportunities escalated to Decision Memo:

---

## 4. Learning Synthesis

### Lessons Created This Month
```dataview
TABLE title AS "Lesson", category AS "Category", related_review AS "Source"
FROM "vault/04-learning/lessons"
WHERE type = "lesson" AND file.ctime >= date(today) - dur(31 days)
```

**Top pattern observed:**
**System improvement to make:**

---

## 5. Monthly Calibration Entry

Create a new calibration note in `vault/04-learning/calibration/` using `templates/forecast-calibration.md`.
Record the aggregate Brier score for this month.
