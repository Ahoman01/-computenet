PEERS = {}

def update_peer(peer_id, success=True):

    PEERS.setdefault(peer_id, {
        "score": 100,
        "success": 0,
        "failures": 0
    })

    if success:
        PEERS[peer_id]["score"] += 1
        PEERS[peer_id]["success"] += 1
    else:
        PEERS[peer_id]["score"] -= 10
        PEERS[peer_id]["failures"] += 1

    return PEERS[peer_id]

def peer_scores():

    return PEERS
