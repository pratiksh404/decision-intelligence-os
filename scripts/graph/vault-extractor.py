#!/usr/bin/env python3
"""
Decision Intelligence OS — Graph Extraction Engine
Phase 3 Implementation

Scans the Obsidian vault, extracts entity nodes and typed relationships
from YAML frontmatter, validates schema compliance, builds graph artifacts,
and produces health diagnostics.

Usage:
    python3 scripts/graph/vault-extractor.py
    python3 scripts/graph/vault-extractor.py --validate-only
    python3 scripts/graph/vault-extractor.py --entity DEC-2026-001

Outputs:
    vault/06-meta-intelligence/graph/exports/nodes.json
    vault/06-meta-intelligence/graph/exports/edges.json
    vault/06-meta-intelligence/graph/exports/graph-export.json
    vault/06-meta-intelligence/graph/diagnostics/diagnostics.json
"""

import os
import sys
import json
import re
import yaml
import argparse
from datetime import datetime, date
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher

# ─── Configuration ─────────────────────────────────────────────────────────────

VAULT_ROOT = Path(__file__).parent.parent.parent / "vault"
OUTPUT_DIR = VAULT_ROOT / "06-meta-intelligence" / "graph" / "exports"
DIAG_DIR   = VAULT_ROOT / "06-meta-intelligence" / "graph" / "diagnostics"
REGISTRY   = VAULT_ROOT / "06-meta-intelligence" / "graph" / "entity-registry.json"

SKIP_DIRS = {".obsidian", "00-inbox"}

# Required fields per entity type
REQUIRED_FIELDS = {
    "signal":                    ["entity_id", "entity_type", "title", "status", "source", "source_quality", "signal_date", "created", "owner"],
    "trend":                     ["entity_id", "entity_type", "title", "status", "direction", "created", "owner"],
    "competitor":                ["entity_id", "entity_type", "name", "status", "created", "owner"],
    "opportunity":               ["entity_id", "entity_type", "title", "status", "composite_score", "created", "owner"],
    "assumption":                ["entity_id", "entity_type", "title", "claim", "status", "invalidation_risk", "created", "owner"],
    "decision":                  ["entity_id", "entity_type", "title", "status", "decision_type", "created", "owner"],
    "forecast":                  ["entity_id", "entity_type", "question", "status", "predicted_probability", "deadline", "resolution_criteria", "created", "owner"],
    "initiative":                ["entity_id", "entity_type", "title", "status", "related_decision", "owner", "created"],
    "risk":                      ["entity_id", "entity_type", "title", "status", "severity", "probability", "impact", "owner", "created"],
    "outcome":                   ["entity_id", "entity_type", "title", "status", "result", "created", "owner"],
    "lesson":                    ["entity_id", "entity_type", "title", "statement", "status", "recurrence_count", "created", "owner"],
    "strategic-theme":           ["entity_id", "entity_type", "title", "status", "time_horizon", "created", "owner"],
    "strategic-bet":             ["entity_id", "entity_type", "title", "status", "conviction_level", "resources_committed", "created", "owner"],
    "kpi":                       ["entity_id", "entity_type", "title", "status", "metric", "target_value", "unit", "created", "owner"],
    "resource-allocation":       ["entity_id", "entity_type", "title", "status", "resource_type", "amount", "unit", "period", "created", "owner"],
    "advisor-review":            ["entity_id", "entity_type", "advisor_name", "subject_entity_id", "recommendation", "confidence", "created"],
    "experiment":                ["entity_id", "entity_type", "title", "hypothesis", "status", "start_date", "end_date", "owner", "created"],
    "evidence":                  ["entity_id", "entity_type", "title", "evidence_type", "strength", "source", "created", "owner"],
    "research-report":           ["entity_id", "entity_type", "title", "status", "scope", "created", "owner"],
    "weekly-intelligence-report":["entity_id", "entity_type", "title", "status", "week_ending", "created", "owner"],
    "bias-audit":                ["entity_id", "entity_type", "title", "status", "audit_period", "biases_identified", "created", "owner"],
    "calibration-record":        ["entity_id", "entity_type", "title", "status", "period", "total_forecasts", "resolved_forecasts", "average_brier_score", "created", "owner"],
    "mental-model":              ["entity_id", "entity_type", "title", "subtype", "status", "description", "core_question", "created", "owner"],
    "scenario":                  ["entity_id", "entity_type", "title", "parent_decision", "scenario_type", "status", "probability", "created", "owner"],
}

