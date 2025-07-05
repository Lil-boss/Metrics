# app/main.py
from fastapi import FastAPI
from prometheus_client import make_asgi_app
from app.middleware.metrics_middleware import MetricsMiddleware
from app.metrics.system_metrics import start_system_metrics_collection
from app.routers import api, health

app = FastAPI()

# Add middleware
app.add_middleware(MetricsMiddleware)

# Include routers
app.include_router(api.router)
app.include_router(health.router)

# Mount /metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

# Start background system metrics
@app.on_event("startup")
async def startup_event():
    start_system_metrics_collection()

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Metrics App"}
