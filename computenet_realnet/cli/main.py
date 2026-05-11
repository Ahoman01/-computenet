import json
import sys

from computenet_realnet.wallet.wallet import create_wallet
from computenet_realnet.chain.blockchain import (
    create_genesis,
    balance,
    load_chain
)
from computenet_realnet.mining.miner import mine
from computenet_realnet.validators.validator import validate

WALLET_FILE = "computenet_realnet/data/wallet.json"

def save_wallet(wallet):
    with open(WALLET_FILE, "w") as f:
        json.dump(wallet, f, indent=2)

def load_wallet():
    with open(WALLET_FILE) as f:
        return json.load(f)

cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

if cmd == "wallet":
    wallet = create_wallet()
    save_wallet(wallet)
    print(json.dumps(wallet, indent=2))

elif cmd == "genesis":
    print(json.dumps(create_genesis(), indent=2))

elif cmd == "mine":
    wallet = load_wallet()
    print(json.dumps(mine(wallet["address"]), indent=2))

elif cmd == "balance":
    wallet = load_wallet()
    print(json.dumps({
        "address": wallet["address"],
        "balance": balance(wallet["address"])
    }, indent=2))

elif cmd == "validate":
    print(json.dumps(validate(), indent=2))

elif cmd == "status":
    chain = load_chain()

    print(json.dumps({
        "network": "ComputeNet",
        "coin": "COMPUTE",
        "blocks": len(chain),
        "supply": sum(b["reward"] for b in chain),
        "valid": validate()["valid"]
    }, indent=2))

else:
    print("""
Commands:

wallet
genesis
mine
balance
validate
status
""")
