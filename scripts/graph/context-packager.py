#!/usr/bin/env python3
"""
Decision Intelligence OS — GraphRAG Context Packager
Phase 4 Implementation

Performs a hybrid search (TF-IDF vector similarity + structural k-hop graph traversal)
over the Decision Graph to build structured, token-efficient Markdown Context Packages.
These packages are injected directly into LLM prompts for strategic reasoning.

Usage:
    python3 scripts/graph/context-packager.py --query "willingness to pay for privacy" --hops 1
    python3 scripts/graph/context-packager.py --query "competitor product launch" --hops 2 --limit 5
"""

import os
import json
import math
import re
import argparse
from pathlib import Path
from collections import Counter, defaultdict

PROJECT_ROOT = Path(__file__).parent.parent.parent
GRAPH_EXPORT = PROJECT_ROOT / "vault" / "06-meta-intelligence" / "graph" / "exports" / "graph-export.json"
OUTPUT_DIR = PROJECT_ROOT / "vault" / "06-meta-intelligence" / "graph" / "exports"

# ─── TF-IDF / Vector Search Utils ─────────────────────────────────────────────

def clean_text(text: str) -> list[str]:
    """Tokenize and clean text into lowercase words."""
    return re.findall(r"\w+", text.lower())

def compute_cosine_similarity(vec1: dict, vec2: dict) -> float:
    """Calculate Cosine Similarity between two term-frequency dict vectors."""
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    return numerator / denominator if denominator else 0.0

class VectorRanker:
    """Simple local TF-IDF semantic database."""
    def __init__(self, idf=None):
        self.documents = []
        self.doc_vectors = []
        self.idf = idf or {}

    def fit_and_add(self, documents: list[dict]):
        self.documents = documents
        all_tokens = []
        doc_tokens = []
        for doc in documents:
            tokens = clean_text(doc["text"])
            doc_tokens.append(tokens)
            all_tokens.extend(set(tokens))
            
        doc_count = len(documents)
        term_df = Counter(all_tokens)
        
        # Compute IDF
        for term, df in term_df.items():
            self.idf[term] = math.log((1 + doc_count) / (1 + df)) + 1
            
        # Compute TF-IDF vectors
        for tokens in doc_tokens:
            tf = Counter(tokens)
            vector = {term: count * self.idf.get(term, 0.0) for term, count in tf.items()}
            self.doc_vectors.append(vector)

    def query(self, query_text: str, top_k: int = 5) -> list[dict]:
        query_tokens = clean_text(query_text)
        query_tf = Counter(query_tokens)
        query_vector = {term: count * self.idf.get(term, 0.0) for term, count in query_tf.items()}
            
        results = []
        for idx, doc_vector in enumerate(self.doc_vectors):
            sim = compute_cosine_similarity(query_vector, doc_vector)
            if sim > 0:
                results.append({
                    "score": round(sim, 4),
                    "node": self.documents[idx]["node"]
                })
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

# ─── Graph Traverser ─────────────────────────────────────────────────────────

def build_node_text(node: dict) -> str:
    """Compile structured metadata into a rich text block for embedding."""
    props = node.get("properties", {})
    desc = props.get("description") or props.get("claim") or props.get("question") or props.get("statement") or ""
    rationale = props.get("allocation_rationale") or props.get("mitigation_plan") or props.get("resolution_criteria") or ""
    tags = ", ".join(node.get("tags", []))
    
    text = f"ID: {node['id']}. Type: {node['type']}. Title: {node['label']}. Status: {node.get('status', 'unknown')}. "
    if desc:
        text += f"Description: {desc}. "
    if rationale:
        text += f"Rationale/Details: {rationale}. "
    if tags:
        text += f"Tags: {tags}. "
    return text

