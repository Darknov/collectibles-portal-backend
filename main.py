from functools import lru_cache

import requests
from fastapi import FastAPI, Depends
import config

app = FastAPI()

@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
def root():
    return {"Hello": "API"}


@app.get("/info")
async def info(settings: config.Settings = Depends(get_settings)):
    return {
        "app_name": settings.admin_email
    }


@app.get("/domain/{domain}")
def get_domain(domain: str):
    response = requests.get("http://ip-api.com/json/" + domain)
    return response.json()


@app.get("/lol/{id}")
def get_lol(id: int):
    return {"REAL SLIM SHADY": id}

