---
title: Graph Health Report
entity_id: <% tp.file.title.split(" — ")[0] || "GHR-YYYY-WNN" %>
entity_type: graph-health-report
status: published
week_ending: <% tp.date.now("YYYY-MM-DD") %>
created: <% tp.file.creation_date("YYYY-MM-DD") %>
owner: Founder/CEO
tags:
  - graph-health
  - meta-intelligence
---

# Graph Health Report — <% tp.date.now("YYYY [W]WW") %>

> Run `bash scripts/graph/graph.sh health` to generate fresh data before completing this report.

## Health Score: /100

**Interpretation:** Excellent (90+) | Good (75-89) | Fair (60-74) | Poor (40-59) | Critical (<40)

---

## Critical Issues (Block new entities if unresolved)
- [ ] 

## Warnings (Resolve within the week)
- [ ] 

---

## Graph Statistics

| Metric | This Week | Last Week | Change |
|---|---|---|---|
| Total Nodes | | | |
| Total Edges | | | |
| Health Score | | | |
| Orphan Nodes | | | |
| Broken Links | | | |
| Schema Violations | | | |
| Unvalidated Critical Assumptions | | | |
| Stale Forecasts | | | |
| Missing Outcomes | | | |
| Missing Lessons | | | |

---

## Node Type Breakdown

| Type | Count | vs Last Week |
|---|---|---|
| Signal | | |
| Trend | | |
| Opportunity | | |
| Assumption | | |
| Decision | | |
| Forecast | | |
| Initiative | | |
| Lesson | | |
| Mental Model | | |
| Evidence | | |

---

## Actions Taken This Week

- [ ] 

---

## Repair Log

| Issue | Entity ID | Action Taken | Resolved? |
|---|---|---|---|
| | | | |

---

## Next Week Priorities

1. 
2. 
3. 

---

## Links
- `[[Graph Export]]` — `vault/06-meta-intelligence/graph/exports/graph-export.json`
- `[[Diagnostics]]` — `vault/06-meta-intelligence/graph/diagnostics/diagnostics.json`
- Previous Report: `[[]]`
