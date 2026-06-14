---
title: Forecast Calibration Dashboard
type: dashboard
created: 2026-06-13
updated: 2026-06-13
tags:
  - dashboard
  - calibration
  - meta-intelligence
---
# 📊 Forecast Calibration Dashboard

> Real-time view of forecasting accuracy across all categories, themes, and agents.
> Brier Score: lower = better. Perfect calibration = 0.00. Random = 0.25.

---

## 🔴 Overdue Forecasts — Needs Resolution

```dataview
TABLE
  question AS "Question",
  predicted_probability AS "Predicted %",
  deadline AS "Deadline",
  related_decision AS "Decision"
FROM "02-decisions/forecasts"
WHERE type = "forecast"
  AND status = "active"
  AND deadline < date(today)
SORT deadline ASC
```

---

## 🟡 Due This Month

```dataview
TABLE
  question AS "Question",
  predicted_probability AS "Predicted %",
  confidence_score AS "Confidence",
  deadline AS "Due"
FROM "02-decisions/forecasts"
WHERE type = "forecast"
  AND status = "active"
  AND deadline >= date(today)
  AND deadline <= date(today) + dur(30 days)
SORT deadline ASC
```

---

## ✅ Resolved Forecasts — Calibration Record

```dataview
TABLE
  question AS "Question",
  predicted_probability AS "Predicted",
  actual_probability AS "Actual",
  brier_score AS "Brier Score",
  calibration_error AS "Error",
  resolution_date AS "Resolved"
FROM "02-decisions/forecasts"
WHERE type = "forecast"
  AND status = "resolved"
SORT resolution_date DESC
```

---

## 📈 Accuracy by Category

```dataview
TABLE
  rows.file.name AS "Forecasts",
  average(rows.brier_score) AS "Avg Brier Score",
  length(rows) AS "Count"
FROM "02-decisions/forecasts"
WHERE type = "forecast" AND status = "resolved"
GROUP BY category
SORT average(rows.brier_score) ASC
```

---

## 🎯 Accuracy by Strategic Theme

```dataview
TABLE
  rows.file.name AS "Forecasts",
  average(rows.brier_score) AS "Avg Brier Score",
  length(rows) AS "Count"
FROM "02-decisions/forecasts"
WHERE type = "forecast" AND status = "resolved" AND strategic_theme != null
GROUP BY strategic_theme
SORT average(rows.brier_score) ASC
```

---

## 📉 Worst Forecasts (Highest Brier Score)

```dataview
TABLE
  question AS "Question",
  predicted_probability AS "Predicted",
  actual_probability AS "Actual",
  brier_score AS "Brier Score",
  category
FROM "02-decisions/forecasts"
WHERE type = "forecast" AND status = "resolved" AND brier_score > 0.15
SORT brier_score DESC
LIMIT 10
```

---

## 🧠 Calibration Audit Logs

```dataview
TABLE
  brier_score_period AS "Period",
  number_of_forecasts AS "# Forecasts",
  average_brier_score AS "Avg Brier"
FROM "04-learning/calibration"
WHERE type = "calibration"
SORT file.ctime DESC
LIMIT 12
```

---

## 📋 Resolution Workflow

When a forecast deadline arrives:

1. Open the forecast note
2. Record `actual_outcome` (description of what happened)
3. Set `actual_probability` to `1` (occurred) or `0` (did not occur)
4. Calculate: `brier_score = (predicted_probability - actual_probability)^2`
5. Calculate: `calibration_error = predicted_probability - actual_probability`
6. Set `status: resolved` and `resolution_date: YYYY-MM-DD`
7. Create linked `[[Outcome Review]]` if this was a major decision forecast
8. Add key learning to `vault/04-learning/lessons/`
9. Run monthly calibration audit via `templates/forecast-calibration.md`

---

## 📐 Brier Score Reference

| Score Range | Interpretation |
|---|---|
| 0.00 – 0.05 | Excellent calibration |
| 0.06 – 0.10 | Good calibration |
| 0.11 – 0.20 | Moderate — review bias |
| 0.21 – 0.25 | Poor — near-random |
| > 0.25 | Worse than random — systematic bias detected |
