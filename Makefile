
##containers
API=api

PROJECT_NAME = api-netzun
export IMAGE_DEPLOY = $(PROJECT_NAME):deploy
CONTAINER_NAME =  $(PROJECT_NAME):app"

# Basic commands for docker-compose
DOCKERCOMPOSE=docker-compose
DCRUN=$(DOCKERCOMPOSE) run
DCBUILD=$(DOCKERCOMPOSE) build
DCUP=$(DOCKERCOMPOSE) up
DCDOWN=$(DOCKERCOMPOSE) down
DCRESTART=$(DOCKERCOMPOSE) restart

# Basic commands for pipenv
PIPENV=$(DCRUN) $(API) pipenv
PEVINSTALL=$(DCRUN) $(API) pipenv install
PERUN=$(DCRUN) $(API) pipenv run

# Basic commands for django project
DJANGOMANAGE=$(PERUN) python /code/application/manage.py


### Containers commands ###

up: ## Run container on background
	cd container/ && $(DCUP) -d

stop:
	cd container/ && $(DCDOWN)

ssh: ## Connect with container
	cd container/ && $(DCRUN) $(API) bash


build: ## Build image
	docker build -f container/build/Dockerfile --no-cache -t $(IMAGE_DEPLOY) .

serve: ## Serve develop server
	cd container/ && $(DCUP)


restart: ## Restart all stopped and running containers
	cd container/ && $(DCRESTART)

### Project commands ###

install:  ## Install all package from Pepfile
	@make build
	cd container/ && $(PEVINSTALL)


test: ## Run tests
	# Run your tests
	echo "Testme"

start: ## start project
	@make build
	@make up
### Django commands ###


migrate:  ## Run migrations
	cd container/ && $(DJANGOMANAGE) migrate
