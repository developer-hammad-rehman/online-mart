from starlette.config import Config

try:
    config = Config(".env")

except FileNotFoundError:
    config = Config()

DATA_BASE_URL= config("DATABASE_URL" , cast=str)
SECRET_KEY = config("SECRET_KEY", cast=str)
ALGORITHM = config("ALGORITHM", cast=str)
KONG_ADMIN_URL = config("KONG_ADMIN_URL", cast=str)
ADMIN_USERNAME = config("ADMIN_USERNAME", cast=str)
ADMIN_PASSWORD= config("ADMIN_PASSWORD", cast=str)
ADMIN_KONG_ID = config("ADMIN_KONG_ID", cast=str)
KAFKA_NOTIFICATION_TOPIC = config("KAFKA_NOTIFICATION_TOPIC", cast=str)
KAFKA_BOOTSTRAP_SERVERS = config("KAFKA_BOOTSTRAP_SERVERS", cast=str)