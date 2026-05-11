import hashlib
import time

from computenet_realnet.reality.adapters.base import RealityAdapter

class SimulatedAdapter(RealityAdapter):

    def execute(self, payload: str):
        return {
            "mode": "simulated",
            "output": payload[:200],
            "proof": hashlib.sha256(payload.encode()).hexdigest(),
            "elapsed": 0.001
        }

    def metadata(self):
        return {
            "adapter": "simulated",
            "deterministic": True,
            "distributed": False
        }
