# Forecast Resolution Workflow

## Trigger
Run when: `deadline < today AND status = active`

Use the Chief of Staff agent or Dataview query in `forecast-calibration-dashboard.md` to identify overdue forecasts.

## Steps

### Step 1 — Retrieve the Forecast
Open the note. Read the `question`, `resolution_criteria`, `predicted_probability`, and `deadline`.

### Step 2 — Determine Actual Outcome
Answer the resolution criteria question with observable evidence.
- Set `actual_outcome`: plain-language description of what happened.
- Set `actual_probability`: `1` if the forecast event occurred, `0` if it did not.

### Step 3 — Calculate Brier Score
```
brier_score = (predicted_probability - actual_probability)^2
```
Example: predicted 0.70, outcome did not occur (0) → `(0.70 - 0)^2 = 0.49`

### Step 4 — Calculate Calibration Error
```
calibration_error = predicted_probability - actual_probability
```
Positive = overconfident. Negative = underconfident.

### Step 5 — Update Frontmatter
```yaml
status: resolved
actual_outcome: "..."
actual_probability: 1   # or 0
brier_score: 0.XX
calibration_error: 0.XX
resolution_date: YYYY-MM-DD
```

### Step 6 — Learning Extraction
If `brier_score > 0.10`, create a lesson note:
- Path: `vault/04-learning/lessons/`
- Tag: `lesson`, `calibration-failure`
- Link back to the forecast

### Step 7 — Update Monthly Calibration Audit
Add this forecast to the current month's `vault/04-learning/calibration/` entry.
Recalculate `average_brier_score` across all resolved forecasts this period.

## Automation (QuickAdd)
Add a QuickAdd command `Resolve Forecast` that:
1. Prompts for `actual_outcome` (text input)
2. Prompts for `actual_probability` (0 or 1)
3. Auto-calculates `brier_score` and `calibration_error`
4. Sets `status: resolved` and stamps `resolution_date`
5. Opens a new lesson note pre-linked to this forecast
