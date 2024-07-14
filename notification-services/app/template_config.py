
def get_register_template(email:str):
    with open("./templates/register.html" , "r") as template:
        content = template.read()
        content = content.replace("{{Email}}", email)
        return content
    


def get_login_template(email:str):
    with open("./templates/login.html" , "r") as template:
        content = template.read()
        content = content.replace("{{Email}}", email)
        return content


def get_approve_template(email:str):
    with open("./templates/approve.html", "r") as template:
        content = template.read()
        content = content.replace("{{Email}}", email)
        return content
    


def get_order_place_template(email:str):
    with open("./templates/orderplace.html", "r") as template:
        content = template.read()
        content = content.replace("{{Email}}", email)
        return content
    


    
def get_order_complete_template(email:str):
    with open("./templates/ordercomplete.html", "r") as template:
        content = template.read()
        content.replace("{{Email}}", email)
        return content
    

def custom_notification(email:str , message:str):
    with open("./templates/custom.html", "r") as template:
        content = template.read()
        content = content.replace("{{Email}}", email)
        content = content.replace("{{message}}", message)
        content = content.replace("{{CallToActionText}}", "Contact Admin")
        return content