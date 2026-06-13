#!/usr/bin/env python3
"""
Decision Intelligence OS — Strategic Scenario Generator
Phase 4 Implementation

Given a Decision Memo ID (e.g., DEC-2026-001), this script parses its metadata
and automatically generates 5 standardized scenario files in the vault:
- Best Case
- Base Case
- Worst Case
- Stretch Case
- Black Swan Case

These scenarios are linked to the parent decision, inherit its tested assumptions,
and define triggers and leading indicators to integrate with the Early Warning System.

Usage:
    python3 scripts/graph/generate-scenarios.py --decision DEC-2026-001
"""

import os
import re
import sys
import json
import yaml
import argparse
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
VAULT_ROOT = PROJECT_ROOT / "vault"
REGISTRY = VAULT_ROOT / "06-meta-intelligence" / "graph" / "entity-registry.json"
SCENARIO_DIR = VAULT_ROOT / "02-decisions" / "scenarios"

# Prefix and suffix details for the 5 scenarios
SCENARIO_CONFIGS = {
    "best-case": {
        "title_suffix": "Ideal Market Adoption",
        "probability": 0.20,
        "narrative": "Assumptions hold perfectly. Customer onboarding is friction-free, and enterprise willingness to pay is high. Competitors are slow to respond.",
        "expected_outcome": "NPV targets exceeded by 40%; payback period shrinks to 6 months.",
        "capital_adjust": -50000,
        "headcount_adjust": 0,
        "trigger": "User growth exceeds 25% month-over-month; CAC drops below $50."
    },
    "base-case": {
        "title_suffix": "Standard Execution Path",
        "probability": 0.50,
        "narrative": "Execution aligns with roadmap estimates. Latency is acceptable, and key escrow features are adopted with standard support guidance.",
        "expected_outcome": "Steady growth matching targets; ROI of 15% achieved within 12 months.",
        "capital_adjust": 0,
        "headcount_adjust": 0,
        "trigger": "Onboarding activation rate stays within 40-50% range; latency averages 120ms."
    },
    "worst-case": {
        "title_suffix": "Key Assumption Failure & Price War",
        "probability": 0.15,
        "narrative": "Enterprise buyers refuse price premium (ASM-2026-001 fails) or localized gateways require massive support overhead. Competitors drop basic pricing.",
        "expected_outcome": "Gross margins compress by 35%. Development is stalled due to technical issues.",
        "capital_adjust": 100000,
        "headcount_adjust": 1,
        "trigger": "Competitor announces free zero-knowledge module; onboarding activation falls below 20%."
    },
    "stretch-case": {
        "title_suffix": "Uncapped Enterprise Demand",
        "probability": 0.10,
        "narrative": "New regulatory mandates (SIG-2026-003) force immediate adoption of zero-knowledge architectures, causing a rush of enterprise inbound sales.",
        "expected_outcome": "Pipeline increases by 300%. Scale requirements double server costs but increase revenue by 5x.",
        "capital_adjust": 150000,
        "headcount_adjust": 2,
        "trigger": "EU draft regulation is formally enacted; inbound leads increase by >100% in a single month."
    },
    "black-swan": {
        "title_suffix": "Systemic Cryptographical Breach",
        "probability": 0.05,
        "narrative": "A major zero-knowledge mathematical primitive is found to have a critical vulnerability, undermining trust in all client-side encrypted telemetry.",
        "expected_outcome": "Complete reputation loss; initiative must be paused or completely refactored using post-quantum primitives.",
        "capital_adjust": 300000,
        "headcount_adjust": 0,
        "trigger": "Academic paper or CVE published details breach of standard homomorphic primitives."
    }
}

def load_registry() -> dict:
    if REGISTRY.exists():
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {"entities": {}, "id_counters": {}}

def save_registry(registry: dict):
    REGISTRY.write_text(json.dumps(registry, indent=2, default=str), encoding="utf-8")

def find_decision_file(decision_id: str) -> Path | None:
    memo_dir = VAULT_ROOT / "02-decisions" / "memos"
    if not memo_dir.exists():
        return None
    for f in memo_dir.glob("*.md"):
        if f.name.startswith(decision_id):
            return f
    return None

def parse_frontmatter(filepath: Path) -> dict | None:
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
        return fm
    except Exception as e:
        print(f"Error parsing frontmatter of {filepath.name}: {e}")
        return None

