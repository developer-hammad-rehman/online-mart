from starlette.config import Config


try:
    config = Config(".env")

except FileNotFoundError:
    config = Config()


STRIPE_KEY = config("STRIPE_KEY", cast=str)
KAFKA_NOTIFICATION_TOPIC = config("KAFKA_NOTIFICATION_TOPIC", cast=str)
KAFKA_BOOTSTRAP_SERVERS = config("KAFKA_BOOTSTRAP_SERVERS", cast=str)
DATA_BASE_URL = config("DATA_BASE_URL", cast=str)