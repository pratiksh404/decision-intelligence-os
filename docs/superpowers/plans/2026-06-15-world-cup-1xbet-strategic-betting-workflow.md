# World Cup 1xBet Strategic Betting Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a reusable World Cup 2026 sports-betting workflow that produces daily 1xBet bet slips governed by a tournament bankroll portfolio.

**Architecture:** Implement this as markdown-first Decision Intelligence OS infrastructure. Add one workflow file and two reusable templates that enforce facts/assumptions/opinions/predictions/decisions separation, advisor-board review, expected-value checks, bankroll caps, no-bet rules, and post-match calibration.

**Tech Stack:** Markdown, YAML frontmatter, Obsidian-compatible internal links, existing Decision Intelligence OS folder conventions.

---

## File Structure

- Create `workflows/sports-betting.md`
  - Defines the operating procedure for sports-betting decisions.
  - Establishes daily bet-slip gates, advisor responsibilities, risk rules, and post-match review.

- Create `templates/daily-bet-slip.md`
  - Reusable template for one matchday's betting slate.
  - Captures odds, no-vig probabilities, OS probabilities, edge, stake sizing, final decision, and review status.

- Create `templates/tournament-bankroll-portfolio.md`
  - Reusable template for tournament-level bankroll governance.
  - Captures starting bankroll, exposure limits, Kelly policy, stop-loss rules, drawdown review, calibration schedule, and decision log.

- Verify existing files only by reading:
  - `docs/superpowers/specs/2026-06-15-world-cup-1xbet-strategic-betting-workflow-design.md`
  - `workflows/forecasting.md`
  - `automation/agent-orchestration.md`
  - `templates/forecast.md`
  - `templates/strategic-bet.md`

## Task 1: Add Sports-Betting Workflow

**Files:**
- Create: `workflows/sports-betting.md`

- [ ] **Step 1: Create the workflow file**

Add this full content to `workflows/sports-betting.md`:

