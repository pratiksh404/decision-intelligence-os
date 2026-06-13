# GraphRAG Strategic Context Package
**Query:** "willingness to pay for privacy"

> [!NOTE]
> This package contains semantically retrieved business intelligence entities and their structural graph dependencies.

## 1. Primary Semantic Matches
These entities are direct semantic matches for the query, ranked by relevance:

### [ASM-2026-001] Enterprise Willingness to Pay for Privacy (Assumption)
- **Status:** unvalidated
- **Claim:** Enterprise buyers are willing to pay a 20%+ price premium for zero-knowledge SaaS compared to standard cloud analytics.
- **Invalidation Risk:** critical
- **Evidence Status:** none
- **Tags:** assumption, decision-layer
- **Source File:** `[[02-decisions/assumptions/ASM-2026-001 — enterprise-willingness-to-pay-for-privacy.md]]`
- **Semantic Score:** 0.5605

### [SIG-2026-001] Customer Demand for Privacy (Signal)
- **Status:** active
- **Tags:** signal, intelligence-layer, privacy
- **Source File:** `[[01-intelligence/signals/SIG-2026-001 — customer-demand-for-privacy.md]]`
- **Semantic Score:** 0.2766

### [RSK-2026-001] Developer Talent Shortage for Cryptography (Risk)
- **Status:** active
- **Severity:** high | **Impact:** 8
- **Mitigation Plan:** Contract a specialized cryptographic engineering agency for core primitives.
- **Tags:** risk, execution-layer
- **Source File:** `[[03-execution/risks/RSK-2026-001 — developer-talent-shortage-for-cryptography.md]]`
- **Semantic Score:** 0.1312

### [OPP-2026-002] Enterprise Privacy Gateway (Opportunity)
- **Status:** draft
- **Tags:** opportunity, intelligence-layer
- **Source File:** `[[01-intelligence/opportunities/OPP-2026-002 — enterprise-privacy-gateway.md]]`
- **Semantic Score:** 0.0907

### [SIG-2026-003] New Privacy Regulation Draft (Signal)
- **Status:** active
- **Tags:** signal, intelligence-layer, regulatory
- **Source File:** `[[01-intelligence/signals/SIG-2026-003 — new-privacy-regulation-draft.md]]`
- **Semantic Score:** 0.0866

## 2. Adjacent Graph Dependencies
These entities are connected to the primary matches via logical dependencies:

### [TRD-2026-001] Privacy First SaaS Demand (Trend)
- **Status:** emerging
- **Tags:** trend, intelligence-layer, market-trends
- **Source File:** `[[01-intelligence/trends/TRD-2026-001 — privacy-first-saas-demand.md]]`
- **Connection:** Connected to `SIG-2026-001` via LEADS_TO (outgoing →) at Hop 1

### [TRD-2026-002] Regulatory Scrutiny on Data (Trend)
- **Status:** emerging
- **Tags:** trend, intelligence-layer, regulatory
- **Source File:** `[[01-intelligence/trends/TRD-2026-002 — regulatory-scrutiny-on-data.md]]`
- **Connection:** Connected to `SIG-2026-003` via LEADS_TO (outgoing →) at Hop 1

### [INI-2026-001] Zero-Knowledge MVP Development (Initiative)
- **Status:** active
- **Tags:** initiative, execution-layer
- **Source File:** `[[03-execution/initiatives/INI-2026-001 — zero-knowledge-mvp-development.md]]`
- **Connection:** Connected to `RSK-2026-001` via GENERATES (incoming ←) at Hop 1

### [OPP-2026-001] Zero Knowledge Analytics (Opportunity)
- **Status:** researching
- **Tags:** opportunity, intelligence-layer
- **Source File:** `[[01-intelligence/opportunities/OPP-2026-001 — zero-knowledge-analytics.md]]`
- **Connection:** Connected to `ASM-2026-001` via DEPENDS_ON (incoming ←) at Hop 1

### [DEC-2026-001] Build Zero-Knowledge Analytics Platform (Decision)
- **Status:** approved
- **Decision Type:** go
- **Reversibility:** reversible
- **Tags:** decision, decision-layer
- **Source File:** `[[02-decisions/memos/DEC-2026-001 — build-zero-knowledge-analytics-platform.md]]`
- **Connection:** Connected to `ASM-2026-001` via ASSUMES (incoming ←) at Hop 1
