# Find Similar Phrases
Fast API endpoint to find phrases similar to a provided phrase from a set of phrases

## Getting started

### Virtual Environment
The Makefile takes care of setting up a virtual environment at `venv` path on the repo. It can be cleaned up using `make clean` command. To recreate the virtual environment, please run `ensure-venv` command.

### Jupyter
Use the make command `make start-jupyter` to start jupyter server. Word2Vec.ipynb in the notebooks directory contains the solutions to the given problem in an easily readable form.

### Running server locally
Use the make command `make start-server` to start a FastAPI server locally. The server runs on 8000 port and accepts GET requests. \
Refer to the sample request and response below.

### Running in Docker
Use command `make start-docker` to start containers using compose. Please note that the vectors CSV is huge and it takes quite some time to build the docker image. 

Please refer to the Makefile for more commands.

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

## Potential improvements

There are some problems with the architecture of the solution. It time permits, the following points can be taken up to improve performance and reliability of the solution.

- Storing phrases and embeddings externally in a VectorDB
- Separate the embedding generation service as a separate deployment, as it is potentially very large and can slow down deployments for the closest phrases service
- Ensuring we are using correct vector operations and the most optimal implementation of these operations