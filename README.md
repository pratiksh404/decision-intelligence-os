# Decision Intelligence OS

Personal AI-powered decision intelligence operating system for a founder/CEO.

This repository is not a note-taking vault and not a second brain. It is a portable operating system for opportunity discovery, market intelligence, forecasting, strategic decision support, and execution planning.

The founder acts as CEO. AI agents perform structured research, critique, probability assessment, and planning.

## Vision

Decision Intelligence OS exists to build a compounding intelligence advantage for a one-person venture studio. Its purpose is to help the founder discover high-quality opportunities earlier, avoid bad decisions faster, forecast uncertain outcomes with discipline, and convert decisions into execution plans.

Every artifact must support one of three outcomes:

- Opportunity Discovery
- Decision Making
- Execution

Anything else is treated as operational noise.

## Architecture

The system has two first-class layers:

1. **Obsidian Intelligence Vault**
   A markdown-native workspace for opportunities, decisions, forecasts, intelligence reports, execution plans, source notes, and reviews.

2. **Portable AI Agent and Workflow System**
   Tool-agnostic advisor definitions, workflow protocols, templates, and operating principles that can be used across Claude Code, Codex, Cursor, Windsurf, Roo Code, Aider, Antigravity, Opencode, Copilot, and other AI assistants.

The repository deliberately avoids vendor lock-in. Markdown is the durable interface. Frontmatter, tags, links, and predictable folder names make the system automation-ready.

## Folder Structure

```text
decision-intelligence-os/
  README.md
  AGENTS.md
  advisors/                 AI advisory board definitions
  workflows/                Repeatable decision and intelligence workflows
  templates/                Obsidian-ready artifact templates
  operating-system/         Principles, standards, metadata, cadence
  vault/                    Working intelligence vault
  reviews/                  Review protocols and scorecards
  automation/               Future automation roadmap and specs
  docs/                     Design specs, implementation plans, usage docs
  .obsidian/                Minimal Obsidian configuration notes
```

## Agent System

The AI Advisory Board contains seven specialized advisors:

- CEO: vision, strategy, positioning, long-term advantage
- CFO: economics, margins, ROI, capital efficiency, risk
- VC: market size, scalability, defensibility, venture potential
- Skeptic: failure modes, invalid assumptions, competitive threats
- Operator: execution plans, resources, process, delivery risk
- Intelligence Analyst: research quality, evidence, trends, source reliability
- Probability Analyst: Bayesian reasoning, scenarios, base rates, confidence

Each advisor has a dedicated file in `advisors/` with mission, responsibilities, diagnostic questions, analysis framework, and output format.

## Workflow System

Core workflows live in `workflows/`:

- Business Opportunity Analysis
- Market Intelligence
- Forecasting
- Decision Memo
- Execution Planning
- Weekly CEO Review

Every major analysis follows:

```text
Question -> Research -> Evidence Collection -> Analysis -> Counterarguments
-> Probability Assessment -> Decision -> Execution Plan -> Review Schedule
```

## Daily Usage

Use the system as a CEO cockpit:

1. Capture raw signals in `vault/00-inbox/`.
2. Convert promising signals into opportunity, forecast, intelligence, or decision artifacts.
3. Run the appropriate workflow with the AI Advisory Board.
4. Record decisions separately from facts and assumptions.
5. Move approved work into execution plans with KPIs and review dates.

Daily questions:

- What changed in the market?
- What new opportunity deserves investigation?
- What decision requires evidence?
- What forecast needs updating?
- What execution plan is off-track?

## Weekly Reviews

Run `workflows/weekly-ceo-review.md` every week. The review should evaluate:

- New signals captured
- Active opportunities
- Open decisions
- Forecast accuracy
- Execution progress
- Major risks
- Next week's priority decisions

The output belongs in `vault/07-reviews/`.

## Forecasting Process

Forecasts must never be binary. Each forecast must include:

- Evidence
- Counter-evidence
- Unknown variables
- Scenario analysis
- Probability estimates
- Confidence rating
- Review trigger
- Resolution criteria

Use `templates/forecast.md` and `workflows/forecasting.md`.

## Business Opportunity Process

Every business opportunity analysis must include:

- Problem
- Customer
- Opportunity
- Why now
- Initial hypothesis
- Market size
- Growth rate
- Trends
- Competitors
- Customer pain points
- Existing solutions
- Advisory Board review
- Probability assessment
- Proceed / Monitor / Reject decision
- 90-day execution plan

Use `templates/opportunity.md` and `workflows/business-opportunity-analysis.md`.

## Future Automation Roadmap

Automation priorities:

1. Ingest sources from web, RSS, newsletters, filings, odds markets, and saved links.
2. Classify signals into opportunity, risk, trend, competitor, forecast, or execution categories.
3. Generate draft intelligence reports from source bundles.
4. Maintain forecast ledgers and calibration scores.
5. Trigger review reminders based on frontmatter dates.
6. Build dashboards for decisions, forecasts, opportunities, and execution.
7. Add agent orchestration for advisor-board review.

See `automation/roadmap.md`.

## Operating Rule

Always separate facts, assumptions, opinions, predictions, and decisions. Never present assumptions as facts. Never make predictions without evidence. Always explain uncertainty and seek disconfirming evidence.

