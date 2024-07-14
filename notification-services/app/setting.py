from starlette.config import Config


try:
    config = Config(".env")

except FileNotFoundError:
    config = Config()

EMAIL = config.get("EMAIL", cast=str)
PASSWORD = config.get("PASSWORD", cast=str)
KAFKA_TOPIC = config.get("KAFKA_TOPIC", cast=str)
KAFKA_GROUP_ID = config.get("KAFKA_GROUP_ID", cast=str)
KAFKA_BOOTSTRAP_SERVERS = config.get("KAFKA_BOOTSTRAP_SERVERS", cast=str)