from app.settings import TEST_DATA_BASE_URL
from fastapi.testclient import TestClient
from app.main import app
from app.db import get_session ,create_engine , SQLModel , Session


connection_string = str(TEST_DATA_BASE_URL).replace("postgresql", "postgresql+psycopg2")

engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

def get_test_session():
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = get_test_session


SQLModel.metadata.drop_all(engine)

SQLModel.metadata.create_all(engine)

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Order Service"}




def test_place_order_route():
    response = client.post("/place-order", json={"product_name": "Shirt", "price": 20, "username": "hammadrehman208@gmail.com" , "quantity" :1})
    assert response.status_code == 200


def test_get_orders_route():
    response = client.get("/get-orders?username=hammadrehman208@gmail.com")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_order_route():
    response = client.delete("/delete-order?order_id=1")
    assert response.status_code == 200
    assert response.json() == {"message":"Order Deleted"}


def test_complete_order_route():
    response = client.post("/complete-order", json={"order_id": 1 , "username":"hammadrehman208@gmail.com" , "product_name":"Shirt" , "quantity":1 , "status":"complete"})
    assert response.status_code == 200
    assert response.json() == {"message": "Order completed"}