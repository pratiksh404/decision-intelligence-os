# CEO Decision Intelligence Platform

A high-performance, compounding decision-intelligence operating system for startup founders and CEOs. Built on a six-layer architecture, this platform integrates market signals, assumptions, decisions, disciplinary forecasting, and outcome reviews to continuously calibrate judgment and build an organizational brain that gets smarter over years.

---

## Vision
The CEO Decision Intelligence Platform exists to build a compounding judgment advantage. It enforces a strict discipline: separating facts, assumptions, predictions, opinions, and decisions, and closing the learning loop so that every success and failure improves future decision quality.

---

## 1. System Architecture (6 Layers)

The platform is organized around six cognitive layers, mapped to the directory structure:

1. **Intelligence Layer** (`vault/01-intelligence/`): Captures inputs (Signals, Trends, Competitor Profiles, Opportunities) before decisions are made.
2. **Decision Layer** (`vault/02-decisions/`): Converts intelligence into choices via the Assumption Registry, Decision Memos, and Disciplinary Forecasting.
3. **Execution Layer** (`vault/03-execution/`): Tracks implementation through Initiatives, KPIs, and Risk Registries.
4. **Learning Layer** (`vault/04-learning/`): Compounds intelligence via Outcome Reviews, forecast Calibration (Brier scores), and Bias Auditing.
5. **Strategy Layer** (`vault/05-strategy/`): Directs focus and resources to long-term pillars via Strategic Themes, Bets, Resource Allocation models, and the Opportunity Portfolio.
6. **Meta-Intelligence Layer** (`vault/06-meta-intelligence/`): Tracks the system's performance, Brier scores, Org IQ, and AI advisor performance.

---

## 2. Directory Structure

The repository has a strict folder convention:

```text
decision-intelligence-os/
├── README.md
├── AGENTS.md                       # Operating principles for AI assistants
├── advisors/                       # Standard definitions of simulated advisors
├── workflows/                      # Repeatable decision and learning workflows
├── templates/                      # 20+ Obsidian Templater-ready schemas
├── operating-system/               # Standards, metadata, and cadence specs
└── vault/                          # Master Data Vault (Obsidian Vault root)
    ├── 00-Inbox/                   # Raw inbox capture
    ├── 01-Intelligence/            # Signals, trends, competitors, opportunities
    ├── 02-Decisions/               # Assumptions, memos, forecasts, review workflows
    ├── 03-Execution/               # Initiatives, KPIs, risks
    ├── 04-Learning/                # Outcome reviews, lessons, calibrations, bias audits
    ├── 05-Strategy/                # Pillars, bets, resource ledgers, portfolios
    └── 06-Meta-Intelligence/       # Cockpits, performance reports, advisor metrics
```

---

## 3. The 10-Agent System

The platform is driven by a coordinated multi-agent team designed to support the CEO:

