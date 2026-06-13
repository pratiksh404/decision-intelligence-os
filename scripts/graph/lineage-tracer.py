#!/usr/bin/env python3
"""
Decision Intelligence OS — Decision Lineage Tracer
Phase 3 Implementation

Given any entity_id, traverses the full decision lineage
both upstream (toward originating signals) and downstream
(toward lessons and mental model improvements).

Usage:
    python3 scripts/graph/lineage-tracer.py --entity DEC-2026-001
    python3 scripts/graph/lineage-tracer.py --entity SIG-2026-007 --direction downstream
    python3 scripts/graph/lineage-tracer.py --entity OPP-2026-001 --direction both --output md
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict, deque
from datetime import datetime

GRAPH_EXPORT = Path(__file__).parent.parent.parent / "vault" / "06-meta-intelligence" / "graph" / "exports" / "graph-export.json"
OUTPUT_DIR   = Path(__file__).parent.parent.parent / "vault" / "06-meta-intelligence" / "graph" / "exports"

# Relationships that go "forward" in the intelligence chain
DOWNSTREAM_RELS = {"LEADS_TO", "GENERATES", "CREATES", "PRODUCES", "FORECASTS", "IMPROVES"}
# Relationships that go "backward" toward origins
UPSTREAM_RELS   = {"LEADS_TO", "DEPENDS_ON", "ASSUMES", "BELONGS_TO"}

MAX_HOPS = 8

def load_graph() -> tuple[dict, dict, dict]:
    """Load graph export and build adjacency structures."""
    if not GRAPH_EXPORT.exists():
        print("ERROR: graph-export.json not found. Run vault-extractor.py first.")
        exit(1)
    data = json.loads(GRAPH_EXPORT.read_text())
    nodes = {n["id"]: n for n in data["nodes"]}
    
    # Forward adjacency (source → [(target, rel_type)])
    forward = defaultdict(list)
    # Backward adjacency (target → [(source, rel_type)])
    backward = defaultdict(list)
    
    for e in data["edges"]:
        forward[e["source"]].append((e["target"], e["type"]))
        backward[e["target"]].append((e["source"], e["type"]))
    
    return nodes, dict(forward), dict(backward)

def bfs_traverse_lineage(
    start_id: str,
    forward: dict,
    backward: dict,
    direction: str,  # "upstream" or "downstream"
    max_hops: int,
    nodes: dict
) -> list[dict]:
    """BFS traversal for lineage tracing in a specified direction."""
    visited = set()
    queue = deque([(start_id, 0, None, None)])  # (id, hop, parent_id, rel_type)
    chain = []

    # Map of relationship directions for upstream vs downstream traversal
    # Upstream means going backward in the strategic chain (towards signals)
    # Downstream means going forward in the strategic chain (towards outcomes/lessons)
    
    # Relationships that point forward in time/logic: SIG -[LEADS_TO]-> TRD -[LEADS_TO]-> OPP -[LEADS_TO]-> DEC -[GENERATES]-> INI -[LEADS_TO]-> OUT -[GENERATES]-> LSN -[IMPROVES]-> MMD
    forward_pointing = {"LEADS_TO", "GENERATES", "CREATES", "PRODUCES", "FORECASTS", "IMPROVES", "INFLUENCES", "SUPPORTS"}
    
    # Relationships that point backward in logic (source depends on target): DEC -[ASSUMES]-> ASM, OPP -[DEPENDS_ON]-> ASM, DEC -[RELATES_TO]-> OPP
    backward_pointing = {"ASSUMES", "DEPENDS_ON", "RELATES_TO", "CONTRADICTS"}

    while queue:
        node_id, hop, parent_id, rel_type = queue.popleft()
        if node_id in visited or hop > max_hops:
            continue
        visited.add(node_id)

        node_data = nodes.get(node_id, {})
        chain.append({
            "entity_id": node_id,
            "entity_type": node_data.get("type", "unknown"),
            "label": node_data.get("label", node_id),
            "status": node_data.get("status"),
            "hop": hop,
            "from_entity": parent_id,
            "via_relationship": rel_type,
        })

        # Find neighbors based on semantic direction of edges
        neighbors = []
        
        if direction == "upstream":
            # 1. Follow incoming forward-pointing edges (e.g. TRD -[LEADS_TO]-> OPP, we go OPP -> TRD)
            for (source, rel) in backward.get(node_id, []):
                if rel in forward_pointing:
                    neighbors.append((source, rel))
            # 2. Follow outgoing backward-pointing edges (e.g. DEC -[ASSUMES]-> ASM, we go DEC -> ASM)
            for (target, rel) in forward.get(node_id, []):
                if rel in backward_pointing:
                    neighbors.append((target, rel))
                    
        elif direction == "downstream":
            # 1. Follow outgoing forward-pointing edges (e.g. DEC -[GENERATES]-> INI, we go DEC -> INI)
            for (target, rel) in forward.get(node_id, []):
                if rel in forward_pointing:
                    neighbors.append((target, rel))
            # 2. Follow incoming backward-pointing edges (e.g. DEC -[ASSUMES]-> ASM, if we are at ASM we can trace to DEC)
            for (source, rel) in backward.get(node_id, []):
                if rel in backward_pointing:
                    neighbors.append((source, rel))

        for (neighbor, rel) in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, hop + 1, node_id, rel))

    return chain

def trace_lineage(entity_id: str, direction: str = "both") -> dict:
    nodes, forward, backward = load_graph()
    
    if entity_id not in nodes:
        print(f"WARNING: Entity '{entity_id}' not found in graph. Run vault-extractor.py to update.")
    
    result = {
        "query_entity": entity_id,
        "query_type": nodes.get(entity_id, {}).get("type", "unknown"),
        "query_label": nodes.get(entity_id, {}).get("label", entity_id),
        "traced_at": datetime.now().isoformat(),
        "upstream_chain": [],
        "downstream_chain": [],
        "summary": {}
    }
    
    if direction in ("upstream", "both"):
        upstream = bfs_traverse_lineage(entity_id, forward, backward, "upstream", MAX_HOPS, nodes)
        result["upstream_chain"] = [u for u in upstream if u["hop"] > 0]
    
    if direction in ("downstream", "both"):
        downstream = bfs_traverse_lineage(entity_id, forward, backward, "downstream", MAX_HOPS, nodes)
        result["downstream_chain"] = [d for d in downstream if d["hop"] > 0]
    
    # Summary
    all_chain = result["upstream_chain"] + result["downstream_chain"]
    type_counts = defaultdict(int)
    for item in all_chain:
        type_counts[item["entity_type"]] += 1
    
    result["summary"] = {
        "total_upstream_nodes": len(result["upstream_chain"]),
        "total_downstream_nodes": len(result["downstream_chain"]),
        "entity_types_in_chain": dict(type_counts),
        "chain_depth_upstream": max((u["hop"] for u in result["upstream_chain"]), default=0),
        "chain_depth_downstream": max((d["hop"] for d in result["downstream_chain"]), default=0),
    }
    
    return result

def render_markdown(lineage: dict) -> str:
    lines = [
        f"# Decision Lineage: {lineage['query_label']}",
        f"",
        f"**Entity:** `{lineage['query_entity']}` ({lineage['query_type']})",
        f"**Traced:** {lineage['traced_at'][:10]}",
        f"",
        f"## Summary",
        f"- Upstream nodes: {lineage['summary']['total_upstream_nodes']}",
        f"- Downstream nodes: {lineage['summary']['total_downstream_nodes']}",
        f"- Entity types: {lineage['summary']['entity_types_in_chain']}",
        f"",
    ]
    
    if lineage["upstream_chain"]:
        lines.append("## Upstream Chain (Origins → This Entity)")
        lines.append("")
        for item in sorted(lineage["upstream_chain"], key=lambda x: -x["hop"]):
            indent = "  " * (item["hop"] - 1)
            rel = f"[{item['via_relationship']}]" if item["via_relationship"] else ""
            lines.append(f"{indent}- `{item['entity_id']}` ({item['entity_type']}) {rel} **{item['label']}**")
        lines.append("")
    
    if lineage["downstream_chain"]:
        lines.append("## Downstream Chain (This Entity → Outcomes)")
        lines.append("")
        for item in sorted(lineage["downstream_chain"], key=lambda x: x["hop"]):
            indent = "  " * (item["hop"] - 1)
            rel = f"[{item['via_relationship']}]" if item["via_relationship"] else ""
            lines.append(f"{indent}- `{item['entity_id']}` ({item['entity_type']}) {rel} **{item['label']}**")
    
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decision Intelligence Lineage Tracer")
    parser.add_argument("--entity", required=True, help="Entity ID to trace (e.g. DEC-2026-001)")
    parser.add_argument("--direction", choices=["upstream", "downstream", "both"], default="both")
    parser.add_argument("--output", choices=["json", "md", "both"], default="both")
    args = parser.parse_args()
    
    result = trace_lineage(args.entity, args.direction)
    
    if args.output in ("json", "both"):
        out_file = OUTPUT_DIR / f"lineage-{args.entity}.json"
        out_file.write_text(json.dumps(result, indent=2))
        print(f"JSON: {out_file}")
    
    if args.output in ("md", "both"):
        md = render_markdown(result)
        out_file = OUTPUT_DIR / f"lineage-{args.entity}.md"
        out_file.write_text(md)
        print(f"Markdown: {out_file}")
    
    print(f"\nLineage Summary for {args.entity}:")
    print(f"  ↑ Upstream:   {result['summary']['total_upstream_nodes']} nodes")
    print(f"  ↓ Downstream: {result['summary']['total_downstream_nodes']} nodes")
    print(f"  Types: {result['summary']['entity_types_in_chain']}")
