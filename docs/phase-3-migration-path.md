# Phase 3 Migration Path — Future Readiness Architecture

> **Status:** Documentation only. Phase 3 is not implemented.
> **Purpose:** Ensure Phase 2 architecture is forward-compatible with graph databases, multi-agent coordination, and simulation.

---

## Phase 2 → Phase 3 Migration Map

| Phase 2 Artifact | Phase 3 Equivalent | Migration Notes |
|---|---|---|
| Obsidian Dataview queries | Neo4j / FalkorDB Cypher queries | Frontmatter maps 1:1 to node properties |
| YAML frontmatter links | Graph edges (typed relationships) | All `related_*` fields become edge types |
| `templates/*.md` | Graph node schema | Each type = node label |
| `vault/` flat files | Graph node store | Files become nodes; links become edges |
| MCP obsidian server | Graph database MCP adapter | Same interface, different backend |
| Weekly intelligence report | GraphRAG retrieval query | Dataview queries → graph traversal |
| Advisor prompts | Agent nodes with memory | Same skills, persistent agent state |
| Composite opportunity score | Portfolio optimization solver | Same formula, applied to full graph |

---

## Phase 2 Architecture Choices That Enable Phase 3

### 1. Strict Frontmatter Schema
Every note has typed `type:`, `status:`, and `related_*` fields.
This maps directly to graph node labels and edge types with zero transformation.

### 2. Explicit Relationship Fields
`related_decisions`, `related_assumptions`, `related_forecasts`, `related_initiatives` are all explicit arrays — not just in-body wikilinks.
Graph edges can be created from these arrays programmatically.

### 3. Typed Status Transitions
Status transitions follow a state machine (see `operating-system/metadata-schema.md`).
This maps to temporal graph edges and enables event sourcing.

### 4. Brier Score on Every Forecast
Calibration data is structured and queryable now.
In Phase 3, this feeds the Portfolio Optimization solver as a probability input.

### 5. Composite Opportunity Score Formula
The 6-factor weighted formula is standardized in `vault/05-strategy/portfolio/opportunity-score.md`.
In Phase 3, this becomes a graph algorithm applied across all opportunities with live data.

---

## Phase 3 Target Architecture

```
Multi-Agent Coordination Layer
    ↓
GraphRAG Retrieval
    ↓
FalkorDB / Neo4j (Knowledge Graph)
    ↓
Decision Intelligence OS Data (migrated from Obsidian vault)
```

### Graph Node Types (from current types)
```cypher
(:Signal), (:Trend), (:Competitor)
(:Opportunity), (:Assumption), (:Decision), (:Forecast)
(:Initiative), (:KPI), (:Risk)
(:OutcomeReview), (:Lesson), (:Calibration), (:BiasAudit)
(:StrategicTheme), (:StrategicBet), (:ResourceAllocation)
```

### Graph Edge Types (from current related_* fields)
```cypher
(:Signal)-[:VALIDATES]->(:Trend)
(:Trend)-[:SUPPORTS]->(:Opportunity)
(:Opportunity)-[:DEPENDS_ON]->(:Assumption)
(:Decision)-[:BASED_ON]->(:Assumption)
(:Decision)-[:PREDICTS]->(:Forecast)
(:Decision)-[:SPAWNS]->(:Initiative)
(:Initiative)-[:MEASURED_BY]->(:KPI)
(:Initiative)-[:EXPOSES]->(:Risk)
(:Forecast)-[:RESOLVED_IN]->(:OutcomeReview)
(:OutcomeReview)-[:PRODUCES]->(:Lesson)
```

---

## Migration Checklist (Phase 3 Readiness)

Run this checklist before initiating Phase 3:

- [ ] All notes have `type:` in frontmatter (validates node label)
- [ ] All notes have `status:` in frontmatter (validates state machine)
- [ ] All `related_*` fields use full note names (not bare text)
- [ ] All forecasts have `brier_score` populated or `status: active`
- [ ] All opportunities have `composite_score` populated
- [ ] No orphan notes (notes with no `related_*` links and no `type:`)
- [ ] Git history is clean (provides audit trail for temporal graph)

## Migration Script Interface (to be built in Phase 3)

```python
# Interface contract — implementation deferred to Phase 3
def migrate_vault_to_graph(vault_path: str, graph_db_uri: str):
    """
    Reads all markdown files in vault_path.
    Creates graph nodes from frontmatter.
    Creates graph edges from related_* fields.
    Returns migration summary: nodes created, edges created, orphans found.
    """
    pass
```

---

## Multi-Agent Coordination (Phase 3 Design)

Phase 2 advisors are invoked sequentially by the human.
Phase 3 introduces a coordinator that routes tasks automatically:

```
CEO Query
    ↓
Coordinator Agent
    ├── Research Analyst (if new signal needed)
    ├── Probability Analyst (if forecast update needed)
    ├── Red Team Advisor (if decision pending)
    ├── Portfolio Manager (if opportunity scored)
    └── Learning Advisor (if outcome to process)
         ↓
    Synthesized Response → Vault Update
```

Phase 2 skill specs in `workflows/skills/` are the exact input contracts for Phase 3 agent nodes.
No changes required to skill specs for Phase 3 adoption.

---

## Scenario Simulation (Phase 3)

Phase 2 scenario analysis is manual (written in notes).
Phase 3 will run Monte Carlo simulations against the graph.

Phase 2 preparation:
- Every forecast has `scenario_analysis` section with Base / Best / Worst case probabilities
- Every opportunity has advisor board analysis as structured text
- These become simulation seeds in Phase 3

---

## GraphRAG Retrieval (Phase 3)

Phase 2: Dataview queries read flat markdown files.
Phase 3: GraphRAG traverses the knowledge graph to retrieve multi-hop context.

Example Phase 3 query (equivalent to current weekly report):
```
MATCH (d:Decision {status: "monitoring"})-[:BASED_ON]->(a:Assumption)
WHERE a.confidence_score < 5
RETURN d.title, a.title, a.confidence_score
ORDER BY a.confidence_score ASC
```

The metadata structure designed in Phase 2 makes this query possible without schema changes.
