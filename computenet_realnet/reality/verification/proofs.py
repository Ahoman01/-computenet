import hashlib
import json

def proof_of_execution(data):

    encoded = json.dumps(
        data,
        sort_keys=True
    ).encode()

    return hashlib.sha256(encoded).hexdigest()

def verify_execution(data, proof):

    return proof_of_execution(data) == proof
