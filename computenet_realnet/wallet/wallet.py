import hashlib
import secrets

def create_wallet():
    key = secrets.token_hex(32)
    address = "cmp_" + hashlib.sha256(key.encode()).hexdigest()[:40]
    return {
        "private_key": key,
        "address": address
    }