class GraphRAGEngine:
    def __init__(self, graph_data: dict):
        self.nodes = {n["id"]: n for n in graph_data.get("nodes", [])}
        self.edges = graph_data.get("edges", [])
        
        # Build adjacency maps
        self.adjacency = defaultdict(list)
        for e in self.edges:
            self.adjacency[e["source"]].append({
                "target": e["target"],
                "type": e["type"],
                "direction": "outgoing",
                "properties": e.get("properties", {})
            })
            self.adjacency[e["target"]].append({
                "target": e["source"],
                "type": e["type"],
                "direction": "incoming",
                "properties": e.get("properties", {})
            })
            
        # Fit vector ranker
        self.ranker = VectorRanker()
        docs = []
        for node in self.nodes.values():
            docs.append({
                "node": node,
                "text": node.get("embedding_ready", {}).get("text_for_embedding") or build_node_text(node)
            })
        self.ranker.fit_and_add(docs)

    def retrieve_context(self, query: str, max_hops: int = 1, limit: int = 5) -> dict:
        """Perform hybrid search: semantic retrieval + k-hop graph traversal."""
        semantic_hits = self.ranker.query(query, top_k=limit)
        
        retrieved_ids = set()
        semantic_nodes = []
        
        for hit in semantic_hits:
            node = hit["node"]
            semantic_nodes.append({
                "node": node,
                "score": hit["score"]
            })
            retrieved_ids.add(node["id"])
            
        # Traverse neighbors (k-Hops)
        adjacent_entities = []
        current_layer = set(retrieved_ids)
        visited = set(retrieved_ids)
        
        for hop in range(1, max_hops + 1):
            next_layer = set()
            for node_id in current_layer:
                neighbors = self.adjacency.get(node_id, [])
                for n in neighbors:
                    target_id = n["target"]
                    if target_id not in visited:
                        visited.add(target_id)
                        next_layer.add(target_id)
                        
                        target_node = self.nodes.get(target_id)
                        if target_node:
                            adjacent_entities.append({
                                "node": target_node,
                                "hop_reached": hop,
                                "relation_type": n["type"],
                                "direction": n["direction"],
                                "connected_to": node_id
                            })
            current_layer = next_layer
            
        return {
            "query": query,
            "semantic_matches": semantic_nodes,
            "adjacent_context": adjacent_entities
        }

# ─── Context Assembly Formatter ──────────────────────────────────────────────

def format_node_markdown(node: dict) -> str:
    """Format a node's properties and tags cleanly in Markdown."""
    props = node.get("properties", {})
    lines = [f"### [{node['id']}] {node['label']} ({node['type'].capitalize()})"]
    lines.append(f"- **Status:** {node.get('status', 'unknown')}")
    
    # Extract primary fields based on entity type
    if node["type"] == "assumption":
        lines.append(f"- **Claim:** {props.get('claim', '')}")
        lines.append(f"- **Invalidation Risk:** {props.get('invalidation_risk', 'unknown')}")
        lines.append(f"- **Evidence Status:** {props.get('evidence_status', 'none')}")
    elif node["type"] == "forecast":
        lines.append(f"- **Question:** {props.get('question', '')}")
        lines.append(f"- **Predicted Probability:** {props.get('predicted_probability', 'unknown')}")
        lines.append(f"- **Deadline:** {props.get('deadline', '')}")
    elif node["type"] == "decision":
        lines.append(f"- **Decision Type:** {props.get('decision_type', 'unknown')}")
        lines.append(f"- **Reversibility:** {props.get('reversibility', 'unknown')}")
    elif node["type"] == "risk":
        lines.append(f"- **Severity:** {props.get('severity', 'unknown')} | **Impact:** {props.get('impact', 'unknown')}")
        lines.append(f"- **Mitigation Plan:** {props.get('mitigation_plan', 'none')}")
    elif node["type"] == "lesson":
        lines.append(f"- **Statement:** {props.get('statement', '')}")
        lines.append(f"- **Recurrence Count:** {props.get('recurrence_count', 1)}")
    elif node["type"] == "outcome":
        lines.append(f"- **Result:** {props.get('result', 'unknown')}")
        
    # Standard tags & file reference
    tags = node.get("tags", [])
    if tags:
        lines.append(f"- **Tags:** {', '.join(tags)}")
    lines.append(f"- **Source File:** `[[{node['metadata']['file_path']}]]`")
    return "\n".join(lines)

