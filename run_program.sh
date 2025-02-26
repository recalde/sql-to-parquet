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
pip install -r src/requirements.txt

# Run the Python script
python src/main.py

# Deactivate the virtual environment
deactivate