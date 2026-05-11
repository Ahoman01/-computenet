import secrets
import time
import socket
from computenet_realnet.storage.state import load, save

def register_provider(address, capabilities):
    providers = load("providers")
    provider = {
        "provider_id": "prov_" + secrets.token_hex(8),
        "address": address,
        "hostname": socket.gethostname(),
        "capabilities": capabilities,
        "reputation": 100,
        "jobs_completed": 0,
        "failed_jobs": 0,
        "created_at": int(time.time())
    }
    providers.append(provider)
    save("providers", providers)
    return provider

def list_providers():
    return load("providers")

def eligible_providers(kind):
    return [
        p for p in list_providers()
        if kind in p.get("capabilities", []) or "all" in p.get("capabilities", [])
    ]
