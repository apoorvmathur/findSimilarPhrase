# Find Similar Phrases
Fast API endpoint to find phrases similar to a provided phrase from a set of phrases

## Getting started
#### Jupyter
Use the make command `make start-jupyter` to start jupyter server. Word2Vec.ipynb in the notebooks directory contains the solutions to the given problem in an interactive form.

#### Running server locally
Use the make command `make start-server` to start a FastAPI server locally.

#### Running in Docker [Some issues with image size]
Use command `make start-docker` to start containers using compose.

## Sample request

```bash
curl --location '127.0.0.1:8000/phrases?phrase=what%20is%20the%20most%20profitable%20company%20in%20india' \
--data ''
```

Response:

```json
{
    "phrase": "most profitable insurance company India",
    "distance": 0.45201218609561494
}
```
