#!/bin/bash

# Create a Conda environment
conda create -n feature_annotation_env python=3.8
conda activate feature_annotation_env

# Install dependencies
conda install -y -c conda-forge bash requests pandas beautifulsoup4

# Install your tool
pip install .

# Deactivate the Conda environment
conda deactivate