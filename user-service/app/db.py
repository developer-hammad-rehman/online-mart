from sqlmodel  import Session , create_engine , SQLModel
from app.settings import DATA_BASE_URL
from app.models import Users

connection_string = str(DATA_BASE_URL).replace(
    "postgresql" , "postgresql+psycopg2"
)

engine = create_engine(url=connection_string , echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

