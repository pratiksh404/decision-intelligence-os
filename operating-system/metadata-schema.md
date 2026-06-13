# Metadata Schema & Standards

This document defines the metadata conventions and frontmatter schema for all entities in the CEO Decision Intelligence Platform. Standardizing this metadata allows AI agents and Obsidian queries (via Dataview) to parse, link, and analyze files reliably.

---

## 1. Standard Frontmatter Template

Every file in the system must contain a YAML frontmatter block at the very top. Below is the master template:

```yaml
---
title: "Descriptive Name"
type: opportunity | forecast | decision | signal | trend | competitor | assumption | initiative | kpi | risk | outcome-review | lesson | calibration | bias-audit | strategic-theme | strategic-bet | resource-allocation | source-note | weekly-review
status: draft | researching | ready-for-review | approved | active | monitoring | rejected | resolved | archived | unvalidated | validated | deprecated | planned | paused | completed | cancelled | mitigated | closed
created: YYYY-MM-DD
updated: YYYY-MM-DD
review_date: YYYY-MM-DD (optional, trigger date for reviews)
owner: "Founder/CEO"
tags:
  - decision-intelligence
  - [type]-layer
confidence_score: 1-10
source_quality: low | medium | high
evidence_strength: weak | moderate | strong
decision_readiness: research-needed | ready-for-review | ready-for-action
related:
  - "[[Related Note 1]]"
  - "[[Related Note 2]]"
---
```

---

## 2. Permitted File Types and Roles

| Type Value | Vault Location | Role / Definition |
| :--- | :--- | :--- |
| `signal` | `vault/01-intelligence/signals/` | Single data points, articles, tweets, or observations. |
| `trend` | `vault/01-intelligence/trends/` | Validated market shifts backed by multiple signals. |
| `competitor` | `vault/01-intelligence/competitors/` | Persistent profile of a competitor. |
| `opportunity` | `vault/01-intelligence/opportunities/` | Startup/business opportunities and strategic options. |
| `assumption` | `vault/02-decisions/assumptions/` | Falsifiable premises that underpin decisions. |
| `decision` | `vault/02-decisions/memos/` | Upgraded Decision Memos / records of choices. |
| `forecast` | `vault/02-decisions/forecasts/` | Disciplinary forecasting questions and probabilities. |
| `initiative` | `vault/03-execution/initiatives/` | Execution projects resulting from decisions. |
| `kpi` | `vault/03-execution/kpis/` | Target metrics measuring project performance. |
| `risk` | `vault/03-execution/risks/` | Identified vulnerabilities and failure modes. |
| `outcome-review` | `vault/04-learning/outcome-reviews/` | Retrospective post-mortems of resolved decisions. |
| `lesson` | `vault/04-learning/lessons/` | Compounded heuristic rules based on outcome reviews. |
| `calibration` | `vault/04-learning/calibration/` | Tracking of forecasting errors and Brier scores. |
| `bias-audit` | `vault/04-learning/bias-audits/` | Audits identifying structural cognitive biases. |
| `strategic-theme` | `vault/05-strategy/themes/` | Pillars representing the studio's primary focus areas. |
| `strategic-bet` | `vault/05-strategy/bets/` | High-conviction capital/time allocations. |
| `resource-allocation`| `vault/05-strategy/resources/` | Budgets and attention allocation mappings. |
| `source-note` | `vault/07-sources/` | Ingested literature notes, book reviews, or logs. |
| `weekly-review` | `vault/06-meta-intelligence/dashboards/weekly-reports/` | CEO Weekly Intelligence Reports. |
| `daily-review` | `vault/06-meta-intelligence/dashboards/daily-reviews/` | Daily inbox triage and priority notes. |
| `monthly-review` | `vault/06-meta-intelligence/dashboards/monthly-reviews/` | Monthly calibration and portfolio reviews. |
| `quarterly-review` | `vault/06-meta-intelligence/dashboards/quarterly-reviews/` | Quarterly strategy and resource reviews. |
| `dashboard` | `vault/06-meta-intelligence/dashboards/` | Dataview-powered cockpit views. |

---

## 3. Allowed Status Transitions

To prevent state fragmentation, files must only utilize the statuses specified for their type:

* **Signals:** `unprocessed` $\to$ `active` $\to$ `archived`
* **Opportunities:** `draft` $\to$ `researching` $\to$ `ready-for-review` $\to$ `approved` $\to$ `rejected` $\to$ `monitoring`
* **Assumptions:** `unvalidated` $\to$ `validated` / `rejected` $\to$ `deprecated`
* **Decisions:** `draft` $\to$ `ready-for-review` $\to$ `approved` $\to$ `rejected` $\to$ `monitoring` $\to$ `resolved`
* **Forecasts:** `active` $\to$ `resolved` $\to$ `archived`
* **Initiatives:** `planned` $\to$ `active` $\to$ `paused` $\to$ `completed` $\to$ `cancelled`
* **Risks:** `active` $\to$ `mitigated` $\to$ `closed`
* **Strategic Themes & Bets:** `active` $\to$ `completed` $\to$ `closed`

---

## 4. Link & Graph Conventions

Relationships must be defined using strict markdown internal linking to preserve graph structure:

* **Signal $\to$ Trend:** A signal must list the trend link in its frontmatter `related_trends: ["[[Trend Name]]"]` and body.
* **Trend $\to$ Opportunity:** Trends should link to target opportunities.
* **Opportunity $\to$ Assumption:** An opportunity must link to the assumptions it is built on.
* **Decision $\to$ Forecast:** A decision memo must reference its core forecast question: `related_forecast: "[[Forecast Name]]"`.
* **Decision $\to$ Initiative:** The decision must list the downstream execution plans: `related_initiative: "[[Initiative Name]]"`.
* **Initiative $\to$ KPI & Risk:** KPI and Risk files must list their parent initiative in the frontmatter.
* **Initiative $\to$ Outcome Review:** Post-mortem review links directly back to the decision memo and initiative.
* **Outcome Review $\to$ Lesson:** Lessons list the outcome review that prompted them: `related_review: "[[Outcome Review Name]]"`.

---

## 5. Phase 2 Additional Fields

### Forecast (Phase 2)
```yaml
category: market | product | competition | execution | financial | hiring
strategic_theme: "[[Theme Name]]"
actual_outcome: "Description of what happened"
actual_probability: 0 | 1
calibration_error: -1.0 to 1.0  # predicted - actual
resolution_date: YYYY-MM-DD
```

### Assumption (Phase 2)
```yaml
category: market | customer | product | competition | financial | team | regulatory
invalidation_risk: low | medium | high | critical
evidence_status: none | weak | moderate | strong
depends_on_assumptions: []
invalidated_by: "[[Note Name]]"
invalidation_date: YYYY-MM-DD
```

### Opportunity (Phase 2)
```yaml
category: new-product | new-market | partnership | acquisition | operational | geographic
score_time_to_value: 1-10
composite_score: 0.0-10.0  # calculated from formula
related_assumptions: []
```

### Lesson (Phase 2)
```yaml
recurrence_count: 1   # increment when same pattern recurs
related_review: "[[Outcome Review]]"
```
