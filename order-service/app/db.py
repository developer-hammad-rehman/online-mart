from sqlmodel import Session , SQLModel , create_engine
from app.settings import DATABASE_URL
from app.models import *

connection_string = str(DATABASE_URL).replace(
    "postgresql" , "postgresql+psycopg2"
)
engine = create_engine(connection_string ,echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session