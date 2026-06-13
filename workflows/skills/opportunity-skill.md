# Skill: Opportunity Evaluation

**Agent:** Portfolio Manager + Advisor Board
**Version:** 2.0

## Purpose
Score and qualify a new opportunity using the weighted scoring formula.

## Inputs
| Input | Required | Description |
|---|---|---|
| `opportunity_note` | ✅ | Path to opportunity note in vault |
| `run_advisor_board` | optional | `true` to run all 7 advisors |

## Process
1. Read the opportunity note via filesystem MCP
2. Read linked trends, competitors, and signals
3. Read active strategic themes
4. Score each factor 1–10 using scoring guide in `vault/05-strategy/portfolio/opportunity-score.md`
5. Calculate composite_score
6. If `run_advisor_board: true`, simulate each advisor independently:
   - CEO: strategic alignment
   - CFO: financial feasibility
   - VC: market size and defensibility
   - Skeptic: attack the best-case assumptions
   - Operator: execution realism
   - Portfolio Manager: portfolio fit and ranking
7. Synthesize consensus recommendation

## Outputs
Updated opportunity note with:
- All 6 `score_*` fields populated
- `composite_score` calculated
- `decision_readiness` updated per threshold table
- Advisor board analysis section filled
- `recommendation`: Pursue / Monitor / Reject / Research Further

If composite_score ≥ 7.0:
- Set `status: ready-for-review`
- Set `review_date: today + 3 days`

## Review Triggers
- On new opportunity creation (auto-prompt user to run this skill)
- On `review_date` for existing opportunities

## Quality Gate
- [ ] All 6 score factors populated
- [ ] Composite score calculated and matches formula
- [ ] At least Skeptic analysis completed
- [ ] Recommendation is explicit
