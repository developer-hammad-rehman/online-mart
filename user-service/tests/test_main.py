from app.settings import TEST_DATA_BASE_URL
from app.main import app
from app.db import get_session, Session , engine, create_engine , SQLModel
from fastapi.testclient import TestClient

#==============================================================================================================

connection_string = str(TEST_DATA_BASE_URL).replace(
    "postgresql", "postgresql+psycopg2"
)


#==============================================================================================================


engine = create_engine(connection_string, echo=True)

#==============================================================================================================

SQLModel.metadata.drop_all(engine)

#==============================================================================================================

SQLModel.metadata.create_all(engine)

#==============================================================================================================

client = TestClient(app=app)

#==================================================================================================================

def get_test_session():
    with Session(engine) as session:
        yield session

#=========================================================================================================

app.dependency_overrides[get_session] = get_test_session


#===========================================================================================================

def test_route_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


#===============================================================================================


def test_health_route():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


#=================================================================================================================================

def test_version_route():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version" : "1.0.0"}


#==================================================================================================================================

def test_info_route():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"app_name" : "User Service" , "app_version" : "1.0.0"}


#==================================================================================================================================

def test_register_route():
    response = client.post("/register" , data={"username":"hammadrehman7000@gmail.com" , "password":"hammad"})
    assert response.status_code == 200
    assert "username" in response.json()


#==================================================================================================================================



def test_login_route():
    response = client.post("/login", data={"username":"hammadrehman7000@gmail.com", "password":"hammad"})
    global access_token
    access_token = response.json()["access_token"]
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()

#========================================================================================================================================


def test_oauth_token_route():
    response = client.post("/oauth-token" , data={"grant_type":"authorization_code" , "code":access_token})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()



#=================================================================================================================================================================================


def test_update_username_route():
    response = client.patch("/update-username" , json={"username":"hammadrehman7000@gmail.com" , "password":"hammad" , "new_username":"hammadrehman208@gmail.com"})
    assert response.status_code == 200


#=============================================================================================================================================================================



def test_delete_account_route():
    response = client.delete("/delete-account?username=hammadrehman208@gmail.com")
    assert response.status_code == 200


#========================================================================================================================================================================================