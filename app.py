from os import environ
from logging import getLogger
from fastapi import FastAPI
from metrics import counter

logger = getLogger(__name__)

app = FastAPI()

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
