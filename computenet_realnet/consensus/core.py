import hashlib
import json
import time
from computenet_realnet.storage.state import load, save

DIFFICULTY_PREFIX = "0000"

def sha(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

def validate_block(block, previous=None):
    test = dict(block)
    stored = test.pop("hash", None)
    if sha(test) != stored:
        return False, "hash_mismatch"
    if previous and block.get("previous_hash") != previous.get("hash"):
        return False, "broken_previous_hash"
    return True, "valid"

def validate_chain():
    chain = load("chain")
    for i, block in enumerate(chain):
        previous = chain[i - 1] if i else None
        ok, reason = validate_block(block, previous)
        if not ok:
            return {"valid": False, "height": i, "reason": reason}
    return {"valid": True, "blocks": len(chain)}

def genesis():
    chain = load("chain")
    if chain:
        return {"status": "exists", "height": len(chain) - 1}
    block = {
        "height": 0,
        "timestamp": int(time.time()),
        "previous_hash": "0" * 64,
        "message": "ComputeNet fair public genesis candidate - no premine, no ICO, no founder allocation",
        "reward": 0,
        "receipts": [],
        "transactions": [],
        "nonce": 0
    }
    block["hash"] = sha(block)
    save("chain", [block])
    return {"status": "created", "block": block}
