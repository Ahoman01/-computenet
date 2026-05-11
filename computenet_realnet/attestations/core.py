import hashlib
import secrets
import time

ATTESTATIONS = []

def attest(execution_id, validator, proof):

    fingerprint = hashlib.sha256(
        proof.encode()
    ).hexdigest()

    att = {
        "attestation_id": "att_" + secrets.token_hex(8),
        "execution_id": execution_id,
        "validator": validator,
        "fingerprint": fingerprint,
        "verified": True,
        "created_at": int(time.time())
    }

    ATTESTATIONS.append(att)

    return att

def list_attestations():

    return ATTESTATIONS