# Typed relationship field → relationship type mapping
RELATIONSHIP_FIELD_MAP = {
    "assumes":                     "ASSUMES",
    "related_assumptions":         "ASSUMES",
    "leads_to":                    "LEADS_TO",
    "related_trends":              "LEADS_TO",
    "generates":                   "GENERATES",
    "related_initiatives":         "GENERATES",
    "depends_on":                  "DEPENDS_ON",
    "depends_on_assumptions":      "DEPENDS_ON",
    "supports":                    "SUPPORTS",
    "supported_by":                "SUPPORTS",
    "contradicts":                 "CONTRADICTS",
    "validates":                   "VALIDATES",
    "invalidates":                 "INVALIDATES",
    "influences":                  "INFLUENCES",
    "related_decisions":           "RELATES_TO",
    "related_decision":            "RELATES_TO",
    "related_forecasts":           "RELATES_TO",
    "related_forecast":            "RELATES_TO",
    "related_opportunities":       "RELATES_TO",
    "related_opportunity":         "RELATES_TO",
    "related_competitors":         "RELATES_TO",
    "related_competitor":          "RELATES_TO",
    "related_lessons":             "RELATES_TO",
    "related_lesson":              "RELATES_TO",
    "related_signals":             "RELATES_TO",
    "related_signal":              "RELATES_TO",
    "related_trends":              "LEADS_TO",
    "related_trend":               "LEADS_TO",
    "related_kpis":                "TRACKS",
    "related_kpi":                 "TRACKS",
    "related_risk":                "RELATES_TO",
    "belongs_to":                  "BELONGS_TO",
    "strategic_theme":             "BELONGS_TO",
    "tracks":                      "TRACKS",
    "mitigates":                   "MITIGATES",
    "reviews":                     "REVIEWS",
    "forecasts":                   "FORECASTS",
    "causes":                      "CAUSES",
    "blocks":                      "BLOCKS",
    "improves":                    "IMPROVES",
    "mental_models_applied":       "INFLUENCES",
    "mental_model_updated":        "IMPROVES",
    "complementary_models":        "RELATES_TO",
    "contradicting_models":        "CONTRADICTS",
    "parent_decision":             "RELATES_TO",
    "assumptions_tested":          "VALIDATES",
    "leading_indicators":          "TRACKS",
}

# ─── Stage 1: Vault Scanner ─────────────────────────────────────────────────────

def scan_vault(vault_root: Path) -> list[Path]:
    """Recursively enumerate all .md files in vault, skipping excluded dirs."""
    md_files = []
    for root, dirs, files in os.walk(vault_root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".md"):
                md_files.append(Path(root) / f)
    return md_files

# ─── Stage 2: Frontmatter Parser ───────────────────────────────────────────────

