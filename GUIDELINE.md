# Decision Intelligence OS — Operating Guidelines

A practical handbook for using the Phase 2 setup effectively. Read this once, then refer to specific sections as needed.

---

## Part 1 — Mental Model

The system has one job: make sure every decision you commit to is based on explicit evidence, tested assumptions, and calibrated probability — and that you learn from the outcome to make the next decision better.

Everything flows through a single cycle:

```
Signal → Trend → Opportunity → Assumption → Decision → Forecast → Execution → Outcome → Lesson
```

You are not the author of most of this content. The AI advisors are. Your job is to:

1. Feed raw intelligence into `vault/00-inbox/`
2. Approve or reject what agents produce
3. Make the actual decision
4. Record the outcome and close the loop

The system compounds over time. A vault with 50 lessons and 100 resolved forecasts is dramatically more powerful than one with 5. Volume and consistency matter more than perfection in any single note.

---

## Part 2 — One-Time Setup

### Step 1 — Install MCP Servers

```bash
# macOS — copy MCP config to Claude Desktop
cp mcp/claude-desktop-config.json \
   "$HOME/Library/Application Support/Claude/claude_desktop_config.json"
```

Then open `mcp/installation-guide.md` and follow steps 1–3 (install Obsidian Local REST API plugin, create `.env` file, restart Claude Desktop).

**Test it works:**
Open Claude Desktop → start a new conversation → type:
> "Search the vault for notes with type: forecast and status: active"

If Claude returns results from your vault, MCP is live.

### Step 2 — Configure Obsidian

**Periodic Notes plugin settings:**

| Period | Template | Folder |
|---|---|---|
| Daily | `templates/daily-review.md` | `vault/06-meta-intelligence/dashboards/daily-reviews/` |
| Weekly | `templates/weekly-intelligence-report.md` | `vault/06-meta-intelligence/dashboards/weekly-reports/` |
| Monthly | `templates/monthly-review.md` | `vault/06-meta-intelligence/dashboards/monthly-reviews/` |
| Quarterly | `templates/quarterly-review.md` | `vault/06-meta-intelligence/dashboards/quarterly-reviews/` |

**Templater plugin:** Set the template folder to `templates/`.

**Homepage plugin:** Set `vault/06-meta-intelligence/dashboards/ceo-cockpit.md` as your vault homepage. This opens every time you launch Obsidian.

**QuickAdd plugin:** Create the following commands (one per row):

| Command Name | Template | Output Folder |
|---|---|---|
| New Signal | `templates/signal.md` | `vault/00-inbox/` |
| New Opportunity | `templates/opportunity-v2.md` | `vault/00-inbox/` |
| New Decision | `templates/decision-memo.md` | `vault/02-decisions/memos/` |
| New Forecast | `templates/forecast-v2.md` | `vault/02-decisions/forecasts/` |
| New Assumption | `templates/assumption-v2.md` | `vault/02-decisions/assumptions/` |
| New Risk | `templates/risk.md` | `vault/03-execution/risks/` |
| New Lesson | `templates/lesson.md` | `vault/04-learning/lessons/` |

### Step 3 — Choose Your AI Tool

The system is AI-tool agnostic. You can use Claude, GPT-4, Gemini, or any other assistant. The workflows and skill specs in `workflows/skills/` are written in plain markdown — paste them into any chat.

With Claude Desktop + MCP: the AI reads your vault directly. Skip the copy-paste steps in any workflow.

Without MCP: copy-paste the relevant note content into the chat alongside the workflow prompt.

---

## Part 3 — Daily Operating Rhythm

**Time investment: 20–30 minutes per day.**

### Morning (10 min)

1. Open Obsidian → homepage loads `ceo-cockpit.md` automatically
2. Scan the **Action Required** table at the top — anything due today?
3. Create today's daily review: `Ctrl+Shift+D` (or Periodic Notes → Today)
4. Triage the inbox:
   - Any raw items in `vault/00-inbox/`?
   - For each item: promote to `vault/01-intelligence/signals/` or delete
5. Set your 3 priorities for the day in the daily review

### During the Day

- **Capture first, refine later.** Any article, tweet, observation, or idea → drop it in `vault/00-inbox/` as a new Signal using QuickAdd
- **Link immediately.** When you create a signal, ask: does this connect to an open opportunity or active assumption? Add the link
- **Don't mix facts and opinions.** If you're not sure something is a fact, put it in the Evidence section of a note under "Supporting Evidence" with a confidence score

