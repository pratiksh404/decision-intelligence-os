---
title: <% tp.file.title %>
type: forecast
status: active
created: <% tp.file.creation_date("YYYY-MM-DD") %>
updated: <% tp.file.last_modified_date("YYYY-MM-DD") %>
review_date: <% tp.date.now("YYYY-MM-DD", 30) %>
owner: Founder/CEO
question: 
category: market | product | competition | execution | financial | hiring
strategic_theme: 
predicted_probability: 0.50
confidence_score: 5
deadline: 
resolution_criteria: 
actual_outcome: 
actual_probability: 
brier_score: 
calibration_error: 
resolution_date: 
related_decision: 
related_assumption: 
related_initiative: 
tags:
  - forecast
  - decision-layer
---
# Forecast: <% tp.file.title %>

## Forecast Question
_State the question in a precise, falsifiable form with a clear resolution date._

**Question:**
**Deadline:**
**Resolution Criteria:** _(What observable fact will confirm or deny this?)_

## Probability Estimate

| Field | Value |
|---|---|
| Predicted Probability | % |
| Confidence Score | /10 |
| Last Updated | <% tp.file.last_modified_date("YYYY-MM-DD") %> |

## Base Rates & Reference Class
- **Reference Class:** _(What is the historical base rate for similar situations?)_
- **Base Rate:** %
- **Adjustment Rationale:** _(Why does this case deviate from base rate?)_

## Evidence Ledger
**Supporting (higher probability):**
- 

**Counter (lower probability):**
- 

**Unknown variables:**
- 

## Scenario Analysis
| Scenario | Probability | Outcome |
|---|---|---|
| Best case | % | |
| Base case | % | |
| Worst case | % | |

## Advisor Probability Checks
- **Probability Analyst:** 
- **Skeptic override:** 
- **Final consensus:** %

## Resolution Log
_Complete this section when the deadline is reached._

| Field | Value |
|---|---|
| Actual Outcome | |
| Actual Probability (0 or 1) | |
| Brier Score | `=(predicted_probability - actual_probability)^2` |
| Calibration Error | `=predicted_probability - actual_probability` |
| Resolution Date | |
| Key Learning | |

## Links
- Decision: `[[]]`
- Assumption: `[[]]`
- Outcome Review: `[[]]`