def parse_frontmatter(filepath: Path) -> dict | None:
    """Extract YAML frontmatter from a markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return None
        parts = text.split("---", 2)
        if len(parts) < 3:
            return None
        fm = yaml.safe_load(parts[1])
        if not isinstance(fm, dict):
            return None
        fm["_file"] = str(filepath.relative_to(VAULT_ROOT))
        fm["_body"] = parts[2]
        return fm
    except Exception as e:
        return None

# ─── Stage 3: Link Extractor ───────────────────────────────────────────────────

WIKI_LINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]')
ENTITY_ID_RE = re.compile(r'^[A-Z]{2,4}-\d{4}-\d{3}$|^[A-Z]{2,4}-\d{3}$|^[A-Z]{2,4}-\d{4}-[A-Z]\d$|^[A-Z]{2,4}-\d{4}-W\d{2}$')

def extract_entity_id_from_link(link: str, registry: dict) -> str | None:
    """Try to resolve a wiki-link text to an entity_id."""
    link = link.strip()
    if ENTITY_ID_RE.match(link.split(" ")[0]):
        return link.split(" ")[0]
    # Search registry by title
    for eid, meta in registry.get("entities", {}).items():
        if meta.get("title", "").lower() == link.lower():
            return eid
    return None

def extract_relationships(fm: dict, registry: dict) -> list[dict]:
    """Extract all typed relationship edges from frontmatter fields."""
    edges = []
    source_id = fm.get("entity_id")
    if not source_id:
        return edges

    for field, rel_type in RELATIONSHIP_FIELD_MAP.items():
        value = fm.get(field)
        if not value:
            continue

        # Normalize to list
        if isinstance(value, str):
            targets = [value]
        elif isinstance(value, list):
            targets = value
        else:
            continue

        for target in targets:
            if not target:
                continue
            # Handle dict items (e.g., {id: "...", link: "[[...]]"})
            if isinstance(target, dict):
                target_id = target.get("id") or extract_entity_id_from_link(
                    target.get("link", "").strip("[]"), registry
                )
                props = {k: v for k, v in target.items() if k not in ("id", "link")}
            else:
                # Try direct ID, then wiki-link extraction
                target_str = str(target).strip()
                wiki_match = WIKI_LINK_RE.match(target_str)
                if wiki_match:
                    target_str = wiki_match.group(1)
                target_id = extract_entity_id_from_link(target_str, registry)
                props = {}

            if target_id and target_id != source_id:
                edges.append({
                    "id": f"E-{source_id}-{rel_type}-{target_id}",
                    "source": source_id,
                    "target": target_id,
                    "type": rel_type,
                    "properties": props,
                    "metadata": {
                        "extracted_from_field": field,
                        "validated": target_id in registry.get("entities", {})
                    }
                })
    return edges

# ─── Stage 4: Entity Validator ─────────────────────────────────────────────────

def validate_entity(fm: dict) -> dict:
    """Validate an entity against its schema. Returns validation report."""
    entity_type = fm.get("entity_type", "unknown")
    required = REQUIRED_FIELDS.get(entity_type, [])
    missing = [f for f in required if f not in fm or fm[f] is None or fm[f] == ""]
    present = len(required) - len(missing)
    completeness = round((present / max(len(required), 1)) * 100)

    return {
        "valid": len(missing) == 0,
        "missing_fields": missing,
        "completeness_score": completeness,
        "entity_type": entity_type,
        "entity_id": fm.get("entity_id"),
    }

# ─── Stage 5+: Graph Assembler ─────────────────────────────────────────────────

def build_node(fm: dict, validation: dict) -> dict:
    """Build a graph node from a parsed frontmatter dict."""
    excluded = {"_file", "_body", "tags"}
    props = {k: v for k, v in fm.items() if k not in excluded and not k.startswith("_")}
    return {
        "id": fm.get("entity_id", fm["_file"]),
        "type": fm.get("entity_type", "unknown"),
        "label": fm.get("title") or fm.get("name") or fm.get("question", "Untitled"),
        "status": fm.get("status"),
        "properties": props,
        "metadata": {
            "file_path": fm["_file"],
            "completeness_score": validation["completeness_score"],
            "last_extracted": date.today().isoformat(),
            "schema_valid": validation["valid"],
            "missing_fields": validation["missing_fields"],
        },
        "tags": fm.get("tags", []),
    }

# ─── Stage 8: Diagnostic Generator ────────────────────────────────────────────

def compute_health_score(diag: dict) -> int:
    score = 100
    score -= len(diag["orphan_nodes"]) * 2
    score -= len(diag["broken_links"]) * 3
    score -= len(diag["duplicate_candidates"]) * 5
    score -= len(diag["unvalidated_critical_assumptions"]) * 4
    score -= len(diag["disconnected_decisions"]) * 3
    score -= len(diag["stale_forecasts"]) * 2
    score -= len(diag["missing_outcomes"]) * 2
    score -= len(diag["missing_lessons"]) * 1
    score -= len(diag["schema_violations"]) * 2
    return max(0, min(100, score))

# Prefix mapping for automatic ID generation
TYPE_PREFIX_MAP = {
    "signal": "SIG",
    "trend": "TRD",
    "competitor": "CMP",
    "opportunity": "OPP",
    "assumption": "ASM",
    "decision": "DEC",
    "forecast": "FRC",
    "initiative": "INI",
    "risk": "RSK",
    "outcome": "OUT",
    "lesson": "LSN",
    "strategic-theme": "STH",
    "strategic-bet": "BET",
    "kpi": "KPI",
    "resource-allocation": "RES",
    "advisor-review": "ADV",
    "experiment": "EXP",
    "evidence": "EVD",
    "research-report": "RPT",
    "weekly-intelligence-report": "WIR",
    "bias-audit": "BAU",
    "calibration-record": "CAL",
    "mental-model": "MMD",
    "scenario": "SCE",
}

def generate_entity_id(entity_type: str, created_date: str, registry: dict) -> str:
    """Generate a unique sequential entity ID based on type and creation date."""
    prefix = TYPE_PREFIX_MAP.get(entity_type)
    if not prefix:
        raise ValueError(f"Unknown entity type for ID generation: {entity_type}")

    try:
        date_obj = datetime.strptime(created_date, "%Y-%m-%d")
    except ValueError:
        date_obj = datetime.now()
    year = str(date_obj.year)

    if prefix == "WIR":
        # ISO week
        week = date_obj.isocalendar()[1]
        return f"WIR-{year}-W{week:02d}"
    elif prefix == "CAL":
        # Quarter
        quarter = (date_obj.month - 1) // 3 + 1
        return f"CAL-{year}-Q{quarter}"
    elif prefix in ("CMP", "STH", "MMD"):
        # Canonical counters (no year)
        counters = registry.setdefault("id_counters", {}).setdefault(prefix, {})
        counter = counters.get("canonical", 0) + 1
        counters["canonical"] = counter
        return f"{prefix}-{counter:03d}"
    else:
        # Year-based counters
        counters = registry.setdefault("id_counters", {}).setdefault(prefix, {})
        counter = counters.get(year, 0) + 1
        counters[year] = counter
        return f"{prefix}-{year}-{counter:03d}"

def save_frontmatter(filepath: Path, fm: dict, body: str):
    """Save updated frontmatter back to a markdown file, retaining body content."""
    clean_fm = {k: v for k, v in fm.items() if not k.startswith("_")}
    yaml_str = yaml.dump(clean_fm, sort_keys=False, default_flow_style=False, allow_unicode=True)
    filepath.write_text(f"---\n{yaml_str}---\n{body}", encoding="utf-8")

# ─── Main Extraction Pipeline ──────────────────────────────────────────────────

def run_extraction(validate_only: bool = False, target_entity: str | None = None):
    print(f"[Phase 3 Extraction] Starting vault scan: {VAULT_ROOT}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DIAG_DIR.mkdir(parents=True, exist_ok=True)

    # Load registry
    registry = json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {"entities": {}, "id_counters": {}}
    if "id_counters" not in registry:
        registry["id_counters"] = {}
    if "entities" not in registry:
        registry["entities"] = {}

    # Stage 1: Scan
    files = scan_vault(VAULT_ROOT)
    print(f"  Found {len(files)} markdown files")

    # Pre-scan files to automatically assign IDs if missing
    for filepath in files:
        fm = parse_frontmatter(filepath)
        if not fm or "entity_type" not in fm:
            continue
        
        entity_type = fm["entity_type"]
        entity_id = fm.get("entity_id")
        
        if not entity_id:
            created_date = fm.get("created")
            if not created_date:
                created_date = date.today().isoformat()
                fm["created"] = created_date
            
            # Generate new ID
            new_id = generate_entity_id(entity_type, created_date, registry)
            fm["entity_id"] = new_id
            
            # Save back to file
            body = fm.get("_body", "")
            save_frontmatter(filepath, fm, body)
            print(f"  [Auto-ID] Assigned ID {new_id} to {filepath.name}")
        else:
            # Sync counters in registry if manual ID is higher
            prefix = TYPE_PREFIX_MAP.get(entity_type)
            if prefix:
                match_canonical = re.match(rf"^{prefix}-(\d{{3}})$", entity_id)
                if match_canonical:
                    val = int(match_canonical.group(1))
                    counters = registry.setdefault("id_counters", {}).setdefault(prefix, {})
                    counters["canonical"] = max(counters.get("canonical", 0), val)
                else:
                    match_year = re.match(rf"^{prefix}-(\d{{4}})-(\d{{3}})$", entity_id)
                    if match_year:
                        year = match_year.group(1)
                        val = int(match_year.group(2))
                        counters = registry.setdefault("id_counters", {}).setdefault(prefix, {})
                        counters[year] = max(counters.get(year, 0), val)

    nodes = []
    edges = []
    node_ids = set()
    schema_violations = []
    all_entity_ids = set(registry.get("entities", {}).keys())

    # Stage 2-5: Parse, validate, extract
    for filepath in files:
        fm = parse_frontmatter(filepath)
        if not fm or "entity_type" not in fm:
            continue
        if not fm.get("entity_id"):
            schema_violations.append(f"Missing entity_id: {filepath.relative_to(VAULT_ROOT)}")
            continue

        if target_entity and fm.get("entity_id") != target_entity:
            continue

        validation = validate_entity(fm)
        if not validation["valid"]:
            schema_violations.append(
                f"{fm.get('entity_id')}: missing {validation['missing_fields']}"
            )

        node = build_node(fm, validation)
        nodes.append(node)
        node_ids.add(node["id"])
        all_entity_ids.add(node["id"])

        file_edges = extract_relationships(fm, registry)
        edges.extend(file_edges)

    if validate_only:
        print(f"  Validation complete. {len(schema_violations)} violations found.")
        for v in schema_violations:
            print(f"  ⚠ {v}")
        return

    # Stage 6: Duplicate detection (fuzzy matching)
    duplicate_candidates = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            n1 = nodes[i]
            n2 = nodes[j]
            t1 = n1["label"].lower().strip()
            t2 = n2["label"].lower().strip()
            sim = SequenceMatcher(None, t1, t2).ratio()
            if sim >= 0.8:
                duplicate_candidates.append({
                    "existing": n1["id"],
                    "candidate": n2["id"],
                    "similarity": round(sim, 2),
                    "titles": [n1["label"], n2["label"]]
                })

    # Stage 7: Diagnostics
    referenced_targets = {e["target"] for e in edges}
    referenced_sources = {e["source"] for e in edges}
    all_connected = referenced_targets | referenced_sources
    orphan_nodes = [n["id"] for n in nodes if n["id"] not in all_connected]

    broken_links = [
        f"{e['source']} → {e['target']} (not found)"
        for e in edges if e["target"] not in node_ids
    ]

    decisions = [n for n in nodes if n["type"] == "decision"]
    decision_ids = {n["id"] for n in decisions}
    decision_assumption_sources = {e["source"] for e in edges if e["type"] == "ASSUMES" and e["source"] in decision_ids}
    disconnected_decisions = [n["id"] for n in decisions if n["id"] not in decision_assumption_sources]

    today_str = date.today().isoformat()
    stale_forecasts = [
        n["id"] for n in nodes
        if n["type"] == "forecast"
        and n.get("status") == "active"
        and str(n["properties"].get("deadline", "9999-99-99")) < today_str
    ]

    assumptions = [n for n in nodes if n["type"] == "assumption"]
    unvalidated_critical = [
        n["id"] for n in assumptions
        if n["properties"].get("status") == "unvalidated"
        and n["properties"].get("invalidation_risk") == "critical"
    ]

    initiatives = [n for n in nodes if n["type"] == "initiative"]
    initiative_ids = {n["id"] for n in initiatives}
    completed_initiatives = {n["id"] for n in initiatives if n.get("status") == "completed"}
    outcomes_from = {e["source"] for e in edges if e["type"] == "LEADS_TO" and e["target"] not in initiative_ids}
    missing_outcomes = list(completed_initiatives - outcomes_from)

    outcomes = [n for n in nodes if n["type"] == "outcome"]
    outcome_ids = {n["id"] for n in outcomes}
    lesson_sources = {e["source"] for e in edges if e["type"] == "GENERATES" and e["target"] not in outcome_ids}
    missing_lessons = list(outcome_ids - lesson_sources)

    # Re-use duplicate_candidates list computed during Stage 6

    node_type_counts = defaultdict(int)
    for n in nodes:
        node_type_counts[n["type"]] += 1

    edge_type_counts = defaultdict(int)
    for e in edges:
        edge_type_counts[e["type"]] += 1

    diag = {
        "orphan_nodes": orphan_nodes,
        "broken_links": broken_links,
        "duplicate_candidates": duplicate_candidates,
        "unvalidated_critical_assumptions": unvalidated_critical,
        "disconnected_decisions": disconnected_decisions,
        "stale_forecasts": stale_forecasts,
        "missing_outcomes": missing_outcomes,
        "missing_lessons": missing_lessons,
        "schema_violations": schema_violations,
    }
    health_score = compute_health_score(diag)

    diag_output = {
        "generated_at": datetime.now().isoformat(),
        "graph_health_score": health_score,
        "health_interpretation": (
            "Excellent" if health_score >= 90 else
            "Good" if health_score >= 75 else
            "Fair" if health_score >= 60 else
            "Poor" if health_score >= 40 else "Critical"
        ),
        "issues": diag,
        "recommendations": _build_recommendations(diag),
    }

    # Stage 7: Output
    nodes_out = {
        "generated_at": datetime.now().isoformat(),
        "total_nodes": len(nodes),
        "node_type_counts": dict(node_type_counts),
        "nodes": nodes
    }

    edges_out = {
        "generated_at": datetime.now().isoformat(),
        "total_edges": len(edges),
        "edge_type_counts": dict(edge_type_counts),
        "edges": edges
    }

    graph_export = {
        "schema_version": "3.0",
        "generated_at": datetime.now().isoformat(),
        "vault_path": str(VAULT_ROOT),
        "statistics": {
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "node_types": dict(node_type_counts),
            "edge_types": dict(edge_type_counts),
            "orphan_nodes": len(orphan_nodes),
            "broken_links": len(broken_links),
            "graph_health_score": health_score,
        },
        "nodes": nodes,
        "edges": edges,
    }

    (OUTPUT_DIR / "nodes.json").write_text(json.dumps(nodes_out, indent=2, default=str))
    (OUTPUT_DIR / "edges.json").write_text(json.dumps(edges_out, indent=2, default=str))
    (OUTPUT_DIR / "graph-export.json").write_text(json.dumps(graph_export, indent=2, default=str))
    (DIAG_DIR / "diagnostics.json").write_text(json.dumps(diag_output, indent=2, default=str))

    # Save updated registry back to entity-registry.json
    if not validate_only:
        current_registry_entities = {}
        for node in nodes:
            eid = node["id"]
            props = node["properties"]
            title = node["label"]
            file_path = node["metadata"]["file_path"]
            current_registry_entities[eid] = {
                "type": node["type"],
                "subtype": props.get("subtype") or props.get("category") or "",
                "title": title,
                "file": file_path,
                "status": node["status"],
                "created": props.get("created") or date.today().isoformat()
            }
        registry["entities"] = current_registry_entities
        registry["total_entities"] = len(nodes)
        registry["last_updated"] = date.today().isoformat()
        REGISTRY.write_text(json.dumps(registry, indent=2, default=str), encoding="utf-8")
        print(f"  Updated entity registry successfully: {REGISTRY}")

    print(f"\n✅ Extraction complete")
    print(f"   Nodes: {len(nodes)} | Edges: {len(edges)}")
    print(f"   Health Score: {health_score}/100 ({diag_output['health_interpretation']})")
    print(f"   Orphans: {len(orphan_nodes)} | Broken links: {len(broken_links)} | Schema violations: {len(schema_violations)}")
    print(f"\n   Output: {OUTPUT_DIR}")
    print(f"   Diagnostics: {DIAG_DIR}")

def _build_recommendations(diag: dict) -> list[str]:
    recs = []
    if diag["schema_violations"]:
        recs.append(f"Fix {len(diag['schema_violations'])} schema violations (missing required fields)")
    if diag["broken_links"]:
        recs.append(f"Repair {len(diag['broken_links'])} broken entity links")
    if diag["orphan_nodes"]:
        recs.append(f"Connect or archive {len(diag['orphan_nodes'])} orphan nodes")
    if diag["unvalidated_critical_assumptions"]:
        recs.append(f"URGENT: Validate {len(diag['unvalidated_critical_assumptions'])} critical unvalidated assumptions")
    if diag["disconnected_decisions"]:
        recs.append(f"Add ASSUMES relationships to {len(diag['disconnected_decisions'])} decisions missing assumption links")
    if diag["stale_forecasts"]:
        recs.append(f"Resolve {len(diag['stale_forecasts'])} forecasts past their deadline")
    if diag["missing_outcomes"]:
        recs.append(f"Create Outcome nodes for {len(diag['missing_outcomes'])} completed initiatives")
    if diag["missing_lessons"]:
        recs.append(f"Extract lessons from {len(diag['missing_lessons'])} outcomes with no lesson generated")
    return recs

# ─── CLI Entry Point ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decision Intelligence OS — Graph Extractor")
    parser.add_argument("--validate-only", action="store_true", help="Run schema validation only, no output files")
    parser.add_argument("--entity", type=str, help="Extract a single entity by entity_id")
    args = parser.parse_args()
    run_extraction(validate_only=args.validate_only, target_entity=args.entity)
