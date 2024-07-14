from app.settings import ADMIN_USERNAME , ADMIN_PASSWORD


def verify_username(username):
    return username == ADMIN_USERNAME

def verify_password(password):
    return password == ADMIN_PASSWORD 

