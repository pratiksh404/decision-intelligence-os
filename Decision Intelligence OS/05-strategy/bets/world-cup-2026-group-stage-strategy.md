# World Cup 2026 Group Stage: Strategic Betting Strategy (1xBet)

## Purpose

This strategy defines the high-level betting logic for the FIFA World Cup 2026 Group Stage. It translates Decision Intelligence OS signals into actionable 1xBet market positions, with a focus on capital preservation and exploiting market inefficiencies created by the 48-team expansion.

## Strategic Objectives

1.  **Exploit the "Debutante Gap":** Systematically target debutant nations (Curaçao, Uzbekistan, Jordan, etc.) who are statistically overmatched in the expanded format.
2.  **Maximize "Host Advantage" Alpha:** Overweight USA, Mexico, and Canada in home-soil matches where market sentiment often lags behind the actual crowd/climate impact.
3.  **Selective Favorite Fading:** Identify Pot 1 teams with "stale" reputations (e.g., aging Belgium) to find high-value draw or underdog opportunities.
4.  **Bankroll Resilience:** Use a tiered stake model to survive the high volatility of the opening 3-match sprint.

---

## 1. Market Categorization & Filter Rules

### Category A: The "Class Gap" Accumulators
*   **Matches:** Pot 1 giants vs. debutants (e.g., Spain vs. Cape Verde, France vs. Iraq).
*   **Logic:** These are "low-yield, high-certainty" events.
*   **1xBet Market:** 1X2 (Win) or Asian Handicap (-1.5 / -2.5).
*   **Rule:** Only bet if decimal odds > 1.25. If below 1.25, look for "Win to Nil" or "Over 2.5 Team Goals" to reach the 1.40+ value zone.

### Category B: The "Host Momentum" Play
*   **Matches:** USA, Mexico, and Canada matches on home soil.
*   **Logic:** In Group A, D, and B, the home crowd and travel fatigue for opponents create a 10–15% "hidden" edge not fully captured in global odds.
*   **1xBet Market:** Moneyline or "Home Team to Win either half."
*   **Rule:** Aggressive Kelly sizing (up to the 1% single-bet cap) is justified here.

### Category C: High-Alpha Fades (The Value Zone)
*   **Matches:** Aging Pot 1 teams against high-pressing Pot 2/3 teams (e.g., Belgium vs. Egypt, Uruguay vs. Spain).
*   **Logic:** Market sentiment often overvalues "Legacy" names.
*   **1xBet Market:** Double Chance (X2) or Handicap (+1.5) on the underdog.
*   **Rule:** Require an OS probability edge of > 5% vs. no-vig bookmaker odds.

---

## 2. Risk Gates & Decision Rules (CFO Layer)

### The "No-Bet" Hard Gates
*   **Stale Information:** Do not bet if lineups are not confirmed or major injury news (e.g., Haaland/Mbappe) is pending.
*   **Negative EV:** Never bet if `(OS_Probability * Decimal_Odds) < 1.05`. We require a 5% minimum expected value.
*   **Red-Zone Exposure:** If the tournament bankroll is in a 10% drawdown, Category C (High-Alpha Fades) bets are suspended until the next weekly review.

### Stake Sizing Tiers
*   **Tier 1 (High Confidence):** 1.0% of Bankroll (e.g., USA vs. Australia, Brazil vs. Haiti).
*   **Tier 2 (Moderate/Value):** 0.5% of Bankroll (e.g., Norway vs. Senegal, Mexico vs. South Korea).
*   **Tier 3 (Speculative/Volatility):** 0.25% of Bankroll (e.g., Draws in Group B or E).

---

## 3. Specific Matchday Targets (June 15 – June 20)

| Date | Target Match | Strategy | Target Odds (1xBet) | Rationale |
|---|---|---|---|---|
| Jun 15 | Spain vs Cape Verde | **Handicap -2.5** | 1.85+ | Complete mismatch; Spain possession-heavy. |
| Jun 16 | Iraq vs Norway | **Norway Win to Nil** | 1.90+ | Haaland efficiency vs Iraq debutant nerves. |
| Jun 18 | Mexico vs South Korea | **Mexico Win** | 1.75+ | Home momentum; South Korea defensively vulnerable to pace. |
| Jun 19 | USA vs Australia | **USA Win** | 1.65+ | US "flying" after opener; high fitness advantage. |
| Jun 20 | Germany vs Ivory Coast | **Germany Win** | 1.55+ | Ivory Coast "disorganized" per intelligence signals. |

---

## 4. Execution Workflow (Operator Layer)

1.  **Odds Verification:** Check 1xBet odds 2 hours before kickoff.
2.  **Daily Slip Generation:** Use `templates/daily-bet-slip.md` to document the analysis.
3.  **Bankroll Check:** Verify current `Exposure Ledger` in the Tournament Portfolio before placing.
4.  **Execution:** Place bet only via the 1xBet primary account.
5.  **Calibration:** Close the loop within 4 hours of match completion to update Brier scores.

---

## 5. Exit & Pivot Rules

*   **Positive Pivot:** If Matchday 1 yield is > 5% of total bankroll, move the 1% single-bet cap to 1.25% for Matchday 2.
*   **Negative Pivot:** If Matchday 1 yield is < -3%, suspend all Tier 3 bets and require a "Skeptic Review" for all Tier 1 bets.
*   **Tournament Exit:** If 20% total drawdown occurs, the strategy is terminated to preserve the remaining 80% capital for the Knockout stage.

---

## Confidence Assessment

*   **Confidence Score:** 8/10
*   **Strategy Type:** Conservative-Aggressive (protecting capital while overweighting high-certainty home advantages).
*   **Review Trigger:** End of Matchday 1 (June 17).
