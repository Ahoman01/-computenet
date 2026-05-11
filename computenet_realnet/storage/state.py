from pathlib import Path
import json
import time

ROOT = Path(".computenet_realnet")
ROOT.mkdir(exist_ok=True)

FILES = {
    "chain": ROOT / "chain.json",
    "peers": ROOT / "peers.json",
    "jobs": ROOT / "jobs.json",
    "executions": ROOT / "executions.json",
    "providers": ROOT / "providers.json",
    "validators": ROOT / "validators.json",
    "receipts": ROOT / "receipts.json",
    "reputation": ROOT / "reputation.json",
    "security_events": ROOT / "security_events.json",
    "economics": ROOT / "economics.json"
}

DEFAULTS = {
    "chain": [],
    "peers": [],
    "jobs": [],
    "executions": [],
    "providers": [],
    "validators": [],
    "receipts": [],
    "reputation": {},
    "security_events": [],
    "economics": {
        "coin": "COMPUTE",
        "supply_cap": 21000000,
        "premine": 0,
        "ico": False,
        "founder_allocation": 0,
        "reward_policy": "fair_public_mining_only"
    }
}

def load(name):
    path = FILES[name]
    if not path.exists():
        save(name, DEFAULTS[name])
    return json.loads(path.read_text())

def save(name, data):
    FILES[name].write_text(json.dumps(data, indent=2))

def event(kind, payload):
    events = load("security_events")
    events.append({
        "kind": kind,
        "payload": payload,
        "created_at": int(time.time())
    })
    save("security_events", events)
    return events[-1]
