---
entity_id: MMD-005
entity_type: mental-model
title: Incentives
subtype: incentives
status: active
description: >
  All behavior is driven by incentives — explicit and implicit, financial and social,
  short-term and long-term. To predict behavior, model the incentive structures.
  To change behavior, change the incentives. "Never attribute to malice what can be
  explained by incentives."
core_question: "What does this person/organization get rewarded for doing?"
application_protocol: |
  1. Identify all stakeholders in the system
  2. For each stakeholder, list their explicit incentives (what they're paid/measured on)
  3. List implicit incentives (status, safety, social approval, avoiding blame)
  4. Identify misaligned incentives (where their incentive conflicts with your goal)
  5. Design around misalignments or create new incentive structures
  6. Predict behavior: follow the incentive trail
failure_modes: >
  Assumes people are purely rational incentive-maximizers.
  Ignores genuine altruism, values-based behavior, and professional norms.
  Over-focus on financial incentives misses status and social incentives.
complementary_models:
  - MMD-006   # Marketplaces (incentive design for two-sided markets)
  - MMD-001   # First Principles (strip assumptions about motivation)
contradicting_models: []
related_decisions: []
related_outcomes: []
related_lessons: []
recommended_for_entity_types:
  - decision
  - assumption
  - competitor
  - opportunity
confidence_score: 10
importance: 10
application_count: 0
tags:
  - mental-model
  - strategy-layer
  - behavioral
  - stakeholder-analysis
created: 2026-06-13
updated: 2026-06-13
owner: Founder/CEO
---

# Mental Model: Incentives

## Core Idea

Charlie Munger's most cited mental model: "Show me the incentive and I'll show you the outcome." Every organizational behavior, market dynamic, and competitive action can be understood by tracing the incentive structure. If you want to predict what someone will do — understand what they're rewarded for.

> "Never, ever, think about something else when you should be thinking about the power of incentives." — Charlie Munger

## Incentive Taxonomy

| Type | Examples |
|---|---|
| Financial | Salary, bonuses, equity, commissions |
| Status | Promotion, recognition, peer respect |
| Social | Team belonging, approval, avoiding embarrassment |
| Safety | Job security, avoiding blame, risk aversion |
| Mission | Genuine belief in the work's purpose |

## When to Apply

- Evaluating a partnership opportunity (what does the partner get from this?)
- Competitor analysis (why is the competitor making this move? what are they incentivized for?)
- Hiring decisions (what incentive structure attracts the right person?)
- Assumption validation (your assumption about user behavior — what are they incentivized to do?)
- Regulatory risk (what are regulators incentivized to do in this market?)

## Decision Intelligence Integration

- When creating Competitor nodes, field: `key_incentives: [growth, defend market share, regulatory capture]`
- When validating Assumptions about customer behavior, apply this model
- Advisor Review: Strategic Advisor must always cite incentive analysis when reviewing partnerships

## Links

- Related Mental Models: `[[MMD-006 — Marketplaces]]`, `[[MMD-001 — First Principles]]`