### End of Day (5 min)

- Mark the 3 priorities complete or carry forward in the daily review
- Capture any open question that needs research tomorrow
- If a decision was made informally today (in a call, in your head), open a Decision Memo and record it

---

## Part 4 — Weekly Operating Rhythm

**Time investment: 45–60 minutes every Monday.**

### Monday Morning

1. Create this week's intelligence report: Periodic Notes → This Week
2. The Dataview queries auto-populate. Review each section — don't skip the Forecast and Risk sections
3. Run the Chief of Staff agent to synthesize Section 7 (What Changed, Biggest Unknown, CEO Priorities):

```
You are the Chief of Staff. Today is [DATE].

Read the weekly intelligence report for [WEEK] from the vault.
Populate Section 7: What Changed, Biggest Unknown, and the 3 CEO priorities for next week.
Base your synthesis only on what is in the vault — signals, decisions, forecasts, risks added this week.
Do not invent data.
```

4. After reading the report, decide:
   - Which open decision needs to move forward this week?
   - Which opportunity deserves a scoring session?
   - Is any active assumption critically weak?

### Weekly Maintenance (15 min)

Run through these checks:

- [ ] Any forecast deadline passed? → Run `workflows/forecast-resolution.md`
- [ ] Any assumption review_date passed? → Open it, update evidence, update confidence
- [ ] Any risk level escalated? → Update impact/probability, add mitigation note
- [ ] Any initiative off track? → Update status, add blocker note

---

## Part 5 — The Decision Workflow

Use this every time you make a significant decision (anything with >$1K cost, >1 week of work, or strategic impact).

### Step 1 — Create the Decision Memo

QuickAdd → New Decision. Fill the frontmatter:
- `status: draft`
- `decision_readiness: research-needed`
- Link the opportunity it came from

### Step 2 — Build the Evidence Base

Run the Research skill with your AI assistant:

```
Read the research-skill.md from workflows/skills/.
Research: [TOPIC]
Depth: deep
Context: [paste relevant opportunity and assumption notes]

Produce: 3–5 signals. Separate facts from assumptions. Assess source quality.
```

Add the signals to `vault/00-inbox/`, then promote them.

### Step 3 — Create and Register Assumptions

For every premise the decision relies on, create an assumption note using `assumption-v2.md`.

Critical fields to set:
- `importance: high` if the decision fails without this being true
- `invalidation_risk: high` if there's real chance it's wrong
- `confidence_score: 3–5` for unvalidated assumptions (be honest)

Link the assumption back to the decision memo: add it to `related_assumptions`.

### Step 4 — Create a Forecast

Every material decision needs at least one forecast.

Use `forecast-v2.md`. Set:
- `question`: a specific, falsifiable question
- `deadline`: when you will know the answer
- `predicted_probability`: your honest estimate
- `resolution_criteria`: the observable event that resolves it

Link the forecast to the decision memo.

### Step 5 — Run Red Team

Run the Decision Challenge skill before finalizing:

```
Read decision-challenge-skill.md from workflows/skills/.
Challenge this decision: [paste decision memo]
Challenge depth: standard
```

Take the red team output seriously. If the Skeptic finds a critical assumption that you cannot defend, go back to Step 3.

### Step 6 — Move to Ready for Review

Set `status: ready-for-review` on the decision memo.

If composite evidence supports the decision, set `decision_readiness: ready-for-action`.

### Step 7 — Make the Decision

Write the actual decision in the Decision Memo. Don't hedge. Use one of:

- Proceed
- Monitor
- Reject
- Delay
- Run Experiment

If Proceed: immediately create an Initiative note and link it.

---

## Part 6 — The Opportunity Pipeline

### How to Score a New Opportunity

1. Capture it in `vault/00-inbox/` using `opportunity-v2.md`
2. Run the Opportunity skill:

```
Read opportunity-skill.md from workflows/skills/.
Evaluate this opportunity: [paste opportunity note]
Run advisor board: true
```

3. Record the composite_score in the frontmatter
4. Check the threshold:
   - Score ≥ 7.0 → Open Decision Memo immediately
   - Score 5.0–6.9 → Set review_date 2 weeks out, continue research
   - Score < 5.0 → Reject or archive

