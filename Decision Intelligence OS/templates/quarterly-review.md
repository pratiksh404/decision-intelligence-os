---
title: Quarterly Review — <% tp.date.now("YYYY") %> Q<% Math.ceil(tp.date.now("M") / 3) %>
type: quarterly-review
status: draft
created: <% tp.file.creation_date("YYYY-MM-DD") %>
quarter: <% tp.date.now("YYYY") %>-Q<% Math.ceil(tp.date.now("M") / 3) %>
owner: Founder/CEO
tags:
  - quarterly-review
  - strategy
  - review
---
# Quarterly Review — <% tp.date.now("YYYY") %> Q<% Math.ceil(tp.date.now("M") / 3) %>

## 1. Strategic Themes — Alignment Check

```dataview
TABLE
  title AS "Theme",
  status AS "Status",
  confidence_score AS "Confidence"
FROM "vault/05-strategy/themes"
WHERE type = "strategic-theme" AND status = "active"
```

**For each theme:** Is resource allocation aligned? Are KPIs trending correctly?

---

## 2. Resource Allocation Review

```dataview
TABLE
  title AS "Allocation",
  file.mtime AS "Last Updated"
FROM "vault/05-strategy/resources"
WHERE type = "resource-allocation"
SORT file.mtime DESC
LIMIT 5
```

**Reallocation decisions needed:**

---

## 3. Strategic Bets — Conviction Update

```dataview
TABLE
  title AS "Bet",
  status AS "Status",
  confidence_score AS "Confidence",
  review_date AS "Review Due"
FROM "vault/05-strategy/bets"
WHERE type = "strategic-bet"
SORT confidence_score ASC
```

**Bets to double down:**
**Bets to exit:**
**New bets to consider:**

---

## 4. Execution Review

### Initiative Health
```dataview
TABLE
  title AS "Initiative",
  status AS "Status",
  review_date AS "Review Date"
FROM "vault/03-execution/initiatives"
WHERE type = "initiative" AND status = "active"
SORT review_date ASC
```

### KPI Trend
```dataview
TABLE
  title AS "KPI",
  status AS "Status",
  file.mtime AS "Updated"
FROM "vault/03-execution/kpis"
WHERE type = "kpi" AND status = "active"
SORT file.mtime DESC
```

---

## 5. Quarterly Calibration Summary

**Total forecasts resolved this quarter:**
**Average Brier score this quarter:**
**Improvement vs previous quarter:**

**Top 3 decisions made this quarter:**
1. 
2. 
3. 

**Top 3 decisions to make next quarter:**
1. 
2. 
3. 

---

## 6. OKR / Priority Reset for Next Quarter

**Carry-forward priorities:**
**New priorities:**
**Sunset initiatives:**
