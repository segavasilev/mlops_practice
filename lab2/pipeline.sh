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
python3 -m venv PROJECT_SOURCE_PATH/venv

# Activate the virtual environment
source PROJECT_SOURCE_PATH/venv/bin/activate

# Install the required packages
pip install -r PROJECT_SOURCE_PATH/lab2/requirements.txt

# Go to the source code directory
cd PROJECT_SOURCE_PATH/lab2

echo "Done"