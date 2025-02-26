#!/bin/bash

# Variables
IMAGE_NAME="recalde/sql-to-parquet"
IMAGE_TAG="latest"

# Build the Docker image
docker build -t $IMAGE_NAME:$IMAGE_TAG .

# Push the Docker image to Docker Hub
docker push $IMAGE_NAME:$IMAGE_TAG