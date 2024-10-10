from os import environ
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def root():
    region = environ.get("AWS_REGION")

    return {"region": region}
