#!/bin/bash
# ============================================================
# Decision Intelligence OS — Graph Automation Scripts
# Phase 3 — Graph Extraction & Health Monitoring
# ============================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Use project venv if available, otherwise system python3
if [ -f "$PROJECT_ROOT/.venv/bin/python3" ]; then
  PYTHON="$PROJECT_ROOT/.venv/bin/python3"
else
  PYTHON="${PYTHON:-python3}"
fi


# ─── extract-graph ───────────────────────────────────────────
extract_graph() {
  echo "🔍 Running full graph extraction..."
  cd "$PROJECT_ROOT"
  $PYTHON scripts/graph/vault-extractor.py
}

# ─── validate-schema ─────────────────────────────────────────
validate_schema() {
  echo "✅ Running schema validation only..."
  cd "$PROJECT_ROOT"
  $PYTHON scripts/graph/vault-extractor.py --validate-only
}

# ─── trace-lineage ───────────────────────────────────────────
trace_lineage() {
  local entity_id="${1:?Usage: graph.sh trace-lineage ENTITY-ID [direction]}"
  local direction="${2:-both}"
  echo "🔗 Tracing lineage for $entity_id ($direction)..."
  cd "$PROJECT_ROOT"
  $PYTHON scripts/graph/lineage-tracer.py --entity "$entity_id" --direction "$direction" --output both
}

# ─── find-similar ────────────────────────────────────────────
find_similar() {
  local entity_id="${1:?Usage: graph.sh find-similar ENTITY-ID QUERY-TYPE}"
  local query_type="${2:?Provide query type: similar_decisions|similar_forecasts|similar_failures|similar_opportunities|relevant_lessons}"
  echo "🔎 Finding similar entities to $entity_id ($query_type)..."
  cd "$PROJECT_ROOT"
  $PYTHON scripts/graph/similarity-engine.py --entity "$entity_id" --type "$query_type"
}

# ─── health-report ───────────────────────────────────────────
health_report() {
  echo "📊 Generating graph health report..."
  cd "$PROJECT_ROOT"
  $PYTHON scripts/graph/vault-extractor.py
  cat vault/06-meta-intelligence/graph/diagnostics/diagnostics.json | python3 -c "
import json, sys
d = json.load(sys.stdin)
print(f\"\\n━━━ Graph Health Report ━━━\")
print(f\"Health Score: {d['graph_health_score']}/100 ({d['health_interpretation']})\")
print(f\"\\nIssues:\")
for issue, items in d['issues'].items():
    if items:
        print(f\"  ⚠  {issue}: {len(items)}\")
print(f\"\\nRecommendations:\")
for rec in d['recommendations']:
    print(f\"  → {rec}\")
"
}

# ─── export-neo4j ────────────────────────────────────────────
export_neo4j() {
  echo "📦 Exporting graph for Neo4j (CSV format)..."
  cd "$PROJECT_ROOT"
  $PYTHON scripts/graph/vault-extractor.py
  $PYTHON -c "
import json, csv
from pathlib import Path

nodes = json.loads(Path('vault/06-meta-intelligence/graph/exports/nodes.json').read_text())['nodes']
edges = json.loads(Path('vault/06-meta-intelligence/graph/exports/edges.json').read_text())['edges']

with open('vault/06-meta-intelligence/graph/exports/nodes.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['entity_id', 'entity_type', 'title', 'status', 'confidence_score', 'importance', 'owner', 'created', 'strategic_theme', 'tags'])
    for n in nodes:
        p = n.get('properties', {})
        w.writerow([n['id'], n['type'], n['label'], n['status'], p.get('confidence_score',''), p.get('importance',''), p.get('owner',''), p.get('created',''), p.get('strategic_theme',''), ';'.join(n.get('tags',[]))])

with open('vault/06-meta-intelligence/graph/exports/edges.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['source_id', 'target_id', 'relationship_type', 'strength', 'confidence', 'date_established'])
    for e in edges:
        p = e.get('properties', {})
        w.writerow([e['source'], e['target'], e['type'], p.get('strength',''), p.get('confidence',''), p.get('date_established','')])

print('CSV exports written: nodes.csv, edges.csv')
"
}

# ─── Dispatcher ──────────────────────────────────────────────
CMD="${1:-help}"
shift || true

case "$CMD" in
  extract)         extract_graph ;;
  validate)        validate_schema ;;
  lineage)         trace_lineage "$@" ;;
  similar)         find_similar "$@" ;;
  health)          health_report ;;
  neo4j-export)    export_neo4j ;;
  *)
    echo "Decision Intelligence OS — Graph CLI"
    echo ""
    echo "Usage: scripts/graph/graph.sh <command> [args]"
    echo ""
    echo "Commands:"
    echo "  extract              Run full vault extraction → nodes/edges/graph-export JSON"
    echo "  validate             Schema validation only (no file output)"
    echo "  lineage ENTITY [dir] Trace decision lineage (dir: upstream|downstream|both)"
    echo "  similar ENTITY TYPE  Find similar entities (TYPE: similar_decisions|similar_forecasts|similar_failures|similar_opportunities|relevant_lessons)"
    echo "  health               Generate and print graph health report"
    echo "  neo4j-export         Export nodes.csv + edges.csv for Neo4j import"
    ;;
esac
