import hashlib
from computenet_realnet.storage.state import event

def sybil_score(address, providers_count, validators_count):
    score = max(0, 100 - ((providers_count + validators_count) * 5))
    return {"address": address, "sybil_resistance_score": score}

def replay_guard(payload_hash, known_hashes):
    replay = payload_hash in known_hashes
    return {"replay_detected": replay}

def workload_guard(kind, payload):
    blocked_terms = ["malware", "exploit", "credential theft", "phishing"]
    text = payload.lower()
    blocked = any(term in text for term in blocked_terms)
    decision = "deny" if blocked else "allow"
    event("workload_guard", {"kind": kind, "decision": decision})
    return {"decision": decision, "blocked": blocked}

def dos_guard(queue_size):
    return {"decision": "throttle" if queue_size > 1000 else "allow", "queue_size": queue_size}

def fingerprint(data):
    return hashlib.sha256(str(data).encode()).hexdigest()
