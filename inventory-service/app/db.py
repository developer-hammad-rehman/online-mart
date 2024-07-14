from sqlmodel import create_engine, SQLModel, Session
from app.models import *
from app.settings import DATABASE_URL

connection_string = str(DATABASE_URL).replace("postgresql", "postgresql+psycopg2")

engine = create_engine(connection_string, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session