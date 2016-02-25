#!/bin/bash
echo $0: Creating virtual environment
virtualenv --prompt="<made>" ./env --python=python3

mkdir ./logs
mkdir ./db
mkdir ./static_content
mkdir ./static_content/static
mkdir ./static_content/media

echo $0: Installing dependencies
source ./env/bin/activate && ./env/bin/pip3 install --requirement=./requirements.conf --log=./logs/build_pip_packages.log

echo $0: Creating virtual environment finished.
