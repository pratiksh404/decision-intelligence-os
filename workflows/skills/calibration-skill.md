# Skill: Forecast Calibration Review

**Agent:** Probability Analyst
**Version:** 2.0

## Purpose
Review active forecasts for staleness, update probabilities based on new evidence, and process resolved forecasts into Brier scores.

## Inputs
| Input | Required | Description |
|---|---|---|
| `review_scope` | ✅ | `overdue` / `this-month` / `all-active` |
| `force_update` | optional | `true` to recalculate all stale forecasts |

## Process

### For Active Forecasts (probability update)
1. Read all forecasts matching scope from `vault/02-decisions/forecasts/`
2. For each: read original evidence and check for new signals in `vault/01-intelligence/`
3. If new signals exist: recalculate probability estimate
4. Update `predicted_probability` and `updated` date
5. If probability change > 0.15: flag for CEO review

### For Resolved Forecasts (calibration)
1. Read all `status: resolved` forecasts from last 30 days
2. Verify `brier_score = (predicted_probability - actual_probability)^2`
3. Verify `calibration_error = predicted_probability - actual_probability`
4. Aggregate into monthly calibration entry
5. Detect systematic bias: if average calibration_error > +0.10 = overconfident, < -0.10 = underconfident

## Outputs
- Updated frontmatter on each reviewed forecast
- New or updated calibration note in `vault/04-learning/calibration/`
- Bias alert if systematic error detected

## Review Triggers
- Monthly (on 1st of month)
- Any forecast deadline reached
- Weekly: surface forecasts due within 7 days

## Quality Gate
- [ ] Every resolved forecast has brier_score populated
- [ ] Monthly calibration entry created
- [ ] Bias flag raised if calibration_error outside ±0.10
