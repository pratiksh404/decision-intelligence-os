---
title: World Cup 2026 1xBet Strategic Betting Workflow Design
type: design-spec
status: draft
created: 2026-06-15
updated: 2026-06-15
tags:
  - sports-betting
  - fifa-2026
  - forecasting
  - bankroll-management
  - decision-intelligence
related:
  - "[[Decision Principles]]"
  - "[[Forecasting Framework]]"
  - "[[Weekly CEO Review]]"
confidence: 7
source_quality: Medium
evidence_strength: Moderate
decision_readiness: Ready for Review
---

# World Cup 2026 1xBet Strategic Betting Workflow Design

## Executive Summary

This design adds a reusable sports-betting workflow to the Decision Intelligence OS for FIFA World Cup 2026 betting decisions on 1xBet.

The workflow has two connected layers:

1. **Daily bet-slip workflow:** Evaluate each matchday's available bets, compare 1xBet odds against Decision Intelligence OS probabilities, and produce a bet/no-bet slip.
2. **Tournament bankroll portfolio:** Govern total exposure across the World Cup through bankroll limits, per-bet caps, daily caps, stop-loss rules, and calibration reviews.

The system must treat "no bet" as a valid and often preferred decision. It should not convert every forecast into a wager.

## Facts

- The repository already includes forecasting, source-note, strategic-bet, advisor, calibration, and orchestration artifacts.
- The current forecasting workflow supports sports analysis, including market odds, recent form, tactical matchups, squad availability, and probability estimates.
- The repository has an existing World Cup group-stage prediction signal at `Decision Intelligence OS/01-intelligence/signals/2026-world-cup-group-stage-predictions.md`.
- The repository does not yet have a betting-specific workflow that enforces expected value checks, bankroll caps, no-bet rules, odds capture, or post-match betting calibration.

## Assumptions

- 1xBet odds are the primary bookmaker input, but the workflow should allow additional market references when available.
- The Decision Intelligence OS model probability may come from a combination of internal forecasts, market odds, recent team data, tactical analysis, and advisor review.
- Betting recommendations are decision-support artifacts, not guarantees of profit.
- The workflow should remain plain markdown first, with script automation added later only where it improves repeatability.

## Opinions

- Sports wagers should not use the same artifact semantics as long-horizon strategic business bets.
- The strongest immediate design is a structured markdown workflow with explicit risk gates.
- Full automation should come after the daily process and portfolio rules have been tested manually.

## Predictions

- Heavy favorite moneyline bets will often fail the risk/reward gate even when the favorite is likely to win.
- Daily bet slips will frequently recommend no bet or only small selective exposure.
- Calibration quality will improve if every resolved bet records implied probability, model probability, stake size, outcome, and Brier score.

## Decisions

- Create a dedicated sports-betting workflow rather than overloading the existing strategic-bet template.
- Use a two-layer operating model: daily bet slips governed by a tournament bankroll portfolio.
- Require every proposed wager to pass odds capture, probability estimation, counterargument review, expected value check, stake sizing, and post-match review.

## Architecture

### Artifact Layer

The implementation should add three first-class markdown artifacts:

1. `workflows/sports-betting.md`
   - Defines the operating procedure for daily betting decisions.
   - Establishes advisor responsibilities and required gates.

2. `templates/daily-bet-slip.md`
   - Captures a daily slate of matches and bet decisions.
   - Compares 1xBet implied probabilities against OS probabilities.
   - Records edge, stake, decision, confidence, and review date.

3. `templates/tournament-bankroll-portfolio.md`
   - Defines the bankroll policy for the tournament.
   - Sets maximum exposure limits, stop-loss rules, and review cadence.

### Data Flow

```text
Match slate
-> 1xBet odds capture
-> implied probability calculation
-> bookmaker margin adjustment
-> evidence collection
-> OS probability estimate
-> advisor critique
-> expected value check
-> stake sizing
-> daily bet-slip decision
-> result capture
-> calibration update
-> bankroll portfolio update
```

### Advisor Roles

- **Intelligence Analyst:** Verifies match context, team news, injuries, travel, venue, and odds movement.
- **Probability Analyst:** Produces win/draw/loss probabilities and checks implied probability, no-vig probability, edge, and Brier scoring.
- **CFO:** Enforces bankroll allocation, exposure caps, Kelly fraction limits, and stop-loss rules.
- **Skeptic:** Searches for disconfirming evidence, market traps, stale assumptions, and overconfidence.
- **Operator:** Converts approved decisions into a clear bet slip and post-match review task.
- **CEO:** Makes the final decision when the recommendation conflicts with risk policy or confidence is below threshold.

## Daily Bet-Slip Workflow

Each daily bet slip should follow this sequence:

1. **Match Intake**
   - List every match under consideration.
   - Capture kickoff time, market type, and available outcomes.

2. **Odds Capture**
   - Record 1xBet odds and capture time.
   - Attribute source URL or note when odds are user-provided.
   - Calculate raw implied probability for each outcome.
   - Calculate no-vig implied probability when all major outcomes are available.

