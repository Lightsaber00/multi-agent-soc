# Architecture

## Objective

The SOC portal is intended to help analysts process alerts faster by combining triage, enrichment, correlation, and summary generation into one guided workflow.

The system is designed to support:
- faster alert understanding,
- fewer repetitive manual checks,
- better prioritization,
- and a clearer case narrative for incident handling.

## High-level view

The project is composed of four main parts:

- Presentation layer.
- Orchestration layer.
- Analysis layer.
- Data layer.

## Layer overview

### 1. Presentation layer
The frontend is the analyst workspace.

Main goals:
- Show open alerts.
- Present enrichment results.
- Display timelines and related entities.
- Surface suggested actions.

### 2. Orchestration layer
The orchestrator coordinates the analysis workflow.

Main goals:
- Accept a new alert or event.
- Determine which checks are needed.
- Route the task to the right module.
- Combine outputs into one case view.

### 3. Analysis layer
This layer performs the actual SOC reasoning.

Main goals:
- Enrich suspicious IPs, domains, or hashes.
- Correlate similar alerts.
- Identify likely severity.
- Produce an analyst summary.

### 4. Data layer
The data layer stores operational context.

Main goals:
- Store alerts.
- Store enrichment results.
- Store incident notes.
- Preserve analysis history.

## Example workflow

1. A new alert arrives.
2. The orchestrator classifies the alert type.
3. Enrichment checks run against threat intel sources.
4. Correlation logic checks for related signals.
5. The system generates a case summary.
6. The analyst reviews and decides the response.

## Future extensions

- SIEM connector.
- Ticketing integration.
- Case management.
- Analyst collaboration features.
- Automated reporting.

## Design principles

- Keep the workflow explainable.
- Prefer modular components over one large script.
- Make analyst actions visible.
- Preserve human decision points.
- Support future production hardening.
