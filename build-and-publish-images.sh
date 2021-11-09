#!/usr/bin/env bash

DOCKER_USER=minorpatch

docker login

echo ""
echo "Docker build and publish images for backend, frontend and trial"
echo "==========================="

echo ""
echo -ne "Build and publish image for backend [ ]" 
docker build -f ./reference-app/backend/Dockerfile ./reference-app/backend -t $DOCKER_USER/metrics-dashboard-backend
docker push $DOCKER_USER/metrics-dashboard-backend
sleep .5
echo -ne "\rBuild and publish image for backend [✓]\n"

echo ""
echo -ne "Build and publish image for frontend [ ]" 
docker build -f ./reference-app/frontend/Dockerfile ./reference-app/frontend -t $DOCKER_USER/metrics-dashboard-frontend
docker push $DOCKER_USER/metrics-dashboard-frontend
sleep .5
echo -ne "\rBuild and publish image for frontend [✓]\n"

echo ""
echo -ne "Build and publish image for trial [ ]" 
docker build -f ./reference-app/trial/Dockerfile ./reference-app/trial -t $DOCKER_USER/metrics-dashboard-trial
docker push $DOCKER_USER/metrics-dashboard-trial
sleep .5
echo -ne "\rBuild and publish image for trial [✓]\n"

echo ""
echo "Done"

exit 0