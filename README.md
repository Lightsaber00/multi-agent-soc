
# Multi-Agent SOC

A portfolio-grade security operations project that demonstrates alert triage, threat intelligence enrichment, event correlation, and incident support workflows.

The goal is to show how a multi-agent SOC pipeline can help analysts reduce noise, prioritize alerts, and understand incidents faster.

## Why this project exists

This project was created to demonstrate a practical SOC workflow that combines automation and human analysis.
It focuses on the core tasks a security operations analyst performs every day: review alerts, enrich findings, correlate evidence, and decide on next actions.

The repository is intentionally structured as a portfolio project to show:
- SOC workflow thinking.
- Event analysis and triage logic.
- LLM-orchestrated analyst support.
- A realistic path toward a production-ready security operations tool.

## Core capabilities

- Alert triage and prioritization.
- Threat intelligence enrichment.
- Event correlation across multiple signals.
- Analyst summary generation.
- Incident context aggregation.
- Playbook-oriented response suggestions.

## Architecture / Layer overview

### 1. Presentation layer
The frontend presents alerts, entity context, timelines, and analyst actions in a simple dashboard.

Main goals:
- Show the current alert queue.
- Display evidence and enrichment results.
- Summarize the likely severity and next steps.

Key entry point:
- `frontend/index.html`

### 2. Orchestration layer
The orchestration layer receives incoming events and routes them to the right agents or analysis modules.

Main goals:
- Decide which enrichment or correlation steps are needed.
- Keep the workflow modular and explainable.
- Merge outputs into one analyst-friendly case view.

Key entry point:
- `backend/app/main.py`

### 3. Analysis layer
This layer contains the logic for alert enrichment, correlation, and case summarization.

Main goals:
- Enrich indicators with threat intel.
- Correlate related events.
- Produce a compact analyst summary.

Key components:
- Alert triage logic.
- Threat intel lookups.
- Event correlation rules.
- Incident summary generation.

### 4. Data layer
The data layer stores alerts, enrichments, cases, and analysis results.

Main goals:
- Keep case history.
- Store alert context.
- Support future API and database integrations.

## Suggested module map

```text
multi-agent-soc/
├── README.md
├── docs/
│   ├── architecture.md
│   └── roadmap.md
├── frontend/
│   └── index.html
├── backend/
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
└── tests/
