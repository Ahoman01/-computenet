import json
from pathlib import Path

checks = {
    "protocol_config": Path("computenet_realnet/config/protocol.json").exists(),
    "fair_launch_docs": Path("computenet_realnet/docs/FAIR_LAUNCH.md").exists(),
    "mainnet_gap_docs": Path("computenet_realnet/docs/PRODUCTION_MAINNET_GAP.md").exists(),
    "open_source_strategy": Path("computenet_realnet/docs/OPEN_SOURCE_STRATEGY.md").exists(),
    "node_api": Path("computenet_realnet/node/api.py").exists(),
    "cli": Path("computenet_realnet/cli/main.py").exists(),
    "storage": Path("computenet_realnet/storage/state.py").exists(),
    "consensus": Path("computenet_realnet/consensus/core.py").exists(),
    "execution": Path("computenet_realnet/execution/core.py").exists(),
    "security": Path("computenet_realnet/security/hardening.py").exists()
}

print(json.dumps({
    "stage": "realnet_alpha",
    "mainnet_ready": False,
    "checks": checks,
    "passed": sum(1 for v in checks.values() if v),
    "total": len(checks)
}, indent=2))
