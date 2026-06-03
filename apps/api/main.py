from fastapi import FastAPI

from apps.api.routers.health_check_router import router as health_check_router
from apps.api.routers.product_refinement_router import router as product_refinement_router

app = FastAPI(
    title="GenAI Automation API",
    description="Backend API for AI-powered product refinement automation.",
    version="0.1.0",
)

app.include_router(health_check_router)
app.include_router(product_refinement_router)