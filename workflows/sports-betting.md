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
