---
entity_id: MMD-004
entity_type: mental-model
title: Switching Costs
subtype: switching-costs
status: active
description: >
  The barriers — financial, operational, psychological, or technical — that prevent
  customers from switching to a competitor. High switching costs create defensibility
  and pricing power. Low switching costs create commoditization risk.
core_question: "What makes it painful to stop using this product and start using a competitor's?"
application_protocol: |
  1. Enumerate all switching costs for the customer
  2. Classify: financial (contracts, sunk costs), operational (data migration, retraining),
     psychological (brand loyalty, familiarity), technical (integration lock-in)
  3. Estimate switching cost in dollars and hours
  4. Compare to competitor pricing advantage needed to overcome the cost
  5. Identify which switching costs you control and can increase
  6. Identify which are eroding and require reinforcement
failure_modes: >
  Switching costs can erode as technology lowers migration barriers.
  Artificially high switching costs (dark patterns) damage brand trust long-term.
  Competitors can intentionally reduce your switching costs (free migration tools).
complementary_models:
  - MMD-003   # Network Effects (network + switching costs = very strong moat)
  - MMD-002   # Power Laws (focus switching cost defense on top 20% of customers)
contradicting_models: []
related_decisions: []
related_outcomes: []
related_lessons: []
recommended_for_entity_types:
  - opportunity
  - strategic-bet
  - competitor
confidence_score: 9
importance: 9
application_count: 0
tags:
  - mental-model
  - strategy-layer
  - competitive-moat
  - defensibility
created: 2026-06-13
updated: 2026-06-13
owner: Founder/CEO
---

# Mental Model: Switching Costs

## Core Idea

Every customer relationship has a switching cost — what it costs the customer (in money, time, risk, or pain) to stop using your product and start using a competitor's. High switching costs = defensible revenue. Low switching costs = commoditized competition.

## Switching Cost Categories

| Type | Examples | Strength |
|---|---|---|
| Financial | Cancellation fees, sunk implementation costs | Medium |
| Data | Historical data trapped in proprietary format | High |
| Technical | Deep API integrations, custom workflows | Very High |
| Operational | Retraining teams, disrupting processes | High |
| Psychological | Brand trust, familiarity, risk aversion | Medium |
| Relationship | Key account manager relationships | Medium |

## When to Apply

- Evaluating an Opportunity for defensibility (how sticky will customers be?)
- Competitor analysis (how hard is it to take their customers?)
- Product decisions (how can we increase switching costs intentionally?)
- Pricing decisions (how much pricing power do switching costs give us?)

## Decision Intelligence Integration

- When evaluating Competitor nodes: score their customer switching cost (1-10)
- When scoring Opportunity composite_score: weight strategic_fit higher if switching costs are inherently high in this market
- Create Assumption node for any Opportunity relying on switching cost moat

## Links

- Related Mental Models: `[[MMD-003 — Network Effects]]`, `[[MMD-002 — Power Laws]]`
