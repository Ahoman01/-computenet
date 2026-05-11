import secrets
import time
from computenet_realnet.storage.state import load, save

def add_peer(url, region="unknown"):
    peers = load("peers")
    peer = {
        "peer_id": "peer_" + secrets.token_hex(8),
        "url": url,
        "region": region,
        "status": "known",
        "created_at": int(time.time())
    }
    peers.append(peer)
    save("peers", peers)
    return peer

def list_peers():
    return load("peers")

def sync_plan():
    return {
        "strategy": "pull_then_validate",
        "requires": [
            "independent_nodes",
            "chain_validation",
            "execution_replay_checks",
            "peer_rate_limits"
        ],
        "peers": list_peers()
    }
