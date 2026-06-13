---
entity_id: <% tp.file.title.split(" — ")[0] %>
entity_type: mental-model
title: <% tp.file.title.split(" — ")[1] || tp.file.title %>
subtype: first-principles | power-laws | network-effects | switching-costs | incentives | marketplaces | optionality | inversion | second-order-effects | base-rates | margin-of-safety | regret-minimization | ooda-loop | activation-energy | feedback-loops | other
status: active
description: >
  [One paragraph: what this model is and what it explains]
core_question: "[The single question this model answers]"
application_protocol: |
  1. 
  2. 
  3. 
failure_modes: >
  [When does this model mislead? When should you NOT use it?]
complementary_models: []
contradicting_models: []
related_decisions: []
related_outcomes: []
related_lessons: []
recommended_for_entity_types:
  - decision
  - opportunity
confidence_score: 7
importance: 7
application_count: 0
tags:
  - mental-model
  - strategy-layer
created: <% tp.file.creation_date("YYYY-MM-DD") %>
updated: <% tp.file.last_modified_date("YYYY-MM-DD") %>
owner: Founder/CEO
---

# Mental Model: <% tp.file.title.split(" — ")[1] || tp.file.title %>

## Core Idea

[2-3 sentences explaining the mental model. Include a memorable quote if one exists.]

## When to Apply

- 
- 
- 

## Application Steps

1. 
2. 
3. 

## Failure Modes

[When does this model lead you astray?]

## Decision Intelligence Integration

[How does this model connect to specific node types, fields, or workflows in the Decision Intelligence OS?]

- When evaluating **[entity type]**: apply by [specific action]
- When creating **[entity type]**: tag with `mental_models_applied: [<% tp.file.title.split(" — ")[0] %>]`

## Worked Example

**Situation:** 

**Application:**

**Outcome:**

## Links

- Related Mental Models: 
- Framework: `[[Decision Principles]]`
- Forecasting: `[[Forecasting Framework]]`
