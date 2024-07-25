from app.settings import TEST_DATA_BASE_URL
from app.db import engine, get_session, Session, SQLModel, create_engine
from fastapi.testclient import TestClient
from app.main import app

#=============================================================================================
# This is for testing the database connection
#=============================================================================================

connection_string = str(TEST_DATA_BASE_URL).replace("postgresql", "postgresql+psycopg2")


#=============================================================================================


engine = create_engine(connection_string, echo=True)

#================================================================================================

def get_test_session():
    with Session(engine) as session:
        yield session


#=====================================================================================================

app.dependency_overrides[get_session] = get_test_session

#=====================================================================================================

client = TestClient(app)

#=======================================================================================================

SQLModel.metadata.drop_all(engine)

#======================================================================================================

SQLModel.metadata.create_all(engine)

#======================================================================================================



def test_root_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Product Service"}

#==========================================================================================================

def test_get_category_route():
    response = client.get("/get-category")
    assert response.status_code == 200

#==========================================================================================================

def test_get_items_route():
    response = client.get("/get-items")
    assert response.status_code == 200

#=============================================================================================================

def test_get_avaliable_stock_route():
    response = client.get("/get-avaliable-items")
    assert response.status_code == 200

#================================================================================================================

def test_get_hot_item_route():
    response = client.get("/get-hot-items")
    assert response.status_code == 200

#================================================================================================================

def test_get_sell_item_route():
    response = client.get("/get-sell-items")
    assert response.status_code == 200

#==================================================================================================================

def test_add_category_route():
    response = client.post(
        "/add-category", json={"name": "test", "description": "test des"}
    )
    assert response.status_code == 200


#============================================================================================================

def add_item_route():
    response = client.post(
        "/add-item",
        json={"name": "test", "description": "test des", "price": 1, "category_id": 1},
    )
    assert response.status_code == 200

#==============================================================================================================

def test_add_hot_item_route():
    response = client.post("/add-hot-item", json={"item_id": 1})
    assert response.status_code == 200

#=================================================================================================================

def test_add_avaliable_stock_route():
    response = client.post("/add-avaliable-stock", json={"item_id": 1, "quantity": 1})
    assert response.status_code == 200


#==================================================================================================================