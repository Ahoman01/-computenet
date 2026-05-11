from computenet_realnet.chain.blockchain import validate_chain

def validate():
    return {
        "valid": validate_chain()
    }
