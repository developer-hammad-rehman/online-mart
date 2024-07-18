from starlette.config import Config

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()


DATABASE_URL = config("DATABASE_URL", cast=str)
KAFKA_BOOTSTRAP_SERVER = config("KAFKA_BOOTSTRAP_SERVER", cast=str)
KAFKA_TOPIC = config("KAFKA_TOPIC", cast=str)
KAFKA_CONNECTION_STRING = config("KAFKA_CONNECTION_STRING", cast=str)
KAFKA_GROUP_ID = config("KAFKA_GROUP_ID", cast=str)