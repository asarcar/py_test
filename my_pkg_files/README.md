# Utilities and tools

This package covers common utilities we use to develop our software. 

## Package tutorial instructions
https://packaging.python.org/en/latest/tutorials/packaging-projects/ 

## Setup and clenup environment
export MY_PKG_DIR=/tmp/dist
rm -fr $MY_PKG_DIR 
mkdir -p $MY_PKG_DIR

## Build
python3 -m build --outdir $MY_PKG_DIR

## API-Key
get the api-key from your account in https://test/pypi.org and copy it to $HOME/.pypirc
[testpypi]
  username = __token__
  password = ** fill in API-KEY here **

## Upload
python3 -m twine upload --repository testpypi $MY_PKG_DIR/*

## Installation
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps utils_asarcar

