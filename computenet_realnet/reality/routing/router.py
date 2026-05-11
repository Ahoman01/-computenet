from computenet_realnet.reality.adapters.simulated import SimulatedAdapter
from computenet_realnet.reality.adapters.local_real import LocalRealAdapter
from computenet_realnet.reality.adapters.distributed import DistributedAdapter

ROUTES = {
    "simulated": SimulatedAdapter,
    "local_real": LocalRealAdapter,
    "distributed": DistributedAdapter
}

def route(mode):

    adapter = ROUTES.get(mode)

    if not adapter:
        raise ValueError("unknown adapter mode")

    return adapter()
