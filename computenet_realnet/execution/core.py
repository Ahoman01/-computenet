import secrets
import time

from computenet_realnet.storage.state import load, save
from computenet_realnet.reality.routing.router import route
from computenet_realnet.reality.verification.proofs import proof_of_execution

DEFAULT_MODE = "local_real"

def execute_job(kind, payload, model="auto", mode=DEFAULT_MODE):

    adapter = route(mode)

    result = adapter.execute(payload)

    proof = proof_of_execution(result)

    execution = {
        "execution_id": "exec_" + secrets.token_hex(8),
        "kind": kind,
        "mode": mode,
        "payload": payload,
        "model": model,
        "result": result,
        "proof": proof,
        "created_at": int(time.time())
    }

    executions = load("executions")

    executions.append(execution)

    save("executions", executions)

    return execution

def list_executions():

    return load("executions")
