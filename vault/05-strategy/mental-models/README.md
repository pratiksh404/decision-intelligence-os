---
title: Mental Model Library
type: dashboard
created: 2026-06-13
updated: 2026-06-13
tags:
  - mental-model
  - strategy-layer
  - dashboard
---

# Mental Model Library

> The cognitive toolkit of the Decision Intelligence OS. Apply these models before every major decision, opportunity evaluation, or forecast.

---

## Core Library

```dataview
TABLE
  subtype AS "Type",
  core_question AS "Core Question",
  application_count AS "Times Applied",
  confidence_score AS "Confidence"
FROM "vault/05-strategy/mental-models"
WHERE entity_type = "mental-model" AND status = "active"
SORT application_count DESC
```

---

## By Subtype

### 🔬 First Principles
- [[MMD-001 — first-principles|First Principles]] — Break problems to fundamentals, reject inherited assumptions

### 📈 Power Laws
- [[MMD-002 — power-laws|Power Laws]] — 20% of inputs produce 80% of outputs; concentrate on the dominant few

### 🕸 Network Effects
- [[MMD-003 — network-effects|Network Effects]] — Value scales with n² as participants grow

### 🔒 Switching Costs
- [[MMD-004 — switching-costs|Switching Costs]] — Map barriers to exit; build defensible revenue

### 💰 Incentives
- [[MMD-005 — incentives|Incentives]] — Predict behavior by tracing incentive structures

### 🏪 Marketplaces
- [[MMD-006 — marketplaces|Marketplaces]] — Multi-sided platform dynamics; chicken-and-egg; take rates

### 🎲 Optionality
- [[MMD-007 — optionality|Optionality]] — Preserve future choices; value asymmetric upside in uncertainty

---

## Model Selection Guide

| Situation | Apply These Models |
|---|---|
| Entering a new market | First Principles, Network Effects, Switching Costs |
| Evaluating a partnership | Incentives, Marketplaces, Optionality |
| Resource allocation decision | Power Laws, Optionality, Incentives |
| Competitive strategy | Network Effects, Switching Costs, Incentives |
| Irreversible commitment | Optionality, First Principles, Inversion |
| Platform business | Marketplaces, Network Effects, Switching Costs |
| Pricing decision | Switching Costs, Incentives, Power Laws |

---

## Recently Applied

```dataview
TABLE
  related_decisions AS "Applied To Decisions",
  related_outcomes AS "Validated By Outcomes",
  updated AS "Last Applied"
FROM "vault/05-strategy/mental-models"
WHERE entity_type = "mental-model" AND application_count > 0
SORT updated DESC
LIMIT 10
```

---

## Validation Status

```dataview
TABLE
  application_count AS "Times Applied",
  confidence_score AS "Current Confidence",
  related_outcomes AS "Outcome Validations"
FROM "vault/05-strategy/mental-models"
WHERE entity_type = "mental-model"
SORT confidence_score DESC
```

---

## Add New Mental Model

Use template: `templates/mental-model.md`
Naming: `MMD-{NNN} — {kebab-case-title}.md`
Location: `vault/05-strategy/mental-models/`

Next ID: MMD-008
