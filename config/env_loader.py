import os
from dotenv import load_dotenv


def load_environment():
    load_dotenv()
    env = {
        "generator_base": os.getenv("GENERATOR_BASE_URL"),
        "generator_model": os.getenv("GENERATOR_MODEL"),
        "generator_key": os.getenv("GENERATOR_API_KEY"),
    }
    for k, v in env.items():
        if not v:
            raise ValueError(f"Missing environment variable: {k}")
    return env