from fastapi.testclient import TestClient
from app import settings
from app.main import app
from app.db_config import get_session , Session , SQLModel , create_engine

connnection_string = str(settings.TEST_DATA_BASE_URL).replace(
    "postgresql" , "postgresql+psycopg2"
)

engine = create_engine(connnection_string, echo=True)



def get_test_session():
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_session] = get_test_session

SQLModel.metadata.drop_all(engine)

SQLModel.metadata.create_all(engine)


client = TestClient(app)


def test_main_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Payemmt Service"}



def test_check_out():
    response = client.get("/checkout?amount=20&quantity=1&product_name=Shirt")
    assert response.status_code == 307