---
entity_id: MMD-006
entity_type: mental-model
title: Marketplaces
subtype: marketplaces
status: active
description: >
  Multi-sided platform dynamics: a business that creates value by connecting two or more
  distinct user groups who benefit from interacting with each other. Marketplaces have
  unique economics — they must solve the chicken-and-egg problem, manage cross-side
  network effects, and balance liquidity across both sides.
core_question: "Are both sides better off? And does adding one side make the other side more valuable?"
application_protocol: |
  1. Identify all sides of the marketplace (typically buyers and sellers)
  2. Define what value each side gets from the marketplace
  3. Map cross-side network effects: does more buyers → more value for sellers? (and vice versa?)
  4. Identify which side is harder to acquire (constrained supply or constrained demand?)
  5. Determine take rate and economics (what % of GMV can you extract without disintermediating?)
  6. Identify disintermediation risk (when do buyers and sellers transact directly?)
  7. Map the chicken-and-egg bootstrapping strategy
failure_modes: >
  Overestimates cross-side network effects in thin or fragmented markets.
  Underestimates disintermediation risk once relationships are established.
  Fails to account for one side gaining market power and renegotiating take rates.
complementary_models:
  - MMD-003   # Network Effects (cross-side NE is the core marketplace moat)
  - MMD-005   # Incentives (each side has distinct incentive structures)
  - MMD-004   # Switching Costs (what locks each side into your marketplace?)
contradicting_models: []
related_decisions: []
related_outcomes: []
related_lessons: []
recommended_for_entity_types:
  - opportunity
  - strategic-bet
  - decision
confidence_score: 9
importance: 9
application_count: 0
tags:
  - mental-model
  - strategy-layer
  - marketplace
  - platform
  - network-effects
created: 2026-06-13
updated: 2026-06-13
owner: Founder/CEO
---

# Mental Model: Marketplaces

## Core Idea

Marketplaces are fundamentally different from single-sided businesses. They don't produce value — they facilitate value exchange between parties. The marketplace's advantage comes from owning the interaction layer, not the supply or demand itself.

**Key Marketplace Metrics:**
- **GMV** — Gross Merchandise Value (total transaction volume)
- **Take Rate** — % of GMV captured as revenue
- **Liquidity** — How quickly supply meets demand
- **NPS (both sides)** — Net Promoter Score from buyers and sellers separately

## The Chicken-and-Egg Problem

Every marketplace must solve: buyers don't come without sellers; sellers don't come without buyers.

**Solutions:**
1. **Subsidize one side** (usually supply first)
2. **Create standalone value** for one side before the other joins
3. **Fake it** — manually fulfill early demand while building supply
4. **Focus on a niche** — achieve liquidity in a small vertical first

## When to Apply

- Evaluating any Opportunity that connects two or more user groups
- Competitor analysis of marketplace competitors
- Pricing and take-rate decisions
- Build vs. partner decisions (join an existing marketplace vs. build your own)

## Decision Intelligence Integration

When an Opportunity is marketplace-type, mandatory Assumption nodes:
- `ASM-XXXX — Sufficient supply acquisition possible at acceptable CAC`
- `ASM-XXXX — Cross-side network effects are genuinely present`
- `ASM-XXXX — Disintermediation risk below X% of completed transactions`

## Links

- Related Mental Models: `[[MMD-003 — Network Effects]]`, `[[MMD-005 — Incentives]]`, `[[MMD-004 — Switching Costs]]`
