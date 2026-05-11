import json
import time
import hashlib
from pathlib import Path

CHAIN_FILE = Path("computenet_realnet/data/chain.json")

MAX_SUPPLY = 21000000
BLOCK_REWARD = 50

def load_chain():
    if not CHAIN_FILE.exists():
        return []
    return json.loads(CHAIN_FILE.read_text())

def save_chain(chain):
    CHAIN_FILE.parent.mkdir(parents=True, exist_ok=True)
    CHAIN_FILE.write_text(json.dumps(chain, indent=2))

def hash_block(block):
    encoded = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()

def create_genesis():
    chain = load_chain()

    if chain:
        return chain[0]

    genesis = {
        "index": 0,
        "timestamp": time.time(),
        "previous_hash": "0" * 64,
        "miner": "genesis",
        "reward": 0,
        "nonce": 0
    }

    genesis["hash"] = hash_block(genesis)

    chain.append(genesis)

    save_chain(chain)

    return genesis

def mine_block(address):
    chain = load_chain()

    if not chain:
        create_genesis()
        chain = load_chain()

    total_supply = sum(b["reward"] for b in chain)

    if total_supply >= MAX_SUPPLY:
        return {"error": "max supply reached"}

    previous = chain[-1]

    block = {
        "index": len(chain),
        "timestamp": time.time(),
        "previous_hash": previous["hash"],
        "miner": address,
        "reward": BLOCK_REWARD,
        "nonce": 0
    }

    block["hash"] = hash_block(block)

    chain.append(block)

    save_chain(chain)

    return block

def balance(address):
    chain = load_chain()

    total = 0

    for block in chain:
        if block.get("miner") == address:
            total += block.get("reward", 0)

    return total

def validate_chain():
    chain = load_chain()

    if not chain:
        return False

    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]

        if current["previous_hash"] != previous["hash"]:
            return False

    return True
