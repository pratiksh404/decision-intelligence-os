# Data Ingestion Spec

## Purpose

Define future source ingestion for market intelligence, forecasts, and opportunity discovery.

## Source Categories

- News and research
- Company announcements
- Competitor websites
- Founder and investor commentary
- Startup databases
- Financial market data
- Sports data
- Betting odds
- Polymarket markets
- Regulatory updates

## Ingestion Fields

```yaml
source_url:
source_name:
published_date:
retrieved_date:
author:
category:
summary:
key_facts:
relevance:
confidence:
related_artifacts:
```

## Processing Steps

1. Capture source.
2. Extract facts and claims.
3. Assess source quality.
4. Classify relevance.
5. Link to opportunities, decisions, or forecasts.
6. Recommend follow-up research.

## Quality Controls

- Prefer primary sources.
- Record retrieval date.
- Do not treat commentary as fact.
- Flag stale sources.
- Triangulate important claims.

