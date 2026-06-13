---
entity_id: MMD-002
entity_type: mental-model
title: Power Laws
subtype: power-laws
status: active
description: >
  In many systems, a small number of inputs produce a disproportionately large share
  of outputs. 20% of decisions produce 80% of results. 1% of customers generate 50%
  of revenue. Focus obsessively on identifying and exploiting the dominant few.
core_question: "Where is the 20% that produces 80% of the outcome?"
application_protocol: |
  1. List all inputs, customers, decisions, or activities
  2. Rank by output contribution
  3. Identify if distribution is power-law shaped (top few dominate)
  4. Concentrate resources on top-ranked items
  5. Ruthlessly eliminate or minimize bottom-ranked items
  6. Periodically re-rank as the system evolves
failure_modes: >
  Can lead to over-concentration and fragility if the dominant few fail.
  Power law distributions shift — today's top input may not be tomorrow's.
  Misidentifying what to measure causes optimization on the wrong axis.
complementary_models:
  - MMD-004   # Switching Costs (protect dominant customers)
  - MMD-007   # Inversion (what destroys the top 20%?)
contradicting_models: []
related_decisions: []
related_outcomes: []
related_lessons: []
recommended_for_entity_types:
  - resource-allocation
  - strategic-bet
  - kpi
confidence_score: 9
importance: 9
application_count: 0
tags:
  - mental-model
  - strategy-layer
  - resource-allocation
created: 2026-06-13
updated: 2026-06-13
owner: Founder/CEO
---

# Mental Model: Power Laws

## Core Idea

Most distributions in business are not normal (bell curve) — they are power-law distributions where a small minority of inputs, customers, or events produce the vast majority of outcomes.

**Pareto Principle:** 80% of results come from 20% of causes.  
**VC Returns:** Top 1% of investments return more than the other 99% combined.  
**Revenue:** Top 10% of customers often generate 60-70% of revenue.

## When to Apply

- Resource allocation decisions (where to concentrate effort)
- Customer segmentation and prioritization
- Evaluating portfolio of Strategic Bets
- Identifying which KPIs actually matter
- Hiring decisions (which role has highest leverage)

## Application in Decision Intelligence

| Context | Power Law Question |
|---|---|
| Signals | Which 20% of signal sources produce 80% of actionable intelligence? |
| Decisions | Which decisions have the most downstream dependencies? |
| Assumptions | Which few assumptions underpin the most decisions? |
| Lessons | Which lessons recur most frequently? (recurrence_count) |
| Mental Models | Which models are applied most often with positive outcomes? |

## Decision Intelligence Integration

- Sort Opportunity nodes by composite_score — pursue top 20% aggressively
- Sort Assumption nodes by number of dependent Decisions — validate these first
- Sort Lesson nodes by recurrence_count — these encode the most valuable patterns

## Links

- Related Mental Models: `[[MMD-004 — Switching Costs]]`, `[[MMD-007 — Inversion]]`
- Framework: `[[Decision Principles]]`
