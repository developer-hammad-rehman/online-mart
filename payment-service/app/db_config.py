from sqlmodel import create_engine , Session , SQLModel
from app.models import *

from app.settings import DATA_BASE_URL

connecting_string = str(DATA_BASE_URL).replace(
    "postgresql" , "postgresql+psycopg2"
)

engine = create_engine(connecting_string , echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)



def get_session():
    with Session(engine) as session:
        yield session