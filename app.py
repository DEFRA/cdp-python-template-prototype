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
    logger.info(f"environment: {Confg.environment}")
    logger.info(f"agent_endpoint: {Confg.agent_endpoint}")
    logger.info(f"service_name: {Confg.service_name}")
    logger.info(f"namespace: {Confg.namespace}")
    logger.info(f"log_group_name: {Confg.log_group_name}")
    logger.info(f"log_stream_name: {Confg.log_stream_name}")
    logger.info(f"ec2_metadata_endpoint: {Confg.ec2_metadata_endpoint}")
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