```markdown
# Sports Betting Workflow

## Purpose

Convert sports forecasts and bookmaker odds into disciplined bet/no-bet decisions with explicit bankroll controls, expected-value checks, and post-match calibration.

This workflow is designed for FIFA World Cup 2026 daily bet slips on 1xBet, but it can be reused for other sports markets that offer decimal odds.

## Core Objective

Support decision quality by answering:

- Which matches are worth evaluating today?
- What are the bookmaker-implied probabilities?
- What are the Decision Intelligence OS probabilities?
- Is there a positive edge after bookmaker margin adjustment?
- What stake is justified under the tournament bankroll policy?
- Should the final decision be bet, watchlist, or no-bet?
- How did the decision perform after resolution?

## Mandatory Separation

Every betting artifact must separate:

- Facts
- Assumptions
- Opinions
- Predictions
- Decisions

Never present a team preference, model estimate, or betting recommendation as a fact.

## Required Inputs

| Input | Required | Notes |
|---|---:|---|
| Match slate | Yes | Include all matches under consideration for the day. |
| 1xBet odds | Yes | Directly captured odds are preferred; user-provided odds are acceptable with source-quality downgrade. |
| Odds capture time | Yes | Betting markets move quickly. |
| Market type | Yes | Example: 1X2, draw, moneyline, totals, handicap. |
| Existing OS forecast | Preferred | Use active forecast or signal notes when available. |
| Current team evidence | Preferred | Injuries, lineups, rest, travel, weather, tactical matchup, form, odds movement. |
| Tournament bankroll portfolio | Yes | Daily slips must obey portfolio limits. |

## Daily Workflow

```text
Question
-> Research
-> Evidence Collection
-> Analysis
-> Counterarguments
-> Probability Assessment
-> Decision
-> Execution Plan
-> Review Schedule
```

### 1. Match Intake

List each match and market under consideration.

Required fields:

- Match
- Competition
- Kickoff time
- Market type
- Available outcomes
- Odds source
- Odds capture time

### 2. Odds Capture

For each market:

1. Record decimal odds.
2. Convert decimal odds to raw implied probability.
3. If all mutually exclusive outcomes are available, normalize to no-vig implied probability.
4. Record whether odds were directly verified or user-provided.

Formula:

```text
raw_implied_probability = 1 / decimal_odds
no_vig_probability = raw_implied_probability / sum(raw_implied_probabilities_for_market)
```

### 3. Evidence Collection

Use the strongest available evidence:

- Existing World Cup signal notes.
- Current lineups and injuries.
- Recent form.
- Tactical matchup.
- Venue, travel, weather, and rest.
- Market odds and odds movement.
- Prior calibration notes for similar forecasts.

Record missing evidence explicitly under Unknown Variables.

### 4. Advisor Board Review

Run the advisors independently before final synthesis:

- **Intelligence Analyst:** Verifies team context, source quality, and odds movement.
- **Probability Analyst:** Produces win/draw/loss probabilities and checks implied probability, no-vig probability, edge, and calibration risk.
- **CFO:** Enforces bankroll allocation, exposure caps, Kelly fraction limits, and stop-loss rules.
- **Skeptic:** Challenges overconfidence, stale assumptions, market traps, and favorite bias.
- **Operator:** Converts approved decisions into a clear slip and review task.
- **CEO:** Makes the final decision when confidence is low, stakes exceed normal limits, or the recommendation conflicts with risk policy.

### 5. Probability Assessment

For 1X2 markets, estimate:

- Home or listed team win probability.
- Draw probability.
- Away or opposing team win probability.

Required probability fields:

- Raw implied probability.
- No-vig implied probability.
- OS probability.
- Edge.
- Confidence score.

Formula:

```text
edge = OS_probability - no_vig_implied_probability
expected_value_per_unit = (OS_probability * decimal_odds) - 1
```

### 6. Decision Rules

- **No Bet Rule:** Recommend no bet unless OS probability exceeds no-vig implied probability by a documented edge.
- **Heavy Favorite Rule:** Avoid low-return favorite moneylines unless the edge is unusually strong and the stake remains small.
- **Draw/Underdog Rule:** Consider higher-volatility outcomes only when the edge is clear and stake sizing reflects variance.
- **Source Rule:** If odds are user-provided rather than directly verified, mark source quality no higher than Medium.
- **Confidence Rule:** Bets below confidence 6/10 require CEO approval or default to watchlist/no-bet.
- **Portfolio Rule:** No daily slip can override tournament exposure limits without an explicit decision note.
- **Calibration Rule:** Every resolved bet must update the calibration log or review section.

### 7. Stake Sizing

Apply portfolio constraints before recommending a stake.

Default policy:

- Maximum daily exposure: 3% of bankroll.
- Maximum single bet exposure: 1% of bankroll.
- Maximum heavy favorite exposure below 1.30 odds: 0.5% of bankroll unless edge is exceptional.
- Fractional Kelly cap: 25% Kelly, capped by per-bet and daily limits.
- Stop-loss trigger: pause new bets after 10% tournament drawdown until review.
- No parlay betting unless explicitly approved.

Kelly formula for decimal odds:

```text
b = decimal_odds - 1
p = OS_probability
q = 1 - p
kelly_fraction = ((b * p) - q) / b
recommended_fraction = min(kelly_fraction * 0.25, per_bet_cap, remaining_daily_cap)
```

If Kelly is negative, the decision must be no-bet.

### 8. Final Bet Slip Decision

Each outcome must receive one of:

- `bet`
- `watchlist`
- `no-bet`

Approved bets must include:

- Market.
- Decimal odds.
- Stake.
- Bankroll percentage.
- Rationale.
- Review trigger.

### 9. Post-Match Review

After resolution, record:

- Final score.
- Outcome.
- Stake.
- Profit/loss.
- Closing odds if available.
- Calibration error.
- Brier score.
- Lesson learned.

Formula:

```text
calibration_error = OS_probability - actual_result
brier_score = (OS_probability - actual_result)^2
```

Where `actual_result` is `1` if the selected outcome occurred and `0` if it did not.

## Output

Use `templates/daily-bet-slip.md` for daily decisions.

Use `templates/tournament-bankroll-portfolio.md` for tournament-level portfolio governance.

## Quality Gate

Before acting on a bet slip, verify:

- [ ] Facts, assumptions, opinions, predictions, and decisions are separated.
- [ ] Odds source and capture time are recorded.
- [ ] Raw implied probability is calculated.
- [ ] No-vig implied probability is calculated or marked unavailable.
- [ ] OS probability is stated with confidence.
- [ ] Edge and EV are calculated.
- [ ] CFO risk gates are applied.
- [ ] No-bet decisions are preserved.
- [ ] Review date is set.
```

