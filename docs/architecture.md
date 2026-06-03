# Architecture

## Overview

GenAI Automation is designed as an AI-powered automation platform to help internal teams streamline repetitive workflows and improve product refinement processes.

The first use case focuses on helping a Product Owner transform a Jira epic and functional documentation into structured, refined Jira cards.

## High-level flow

User / Product Owner
        ↓
n8n Workflow
        ↓
Python Backend
        ↓
LLM / Agents / RAG
        ↓
Validated refinement output
        ↓
Human approval
        ↓
Jira cards creation or update

## Main components

### n8n

n8n is used as the workflow orchestrator.

Responsibilities:

- Receive user requests through a webhook, form, or chat trigger.
- Connect with external tools such as Jira, Google Drive, Slack, or Gmail.
- Call the Python backend.
- Coordinate approval steps.
- Trigger the creation or update of Jira cards.

### Python Backend

Python is used for the core business logic.

Responsibilities:

- Receive requests from n8n.
- Process functional documentation.
- Validate inputs and outputs.
- Execute agents and skills.
- Prepare structured responses.
- Generate payloads for external tools such as Jira.

### LLM Layer

The LLM layer is responsible for understanding natural language, analyzing context, and generating structured outputs.

Responsibilities:

- Interpret the Product Owner request.
- Analyze epic and documentation content.
- Extract business rules.
- Identify gaps and open questions.
- Generate refined Jira cards.
- Suggest acceptance criteria and dependencies.

### RAG

RAG is used to retrieve relevant context from functional documentation, product guidelines, templates, and internal knowledge.

Responsibilities:

- Index functional documents.
- Retrieve relevant sections based on the user request.
- Provide grounded context to the LLM.
- Reduce hallucinations by using project-specific information.

### Agents

Agents are specialized components that execute specific reasoning tasks.

Initial agents:

- Coordinator Agent
- Product Analyst Agent
- Backlog Refinement Agent
- Risk Discovery Agent
- Card Quality Reviewer Agent

### Skills

Skills are controlled tools that agents can use.

Initial skills:

- Read Jira epic
- Read functional documentation
- Search product context
- Extract business rules
- Generate user stories
- Generate acceptance criteria
- Detect open questions
- Validate card quality
- Create or update Jira cards

## First use case

The first implemented flow will support this scenario:

txt As a Product Owner, I want to provide a Jira epic and functional documentation, so that the assistant can generate refined Jira cards with acceptance criteria, dependencies, risks, and open questions. 

Example domain:

txt B2B debit card request flow for individuals and legal entities. 

## Design principles

- Human approval before creating or updating Jira cards.
- Agents should not execute irreversible actions directly.
- Outputs must be structured and validated.
- Business rules should come from documentation when possible.
- The system should be modular and extensible.
- Each integration should be replaceable or mockable.
- The project should support future workflows beyond product refinement.