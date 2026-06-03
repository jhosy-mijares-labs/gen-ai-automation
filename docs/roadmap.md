:::writing{variant="document" id="69427"}
# Roadmap

## Goal

Build an AI-powered automation assistant that helps internal teams refine product epics, analyze functional documentation, and generate actionable Jira cards.

The roadmap is divided into small phases to keep the implementation clear, testable, and scalable.

## Phase 1: Project setup

Status: In progress

Objectives:

- Configure local development environment.
- Set up Docker.
- Run n8n locally.
- Configure Python dependencies.
- Add Playwright validation script.
- Add basic project documentation.

Deliverables:

- `docker-compose.yml`
- `requirements.txt`
- `scripts/start.sh`
- `scripts/stop.sh`
- `scripts/playwright_test.py`
- `README.md`
- `docs/architecture.md`
- `docs/roadmap.md`

## Phase 2: Python backend foundation

Objectives:

- Create a basic Python backend.
- Add a health check endpoint.
- Prepare the project structure for services, schemas, agents, and skills.
- Validate that n8n can call the backend.

Deliverables:

- Basic FastAPI app.
- `/health` endpoint.
- Project structure for backend modules.
- Local backend execution command.

## Phase 3: n8n integration with Python backend

Objectives:

- Create the first n8n workflow.
- Trigger a request from n8n.
- Call the Python backend.
- Return a mocked refinement response.

Deliverables:

- n8n workflow file.
- Webhook or manual trigger.
- HTTP request from n8n to Python.
- Mocked response with sample refined cards.

## Phase 4: Functional documentation processing

Objectives:

- Read a `.docx` functional document.
- Extract text from the document.
- Normalize and prepare the content for analysis.
- Use a sample document for the first demo.

Deliverables:

- Document reader service.
- Sample functional document.
- Parsed document output.
- Tests for document parsing.

## Phase 5: Product refinement mock

Objectives:

- Generate a structured refinement proposal from mocked epic data and parsed documentation.
- Create sample output without calling Jira yet.

Deliverables:

- Product analysis schema.
- Jira card schema.
- Refinement result schema.
- Mock epic input.
- Mock generated cards.

## Phase 6: LLM integration

Objectives:

- Connect the backend with an LLM provider.
- Send epic and documentation context to the LLM.
- Receive structured JSON output.
- Validate the output before using it.

Deliverables:

- LLM service.
- Prompt templates.
- Structured output validation.
- Error handling for invalid LLM responses.

## Phase 7: RAG foundation

Objectives:

- Index functional documentation.
- Retrieve relevant context for a specific epic.
- Use retrieved context as input for the LLM.

Deliverables:

- Basic vector store setup.
- Document chunking.
- Retrieval service.
- Context-enriched refinement output.

## Phase 8: Agents and skills

Objectives:

- Implement the first specialized agents.
- Create reusable skills.
- Coordinate the refinement flow through agents.

Initial agents:

- Coordinator Agent
- Product Analyst Agent
- Backlog Refinement Agent
- Risk Discovery Agent
- Card Quality Reviewer Agent

Initial skills:

- Read epic
- Read document
- Search context
- Generate cards
- Detect risks
- Validate card quality

Deliverables:

- Agent structure.
- Skill structure.
- First end-to-end agent flow.

## Phase 9: Jira integration

Objectives:

- Connect with Jira API.
- Read an epic.
- Create or update Jira cards after human approval.
- Add comments to the epic with refinement summary.

Deliverables:

- Jira client.
- Read epic functionality.
- Create card functionality.
- Approval step before write actions.

## Phase 10: Google Drive integration

Objectives:

- Connect with Google Drive.
- Read functional `.docx` files.
- Match documents with the requested epic or product context.

Deliverables:

- Google Drive client.
- Document download flow.
- Integration with document parser.

## Phase 11: Human approval flow

Objectives:

- Add a review step before creating Jira cards.
- Allow the user to approve, reject, or request changes.
- Keep a record of the generated proposal.

Deliverables:

- Approval workflow in n8n.
- Refinement preview.
- Approval status handling.

## Phase 12: Demo scenario

Objectives:

- Build a complete demo using the B2B debit card request flow.
- Show the full path from epic and documentation to refined Jira cards.

Demo case:

```txt
B2B debit card request flow for individuals and legal entities.

Deliverables:

* Sample epic.
* Sample functional document.
* Generated cards.
* Architecture explanation.
* Demo script.

:::

## Cómo estos archivos nos ayudan en la implementación

`architecture.md` nos evita improvisar. Cada vez que vayamos a crear algo nuevo, nos preguntamos: “¿esto es un agente, una skill, un servicio, un workflow de n8n o una integración externa?”. Eso mantiene el proyecto ordenado.

`roadmap.md` nos da el camino. En vez de empezar directo con Jira + Drive + LLM + RAG + agentes todo junto, vamos por fases. Primero mock, luego backend, luego n8n, después documentos, después LLM, después RAG, y recién después Jira real. Mucho más sano.

Mi recomendación ahora: pega esos dos archivos, haz commit, y el próximo paso sería crear la estructura base del backend con FastAPI.