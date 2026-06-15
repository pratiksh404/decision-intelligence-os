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
