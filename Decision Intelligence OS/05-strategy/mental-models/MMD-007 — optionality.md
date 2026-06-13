---
entity_id: MMD-007
entity_type: mental-model
title: Optionality
subtype: optionality
status: active
description: >
  Preserve the right to make future choices. Actions and investments that keep options
  open have asymmetric value: their upside is uncapped, their downside is limited.
  Sacrificing optionality for short-term certainty is a common strategic mistake.
  In uncertainty, optionality is a form of capital.
core_question: "Does this decision preserve, create, or destroy future options?"
application_protocol: |
  1. Identify what options this decision creates (new paths opened)
  2. Identify what options this decision forecloses (paths permanently closed)
  3. Estimate the value of the foreclosed options (option value, not expected value)
  4. Compare: is the certain gain worth the lost optionality?
  5. Search for ways to achieve the same goal while preserving more optionality
  6. Flag irreversible decisions for higher scrutiny (see reversibility field in Decision nodes)
  7. When uncertain, prefer the option that creates more future options
failure_modes: >
  Overvaluing optionality can lead to indecision — the "option value trap."
  Some decisions require commitment to capture full value (network effects require scale).
  Optionality preservation can be used as rationalization for avoiding hard decisions.
complementary_models:
  - MMD-001   # First Principles (what do we actually know about the future state?)
  - MMD-008   # Second-Order Effects (what options do second-order effects create/destroy?)
contradicting_models: []
related_decisions: []
related_outcomes: []
related_lessons: []
recommended_for_entity_types:
  - decision
  - strategic-bet
  - resource-allocation
confidence_score: 9
importance: 10
application_count: 0
tags:
  - mental-model
  - strategy-layer
  - decision-making
  - irreversibility
created: 2026-06-13
updated: 2026-06-13
owner: Founder/CEO
---

# Mental Model: Optionality

## Core Idea

Nassim Taleb's concept: in an uncertain world, actions that preserve or create future options are more valuable than their expected-value calculations suggest. Asymmetry matters: options cap your downside (you can choose not to exercise) while leaving upside open.

> "Optionality, the ability to switch course, is the most valuable thing in an uncertain world." — Nassim Taleb

## Optionality Analysis Framework

| Decision Property | Optionality Impact |
|---|---|
| **Reversible** | High optionality preserved |
| **Irreversible** | Optionality destroyed — requires extra scrutiny |
| **Modular** | Creates new options downstream |
| **Monolithic** | Locks in architecture, forecloses alternatives |
| **Staged** | Optionality at each gate — can stop before next stage |
| **All-in** | Bets everything on one path |

## Decision Intelligence Integration

This model is directly mapped to the `reversibility` field on Decision nodes:
- `reversible` → high optionality, lower scrutiny bar
- `partially-reversible` → moderate optionality, standard bar
- `irreversible` → optionality destroyed, apply highest scrutiny; require Skeptic advisor sign-off

**Rule:** Any Decision node with `reversibility: irreversible` must have:
- At minimum 3 validated Assumption nodes
- At minimum 1 Skeptic Advisor Review
- A pre-mortem Forecast

## Application to Resource Allocation

When allocating resources, prefer:
- Staged investments over lump-sum
- Experiments over full commitment
- Reversible contracts over lock-in

## Links

- Related Mental Models: `[[MMD-001 — First Principles]]`, `[[MMD-008 — Second-Order Effects]]`
- Framework: `[[Decision Principles]]`
