# MCP Agent Access Model

## Vault Permission Matrix

| Layer | Path | Agent Read | Agent Write | Notes |
|---|---|---|---|---|
| Inbox | `vault/00-inbox/` | ✅ | ✅ | Agents land all output here |
| Intelligence | `vault/01-intelligence/` | ✅ | ❌ | Read-only; human promotes |
| Decisions | `vault/02-decisions/` | ✅ | ❌ | Human-gated |
| Execution | `vault/03-execution/` | ✅ | ❌ | Human-gated |
| Learning | `vault/04-learning/` | ✅ | ❌ | Human-gated |
| Strategy | `vault/05-strategy/` | ✅ | ❌ | Human-gated |
| Meta-Intelligence | `vault/06-meta-intelligence/` | ✅ | ❌ | Human-gated |
| Templates | `templates/` | ✅ | ❌ | Reference only |
| Workflows | `workflows/` | ✅ | ❌ | Reference only |
| Advisors | `advisors/` | ✅ | ❌ | Reference only |

## Context Building Sequence

When an AI agent is invoked, it must build context in this order:

1. **Read active decisions** — `vault/02-decisions/memos/` (status: approved OR monitoring)
2. **Read linked assumptions** — resolve `related_assumptions` frontmatter links
3. **Read linked forecasts** — resolve `related_forecast` links
4. **Read relevant lessons** — search `vault/04-learning/lessons/` by tag match
5. **Read strategic themes** — `vault/05-strategy/themes/` (status: active)
6. **Read recent signals** — last 14 days from `vault/01-intelligence/signals/`

## MCP Search Queries Used by Agents

### Chief of Staff — Weekly Triage
```
type:signal status:unprocessed
type:forecast deadline:<7d status:active
type:assumption status:unvalidated importance:high
```

### Probability Analyst — Calibration Review
```
type:forecast status:resolved brier_score:*
type:calibration
```

### Portfolio Manager — Opportunity Ranking
```
type:opportunity status:researching OR status:ready-for-review
```

### Research Analyst — Signal Ingestion
```
type:trend status:active
type:competitor status:active
```
