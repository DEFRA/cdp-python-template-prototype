from os import environ
from logging import getLogger
from contextlib import asynccontextmanager
from fastapi import FastAPI
from metrics import counter
from aws_embedded_metrics.config import get_config

Confg = get_config()
logger = getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"EMF Environment: {Confg.environment}")
    logger.info(f"EMF Agent Endpoint: {Confg.agent_endpoint}")
    logger.info(f"EMF Service Name: {Confg.service_name}")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    region = environ.get("AWS_REGION")

    logger.info(f"Region: {region}")

    counter("Root", 1)

    return {"region": region}

# Do not remove - used for health checks
@app.get("/health")
async def health():
    return {"status": "ok"}
