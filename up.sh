#!/usr/bin/env bash

if ! docker network ls | grep -q hckrlabs-quant-self; then
docker network create hckrlabs-quant-self
fi

docker-compose -p hckrlabs-quant-self -f ./build/docker-compose.yml up -d

docker attach $(docker-compose -p hckrlabs-quant-self -f ./build/docker-compose.yml ps -q app)

