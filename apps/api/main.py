from fastapi import FastAPI

app = FastAPI(
    title="GenAI Automation API",
    description="Backend API for AI-powered product refinement automation.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}