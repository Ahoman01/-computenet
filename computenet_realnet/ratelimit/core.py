import time

WINDOW = {}
LIMIT = 20

def check_rate_limit(identity):

    now = int(time.time())

    WINDOW.setdefault(identity, [])

    WINDOW[identity] = [
        t for t in WINDOW[identity]
        if now - t < 60
    ]

    if len(WINDOW[identity]) >= LIMIT:

        return {
            "allowed": False,
            "reason": "rate_limit_exceeded",
            "requests": len(WINDOW[identity])
        }

    WINDOW[identity].append(now)

    return {
        "allowed": True,
        "requests": len(WINDOW[identity])
    }