def generate_id(registry: dict, year: str) -> str:
    """Assign the next sequential SCE ID."""
    counters = registry.setdefault("id_counters", {}).setdefault("SCE", {})
    counter = counters.get(year, 0) + 1
    counters[year] = counter
    return f"SCE-{year}-{counter:03d}"

def clean_kebab(title: str) -> str:
    return re.sub(r"\W+", "-", title.lower()).strip("-")

def main():
    parser = argparse.ArgumentParser(description="Strategic Scenario Generator")
    parser.add_argument("--decision", required=True, help="Decision Memo ID (e.g. DEC-2026-001)")
    args = parser.parse_args()

    decision_id = args.decision.upper()
    decision_file = find_decision_file(decision_id)
    if not decision_file:
        print(f"Error: Decision file with ID {decision_id} not found in memos folder.")
        sys.exit(1)

    fm = parse_frontmatter(decision_file)
    if not fm:
        print(f"Error: Could not parse frontmatter for decision {decision_file.name}.")
        sys.exit(1)

    decision_title = fm.get("title", "Untitled Decision")
    assumptions = fm.get("assumes", [])
    owner = fm.get("owner", "Founder/CEO")
    
    # Standardize assumptions format to list of wiki-links
    assumptions_links = []
    for a in assumptions:
        a_str = str(a).strip()
        if not a_str.startswith("[["):
            a_str = f"[[{a_str}]]"
        assumptions_links.append(a_str)

    # Load registry to generate fresh sequential IDs
    registry = load_registry()
    year = str(date.today().year)
    
    SCENARIO_DIR.mkdir(parents=True, exist_ok=True)
    created_scenarios = []

    print(f"Generating 5 scenarios for Decision: '{decision_title}' ({decision_id})")

    for scenario_type, config in SCENARIO_CONFIGS.items():
        sce_id = generate_id(registry, year)
        sce_title = f"{decision_title} — {config['title_suffix']}"
        kebab_title = clean_kebab(f"{decision_id} {scenario_type} {config['title_suffix']}")
        filename = f"{sce_id} — {kebab_title}.md"
        filepath = SCENARIO_DIR / filename

        # YAML Frontmatter
        frontmatter = {
            "entity_id": sce_id,
            "entity_type": "scenario",
            "title": sce_title,
            "parent_decision": f"[[{decision_file.stem}]]",
            "scenario_type": scenario_type,
            "status": "active" if scenario_type == "base-case" else "inactive",
            "probability": config["probability"],
            "assumptions_tested": assumptions_links,
            "triggers": [config["trigger"]],
            "expected_outcome": config["expected_outcome"],
            "resource_impact": {
                "headcount_adjustment": config["headcount_adjust"],
                "additional_capital": config["capital_adjust"]
            },
            "leading_indicators": [],
            "tags": ["decision-layer", "scenario"],
            "created": date.today().isoformat(),
            "updated": date.today().isoformat(),
            "owner": owner
        }

        yaml_str = yaml.dump(frontmatter, sort_keys=False, default_flow_style=False, allow_unicode=True)
        
        # Markdown Body
        content = f"""---
{yaml_str}---

# Scenario: {sce_title}

## Core Narrative
{config['narrative']}

## Assumptions Tested
This scenario evaluates the robustness of the following assumptions under variance:
{chr(10).join([f'- {a}' for a in assumptions_links])}

## Key Triggers & Leading Indicators
This scenario is activated when the following trigger conditions are detected:
- **Trigger:** {config['trigger']}

## Expected Outcomes & Resource Requirements
* **Outcome:** {config['expected_outcome']}
* **Capital Adjustment:** ${config['capital_adjust']:,}
* **Headcount Adjustment:** {config['headcount_adjust']} additional role(s) required.
"""

        filepath.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"  [{scenario_type.upper()}] Created: {filename}")
        
        # Add to registry entities
        registry["entities"][sce_id] = {
            "type": "scenario",
            "subtype": scenario_type,
            "title": sce_title,
            "file": str(filepath.relative_to(VAULT_ROOT)),
            "status": frontmatter["status"],
            "created": date.today().isoformat()
        }
        created_scenarios.append(sce_id)

    # Save registry changes
    registry["total_entities"] = len(registry["entities"])
    save_registry(registry)
    print(f"Updated entity registry. Registered {len(created_scenarios)} scenarios.")

    # Re-run extraction engine to update exports/graphs
    print("\nTriggering graph extraction to sync new scenario nodes...")
    os.system(f"{sys.executable} scripts/graph/vault-extractor.py")
    print("Graph extraction complete!")

if __name__ == "__main__":
    main()
