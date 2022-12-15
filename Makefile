ENV_FILE=.env

include ${ENV_FILE}
export

.SILENT:

## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

## install: create and start containers
.PHONY: install
install:
	docker-compose stop
	docker-compose rm -f
	docker-compose -f docker-compose.yml --env-file .env up -d --build --remove-orphans
