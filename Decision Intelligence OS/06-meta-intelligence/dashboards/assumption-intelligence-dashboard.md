---
title: Assumption Intelligence Dashboard
type: dashboard
created: 2026-06-13
updated: 2026-06-13
tags:
  - dashboard
  - assumption
  - meta-intelligence
---
# 🧩 Assumption Intelligence Dashboard

> Track the health of all assumptions underlying active decisions.
> Weak or invalidated assumptions signal decision risk.

---

## 🔴 Invalidated Assumptions — Immediate Review Required

```dataview
TABLE
  title AS "Assumption",
  category AS "Category",
  invalidation_date AS "Invalidated",
  related_decisions AS "Linked Decisions"
FROM "02-decisions/assumptions"
WHERE type = "assumption" AND status = "rejected"
SORT invalidation_date DESC
```

---

## ⚠️ Weak Assumptions (Confidence ≤ 4)

```dataview
TABLE
  title AS "Assumption",
  confidence_score AS "Confidence",
  evidence_status AS "Evidence",
  importance AS "Importance",
  related_decisions AS "Decisions"
FROM "02-decisions/assumptions"
WHERE type = "assumption"
  AND status = "unvalidated"
  AND confidence_score <= 4
SORT confidence_score ASC
```

---

## 🎯 Critical Assumptions (Many Decisions Depend)

```dataview
TABLE
  title AS "Assumption",
  confidence_score AS "Confidence",
  invalidation_risk AS "Risk",
  length(related_decisions) AS "# Decisions"
FROM "02-decisions/assumptions"
WHERE type = "assumption"
  AND status != "rejected"
  AND length(related_decisions) > 1
SORT length(related_decisions) DESC
```

---

## 🟡 Overdue for Review

```dataview
TABLE
  title AS "Assumption",
  review_date AS "Review Due",
  confidence_score AS "Confidence",
  status AS "Status"
FROM "02-decisions/assumptions"
WHERE type = "assumption"
  AND review_date < date(today)
  AND status != "rejected"
  AND status != "validated"
SORT review_date ASC
```

---

## 🏗️ High Invalidation Risk

```dataview
TABLE
  title AS "Assumption",
  invalidation_risk AS "Risk Level",
  confidence_score AS "Confidence",
  evidence_status AS "Evidence"
FROM "02-decisions/assumptions"
WHERE type = "assumption"
  AND invalidation_risk = "high" OR invalidation_risk = "critical"
  AND status = "unvalidated"
SORT invalidation_risk DESC
```

---

## ✅ Validated Assumptions

```dataview
TABLE
  title AS "Assumption",
  category AS "Category",
  confidence_score AS "Confidence",
  updated AS "Validated"
FROM "02-decisions/assumptions"
WHERE type = "assumption" AND status = "validated"
SORT updated DESC
LIMIT 10
```

---

## 📊 Assumption Health by Category

```dataview
TABLE
  rows.file.name AS "Assumptions",
  length(rows) AS "Count",
  average(rows.confidence_score) AS "Avg Confidence"
FROM "02-decisions/assumptions"
WHERE type = "assumption" AND status != "rejected"
GROUP BY category
SORT average(rows.confidence_score) ASC
```

---

## 🔗 Assumption Dependency Graph

_Open the Obsidian graph view filtered to `type:assumption` to see the full dependency network._

Key dependencies to review manually:
```dataview
TABLE
  title AS "Assumption",
  depends_on_assumptions AS "Depends On"
FROM "02-decisions/assumptions"
WHERE type = "assumption"
  AND depends_on_assumptions != null
  AND length(depends_on_assumptions) > 0
```

---

## 📋 Review Workflow

**Weekly:** Run the `⚠️ Weak Assumptions` query. For each confidence ≤ 4:
1. Has new evidence emerged? Update evidence ledger.
2. Recalculate confidence score.
3. If evidence is strong enough, move to `status: validated`.
4. If disproven, move to `status: rejected`, set `invalidation_date`, and alert linked decisions.

**Monthly:** Run the `🎯 Critical Assumptions` query. Red-team each critical assumption.

**On Assumption Rejection:**
1. Set `status: rejected` and `invalidation_date`
2. Review all notes in `related_decisions`
3. Reassess those decisions — mark `status: ready-for-review`
4. Create a lesson note documenting the invalidation
