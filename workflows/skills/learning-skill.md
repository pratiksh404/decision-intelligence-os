# Skill: Learning & Outcome Analysis

**Agent:** Learning Advisor
**Version:** 2.0

## Purpose
Extract compounding lessons from resolved decisions, completed initiatives, and resolved forecasts.

## Inputs
| Input | Required | Description |
|---|---|---|
| `source_note` | ✅ | Path to outcome-review, resolved decision, or resolved forecast |
| `extract_heuristic` | optional | `true` to generate a reusable decision rule |

## Process
1. Read the source note and all linked assumptions, forecasts, and signals
2. Reconstruct the decision logic as it existed at the time
3. Compare predicted outcome vs actual outcome
4. Identify:
   - What information was missing at decision time?
   - Which assumptions proved wrong?
   - What would have changed the decision?
   - What bias contributed to any error?
5. Check: does a lesson for this pattern already exist in `vault/04-learning/lessons/`?
   - If yes: increment `recurrence_count` on existing lesson
   - If no: create new lesson note

## Outputs

### Outcome Review Note
- Path: `vault/04-learning/outcome-reviews/`
- Template: `templates/outcome-review.md`
- Fields: `decision_quality`, `forecast_accuracy`, `execution_quality`, `key_learning`

### Lesson Note (when extract_heuristic: true)
- Path: `vault/04-learning/lessons/`
- Template: `templates/lesson.md`
- Format: "When [context], do [action] because [evidence]."
- Fields: `category`, `recurrence_count`, `related_review`, `confidence_score`

## Review Triggers
- When any decision reaches `status: resolved`
- When any initiative reaches `status: completed` or `cancelled`
- When any forecast is resolved with `brier_score > 0.15`

## Quality Gate
- [ ] Lesson is actionable (not a vague observation)
- [ ] Lesson cites the source review
- [ ] Recurrence check performed
- [ ] At least one bias identified (if error occurred)
