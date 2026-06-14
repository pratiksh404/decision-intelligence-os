---
title: Weekly Intelligence Report — <% tp.date.now("YYYY-[W]WW") %>
type: weekly-review
status: draft
created: <% tp.file.creation_date("YYYY-MM-DD") %>
updated: <% tp.file.last_modified_date("YYYY-MM-DD") %>
week: <% tp.date.now("YYYY-[W]WW") %>
owner: Founder/CEO
tags:
  - weekly-review
  - intelligence-report
  - meta-intelligence
---
# 📋 CEO Weekly Intelligence Report — <% tp.date.now("MMMM D, YYYY") %>

> **Purpose:** Synthesize what changed this week. Focus attention on signal over noise.
> **Time to complete:** 30–45 minutes.

---

## 1. Intelligence Summary

### New Signals This Week
```dataview
TABLE
  title AS "Signal",
  source AS "Source",
  confidence_score AS "Confidence",
  file.ctime AS "Captured"
FROM "vault/01-intelligence/signals"
WHERE type = "signal"
  AND file.ctime >= date(today) - dur(7 days)
SORT file.ctime DESC
```

### New Trends Identified
```dataview
TABLE
  title AS "Trend",
  confidence_score AS "Confidence",
  status AS "Status"
FROM "vault/01-intelligence/trends"
WHERE type = "trend"
  AND file.ctime >= date(today) - dur(7 days)
```

### Competitor Moves
```dataview
TABLE
  title AS "Competitor",
  status AS "Status",
  file.mtime AS "Last Updated"
FROM "vault/01-intelligence/competitors"
WHERE type = "competitor"
  AND file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
```

**This week's intelligence summary:**
_[Synthesize the 3 most important signals/trends/moves and their implications]_

---

## 2. Opportunity Summary

### New Opportunities
```dataview
TABLE
  title AS "Opportunity",
  market AS "Market",
  confidence_score AS "Confidence",
  decision_readiness AS "Readiness"
FROM "vault/01-intelligence/opportunities"
WHERE type = "opportunity"
  AND file.ctime >= date(today) - dur(7 days)
```

### Highest Scoring Active Opportunities
```dataview
TABLE
  title AS "Opportunity",
  market AS "Market",
  composite_score AS "Score",
  status AS "Status"
FROM "vault/01-intelligence/opportunities" OR "vault/05-strategy/portfolio"
WHERE type = "opportunity"
  AND (status = "researching" OR status = "ready-for-review")
SORT composite_score DESC
LIMIT 5
```

**Opportunity focus this week:**
_[Which opportunity deserves the most attention next week and why?]_

---

## 3. Decision Summary

### Open Decisions — Awaiting Action
```dataview
TABLE
  title AS "Decision",
  status AS "Status",
  review_date AS "Review Due",
  confidence_score AS "Confidence"
FROM "vault/02-decisions/memos"
WHERE type = "decision"
  AND (status = "draft" OR status = "ready-for-review")
SORT review_date ASC
```

### Decisions Under Monitoring
```dataview
TABLE
  title AS "Decision",
  review_date AS "Next Review",
  related_initiative AS "Initiative"
FROM "vault/02-decisions/memos"
WHERE type = "decision" AND status = "monitoring"
SORT review_date ASC
```

**Decision actions needed:**
_[Which decision must be resolved this week?]_

---

## 4. Forecast Summary

### Forecasts Due (Next 30 Days)
```dataview
TABLE
  question AS "Question",
  predicted_probability AS "Probability",
  deadline AS "Due Date",
  category AS "Category"
FROM "vault/02-decisions/forecasts"
WHERE type = "forecast"
  AND status = "active"
  AND deadline <= date(today) + dur(30 days)
SORT deadline ASC
```

### Forecasts Resolved This Week
```dataview
TABLE
  question AS "Question",
  predicted_probability AS "Predicted",
  actual_probability AS "Actual",
  brier_score AS "Brier Score"
FROM "vault/02-decisions/forecasts"
WHERE type = "forecast"
  AND status = "resolved"
  AND resolution_date >= date(today) - dur(7 days)
```

**Calibration note:**
_[Any systematic bias observed this week?]_

---

## 5. Risk Summary

### Emerging Risks (New This Week)
```dataview
TABLE
  title AS "Risk",
  impact AS "Impact",
  probability AS "Probability",
  related_initiative AS "Initiative"
FROM "vault/03-execution/risks"
WHERE type = "risk"
  AND status = "active"
  AND file.ctime >= date(today) - dur(7 days)
```

### High Impact Active Risks
```dataview
TABLE
  title AS "Risk",
  impact AS "Impact",
  probability AS "Probability",
  mitigation AS "Mitigation"
FROM "vault/03-execution/risks"
WHERE type = "risk"
  AND status = "active"
  AND impact = "high"
SORT probability DESC
```

**Risk posture this week:**
_[Has our overall risk level increased, decreased, or stayed stable?]_

---

## 6. Learning Summary

### Lessons Learned This Week
```dataview
TABLE
  title AS "Lesson",
  category AS "Category",
  related_review AS "Source Review"
FROM "vault/04-learning/lessons"
WHERE type = "lesson"
  AND file.ctime >= date(today) - dur(7 days)
```

### Patterns: Repeated Failures
```dataview
TABLE
  title AS "Lesson",
  recurrence_count AS "Times Seen",
  category AS "Category"
FROM "vault/04-learning/lessons"
WHERE type = "lesson"
  AND recurrence_count > 1
SORT recurrence_count DESC
LIMIT 5
```

---

## 7. Weekly Synthesis

### What Changed
_[2–3 sentences on the most important development this week]_

### Biggest Unknown
_[What do we most need to learn or resolve next week?]_

### CEO Priority for Next Week
1. 
2. 
3. 

### Confidence Assessment
- **Overall signal quality this week:** Low / Medium / High
- **Decision readiness:** Research Needed / Ready for Review / Ready for Action
- **Overall system health:** 🟢 On Track / 🟡 Watch / 🔴 Action Required
