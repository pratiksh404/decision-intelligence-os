#!/usr/bin/env python3
"""
Decision Intelligence OS — Mock Data Generator
Generates a complete, interconnected synthetic decision chain in the vault
to test and validate the extraction engine, lineage tracer, and similarity engine.
"""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
VAULT_ROOT = PROJECT_ROOT / "vault"

def create_file(relative_path: str, content: str):
    full_path = VAULT_ROOT / relative_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Created mock file: {relative_path}")

def main():
    print("Generating synthetic decision chain in vault...")

    # 1. Signals
    create_file(
        "01-intelligence/signals/SIG-2026-001 — customer-demand-for-privacy.md",
        """---
entity_id: SIG-2026-001
entity_type: signal
title: Customer Demand for Privacy
status: active
source: "https://example.com/privacy-survey-2026"
source_quality: high
signal_date: 2026-05-10
created: 2026-05-10
owner: "Founder/CEO"
signal_type: customer
strength: strong
related_trends:
  - "[[TRD-2026-001 — privacy-first-saas-demand]]"
tags:
  - signal
  - intelligence-layer
  - privacy
---
# Signal: Customer Demand for Privacy

Survey of 500 enterprise buyers reveals 78% consider "zero-knowledge encryption" a must-have for SaaS products in 2026, up from 42% in 2024.
"""
    )

    create_file(
        "01-intelligence/signals/SIG-2026-002 — competitors-adopting-e2ee.md",
        """---
entity_id: SIG-2026-002
entity_type: signal
title: Competitors Adopting E2EE
status: active
source: "SecureCorp Product Update Announcement"
source_quality: medium
signal_date: 2026-05-15
created: 2026-05-15
owner: "Founder/CEO"
signal_type: competitor
strength: moderate
related_trends:
  - "[[TRD-2026-001 — privacy-first-saas-demand]]"
related_competitors:
  - "[[CMP-001 — securecorp]]"
tags:
  - signal
  - intelligence-layer
  - competitor
---
# Signal: Competitors Adopting E2EE

SecureCorp (CMP-001) announced beta support for end-to-end encryption (E2EE) on all documents in their cloud suite.
"""
    )

    create_file(
        "01-intelligence/signals/SIG-2026-003 — new-privacy-regulation-draft.md",
        """---
entity_id: SIG-2026-003
entity_type: signal
title: New Privacy Regulation Draft
status: active
source: "EU Privacy Council Press Release"
source_quality: high
signal_date: 2026-05-20
created: 2026-05-20
owner: "Founder/CEO"
signal_type: regulatory
strength: strong
related_trends:
  - "[[TRD-2026-002 — regulatory-scrutiny-on-data]]"
tags:
  - signal
  - intelligence-layer
  - regulatory
---
# Signal: New Privacy Regulation Draft

Draft EU regulation mandates zero-knowledge design patterns for all business processing employee telemetry by 2027.
"""
    )

    # 2. Trends
    create_file(
        "01-intelligence/trends/TRD-2026-001 — privacy-first-saas-demand.md",
        """---
entity_id: TRD-2026-001
entity_type: trend
title: Privacy First SaaS Demand
status: emerging
direction: up
created: 2026-05-22
owner: "Founder/CEO"
category: market
time_horizon: 12mo
magnitude: high
evidence_strength: strong
supporting_signals:
  - "[[SIG-2026-001]]"
  - "[[SIG-2026-002]]"
leads_to:
  - "[[OPP-2026-001 — zero-knowledge-analytics]]"
tags:
  - trend
  - intelligence-layer
  - market-trends
---
# Trend: Privacy-First SaaS Demand

Accelerating demand among enterprise customers for zero-knowledge cloud applications. Driven by security concerns and competitor E2EE features.
"""
    )

    create_file(
        "01-intelligence/trends/TRD-2026-002 — regulatory-scrutiny-on-data.md",
        """---
entity_id: TRD-2026-002
entity_type: trend
title: Regulatory Scrutiny on Data
status: emerging
direction: up
created: 2026-05-23
owner: "Founder/CEO"
category: regulatory
time_horizon: 24mo
magnitude: high
evidence_strength: moderate
supporting_signals:
  - "[[SIG-2026-003]]"
leads_to:
  - "[[OPP-2026-002 — enterprise-privacy-gateway]]"
tags:
  - trend
  - intelligence-layer
  - regulatory
---
# Trend: Regulatory Scrutiny on Data

Upcoming EU privacy rules will heavily penalize non-zero-knowledge architectures processing corporate telemetry.
"""
    )

    # 3. Competitors
    create_file(
        "01-intelligence/competitors/CMP-001 — securecorp.md",
        """---
entity_id: CMP-001
entity_type: competitor
name: SecureCorp
status: active
founded: 2021
created: 2026-05-15
owner: "Founder/CEO"
category: direct
funding_stage: series-b
headcount: 85
threat_level: high
related_opportunities:
  - "[[OPP-2026-001]]"
tags:
  - competitor
  - intelligence-layer
---
# Competitor Dossier: SecureCorp

Direct competitor offering enterprise document collaboration software. Building E2EE and privacy solutions.
"""
    )

    # 4. Opportunities
    create_file(
        "01-intelligence/opportunities/OPP-2026-001 — zero-knowledge-analytics.md",
        """---
entity_id: OPP-2026-001
entity_type: opportunity
title: Zero Knowledge Analytics
status: researching
composite_score: 8.2
created: 2026-05-25
owner: "Founder/CEO"
category: new-product
market: Enterprise SaaS
estimated_value: 12000000
time_to_value: 9mo
score_expected_return: 9
score_probability: 7
score_strategic_fit: 9
score_execution_complexity: 6
score_resource_requirement: 5
score_risk: 4
related_trends:
  - "[[TRD-2026-001]]"
depends_on:
  - "[[ASM-2026-001 — enterprise-willingness-to-pay-for-privacy]]"
  - "[[ASM-2026-002 — zero-knowledge-performance-overhead-is-acceptable]]"
  - "[[ASM-2026-003 — competitive-moat-via-switching-costs]]"
related_competitors:
  - "[[CMP-001]]"
tags:
  - opportunity
  - intelligence-layer
---
# Opportunity: Zero-Knowledge Analytics

Develop a zero-knowledge analytics dashboard allowing privacy-sensitive customers to generate reports without revealing underlying customer data to the analytics host.
"""
    )

    create_file(
        "01-intelligence/opportunities/OPP-2026-002 — enterprise-privacy-gateway.md",
        """---
entity_id: OPP-2026-002
entity_type: opportunity
title: Enterprise Privacy Gateway
status: draft
composite_score: 6.8
created: 2026-05-26
owner: "Founder/CEO"
category: new-product
market: Security Infrastructure
estimated_value: 8000000
time_to_value: 12mo
score_expected_return: 7
score_probability: 6
score_strategic_fit: 8
score_execution_complexity: 7
score_resource_requirement: 6
score_risk: 5
related_trends:
  - "[[TRD-2026-002]]"
tags:
  - opportunity
  - intelligence-layer
---
# Opportunity: Enterprise Privacy Gateway

An on-premise proxy that automatically encrypts sensitive employee telemetry before exporting it to public cloud services.
"""
    )

    # 5. Assumptions
    create_file(
        "02-decisions/assumptions/ASM-2026-001 — enterprise-willingness-to-pay-for-privacy.md",
        """---
entity_id: ASM-2026-001
entity_type: assumption
title: Enterprise Willingness to Pay for Privacy
claim: Enterprise buyers are willing to pay a 20%+ price premium for zero-knowledge SaaS compared to standard cloud analytics.
status: unvalidated
invalidation_risk: critical
created: 2026-05-25
owner: "Founder/CEO"
category: market
evidence_status: none
validation_method: "Conjoint analysis survey of 100 enterprise CTOs"
validation_deadline: 2026-07-01
tags:
  - assumption
  - decision-layer
---
# Assumption: Enterprise Willingness to Pay for Privacy

We assume zero-knowledge features represent a premium value proposition rather than a table-stakes commodity feature. If false, margins will compress.
"""
    )

    create_file(
        "02-decisions/assumptions/ASM-2026-002 — zero-knowledge-performance-overhead-is-acceptable.md",
        """---
entity_id: ASM-2026-002
entity_type: assumption
title: Zero-Knowledge Performance Overhead is Acceptable
claim: Zero-knowledge query protocols will run with less than 200ms latency overhead, keeping UI load times under 2 seconds.
status: unvalidated
invalidation_risk: high
created: 2026-05-25
owner: "Founder/CEO"
category: product
evidence_status: none
validation_method: "Performance prototyping with WASM cryptographical primitives"
validation_deadline: 2026-06-30
tags:
  - assumption
  - decision-layer
---
# Assumption: Zero-Knowledge Performance Overhead is Acceptable

Mathematical operations on encrypted data are computationally expensive. We assume clients can perform these calculations in-browser without violating UX standards.
"""
    )

    create_file(
        "02-decisions/assumptions/ASM-2026-003 — competitive-moat-via-switching-costs.md",
        """---
entity_id: ASM-2026-003
entity_type: assumption
title: Competitive Moat via Switching Costs
claim: Zero-knowledge key escrow systems establish high switching costs because users cannot easily migrate historical encrypted records to other platforms.
status: unvalidated
invalidation_risk: medium
created: 2026-05-25
owner: "Founder/CEO"
category: competition
evidence_status: none
mental_models_applied:
  - "[[MMD-004]]"
tags:
  - assumption
  - decision-layer
---
# Assumption: Competitive Moat via Switching Costs

Applying the Switching Costs (MMD-004) mental model to lock-in dynamics.
"""
    )

    # 6. Decision Memos
    create_file(
        "02-decisions/memos/DEC-2026-001 — build-zero-knowledge-analytics-platform.md",
        """---
entity_id: DEC-2026-001
entity_type: decision
title: Build Zero-Knowledge Analytics Platform
status: approved
decision_type: go
created: 2026-05-28
resolved_date: 2026-05-28
owner: "Founder/CEO"
category: product
reversibility: reversible
confidence_at_decision: 8
related_opportunity: "[[OPP-2026-001]]"
assumes:
  - "[[ASM-2026-001]]"
  - "[[ASM-2026-002]]"
  - "[[ASM-2026-003]]"
generates:
  - "[[INI-2026-001 — zero-knowledge-mvp-development]]"
  - "[[FRC-2026-001 — securecorp-launches-competing-product-by-q4]]"
mental_models_applied:
  - "[[MMD-001]]"
  - "[[MMD-003]]"
tags:
  - decision
  - decision-layer
---
# Decision Memo: Build Zero-Knowledge Analytics Platform

Formal go-decision to commit initial developer resources to the development of our privacy-preserving zero-knowledge telemetry system.
"""
    )

    # 7. Forecasts
    create_file(
        "02-decisions/forecasts/FRC-2026-001 — securecorp-launches-competing-product-by-q4.md",
        """---
entity_id: FRC-2026-001
entity_type: forecast
question: Will SecureCorp launch a zero-knowledge analytics product by October 31, 2026?
status: active
predicted_probability: 0.65
deadline: 2026-10-31
resolution_criteria: SecureCorp press announcement or product release of zero-knowledge, E2EE, or homomorphic analytics dashboard prior to Oct 31, 2026.
created: 2026-05-28
owner: "Founder/CEO"
category: competition
related_decision: "[[DEC-2026-001]]"
assumes:
  - "[[ASM-2026-003]]"
tags:
  - forecast
  - decision-layer
---
# Forecast: Will SecureCorp Launch Competitor Product?

Our probability assessment is 65% based on their active beta test announcements for E2EE (SIG-2026-002).
"""
    )

    # 9. Initiatives
    create_file(
        "03-execution/initiatives/INI-2026-001 — zero-knowledge-mvp-development.md",
        """---
entity_id: INI-2026-001
entity_type: initiative
title: Zero-Knowledge MVP Development
status: active
related_decision: "[[DEC-2026-001]]"
owner: "Founder/CEO"
created: 2026-05-30
category: product
target_completion: 2026-09-01
progress_percent: 15
generates:
  - "[[RSK-2026-001 — developer-talent-shortage-for-cryptography]]"
tags:
  - initiative
  - execution-layer
---
# Initiative: Zero-Knowledge MVP Development

Engineering project implementing the first client-side encrypted telemetry receiver.
"""
    )

    # 9. Risks
    create_file(
        "03-execution/risks/RSK-2026-001 — developer-talent-shortage-for-cryptography.md",
        """---
entity_id: RSK-2026-001
entity_type: risk
title: Developer Talent Shortage for Cryptography
status: active
severity: high
probability: 6
impact: 8
risk_score: 48
owner: "Founder/CEO"
created: 2026-05-30
category: team
mitigation_plan: "Contract a specialized cryptographic engineering agency for core primitives."
related_initiative: "[[INI-2026-001]]"
tags:
  - risk
  - execution-layer
---
# Risk: Developer Talent Shortage for Cryptography

Building E2EE systems in WASM requires rare cryptographic skillsets. If hiring takes too long, MVP deadline will slip.
"""
    )

    # 10. Outcomes
    create_file(
        "04-learning/outcomes/OUT-2026-001 — zero-knowledge-mvp-release.md",
        """---
entity_id: OUT-2026-001
entity_type: outcome
title: Zero-Knowledge MVP Release
status: complete
result: success
created: 2026-06-10
resolution_date: 2026-06-10
owner: "Founder/CEO"
related_decision: "[[DEC-2026-001]]"
related_initiative: "[[INI-2026-001]]"
generates:
  - "[[LSN-2026-001 — complexity-of-zero-knowledge-ux]]"
tags:
  - outcome
  - learning-layer
---
# Outcome: Zero-Knowledge MVP Release

The MVP was successfully launched on June 10, 2026. Latency overhead was measured at 110ms, validating ASM-2026-002.
"""
    )

    # 11. Lessons
    create_file(
        "04-learning/lessons/LSN-2026-001 — complexity-of-zero-knowledge-ux.md",
        """---
entity_id: LSN-2026-001
entity_type: lesson
title: Complexity of Zero-Knowledge UX
statement: Enterprise users struggle with manual key management; automated key escrow integrations improve onboarding activation by 40%.
status: active
recurrence_count: 1
created: 2026-06-12
owner: "Founder/CEO"
category: product
related_outcome: "[[OUT-2026-001]]"
related_decision: "[[DEC-2026-001]]"
mental_model_updated: "[[MMD-001]]"
tags:
  - lesson
  - learning-layer
---
# Lesson: Complexity of Zero-Knowledge UX

Key escrow management was the primary friction point. Moving forward, we should automate keys inside identity provider integrations (Okta/AD).
"""
    )

    print("Synthetic decision chain populated successfully!")

if __name__ == "__main__":
    main()