3. **Evidence Collection**
   - Use the existing World Cup prediction signal.
   - Add current evidence when available: injuries, lineups, recent form, tactical matchup, travel, rest, venue, weather, and odds movement.

4. **Probability Estimate**
   - Produce OS probability for win, draw, and loss.
   - State confidence and unknown variables.
   - Avoid binary predictions.

5. **Counterarguments**
   - Require a skeptic note for each proposed bet.
   - Record what evidence would change the decision.

6. **Expected Value Check**
   - Compare OS probability against no-vig implied probability.
   - Estimate edge.
   - Mark bets with insufficient edge as `no-bet`.

7. **Stake Sizing**
   - Apply portfolio constraints before stake recommendation.
   - Use fractional Kelly only when edge and confidence are sufficient.
   - Default to fixed small stakes or no bet when uncertainty is high.

8. **Bet Slip Decision**
   - Produce one of: `bet`, `watchlist`, or `no-bet`.
   - Include exact stake, odds, market, and rationale for approved bets.

9. **Post-Match Review**
   - Record result, profit/loss, calibration error, and Brier score.
   - Update bankroll portfolio and forecast calibration log.

## Tournament Bankroll Portfolio

The tournament portfolio should define:

- Starting bankroll.
- Maximum daily exposure.
- Maximum per-match exposure.
- Maximum per-market exposure.
- Stop-loss trigger.
- Drawdown review trigger.
- Kelly fraction policy.
- Favorite-moneyline rule.
- Draw and underdog rule.
- Parlay restriction.
- Review cadence.

### Default Risk Policy

The initial default policy should be conservative:

- Maximum daily exposure: 3% of bankroll.
- Maximum single bet exposure: 1% of bankroll.
- Maximum exposure on heavy favorite moneylines below 1.30 odds: 0.5% of bankroll unless edge is exceptional.
- Fractional Kelly cap: 25% Kelly, capped by the per-bet and daily limits.
- Stop-loss trigger: pause new bets after a 10% tournament bankroll drawdown until review.
- No parlay betting unless explicitly approved in a daily slip.
- No bet unless expected value is positive after margin adjustment.

These defaults can be changed in the tournament portfolio artifact, but every change should be recorded as a decision.

## Decision Rules

- **No Bet Rule:** Recommend no bet unless OS probability exceeds no-vig implied probability by a documented edge.
- **Heavy Favorite Rule:** Avoid low-return favorite moneylines unless the probability edge is unusually strong and the stake remains small.
- **Draw/Underdog Rule:** Consider higher-volatility outcomes only when the edge is clear and stake sizing reflects variance.
- **Source Rule:** If odds are user-provided rather than directly verified, mark source quality no higher than Medium.
- **Confidence Rule:** Bets below confidence 6/10 require CEO approval or default to watchlist/no-bet.
- **Portfolio Rule:** No individual daily slip can override tournament exposure limits without an explicit decision note.
- **Calibration Rule:** Every resolved bet must update the calibration log.

## Error Handling

- If 1xBet pages are unavailable or redirected, use user-provided odds only with source-quality downgrade.
- If a match lacks current team news, record the unknown and lower confidence.
- If only one side of a market is available, do not calculate no-vig probabilities; mark the edge estimate incomplete.
- If odds move materially after the slip is created, re-run the EV check before placing the bet.

## Testing and Verification

Manual verification should confirm that:

- The sports-betting workflow preserves the repository's mandatory separation of facts, assumptions, opinions, predictions, and decisions.
- Daily bet slips calculate implied probability and edge consistently.
- Portfolio rules can reject an otherwise attractive bet when exposure caps are reached.
- Resolved bets can feed forecast calibration.
- A no-bet recommendation is represented as a first-class decision.

Future script automation can test:

- Decimal odds to implied probability conversion.
- No-vig probability normalization.
- Expected value calculation.
- Fractional Kelly stake sizing.
- Exposure cap enforcement.
- Brier score calculation.

## Risks

- Betting markets can change quickly, making stale odds misleading.
- Internal model probabilities may be overconfident if based on thin evidence.
- High payout draw/underdog bets can look attractive while carrying high variance.
- Automation could create false precision if source quality is weak.
- The user may be tempted to override no-bet recommendations after manual review.

## Next Actions

After this design is approved:

1. Create an implementation plan.
2. Add `workflows/sports-betting.md`.
3. Add `templates/daily-bet-slip.md`.
4. Add `templates/tournament-bankroll-portfolio.md`.
5. Optionally add a first World Cup 2026 portfolio note under the vault.
6. Optionally add a daily slip for the current matchday using verified or user-provided 1xBet odds.

## Confidence Assessment

- **Confidence Score:** 7/10
- **Source Quality:** Medium
- **Evidence Strength:** Moderate
- **Decision Readiness:** Ready for Review

The design is strong enough for review and implementation planning. It should not be treated as a betting recommendation until the daily slip artifacts are created with current odds and match evidence.
