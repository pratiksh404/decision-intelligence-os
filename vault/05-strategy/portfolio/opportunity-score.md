---
title: Opportunity Scoring Engine
type: reference
created: 2026-06-13
updated: 2026-06-13
tags:
  - opportunity
  - scoring
  - strategy-layer
---
# Opportunity Scoring Engine

## Scoring Formula

```
composite_score =
  (score_expected_return    × 0.25)
+ (score_probability        × 0.20)
+ (score_strategic_fit      × 0.20)
- (score_execution_complexity × 0.15)
- (score_resource_requirement × 0.10)
- (score_risk               × 0.10)
```

All inputs scored 1–10. Higher composite = better opportunity.

## Factor Definitions

| Factor | Weight | Scoring Guide |
|---|---|---|
| Expected Return | +25% | 1=minimal, 5=meaningful, 10=transformative |
| Probability of Success | +20% | 1=<10%, 5=~50%, 10=>90% |
| Strategic Fit | +20% | 1=unrelated, 5=adjacent, 10=core theme |
| Execution Complexity | -15% | 1=trivial, 5=moderate, 10=extremely hard |
| Resource Requirement | -10% | 1=low-cost, 5=moderate, 10=capital-intensive |
| Risk | -10% | 1=minimal downside, 5=recoverable, 10=existential |

## Portfolio Ranking Dashboard

```dataview
TABLE
  title AS "Opportunity",
  market AS "Market",
  composite_score AS "Score",
  score_probability AS "P(Success)",
  score_strategic_fit AS "Fit",
  status AS "Status",
  decision_readiness AS "Readiness"
FROM "vault/01-intelligence/opportunities" OR "vault/05-strategy/portfolio"
WHERE type = "opportunity"
  AND status != "rejected"
SORT composite_score DESC
```

## Top Opportunities by Strategic Theme

```dataview
TABLE
  rows.file.name AS "Opportunity",
  max(rows.composite_score) AS "Best Score",
  length(rows) AS "Count"
FROM "vault/01-intelligence/opportunities" OR "vault/05-strategy/portfolio"
WHERE type = "opportunity" AND status != "rejected"
GROUP BY strategic_theme
SORT max(rows.composite_score) DESC
```

## Scoring Calibration Thresholds

| Composite Score | Action |
|---|---|
| ≥ 7.0 | Escalate to Decision Memo immediately |
| 5.0–6.9 | Assign Research Analyst, revisit in 2 weeks |
| 3.0–4.9 | Monitor; require new signal before re-scoring |
| < 3.0 | Reject; archive with rejection note |

## Agent Scoring Protocol

When the Portfolio Manager scores a new opportunity:

1. Read the opportunity note via MCP
2. Score each of the 6 factors independently
3. Apply the formula above
4. Write `composite_score` to frontmatter
5. Update `decision_readiness` based on threshold table
6. If score ≥ 7.0: automatically set `status: ready-for-review` and set `review_date: +3 days`
