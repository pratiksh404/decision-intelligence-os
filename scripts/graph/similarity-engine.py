#!/usr/bin/env python3
"""
Decision Intelligence OS — Similarity Retrieval Engine
Phase 3 Implementation

Finds similar entities across the graph using metadata matching,
property scoring, and relationship overlap.

Usage:
    python3 scripts/graph/similarity-engine.py --entity DEC-2026-001 --type similar_decisions
    python3 scripts/graph/similarity-engine.py --entity OPP-2026-001 --type similar_opportunities
    python3 scripts/graph/similarity-engine.py --entity FRC-2026-001 --type similar_forecasts
    python3 scripts/graph/similarity-engine.py --entity OUT-2026-001 --type similar_failures
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict

GRAPH_EXPORT = Path(__file__).parent.parent.parent / "vault" / "06-meta-intelligence" / "graph" / "exports" / "graph-export.json"

QUERY_TYPE_CONFIG = {
    "similar_decisions": {
        "target_type": "decision",
        "match_fields": ["decision_type", "category", "reversibility"],
        "match_tags": True,
        "match_theme": True,
        "shared_neighbor_types": ["assumption", "mental-model"],
    },
    "similar_forecasts": {
        "target_type": "forecast",
        "match_fields": ["category"],
        "match_tags": True,
        "match_theme": True,
        "shared_neighbor_types": ["assumption", "decision"],
    },
    "similar_failures": {
        "target_type": "outcome",
        "filter": {"result": "failure"},
        "match_fields": ["related_initiative_type"],
        "match_tags": True,
        "shared_neighbor_types": ["risk", "assumption"],
    },
    "similar_opportunities": {
        "target_type": "opportunity",
        "match_fields": ["category", "market"],
        "match_tags": True,
        "match_theme": True,
        "shared_neighbor_types": ["trend", "assumption", "competitor"],
    },
    "relevant_lessons": {
        "target_type": "lesson",
        "match_fields": ["category"],
        "match_tags": True,
        "sort_by": "recurrence_count",
    },
}

def load_graph():
    data = json.loads(GRAPH_EXPORT.read_text())
    nodes = {n["id"]: n for n in data["nodes"]}
    neighbors = defaultdict(set)
    for e in data["edges"]:
        neighbors[e["source"]].add(e["target"])
        neighbors[e["target"]].add(e["source"])
    return nodes, dict(neighbors)

def jaccard(set_a: set, set_b: set) -> float:
    if not set_a and not set_b:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)

def score_similarity(query: dict, candidate: dict, neighbors: dict, config: dict) -> float:
    score = 0.0

    # 1. Field match (40%)
    match_fields = config.get("match_fields", [])
    if match_fields:
        field_hits = sum(
            1 for f in match_fields
            if query["properties"].get(f) and query["properties"].get(f) == candidate["properties"].get(f)
        )
        score += (field_hits / max(len(match_fields), 1)) * 0.40

    # 2. Tag overlap (20%)
    if config.get("match_tags"):
        q_tags = set(query.get("tags", []))
        c_tags = set(candidate.get("tags", []))
        score += jaccard(q_tags, c_tags) * 0.20

    # 3. Strategic theme match (10%)
    if config.get("match_theme"):
        q_theme = query["properties"].get("strategic_theme")
        c_theme = candidate["properties"].get("strategic_theme")
        if q_theme and q_theme == c_theme:
            score += 0.10

    # 4. Shared neighbors (30%)
    q_neighbors = set(neighbors.get(query["id"], set()))
    c_neighbors = set(neighbors.get(candidate["id"], set()))
    score += jaccard(q_neighbors, c_neighbors) * 0.30

    return round(score, 4)

def find_similar(entity_id: str, query_type: str, top_k: int = 5) -> dict:
    nodes, neighbors = load_graph()
    config = QUERY_TYPE_CONFIG.get(query_type, {})

    if entity_id not in nodes:
        return {"error": f"Entity {entity_id} not found in graph"}

    query_node = nodes[entity_id]
    target_type = config.get("target_type")
    filter_props = config.get("filter", {})

    candidates = [
        n for n in nodes.values()
        if n["type"] == target_type
        and n["id"] != entity_id
        and all(n["properties"].get(k) == v for k, v in filter_props.items())
    ]

    scored = []
    for c in candidates:
        sim = score_similarity(query_node, c, neighbors, config)
        if sim > 0.0:
            scored.append({
                "entity_id": c["id"],
                "entity_type": c["type"],
                "label": c["label"],
                "status": c["status"],
                "similarity_score": sim,
                "match_explanation": {
                    "shared_tags": list(set(query_node.get("tags", [])) & set(c.get("tags", []))),
                    "shared_neighbors": list(
                        set(neighbors.get(entity_id, set())) & set(neighbors.get(c["id"], set()))
                    )[:5],
                },
                "key_properties": {k: c["properties"].get(k) for k in config.get("match_fields", [])},
            })

    # Sort
    sort_field = config.get("sort_by")
    if sort_field:
        scored.sort(key=lambda x: x.get(sort_field, 0), reverse=True)
    else:
        scored.sort(key=lambda x: x["similarity_score"], reverse=True)

    return {
        "query_entity": entity_id,
        "query_label": query_node["label"],
        "query_type": query_type,
        "total_candidates": len(candidates),
        "results": scored[:top_k],
        "context_package": {
            "query_node": query_node,
            "similar_nodes": scored[:top_k],
            "summary_for_ai": (
                f"Query: {query_node['label']} ({entity_id}, {query_node['type']}). "
                f"Found {len(scored)} similar entities. "
                f"Top match: {scored[0]['label'] if scored else 'none'} "
                f"(similarity: {scored[0]['similarity_score'] if scored else 0})."
            )
        }
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decision Intelligence Similarity Engine")
    parser.add_argument("--entity", required=True)
    parser.add_argument("--type", required=True, choices=list(QUERY_TYPE_CONFIG.keys()))
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()

    result = find_similar(args.entity, args.type, args.top_k)
    print(json.dumps(result, indent=2))
