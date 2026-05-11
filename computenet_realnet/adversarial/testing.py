def adversarial_suite():

    return {
        "tests": [
            "replay_attack",
            "spam_attack",
            "fake_provider",
            "invalid_receipt",
            "validator_collusion",
            "fork_attempt",
            "duplicate_execution",
            "malicious_payload"
        ],
        "status": "ready"
    }
