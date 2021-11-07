#!/usr/bin/env bash

DOCKER_USER=minorpatch

docker login

docker build -f ./reference-app/backend/Dockerfile ./reference-app/backend -t $DOCKER_USER/metrics-dashboard-backend
docker build -f ./reference-app/frontend/Dockerfile ./reference-app/frontend -t $DOCKER_USER/metrics-dashboard-frontend
docker build -f ./reference-app/trial/Dockerfile ./reference-app/trial -t $DOCKER_USER/metrics-dashboard-trial

docker push $DOCKER_USER/metrics-dashboard-backend
docker push $DOCKER_USER/metrics-dashboard-frontend
docker push $DOCKER_USER/metrics-dashboard-trial