1. [Research Analyst](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/research-analyst.md): Sources and verifies facts, TAM, and data.
2. [Competitive Analyst](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/competitive-analyst.md): Teardowns competitor features, pricing, and threats.
3. [Probability Analyst](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/probability-analyst.md): Removes forecasting bias and calculates Brier calibration.
4. [Risk Analyst](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/risk-analyst.md): Runs pre-mortems and designs risk mitigations.
5. [Strategic Advisor](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/strategic-advisor.md): Maps projects to Strategic Themes and Bets.
6. [Red Team Advisor](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/red-team-advisor.md): Attacks assumptions and negates hypotheses.
7. [Execution Advisor](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/execution-advisor.md): Builds milestones, tracks hours, and monitors lead metrics.
8. [Learning Advisor](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/learning-advisor.md): Conducts outcome post-mortems and extracts heuristic rules.
9. [Portfolio Manager](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/portfolio-manager.md): Ranks opportunities using a weighted scoring model.
10. [Chief of Staff](file:///Users/pratiksh/Documents/work/decision-intelligence-os/advisors/chief-of-staff.md): Synthesis reports, manages review dates, and maintains metadata hygiene.

Simulate these board members before signing off on any decision by running the workflows in `workflows/` with your AI coding assistant.

---

## 4. Key Cockpit Queries (Dataview)

To run the real-time cockpits in Obsidian, use the queries documented in [docs/platform-architecture.md](file:///Users/pratiksh/Documents/work/decision-intelligence-os/docs/platform-architecture.md#L300-L360). 

### Example: Opportunity Ranking Query
```sql
TABLE market, confidence_score, estimated_value, 
  ((score_expected_return * 0.3) + (score_probability * 0.2) + (score_strategic_fit * 0.2) - (score_execution_complexity * 0.15) - (score_resource_requirement * 0.15)) AS composite_score
FROM "vault/01-intelligence/opportunities" OR "vault/05-strategy/portfolio"
WHERE status = "researching" OR status = "ready-for-review"
SORT composite_score DESC
```

---

## 5. Phase 2 — Active Intelligence System

Phase 2 transforms the vault from a structured repository into an active intelligence system.

### New Directories
```text
mcp/                            # MCP integration configs and installation guide
workflows/skills/               # Reusable agent skill specifications
vault/06-meta-intelligence/dashboards/
  ├── ceo-cockpit.md            # Executive Intelligence Dashboard (6-layer view)
  ├── forecast-calibration-dashboard.md
  ├── assumption-intelligence-dashboard.md
  ├── weekly-reports/
  ├── daily-reviews/
  ├── monthly-reviews/
  └── quarterly-reviews/
vault/05-strategy/portfolio/
  └── opportunity-score.md      # Scoring engine spec and formula
```

### New Templates
| Template | Purpose |
|---|---|
| `forecast-v2.md` | Full calibration fields: category, brier_score, calibration_error |
| `assumption-v2.md` | invalidation_risk, depends_on_assumptions, evidence_status |
| `opportunity-v2.md` | 6-factor weighted scoring with composite_score |
| `weekly-intelligence-report.md` | Automated 7-section CEO briefing |
| `daily-review.md` | Daily inbox triage and priorities |
| `monthly-review.md` | Calibration, bias detection, portfolio review |
| `quarterly-review.md` | Strategy, resources, bets |

### MCP Integration
Four MCP servers for AI-first operation:
- **obsidian-mcp**: vault search, read, metadata update
- **filesystem-mcp**: templates, workflows, advisors read access
- **git-mcp**: audit trail and decision rollback
- **firecrawl-mcp**: market research and signal ingestion

See `mcp/installation-guide.md` to set up.

### Opportunity Scoring Formula
```
composite_score = (expected_return × 0.25) + (probability × 0.20)
                + (strategic_fit × 0.20)   - (execution_complexity × 0.15)
                - (resource_requirement × 0.10) - (risk × 0.10)
```

### Agent Skills
Five reusable AI workflows in `workflows/skills/`:
- `research-skill.md` — signal, trend, competitor artifact production
- `opportunity-skill.md` — full advisor board scoring
- `decision-challenge-skill.md` — red team + pre-mortem
- `calibration-skill.md` — Brier score calculation and bias detection
- `learning-skill.md` — lesson extraction and recurrence tracking

---

## 6. Daily & Weekly Operating Cadence

1. **Daily (Ingress & Triage):**
   - Save web articles, statistics, or competitive actions to `vault/00-Inbox/`.
   - Ask the Chief of Staff agent to triage and compile them into Signals (`vault/01-intelligence/signals/`).
2. **Weekly Review (Evaluation & Alignment):**
   - Run the [weekly review workflow](file:///Users/pratiksh/Documents/work/decision-intelligence-os/workflows/weekly-ceo-review.md).
   - Evaluate new opportunities, update forecast probabilities, check KPI health, and monitor active risks.
3. **Monthly Audit (Learning & Calibration):**
   - Resolve expired forecasts, calculate Brier scores, conduct outcome reviews for completed decisions, and extract new heuristic rules.
