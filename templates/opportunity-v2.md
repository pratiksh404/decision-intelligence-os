---
title: <% tp.file.title %>
type: opportunity
status: draft
created: <% tp.file.creation_date("YYYY-MM-DD") %>
updated: <% tp.file.last_modified_date("YYYY-MM-DD") %>
review_date: <% tp.date.now("YYYY-MM-DD", 14) %>
owner: Founder/CEO
market: 
estimated_value: 0
category: new-product | new-market | partnership | acquisition | operational | geographic
strategic_theme: 

# --- Scoring Inputs (1–10 each) ---
score_expected_return: 5
score_probability: 5
score_strategic_fit: 5
score_execution_complexity: 5
score_resource_requirement: 5
score_time_to_value: 5
score_risk: 5

# --- Composite Score (auto-calculated or manual) ---
# Formula: (expected_return * 0.25) + (probability * 0.20) + (strategic_fit * 0.20)
#          - (execution_complexity * 0.15) - (resource_requirement * 0.10)
#          - (risk * 0.10)
composite_score: 0

confidence_score: 5
source_quality: low
evidence_strength: weak
decision_readiness: research-needed
related_trends: []
related_competitors: []
related_decisions: []
related_assumptions: []
tags:
  - opportunity
  - strategy-layer
---
# Opportunity: <% tp.file.title %>

## Composite Opportunity Score

| Factor | Weight | Score | Weighted |
|---|---|---|---|
| Expected Return | 25% | /10 | |
| Probability of Success | 20% | /10 | |
| Strategic Fit | 20% | /10 | |
| Execution Complexity | -15% | /10 | |
| Resource Requirement | -10% | /10 | |
| Risk | -10% | /10 | |
| **Composite Score** | | | **/10** |

**Score Interpretation:**
- 7.0–10.0 → Pursue aggressively
- 5.0–6.9 → Monitor / gather more evidence
- 3.0–4.9 → Low priority unless strategic
- < 3.0 → Reject

---

## Executive Summary
_[2–3 sentence synthesis of the opportunity and why it matters now]_

## Problem & Market
- **Customer segment:** 
- **Core pain point:** 
- **Market size (TAM/SAM/SOM):** 
- **Why now:** 
- **Key competitors:** 

## Scoring Rationale
**Expected Return (score: /10):**
_[What is the realistic upside? Revenue, strategic value, optionality?]_

**Probability of Success (score: /10):**
_[What is the base rate for this type of opportunity? What are our specific advantages/disadvantages?]_

**Strategic Fit (score: /10):**
_[Does this align with active strategic themes? Does it compound existing assets?]_

**Execution Complexity (score: /10, higher = more complex):**
_[What are the hardest execution challenges? Dependencies?]_

**Resource Requirement (score: /10, higher = more resource-intensive):**
_[Capital, time, headcount required? Opportunity cost?]_

**Risk (score: /10, higher = riskier):**
_[What are the key downside scenarios? What could kill this?]_

---

## Advisor Board Analysis
- **CEO:** 
- **CFO:** 
- **VC:** 
- **Skeptic:** 
- **Operator:** 
- **Portfolio Manager:** 

## Assumptions Underlying This Opportunity
- [ ] `[[Assumption — ]]`

## Decision
- **Recommendation:** Pursue / Monitor / Reject / Research Further
- **Next action:** 
- **Review date:** 

## Execution Plan (if approved)
- **MVP:** 
- **90-day milestones:** 
- **Capital required:** 
- **Team:** 