### Reading the Opportunity Dashboard

Open `vault/05-strategy/portfolio/opportunity-score.md` or the Opportunities section of the CEO Cockpit. The Dataview table ranks everything by composite_score automatically.

Focus your energy on the top 3 opportunities. The rest should be at "Monitor" or "Reject" status — don't let the pipeline bloat.

---

## Part 7 — Forecast Calibration

### Resolving a Forecast

When a forecast deadline arrives:

1. The Forecast Calibration Dashboard (`vault/06-meta-intelligence/dashboards/forecast-calibration-dashboard.md`) shows it in the "Overdue" table
2. Open the forecast note
3. Answer the resolution criteria: did it happen?
4. Set `actual_probability: 1` (yes) or `0` (no)
5. Calculate `brier_score = (predicted_probability - actual_probability)^2`
6. Set `status: resolved` and `resolution_date: today`
7. If `brier_score > 0.15`: create a lesson note about the calibration failure

### Reading Your Calibration Score

Open the Forecast Calibration Dashboard. Look at the "Avg Brier Score" column.

| Score | What it means |
|---|---|
| < 0.10 | You are well-calibrated. Trust your probability estimates. |
| 0.10–0.20 | Moderate bias. Check for overconfidence. |
| > 0.20 | Systematic bias. Run a Bias Audit. |

### If Calibration is Poor

Run the Calibration skill on your resolved forecasts:

```
Read calibration-skill.md from workflows/skills/.
Review scope: all-active
Force update: true

Identify: am I systematically overconfident or underconfident?
Which categories have the worst calibration?
```

Create a bias audit note in `vault/04-learning/bias-audits/`.

---

## Part 8 — Assumption Intelligence

### The Most Important Dashboard

`vault/06-meta-intelligence/dashboards/assumption-intelligence-dashboard.md`

Check this weekly. The critical section is **Invalidated Assumptions** — any decision that rests on a rejected assumption must be immediately reassessed.

### When an Assumption is Invalidated

1. Set the assumption to `status: rejected`, add `invalidation_date`
2. Open every note in `related_decisions`
3. For each linked decision: set `status: ready-for-review`
4. Run the Decision Challenge skill on each affected decision
5. Create a lesson note: "Assumption X was invalidated. Decisions that depended on it were..."

### Improving Weak Assumptions

For any assumption with `confidence_score ≤ 4`:

1. Ask: what is the cheapest experiment that would raise confidence by 3 points?
2. Fill the Validation Plan section
3. Set `review_date` to the experiment deadline
4. After the experiment: update evidence, recalculate confidence score

---

## Part 9 — Monthly Review

**Time investment: 90 minutes on the 1st of each month.**

1. Create the monthly review: Periodic Notes → This Month
2. Work through each section in order:
   - Section 1: Resolve any overdue forecasts
   - Section 2: Run bias detection checklist — honest self-assessment
   - Section 3: Re-rank the opportunity portfolio; reject anything stale
   - Section 4: Synthesize the top lesson pattern
3. Create this month's calibration entry in `vault/04-learning/calibration/`
4. Ask the Probability Analyst agent:

```
Read calibration-skill.md from workflows/skills/.
Review scope: this-month

Calculate my average Brier score for [MONTH].
Identify any systematic bias.
Recommend one specific change to my forecasting process.
```

---

## Part 10 — Quarterly Review

**Time investment: 2–3 hours at the start of each quarter.**

1. Create the quarterly review: Periodic Notes → This Quarter
2. Work through sections:
   - **Strategy:** Is each strategic theme still correct? Should any be retired?
   - **Bets:** Which bets are gaining conviction? Which should be exited?
   - **Resources:** Is capital/time allocated to your highest-score opportunities?
   - **Execution:** Which initiatives should be accelerated, paused, or killed?
3. Update `score_strategic_fit` on all active opportunities — strategic context changes quarterly

---

## Part 11 — Using the CEO Cockpit

The cockpit at `vault/06-meta-intelligence/dashboards/ceo-cockpit.md` is the daily dashboard. The Dataview queries are live — they update automatically as you add notes.

**How to read it efficiently:**

