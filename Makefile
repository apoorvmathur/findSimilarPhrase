.PHONY: clean build-venv rebuild-venv start-server format start-docker stop-docker

SHELL:=/bin/bash
VIRTUAL_ENV=venv
ACTIVATE_ENV=source ${VIRTUAL_ENV}/bin/activate

clean: ## >> remove all environment and build files
	@echo "Removing virtual environment"
	rm -rf $(VIRTUAL_ENV)

$(VIRTUAL_ENV):
	@echo "Create virtualenv"
	virtualenv $(VIRTUAL_ENV) -p `which python3.12`

ensure-venv: venv requirements.txt ##@main >> update requirements.txt inside the virtual environment
	@echo "Updating packages"
	$(ACTIVATE_ENV) && python3 -m pip install -r requirements.txt

start-server: ensure-venv
	@echo "Starting server locally"
	$(ACTIVATE_ENV) && uvicorn main:app --reload

start-jupyter: ensure-venv
	@echo "Starting Jupyter"
	$(ACTIVATE_ENV) && jupyter lab --NotebookApp.token='' --NotebookApp.password=''