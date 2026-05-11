#!/bin/bash

source .venv/bin/activate

python -m computenet_realnet.cli.main wallet
python -m computenet_realnet.cli.main genesis
python -m computenet_realnet.cli.main mine
python -m computenet_realnet.cli.main balance