def compile_context_package(context_data: dict) -> str:
    """Compile retrieved results into a structured strategic context package."""
    md = []
    md.append("# GraphRAG Strategic Context Package")
    md.append(f"**Query:** \"{context_data['query']}\"")
    md.append("")
    md.append("> [!NOTE]")
    md.append("> This package contains semantically retrieved business intelligence entities and their structural graph dependencies.")
    md.append("")
    
    # 1. Primary Semantic Matches
    md.append("## 1. Primary Semantic Matches")
    md.append("These entities are direct semantic matches for the query, ranked by relevance:")
    md.append("")
    for item in context_data["semantic_matches"]:
        node = item["node"]
        md.append(format_node_markdown(node))
        md.append(f"- **Semantic Score:** {item['score']}")
        md.append("")
        
    # 2. Adjacent Dependencies
    md.append("## 2. Adjacent Graph Dependencies")
    md.append("These entities are connected to the primary matches via logical dependencies:")
    md.append("")
    if not context_data["adjacent_context"]:
        md.append("*No adjacent dependency nodes retrieved.*")
    else:
        for item in context_data["adjacent_context"]:
            node = item["node"]
            md.append(format_node_markdown(node))
            dir_indicator = "→" if item["direction"] == "outgoing" else "←"
            md.append(f"- **Connection:** Connected to `{item['connected_to']}` via {item['relation_type']} ({item['direction']} {dir_indicator}) at Hop {item['hop_reached']}")
            md.append("")
            
    # 3. Learning & Heuristics Section
    lessons = [n for n in context_data["semantic_matches"] if n["node"]["type"] == "lesson"] + \
              [n for n in context_data["adjacent_context"] if n["node"]["type"] == "lesson"]
              
    if lessons:
        md.append("## 3. Historical Lessons & Rules")
        md.append("Compounded heuristics that are relevant to this decision context:")
        md.append("")
        for item in lessons:
            node = item.get("node")
            props = node.get("properties", {})
            md.append(f"* **{node['label']}:** {props.get('statement')} (Applied {props.get('recurrence_count', 1)}x)")
        md.append("")

    return "\n".join(md)

# ─── Main Pipeline ───────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Decision Intelligence OS — GraphRAG Context Packager")
    parser.add_argument("--query", required=True, help="Semantic query to run against the graph")
    parser.add_argument("--hops", type=int, default=1, help="Max hops to traverse neighbors (1 or 2)")
    parser.add_argument("--limit", type=int, default=5, help="Max semantic matches to return")
    parser.add_argument("--output", action="store_true", help="Save the compiled context package as an export file")
    args = parser.parse_args()

    if not GRAPH_EXPORT.exists():
        print(f"Error: Graph export file not found at {GRAPH_EXPORT}. Please run vault-extractor.py first.")
        return

    # Load Graph Export
    graph_data = json.loads(GRAPH_EXPORT.read_text(encoding="utf-8"))
    
    # Run Retrieval
    engine = GraphRAGEngine(graph_data)
    context_data = engine.retrieve_context(args.query, max_hops=args.hops, limit=args.limit)
    
    # Format Package
    compiled_markdown = compile_context_package(context_data)
    
    # Output to screen
    print(compiled_markdown)
    
    # Output to file
    if args.output:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        safe_query = re.sub(r"\W+", "-", args.query.lower()).strip("-")
        filename = f"context-package-{safe_query}.md"
        dest = OUTPUT_DIR / filename
        dest.write_text(compiled_markdown, encoding="utf-8")
        print(f"\n[GraphRAG] Saved compiled Context Package to:")
        print(f"👉 {dest}")

if __name__ == "__main__":
    main()
