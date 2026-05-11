import hashlib
import time

from computenet_realnet.reality.adapters.base import RealityAdapter

class LocalRealAdapter(RealityAdapter):

    def execute(self, payload: str):
        start = time.time()

        x = payload

        for _ in range(25000):
            x = hashlib.sha256(x.encode()).hexdigest()

        elapsed = round(time.time() - start, 6)

        return {
            "mode": "local_real",
            "proof": x,
            "elapsed": elapsed
        }

    def metadata(self):
        return {
            "adapter": "local_real",
            "deterministic": True,
            "distributed": False
        }
