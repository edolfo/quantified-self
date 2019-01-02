#!/usr/bin/env bash

docker-compose -p hckrlabs-quant-self -f ./build/docker-compose.yml down

if [ "$(docker network inspect hckrlabs-quant-self --format "{{range .Containers}}T{{end}}")" == "" ]; then
docker network rm hckrlabs-quant-self
fi

docker rmi hckrlabs-quant-self_app
