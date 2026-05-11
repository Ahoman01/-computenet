import hashlib

SEEN = set()

def replay_protect(payload):

    fingerprint = hashlib.sha256(
        payload.encode()
    ).hexdigest()

    if fingerprint in SEEN:

        return {
            "allowed": False,
            "reason": "replay_detected",
            "fingerprint": fingerprint
        }

    SEEN.add(fingerprint)

    return {
        "allowed": True,
        "fingerprint": fingerprint
    }
