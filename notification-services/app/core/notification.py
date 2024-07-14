import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.setting import EMAIL , PASSWORD
from fastapi import HTTPException
from app.template_config import get_approve_template , get_login_template , get_order_complete_template , get_order_place_template ,get_register_template , custom_notification

def send_email(email: str , html_content:str):
    try:
        # Load the HTML template
        # html_content = get_register_template(email=email)
        # Replace placeholders in the template
        subject = "Welcome to our app"  # Replace with your subject
        # Create a MIME message object
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = EMAIL  # Replace with your email address
        msg['To'] = email

        # Attach HTML part to the message
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)

        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL, PASSWORD)  # Replace with your email credentials
            server.sendmail(msg['From'], msg['To'], msg.as_string())

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
    

def send_notification(notification_data:dict):
    if notification_data["type"] == "register":
        template = get_register_template(email=notification_data["email"])
        send_email(notification_data["email"], template)
    elif notification_data["type"] == "login":
        template = get_login_template(email=notification_data["email"])
        send_email(notification_data["email"], template)
    elif notification_data["type"] == "order_placed":
        template = get_order_place_template(email=notification_data["email"])
        send_email(notification_data["email"], template)
    elif notification_data["type"] == "order_completed":
        template = get_order_complete_template(email=notification_data["email"])
        send_email(notification_data["email"], template)
    else:
        raise HTTPException(status_code=400, detail="Invalid notification type")
    


def send_custom_notification(username:str , message:str):
    template = custom_notification(email=username, message=message)
    print(username , message)
    send_email(username, template)