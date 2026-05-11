import platform

def gpu_info():

    return {
        "gpu_available": False,
        "current_mode": "placeholder",
        "future_targets": [
            "cuda",
            "metal",
            "mlx",
            "torch",
            "distributed_vram"
        ],
        "system": platform.platform()
    }
