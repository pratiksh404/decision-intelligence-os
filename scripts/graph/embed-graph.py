#!/usr/bin/env python3
"""
Decision Intelligence OS — Hybrid GraphRAG Vector Search Baseline
Phase 3.5 Implementation

Loads the Decision Graph, compiles nodes into embedding-ready text representations,
generates a simulated vector database using TF-IDF / Cosine Similarity, and
provides a search interface to demonstrate semantic query resolution.

Includes placeholder code for production libraries (sentence-transformers).
"""

import json
import math
import re
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).parent.parent.parent
GRAPH_EXPORT = PROJECT_ROOT / "vault" / "06-meta-intelligence" / "graph" / "exports" / "graph-export.json"

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
    
    if not denominator:
        return 0.0
    return numerator / denominator

class VectorDBMock:
    """A lightweight, local, zero-dependency TF-IDF semantic database."""
    def __init__(self):
        self.documents = []
        self.doc_vectors = []
        self.idf = {}

    def fit_and_add(self, documents: list[dict]):
        self.documents = documents
        
        # Count document frequencies for IDF
        all_tokens = []
        doc_tokens = []
        for doc in documents:
            tokens = clean_text(doc["text_to_embed"])
            doc_tokens.append(tokens)
            all_tokens.extend(set(tokens))
            
        doc_count = len(documents)
        term_df = Counter(all_tokens)
        
        # Compute IDF
        for term, df in term_df.items():
            self.idf[term] = math.log((1 + doc_count) / (1 + df)) + 1
            
        # Compute TF-IDF vectors for documents
        for tokens in doc_tokens:
            tf = Counter(tokens)
            vector = {}
            for term, count in tf.items():
                vector[term] = count * self.idf.get(term, 0.0)
            self.doc_vectors.append(vector)

    def query(self, query_text: str, top_k: int = 5) -> list[dict]:
        query_tokens = clean_text(query_text)
        query_tf = Counter(query_tokens)
        query_vector = {}
        for term, count in query_tf.items():
            query_vector[term] = count * self.idf.get(term, 0.0)
            
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

def prepare_node_text(node: dict) -> str:
    """Compile a rich text block representing the node for semantic embedding."""
    node_id = node["id"]
    node_type = node["type"]
    label = node["label"]
    status = node.get("status", "unknown")
    
    props = node.get("properties", {})
    tags = ", ".join(node.get("tags", []))
    
    # Extract descriptions and claims
    desc = props.get("description") or props.get("claim") or props.get("question") or props.get("statement") or ""
    rationale = props.get("allocation_rationale") or props.get("mitigation_plan") or props.get("resolution_criteria") or ""
    
    # Formulate unstructured text block
    text = f"ID: {node_id}. Type: {node_type}. Title: {label}. Status: {status}. "
    if desc:
        text += f"Description: {desc}. "
    if rationale:
        text += f"Rationale/Details: {rationale}. "
    if tags:
        text += f"Tags: {tags}. "
        
    return text

def main():
    print("[Vector Search Baseline] Loading graph...")
    if not GRAPH_EXPORT.exists():
        print(f"Error: {GRAPH_EXPORT} does not exist. Run vault-extractor.py first.")
        return

    graph = json.loads(GRAPH_EXPORT.read_text(encoding="utf-8"))
    nodes = graph.get("nodes", [])
    print(f"Found {len(nodes)} nodes for embedding.")

    # Compile embedding documents
    embed_docs = []
    for node in nodes:
        text_to_embed = prepare_node_text(node)
        embed_docs.append({
            "node": node,
            "text_to_embed": text_to_embed
        })
        # Save compiled embedding text back to export-ready nodes
        node["embedding_ready"] = {
            "text_for_embedding": text_to_embed
        }

    # Initialize and fit our mock vector DB
    vdb = VectorDBMock()
    vdb.fit_and_add(embed_docs)
    print("Vector database fitted with TF-IDF weights.")

    # Demonstration Queries
    queries = [
        "What are the privacy requirements for SaaS analytics?",
        "Competitor security updates and E2EE",
        "switching costs and customer lock-in",
        "talent shortage and hiring issues"
    ]

    print("\n--- Running Semantic Query Demonstration ---")
    for q in queries:
        print(f"\nQuery: '{q}'")
        matches = vdb.query(q, top_k=3)
        if not matches:
            print("  No semantic matches found.")
        for idx, match in enumerate(matches):
            node = match["node"]
            print(f"  [{idx+1}] Score: {match['score']:.4f} | {node['id']} ({node['type']}) — {node['label']}")

    # Save vector metadata or write to graph-export to demonstrate GraphRAG readiness
    # (re-writing graph-export with the new "embedding_ready" attributes)
    GRAPH_EXPORT.write_text(json.dumps(graph, indent=2, default=str), encoding="utf-8")
    print(f"\n[Vector Search Baseline] Added 'embedding_ready' text to graph-export.json")

if __name__ == "__main__":
    main()
