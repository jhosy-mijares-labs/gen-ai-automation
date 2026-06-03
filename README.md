## GenAI Automation

AI-powered automation project designed to help internal teams streamline repetitive workflows, refine product epics, read functional documentation, and generate actionable Jira cards.

## Purpose

This project explores how Generative AI, automation workflows, and intelligent agents can support Product, Operations, and Engineering teams by reducing manual work and improving the quality of product refinement.

The first use case focuses on helping a Product Owner transform a Jira epic and functional documentation into structured, refined Jira cards.

## Stack

- Python
- FastAPI
- Playwright
- n8n
- Docker
- LLMs
- RAG
- Jira API
- Google Drive API

## Start local services

Start Docker-based services such as n8n:

```bash
./scripts/start-local-services.sh
```

n8n should be available at:

```txt
http://localhost:5678
```

## Start Product Refinement API

Start the FastAPI backend used by the n8n workflow:

```bash
./scripts/run-product-refinement-api.sh
```

The API documentation should be available at:

```txt
http://localhost:8000/docs
```

The health check endpoint should be available at:

```txt
http://localhost:8000/health
```

## Run the n8n workflow

To test the current product refinement flow, keep both services running:

```txt
Terminal 1: ./scripts/start-local-services.sh
Terminal 2: ./scripts/run-product-refinement-api.sh
```

Then execute the n8n workflow that calls:

```txt
POST http://host.docker.internal:8000/product-refinement/generate
```

## Stop local services

Stop Docker-based services:

```bash
./scripts/stop-local-services.sh
```

## Run Playwright validation

Validate that Playwright is correctly installed and working:

```bash
./venv/bin/python3 scripts/validate-playwright-setup.py
```