- [ ] **Step 2: Verify the workflow contains required sections**

Run:

```bash
rg -n "Purpose|Daily Workflow|Advisor Board Review|Decision Rules|Stake Sizing|Post-Match Review|Quality Gate" workflows/sports-betting.md
```

Expected output includes one line for each required section.

- [ ] **Step 3: Commit the workflow**

Run:

```bash
git add workflows/sports-betting.md
git commit -m "Add sports betting workflow"
```

Expected: commit succeeds with one new file.

## Task 2: Add Daily Bet-Slip Template

**Files:**
- Create: `templates/daily-bet-slip.md`

- [ ] **Step 1: Create the daily slip template**

Add this full content to `templates/daily-bet-slip.md`:

```markdown
---
title:
type: daily-bet-slip
status: draft
created:
updated:
competition: FIFA World Cup 2026
bookmaker: 1xBet
bet_date:
bankroll_portfolio:
daily_bankroll_start:
daily_exposure_cap_pct: 3
daily_exposure_used_pct: 0
confidence_score: 5
source_quality: Medium
evidence_strength: Moderate
decision_readiness: Research Needed
review_date:
tags:
  - sports-betting
  - daily-bet-slip
  - fifa-2026
  - forecasting
related:
  - "[[Forecasting Framework]]"
  - "[[Weekly CEO Review]]"
---

# Daily Bet Slip: {{title}}

## Executive Summary

## Facts

- **Bet Date:**
- **Bookmaker:** 1xBet
- **Odds Capture Time:**
- **Odds Source:** Direct / User-provided / Mixed
- **Tournament Bankroll Portfolio:**
- **Daily Bankroll Start:**
- **Daily Exposure Cap:**

## Assumptions

- 

## Opinions

- 

## Predictions

- 

## Decisions

- 

## Match Slate

| Match | Kickoff | Market | Outcome | Decimal Odds | Raw Implied % | No-Vig Implied % | OS Probability % | Edge % | EV / Unit | Confidence | Decision | Stake | Notes |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
|  |  | 1X2 |  |  |  |  |  |  |  |  | no-bet |  |  |

## Odds Capture

### Source Notes

- 

### Calculation Notes

```text
raw_implied_probability = 1 / decimal_odds
no_vig_probability = raw_implied_probability / sum(raw_implied_probabilities_for_market)
edge = OS_probability - no_vig_implied_probability
expected_value_per_unit = (OS_probability * decimal_odds) - 1
```

## Evidence Collection

### Supporting Evidence

- 

### Counter-Evidence

- 

### Unknown Variables

- 

## Advisor Board Analysis

### Intelligence Analyst

- Source Quality:
- Match Context:
- Odds Movement:
- Recommendation:

### Probability Analyst

- Probability Estimate:
- Edge Assessment:
- Calibration Risk:
- Recommendation:

### CFO

- Daily Exposure:
- Per-Bet Exposure:
- Kelly / Stake Sizing:
- Stop-Loss Status:
- Recommendation:

### Skeptic

- Disconfirming Evidence:
- Overconfidence Risk:
- Market Trap Risk:
- Recommendation:

### Operator

- Execution Clarity:
- Bet Slip Readiness:
- Review Task:
- Recommendation:

### CEO

- Final Decision:
- Override Notes:

## Probability Assessment

| Match | Outcome | No-Vig Implied % | OS Probability % | Edge % | Confidence | Decision |
|---|---|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |

## Stake Sizing

| Bet | Bankroll % | Stake Amount | Kelly Fraction | Cap Applied | Final Stake |
|---|---:|---:|---:|---|---:|
|  |  |  |  |  |  |

## Recommended Bet Slip

| Status | Match | Market | Outcome | Odds | Stake | Rationale |
|---|---|---|---|---:|---:|---|
| no-bet |  |  |  |  |  |  |

## Risks

- 

## Next Actions

- [ ] Re-check odds before placing any approved bet.
- [ ] Confirm total exposure is within tournament portfolio limits.
- [ ] Record placed-bet timestamp if any bet is executed.
- [ ] Update post-match review after resolution.

## Post-Match Review

| Match | Outcome Selected | Actual Result | Stake | Profit/Loss | OS Probability % | Calibration Error | Brier Score | Lesson |
|---|---|---|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |  |  |

## Confidence Assessment

- **Confidence Score:** /10
- **Source Quality:** Low / Medium / High
- **Evidence Strength:** Weak / Moderate / Strong
- **Decision Readiness:** Research Needed / Ready for Review / Ready for Action
```

