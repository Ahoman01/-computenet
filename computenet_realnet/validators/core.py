import secrets
import time
import socket
from computenet_realnet.storage.state import load, save

def register_validator(address):
    validators = load("validators")
    validator = {
        "validator_id": "val_" + secrets.token_hex(8),
        "address": address,
        "hostname": socket.gethostname(),
        "score": 100,
        "validated": 0,
        "slashed": 0,
        "created_at": int(time.time())
    }
    validators.append(validator)
    save("validators", validators)
    return validator

def list_validators():
    return load("validators")
