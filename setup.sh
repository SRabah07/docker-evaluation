#!/bin/bash

echo "Building Docker image of the API test... "
docker image build . -t ml-sentiment-api-test:0.0.1 

echo "Start the ML sentiment analysis API Docker image and pubslishes on port 8200"
docker container run -p 8200:8000 -it -d --rm datascientest/fastapi:1.0.0

echo "Start a docker image for API testing: it will test the authentication."
docker container run -it --name api-test-v2 -d --env-file=.env ml-sentiment-api-test:0.0.1

