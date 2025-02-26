#!/bin/bash

# Set environment variables
export GIT_REPO_URL="https://github.com/example/repo.git"
export CLONE_DIR="./repo_clone"
export OUTPUT_DIR="./parquet_output"

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Python script
python program.py

# Deactivate the virtual environment
deactivate

# Build Docker image
docker build -t sql-to-parquet .

# Run Docker container with environment variables
docker run -e GIT_REPO_URL="$GIT_REPO_URL" -e CLONE_DIR="$CLONE_DIR" -e OUTPUT_DIR="$OUTPUT_DIR" sql-to-parquet
