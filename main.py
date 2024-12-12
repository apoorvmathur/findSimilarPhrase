from fastapi import FastAPI, Request, Depends, HTTPException, status
from contextlib import asynccontextmanager

from json import loads

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initialising app")
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)

@app.get("/phrases")
async def get_method(request: Request):
    params = dict(request.query_params)
    phrase = params.get('phrase')
    print(phrase)
    return {"message": "Success"}


@app.get("/")
async def health_check():
    return {"status": "ok"}
