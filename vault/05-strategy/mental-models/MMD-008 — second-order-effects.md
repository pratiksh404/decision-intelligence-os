---
entity_id: MMD-008
entity_type: mental-model
title: Second-Order Effects
subtype: second-order-effects
status: active
description: >
  Evaluate the downstream consequences of decisions beyond the immediate, obvious results.
  First-order thinking asks: "What will happen?" Second-order thinking asks: "And then what?"
  Failing to anticipate second-order effects leads to unintended consequences and policy resistance.
core_question: "What are the downstream consequences of this decision, and what happens next?"
application_protocol: |
  1. Identify the direct, first-order outcome of the decision.
  2. For that outcome, ask: "And then what? What does this trigger?"
  3. Map out the secondary and tertiary consequences (branching paths).
  4. Look for feedback loops (positive or negative reinforcement).
  5. Pay special attention to delayed reactions or systemic reactions (e.g., competitor response).
  6. Assess whether the first-order benefit is worth the second-order cost.
failure_modes: >
  Can lead to analysis paralysis.
  Downstream consequences become increasingly speculative and harder to predict.
  May cause over-cautiousness.
complementary_models:
  - MMD-001   # First Principles
  - MMD-007   # Optionality
contradicting_models: []
related_decisions: []
related_outcomes: []
related_lessons: []
recommended_for_entity_types:
  - decision
  - strategic-bet
  - risk
confidence_score: 9
importance: 10
application_count: 0
tags:
  - mental-model
  - strategy-layer
  - systems-thinking
created: 2026-06-13
updated: 2026-06-13
owner: Founder/CEO
---

# Mental Model: Second-Order Effects

## Core Idea

First-order thinking is fast and easy. It looks for immediate, direct results. Second-order thinking is slow and deliberate. It considers the consequences of consequences. Popularized by Howard Marks and Shane Parrish, it is crucial for avoiding the "cobra effect" or unintended negative side effects of policy/strategic decisions.

> "First-order thinking is simple and superficial, and just about everyone can do it. Second-order thinking is more complex and demanding." — Howard Marks

## The "And Then What?" Framework

To practice second-order thinking, continuously ask:

1. **And then what?** What happens after the immediate result occurs?
2. **Who else is affected?** How will competitors, customers, or employees react to this change?
3. **What are the temporal dynamics?** Is there a short-term benefit that turns into a long-term liability?
4. **Where are the feedback loops?** Does the action trigger a reaction that amplifies or dampens the original effect?

## Decision Intelligence Integration

- Tag decisions where second-order analysis is crucial: `mental_models_applied: [MMD-008]`
- Use this model when evaluating **risks** and **assumptions** (particularly systemic risks like hiring or competition).
- Integrate with pre-mortems to map downstream failure pathways.

## Links

- Related Mental Models: `[[MMD-001 — First Principles]]`, `[[MMD-007 — Optionality]]`
- Framework: `[[Decision Principles]]`
