from starlette.config import Config

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()


DATABASE_URL = config("DATABASE_URL", cast=str)
KAFKA_PORT = config("KAFKA_PORT", cast=str)
