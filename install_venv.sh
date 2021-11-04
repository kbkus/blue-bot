#!/usr/bin/env bash
# Run this script to install the virtual environment for this project.

set -e

# Create environment
VIRTUAL_ENVIRONMENT='venv-bluebot'
python3 -m venv ${VIRTUAL_ENVIRONMENT}

# Activate
. ${VIRTUAL_ENVIRONMENT}/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
