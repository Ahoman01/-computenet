import hashlib
import subprocess
import json
import time

class OllamaAdapter:

    def execute(self, model: str, prompt: str):

        try:
            start = time.time()

            result = subprocess.check_output(
                ["ollama", "run", model, prompt],
                stderr=subprocess.DEVNULL,
                timeout=120
            ).decode().strip()

            elapsed = round(time.time() - start, 4)

            return {
                "mode": "ollama_real",
                "model": model,
                "result": result[:4000],
                "proof": hashlib.sha256(result.encode()).hexdigest(),
                "elapsed": elapsed
            }

        except Exception as e:

            return {
                "mode": "ollama_error",
                "error": str(e)
            }
