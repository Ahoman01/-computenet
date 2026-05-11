from fastapi import FastAPI
from pydantic import BaseModel

from computenet_realnet.execution.core import execute_job, list_executions
from computenet_realnet.distributed_testnet.network import (
    register_node,
    list_nodes,
    network_status
)
from computenet_realnet.replay.protection import replay_protect
from computenet_realnet.ratelimit.core import check_rate_limit
from computenet_realnet.peer_scoring.core import (
    update_peer,
    peer_scores
)
from computenet_realnet.attestations.core import (
    attest,
    list_attestations
)
from computenet_realnet.adversarial.testing import adversarial_suite

app = FastAPI(title="ComputeNet Distributed Testnet")

class JobIn(BaseModel):
    kind: str
    payload: str
    model: str = "auto"
    mode: str = "local_real"

class NodeIn(BaseModel):
    hostname: str
    region: str
    role: str

class AttestationIn(BaseModel):
    execution_id: str
    validator: str
    proof: str

@app.get("/")
def root():

    return {
        "network": "ComputeNet",
        "epoch": "Distributed Testnet + Hardening",
        "stage": "public_testnet_candidate"
    }

@app.post("/node")
def api_node(node: NodeIn):

    return register_node(
        node.hostname,
        node.region,
        node.role
    )

@app.get("/nodes")
def api_nodes():

    return list_nodes()

@app.get("/network-status")
def api_network_status():

    return network_status()

@app.post("/execute")
def api_execute(job: JobIn):

    replay = replay_protect(job.payload)

    if not replay["allowed"]:
        return replay

    limit = check_rate_limit("global")

    if not limit["allowed"]:
        return limit

    return execute_job(
        job.kind,
        job.payload,
        job.model,
        job.mode
    )

@app.get("/executions")
def api_executions():

    return list_executions()

@app.post("/peer-success")
def api_peer_success(peer_id: str):

    return update_peer(peer_id, True)

@app.post("/peer-failure")
def api_peer_failure(peer_id: str):

    return update_peer(peer_id, False)

@app.get("/peer-scores")
def api_peer_scores():

    return peer_scores()

@app.post("/attest")
def api_attest(data: AttestationIn):

    return attest(
        data.execution_id,
        data.validator,
        data.proof
    )

@app.get("/attestations")
def api_attestations():

    return list_attestations()

@app.get("/adversarial-suite")
def api_adversarial():

    return adversarial_suite()