- [ ] **Step 2: Verify the template contains required decision fields**

Run:

```bash
rg -n "Match Slate|Raw Implied|No-Vig|OS Probability|Edge|EV / Unit|Stake Sizing|Post-Match Review|Confidence Assessment" templates/daily-bet-slip.md
```

Expected output includes all required daily slip sections and table fields.

- [ ] **Step 3: Commit the template**

Run:

```bash
git add templates/daily-bet-slip.md
git commit -m "Add daily bet slip template"
```

Expected: commit succeeds with one new file.

## Task 3: Add Tournament Bankroll Portfolio Template

**Files:**
- Create: `templates/tournament-bankroll-portfolio.md`

- [ ] **Step 1: Create the tournament portfolio template**

Add this full content to `templates/tournament-bankroll-portfolio.md`:

```markdown
---
title:
type: tournament-bankroll-portfolio
status: active
created:
updated:
competition: FIFA World Cup 2026
bookmaker_scope: 1xBet primary
starting_bankroll:
current_bankroll:
max_daily_exposure_pct: 3
max_single_bet_exposure_pct: 1
heavy_favorite_cap_pct: 0.5
stop_loss_pct: 10
kelly_fraction_cap: 0.25
confidence_score: 5
source_quality: Medium
evidence_strength: Moderate
decision_readiness: Ready for Review
review_date:
tags:
  - sports-betting
  - bankroll-management
  - fifa-2026
  - portfolio
related:
  - "[[Decision Principles]]"
  - "[[Forecasting Framework]]"
  - "[[Weekly CEO Review]]"
---

# Tournament Bankroll Portfolio: {{title}}

## Executive Summary

## Facts

- **Competition:** FIFA World Cup 2026
- **Bookmaker Scope:** 1xBet primary
- **Starting Bankroll:**
- **Current Bankroll:**
- **Realized Profit/Loss:**
- **Open Exposure:**
- **Last Review Date:**

## Assumptions

- Betting decisions are made only from documented daily bet slips.
- No bet is placed unless it passes the daily workflow and portfolio risk gates.
- User-provided odds are acceptable when direct capture is unavailable, but source quality is capped at Medium.

## Opinions

- Preserving bankroll matters more than maximizing action.
- Heavy favorite moneylines require stricter edge thresholds because payout asymmetry is poor.
- Draws and underdogs should be sized for high variance even when edge appears positive.

## Predictions

- The portfolio will produce many no-bet decisions.
- The best value will likely come from selective mispriced draws, underdogs, or favorites with unusually strong edges.
- Calibration review will reveal whether OS probabilities are systematically overconfident or underconfident.

## Decisions

- **Portfolio Status:** Active / Paused / Closed
- **Approved Betting Scope:** 1X2 / Moneyline / Draw / Totals / Handicap
- **Parlay Policy:** Disabled unless explicitly approved in a daily slip.

## Bankroll Policy

| Rule | Default | Active Setting | Notes |
|---|---:|---:|---|
| Starting Bankroll |  |  |  |
| Maximum Daily Exposure | 3% |  | Total stake across one daily slip. |
| Maximum Single Bet Exposure | 1% |  | Applies before Kelly sizing. |
| Heavy Favorite Cap | 0.5% |  | Applies to odds below 1.30 unless exception is approved. |
| Stop-Loss Trigger | 10% |  | Pause new bets until review. |
| Kelly Fraction Cap | 25% |  | Also capped by daily and per-bet limits. |
| Parlay Exposure | 0% |  | Disabled by default. |

## Favorite-Moneyline Rules

- Avoid odds below 1.30 unless OS probability edge is exceptional.
- If approved, stake must remain below the heavy favorite cap.
- Record why the downside-to-upside profile is acceptable.

## Draw and Underdog Rules

- Require positive EV after margin adjustment.
- Require explicit variance note from CFO.
- Require Skeptic review for market-trap risk.
- Stake must remain within single-bet and daily exposure caps.

## Kelly Policy

Formula:

```text
b = decimal_odds - 1
p = OS_probability
q = 1 - p
kelly_fraction = ((b * p) - q) / b
recommended_fraction = min(kelly_fraction * 0.25, per_bet_cap, remaining_daily_cap)
```

If Kelly is negative, the decision must be no-bet.

## Stop-Loss and Pause Rules

Pause new bets and require CEO review when any condition is true:

- Tournament bankroll drawdown reaches 10%.
- Three consecutive daily slips produce negative realized P/L.
- Any placed bet exceeded the approved stake.
- A major data-quality issue is discovered after a bet is placed.

## Exposure Ledger

| Date | Daily Slip | Starting Bankroll | Stake Total | Exposure % | Realized P/L | Ending Bankroll | Status |
|---|---|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |  |

## Decision Log

| Date | Decision | Rationale | Approved By | Review Trigger |
|---|---|---|---|---|
|  |  |  |  |  |

## Calibration Schedule

- Daily: Update resolved bet results after matches finish.
- Weekly: Review calibration error and realized P/L.
- Triggered: Review immediately after stop-loss or major odds/data-quality issue.
- Tournament End: Produce final betting calibration report.

## Confidence Assessment

- **Confidence Score:** /10
- **Source Quality:** Low / Medium / High
- **Evidence Strength:** Weak / Moderate / Strong
- **Decision Readiness:** Research Needed / Ready for Review / Ready for Action
```

