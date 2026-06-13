# Skill: Decision Challenge (Red Team)

**Agent:** Red Team Advisor + Skeptic
**Version:** 2.0

## Purpose
Attack a proposed decision or assumption to surface hidden risks, weak logic, and disconfirming evidence before commitment.

## Inputs
| Input | Required | Description |
|---|---|---|
| `decision_note` | ✅ | Path to decision memo or assumption note |
| `challenge_depth` | ✅ | `standard` (5 challenges) or `deep` (10 challenges) |

## Process
1. Read the decision note and all linked assumptions, forecasts, and evidence
2. Identify the 3 strongest assumptions underlying the decision
3. For each assumption, generate the sharpest possible counterargument
4. Run pre-mortem: "It is 12 months from now and this decision failed. What went wrong?"
5. Identify any cognitive biases in the reasoning:
   - Confirmation bias
   - Overconfidence
   - Availability bias
   - Sunk cost
6. Assign probability to the failure scenario
7. Generate 3 concrete data points that would change the recommendation

## Outputs
Red Team Analysis note or inline section with:
- `top_risks`: list of the 3 highest-impact challenges
- `failure_scenario`: pre-mortem narrative
- `bias_flags`: list of detected biases
- `invalidating_evidence`: 3 things that would cause abandonment
- `red_team_verdict`: Proceed / Reconsider / Block
- `confidence_adjustment`: suggested delta to existing confidence score

## Review Triggers
- Automatically triggered when any decision reaches `status: ready-for-review`
- Manually triggered via QuickAdd: "Run Red Team on Decision"

## Quality Gate
- [ ] At least 3 assumptions challenged
- [ ] Pre-mortem completed
- [ ] At least one cognitive bias explicitly checked
- [ ] Verdict is explicit and unconditional
