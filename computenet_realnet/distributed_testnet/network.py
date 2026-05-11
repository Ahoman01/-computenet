import secrets
import time

NODES = []

def register_node(hostname, region, role):

    node = {
        "node_id": "node_" + secrets.token_hex(8),
        "hostname": hostname,
        "region": region,
        "role": role,
        "status": "online",
        "created_at": int(time.time())
    }

    NODES.append(node)

    return node

def list_nodes():

    return NODES

def network_status():

    return {
        "distributed_nodes": len(NODES),
        "regions": list(set([n["region"] for n in NODES])),
        "roles": list(set([n["role"] for n in NODES])),
        "status": "distributed_testnet_candidate"
    }
