from starlette.config import Config


try:
    config = Config(".env")

except FileNotFoundError:
    config = Config()


STRIPE_KEY = config("STRIPE_KEY", cast=str)
KAFKA_NOTIFICATION_TOPIC = config("KAFKA_NOTIFICATION_TOPIC", cast=str)
KAFKA_BOOTSTRAP_SERVER = config("KAFKA_BOOTSTRAP_SERVER", cast=str)
DATA_BASE_URL = config("DATA_BASE_URL", cast=str)
KAFKA_TOPIC = config("KAFKA_TOPIC", cast=str)
KAFKA_GROUP_ID = config("KAFKA_GROUP_ID", cast=str)
KAFKA_CONNECTION_STRING  = config("KAFKA_CONNECTION_STRING", cast=str)
TEST_DATA_BASE_URL = config("TEST_DATA_BASE_URL" , cast=str)