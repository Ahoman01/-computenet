#!/bin/bash

python -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install fastapi uvicorn pydantic requests
