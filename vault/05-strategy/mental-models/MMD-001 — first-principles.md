---
entity_id: MMD-001
entity_type: mental-model
title: First Principles
subtype: first-principles
status: active
description: >
  Decompose problems to their fundamental, axiomatic truths and reason up from there.
  Reject inherited assumptions, analogies, and conventional wisdom as starting points.
  Ask: "What do I know to be absolutely true here?"
core_question: "What would have to be true for this to be correct, and how do I know that?"
application_protocol: |
  1. State the claim or problem as clearly as possible
  2. List all assumptions embedded in the claim
  3. Challenge each assumption: "How do I know this is true?"
  4. Strip away everything that is assumed, analogized, or inherited
  5. Identify the irreducible facts
  6. Rebuild reasoning from those facts upward
failure_modes: >
  Can become paralytic — stripping to first principles on every decision wastes time.
  Use when the conventional approach is clearly wrong or producing bad outcomes.
  Overuse leads to reinventing wheels unnecessarily.
complementary_models:
  - MMD-007   # Inversion
  - MMD-008   # Second-Order Effects
contradicting_models: []
related_decisions: []
related_outcomes: []
related_lessons: []
recommended_for_entity_types:
  - decision
  - opportunity
  - strategic-bet
confidence_score: 10
importance: 10
application_count: 0
tags:
  - mental-model
  - strategy-layer
  - reasoning
created: 2026-06-13
updated: 2026-06-13
owner: Founder/CEO
---

# Mental Model: First Principles

## Core Idea

Break any problem down to its most fundamental truths — the things you know with certainty — and rebuild your understanding from there. Named after Aristotle's "first principles" of philosophy, popularized in business by Elon Musk (SpaceX battery cost reasoning).

> "I think it's important to reason from first principles rather than by analogy. The normal way we conduct our lives is we reason by analogy." — Elon Musk

## When to Apply

- Before accepting any inherited assumption as fact
- When an industry-standard approach seems expensive, slow, or wrong
- When entering a new market and conventional wisdom may not transfer
- During assumption validation sessions (every Assumption node)
- When an advisor says "that's just how it's done"

## Application Example

**Problem:** "Can we build a product in this market?"  
**Conventional:** "No, incumbents have years of head start."  
**First Principles:**  
1. What does the customer actually need? (not what the incumbent provides)  
2. What technology constraints actually exist vs. assumed?  
3. What would this cost if built from scratch today vs. when incumbents built it?  
4. What's the actual switching cost for customers?

## Decision Intelligence Integration

- Tag decisions where this model is applied: `mental_models_applied: [MMD-001]`
- After outcome, record whether first-principles analysis held or was disproved
- If disproved: add CONTRADICTS link from Outcome to this Mental Model

## Links

- Related Mental Models: `[[MMD-007 — Inversion]]`, `[[MMD-008 — Second-Order Effects]]`
- Framework: `[[Decision Principles]]`

