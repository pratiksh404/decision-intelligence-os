---
title: <% tp.file.title %>
type: assumption
status: unvalidated
created: <% tp.file.creation_date("YYYY-MM-DD") %>
updated: <% tp.file.last_modified_date("YYYY-MM-DD") %>
review_date: <% tp.date.now("YYYY-MM-DD", 30) %>
owner: Founder/CEO
importance: high
confidence_score: 5
category: market | customer | product | competition | financial | team | regulatory
invalidation_risk: low | medium | high | critical
evidence_status: none | weak | moderate | strong
related_decisions: []
related_forecasts: []
related_initiatives: []
related_opportunities: []
depends_on_assumptions: []
invalidated_by: 
invalidation_date: 
tags:
  - assumption
  - decision-layer
---
# Assumption: <% tp.file.title %>

## Statement
_State precisely and in falsifiable form. A good assumption can be proven wrong._

**Assumption:** 

## Why It Matters
- **Decision(s) that rely on this:** 
- **If wrong, impact is:** 
- **Invalidation risk:** Low / Medium / High / Critical

## Confidence Assessment
- **Current confidence:** /10
- **Evidence status:** None / Weak / Moderate / Strong
- **Main uncertainty:** 

## Validation Plan
| Field | Value |
|---|---|
| How to test | |
| Passing threshold | |
| Experiment deadline | |
| Assigned to | |

## Evidence Ledger
**Supporting evidence:**
- 

**Disconfirming evidence:**
- 

**Gaps — what we don't know:**
- 

## Dependency Map
_Which other assumptions or forecasts does this depend on?_
- Depends on: `[[]]`
- Depended on by: `[[]]`

## Linked Decisions
```dataview
LIST
FROM "vault/02-decisions/memos"
WHERE contains(related_assumptions, this.file.name)
```

## Status Log
| Date | Status | Note |
|---|---|---|
| <% tp.file.creation_date("YYYY-MM-DD") %> | unvalidated | Created |
