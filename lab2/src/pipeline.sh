#!/bin/bash

# This script will run the pipeline for the lab2

# Set required variables

# Path to the Jenkins home directory
JENKINS_HOME="$JENKINS_HOME"

# Path to the Jenkins workspace
JENKINS_WORKSPACE="$JENKINS_HOME/workspace"

# Path to the source code
PROJECT_SOURCE_PATH="$JENKINS_WORKSPACE/lab2"

# Create  virtual environment
python3 -m venv "$PROJECT_SOURCE_PATH/venv"

# Activate the virtual environment
source "$PROJECT_SOURCE_PATH/venv/bin/activate"

# Update pip
pip install --upgrade pip

# Install the required packages
pip install -r "$PROJECT_SOURCE_PATH/lab2/requirements.txt"

# Go to the source code directory
cd "$PROJECT_SOURCE_PATH/lab2"

echo "Running the pipeline"

echo "Running the creation of the files"
# Run the data creation script
python3 src/data_creation.py --lat 7.8804 --lon 98.3923 --alt 10.0 --start_date "2020-01-01 00:00:00" --end_date "2020-1-31 23:00:00"

echo "Running the preprocessing of the data"
# Run the data preprocessing script
python3 src/data_preprocessing.py --target_variable 'rhum'

echo "Running the model preparation"
# Run the model preparation script
python3 src/model_preparation.py

echo "Running the model testing"
# Run the model testing script
python3 src/model_testing.py

# Deactivate the virtual environment
deactivate

echo "Pipeline completed"