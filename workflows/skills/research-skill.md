# Skill: Research

**Agent:** Research Analyst
**Version:** 2.0

## Purpose
Ingest external intelligence and produce structured vault artifacts ready for review.

## Inputs
| Input | Required | Description |
|---|---|---|
| `topic` | ✅ | What to research (market, competitor, technology) |
| `depth` | ✅ | `quick` (15 min) or `deep` (45 min) |
| `context_notes` | optional | Existing vault notes to anchor research |
| `strategic_theme` | optional | Theme to align research against |

## Process
1. Read active strategic themes from `vault/05-strategy/themes/`
2. Read existing signals and trends related to `topic`
3. Use `brave-search` MCP to retrieve current sources (3–5 sources minimum)
4. Separate: facts, statistics, competitor moves, trends
5. Evaluate source quality: Low / Medium / High
6. Score confidence: 1–10

## Outputs

### Signal Note (always produced)
- Path: `vault/00-inbox/`
- Template: `templates/signal.md`
- Minimum fields: `title`, `type: signal`, `source`, `confidence_score`, `source_quality`

### Trend Note (when pattern found across ≥ 2 signals)
- Path: `vault/00-inbox/`
- Template: `templates/trend.md`

### Competitor Profile (when competitor identified)
- Path: `vault/00-inbox/`
- Template: `templates/competitor-profile.md`

## Review Triggers
- Produced note lands in `vault/00-inbox/`
- Chief of Staff promotes to `vault/01-intelligence/` after human review

## Automation Trigger
```
QuickAdd: "Research Signal"
Prompt: topic, depth
Invokes: Research Analyst agent with vault context
```

## Quality Gate
Before submitting, the Research Analyst must verify:
- [ ] Source URLs included
- [ ] Source quality assessed
- [ ] No assumptions presented as facts
- [ ] Confidence score set
- [ ] Tags include `signal` or `trend`