- [ ] **Step 2: Verify the portfolio template contains required risk controls**

Run:

```bash
rg -n "Maximum Daily Exposure|Maximum Single Bet Exposure|Heavy Favorite Cap|Stop-Loss|Kelly|Draw and Underdog|Exposure Ledger|Calibration Schedule" templates/tournament-bankroll-portfolio.md
```

Expected output includes every required risk-control section.

- [ ] **Step 3: Commit the template**

Run:

```bash
git add templates/tournament-bankroll-portfolio.md
git commit -m "Add tournament bankroll portfolio template"
```

Expected: commit succeeds with one new file.

## Task 4: Verify Spec Coverage and Repository State

**Files:**
- Read: `docs/superpowers/specs/2026-06-15-world-cup-1xbet-strategic-betting-workflow-design.md`
- Read: `workflows/sports-betting.md`
- Read: `templates/daily-bet-slip.md`
- Read: `templates/tournament-bankroll-portfolio.md`

- [ ] **Step 1: Verify the three planned artifacts exist**

Run:

```bash
test -f workflows/sports-betting.md
test -f templates/daily-bet-slip.md
test -f templates/tournament-bankroll-portfolio.md
```

Expected: all commands exit with status `0`.

- [ ] **Step 2: Verify no unresolved placeholder markers were introduced**

Run:

```bash
rg -n "TB[D]|TO[D]O|implement[ ]later|fill[ ]in[ ]details" workflows/sports-betting.md templates/daily-bet-slip.md templates/tournament-bankroll-portfolio.md
```

Expected: no matches.

- [ ] **Step 3: Verify workflow preserves mandatory separation**

Run:

```bash
rg -n "Facts|Assumptions|Opinions|Predictions|Decisions" templates/daily-bet-slip.md templates/tournament-bankroll-portfolio.md workflows/sports-betting.md
```

Expected: output shows the mandatory separation in all relevant artifacts.

- [ ] **Step 4: Verify git status before final response**

Run:

```bash
git status --short
```

Expected: only pre-existing unrelated Obsidian/dashboard changes remain, unless the user requested additional artifacts.

## Implementation Notes

- Do not modify existing unrelated Obsidian configuration files.
- Do not change the existing World Cup prediction signal in this plan.
- Do not add automation scripts in this plan.
- Do not create an actual daily bet slip or portfolio instance unless the user explicitly requests it after these reusable artifacts are implemented.
- Commit each task separately so the workflow, daily template, and portfolio template can be reviewed independently.

## Self-Review

- **Spec coverage:** The plan implements the approved workflow file, daily bet-slip template, and tournament bankroll portfolio template. It also includes verification steps for facts/assumptions/opinions/predictions/decisions separation, odds/probability fields, risk gates, and calibration.
- **Placeholder scan:** The plan avoids unresolved placeholder markers. Blank template fields are intentional reusable template slots.
- **Type consistency:** The plan consistently uses `OS probability`, `raw implied probability`, `no-vig implied probability`, `edge`, `expected_value_per_unit`, `kelly_fraction`, `daily exposure`, and `single bet exposure` across workflow and templates.
