from computenet_realnet.consensus.core import genesis, validate_chain
from computenet_realnet.economics.core import economics

def test_genesis_and_validate():
    genesis()
    assert validate_chain()["valid"] is True

def test_no_premine():
    e = economics()
    assert e["premine"] == 0
    assert e["ico"] is False
    assert e["founder_allocation"] == 0
