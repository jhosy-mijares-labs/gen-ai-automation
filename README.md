# GenAI Automation

AI-powered automation project designed to help internal teams streamline repetitive workflows, refine product epics, read functional documentation, and generate actionable Jira cards.

## Purpose

This project explores how Generative AI, automation workflows, and intelligent agents can support Product, Operations, and Engineering teams by reducing manual work and improving the quality of product refinement.

The first use case focuses on helping a Product Owner transform a Jira epic and functional documentation into structured, refined Jira cards.

## Stack

- Python
- Playwright
- n8n
- Docker
- LLMs
- RAG
- Jira API
- Google Drive API

## Start project

bash ./scripts/start-local-services.sh

## Stop project

bash ./scripts/stop-local-services.sh

## Run Playwright validation

bash ./venv/bin/python3 scripts/validate-playwright-setup.py 