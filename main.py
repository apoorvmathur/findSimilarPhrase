from fastapi import FastAPI, Request, Depends, HTTPException, status
from contextlib import asynccontextmanager

from lookup.agents.LookupAgent import LookupAgent

WORD2VEC_MODEL_PATH = "models/GoogleNews-vectors-negative300.bin.gz"
PHRASES_FILE_PATH = "data/phrases.csv"
VECTORS_FILE_PATH = "data/vectors.csv"

lookup_agent = LookupAgent(PHRASES_FILE_PATH, VECTORS_FILE_PATH)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading word2vec model")
    lookup_agent.load()
    print("Done")
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)

@app.get("/phrases")
async def get_method(request: Request):
    params = dict(request.query_params)
    phrase = params.get('phrase')
    print(phrase)
    closest_phrase, distance = lookup_agent.get_closest_phrase(phrase)
    return {"phrase": closest_phrase, "distance": distance}


@app.get("/")
async def health_check():
    return {"status": "ok"}
