---
entity_id: MMD-003
entity_type: mental-model
title: Network Effects
subtype: network-effects
status: active
description: >
  A product or service becomes more valuable as more participants join. Value scales
  superlinearly with users — Metcalfe's Law states value ~ n². Network effects are
  the strongest form of competitive moat when they exist genuinely.
core_question: "Does each additional user make the product more valuable to existing users?"
application_protocol: |
  1. Identify who connects to whom in this network (same-side or cross-side)
  2. Classify network type: direct (same-side), indirect (cross-side), data, protocol
  3. Estimate value added per additional node
  4. Identify the minimum viable network (critical mass threshold)
  5. Estimate time and cost to reach critical mass
  6. Identify whether network effect is defensible or leaky
failure_modes: >
  Overstated in thin or commoditized markets where users don't actually interact.
  Assumes all nodes are equally valuable — power law node distributions often mean
  top nodes generate most of the network's value.
  Multi-homing can nullify network effects if switching cost is low.
complementary_models:
  - MMD-004   # Switching Costs (reinforce network stickiness)
  - MMD-006   # Marketplaces (cross-side network effects)
contradicting_models: []
related_decisions: []
related_outcomes: []
related_lessons: []
recommended_for_entity_types:
  - opportunity
  - strategic-bet
  - decision
confidence_score: 9
importance: 10
application_count: 0
tags:
  - mental-model
  - strategy-layer
  - competitive-moat
  - marketplace
created: 2026-06-13
updated: 2026-06-13
owner: Founder/CEO
---

# Mental Model: Network Effects

## Core Idea

Value increases with scale. In true network effect businesses, each new user makes the product more valuable for every existing user. This creates a self-reinforcing moat: market leaders compound their advantage with every new participant.

**Types:**
- **Direct (Same-side):** More users → better for each user (WhatsApp, LinkedIn)
- **Indirect (Cross-side):** More buyers → better marketplace for sellers, and vice versa (eBay, Uber)
- **Data:** More usage → better AI/recommendations → more usage (Google, Spotify)
- **Protocol:** Standard adoption → more value for all participants (TCP/IP, Visa)

## Defensibility Threshold

Network effects only become defensive moats after reaching **critical mass** — the minimum network size where the product is self-sustaining. Before critical mass, the network is fragile.

## When to Apply

- Evaluating new market opportunities for platform dynamics
- Assessing competitor moats (is their advantage real network effects or brand?)
- Decision to enter a marketplace or platform business
- Assessing whether a product generates data network effects

## Questions for Assumption Nodes

When an Opportunity depends on network effects, create these Assumption nodes:
- `ASM-XXXX — Critical mass achievable within [timeline] at [cost]`
- `ASM-XXXX — Same-side users actually benefit from additional users`
- `ASM-XXXX — Switching costs sufficient to prevent multi-homing`

## Links

- Related Mental Models: `[[MMD-004 — Switching Costs]]`, `[[MMD-006 — Marketplaces]]`