1. **Action Required** (top of cockpit) — always check this first. These are items with review dates in the next 3 days
2. **Intelligence Layer** — new signals and trends. Are any of these changing an active assumption?
3. **Decision Layer** — open decisions. Is anything stuck at `draft` for more than 2 weeks?
4. **Forecasting Layer** — forecasts due in 30 days. Which ones need probability updates?
5. **Execution Layer** — active initiatives and risks. Any initiative stalled?
6. **Learning Layer** — repeated failures are the most important row. If you've made the same mistake twice, make a rule
7. **Strategy Layer** — top opportunities ranked by composite_score. This is your priority allocation

---

## Part 12 — Working with AI Agents

### The Rule

Agents produce drafts. You approve, edit, and decide. Never let an agent make or record a final decision without your explicit sign-off.

### How to Invoke Any Skill

1. Open the skill file from `workflows/skills/`
2. Copy the entire skill spec
3. Paste it into your AI assistant as the first message
4. Follow it with the input content from your vault
5. Review the output
6. Paste accepted content into `vault/00-inbox/`
7. Promote it to the right layer after review

### Best Prompting Patterns

**For research:**
> "You are the Research Analyst. Follow research-skill.md. Research [TOPIC]. Use firecrawl MCP. Separate facts from assumptions."

**For decision review:**
> "You are the Red Team Advisor. Follow decision-challenge-skill.md. Challenge this decision. Be adversarial. Find the weakest assumption."

**For weekly synthesis:**
> "You are the Chief of Staff. Read all signals, opportunities, and decisions created this week from the vault. Summarize: what changed, what is the biggest unknown, and what are the top 3 priorities for next week."

**For forecast update:**
> "You are the Probability Analyst. Follow calibration-skill.md. Review my active forecasts. For each, check if new signals in the vault should change the probability estimate."

### What Agents Are Not For

- Making strategic bets on your behalf
- Deciding whether to invest capital or headcount
- Overriding the Red Team's concerns because they are inconvenient
- Inflating confidence scores to make a decision look better

---

## Part 13 — Common Mistakes to Avoid

**Skipping the assumption registration step.** If you don't register assumptions before deciding, you can't track which ones failed later. This breaks the learning loop.

**Using forecasts without deadlines.** A forecast without a deadline can never be resolved. Every forecast must have a specific date.

**Setting confidence scores too high too early.** Default to 4–6 for anything unvalidated. 7+ should require documented evidence.

**Letting the inbox accumulate.** If `vault/00-inbox/` has more than 20 items, the system is behind. Triage daily, even briefly.

**Only using the system for big decisions.** Small decisions compound too. A $500 experiment, a hiring conversation, a pricing change — log them. The lessons are often sharper.

**Ignoring the Skeptic.** The Skeptic advisor exists because you will naturally look for confirming evidence. Force a response from the Skeptic on every opportunity and decision before committing.

**Resolving forecasts as "close enough."** Use binary actual_probability: 1 or 0. If the resolution criteria were ambiguous, that is itself a lesson — write it down.

---

## Part 14 — File Naming Convention

```
vault/01-intelligence/signals/    YYYY-MM-DD Signal Name.md
vault/01-intelligence/trends/     YYYY-MM-DD Trend Name.md
vault/02-decisions/memos/         YYYY-MM-DD Decision — Short Name.md
vault/02-decisions/forecasts/     YYYY-MM-DD Forecast — Question.md
vault/02-decisions/assumptions/   Assumption — Statement.md
vault/03-execution/initiatives/   YYYY-MM-DD Initiative — Name.md
vault/04-learning/lessons/        Lesson — Topic.md
vault/04-learning/outcome-reviews/ YYYY-MM-DD Review — Decision Name.md
vault/05-strategy/bets/           Bet — Name.md
```

Dates are required on time-sensitive artifacts (signals, decisions, forecasts, initiatives, reviews). Evergreen artifacts (assumptions, lessons, bets) use descriptive names without dates.

---

## Part 15 — Phase 3 Migration Readiness

As your vault grows, maintain these habits to keep it migration-ready for Neo4j/FalkorDB (Phase 3):

- Every note has `type:` in frontmatter
- All `related_*` fields use exact note titles (not approximations)
- Every forecast has `brier_score` or is still `status: active`
- Every opportunity has `composite_score` calculated
- No orphan notes without at least one link

Run the migration readiness checklist in `docs/phase-3-migration-path.md` before any major architecture change.
