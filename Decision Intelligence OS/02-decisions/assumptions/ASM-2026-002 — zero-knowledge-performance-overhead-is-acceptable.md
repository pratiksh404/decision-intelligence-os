---
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
