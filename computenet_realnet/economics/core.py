from computenet_realnet.storage.state import load

BASE_PRICES = {
    "embedding": 3,
    "classify": 1,
    "benchmark": 5,
    "ollama": 10,
    "agent": 8,
    "gpu": 50
}

def economics():
    data = load("economics")
    data["base_prices"] = BASE_PRICES
    data["legal_posture"] = {
        "no_premine": True,
        "no_ico": True,
        "no_founder_allocation": True,
        "no_investment_promise": True,
        "utility_first": True
    }
    return data
