import smtplib
from email.mime.text import MIMEText
from plyer import notification
import logging

def send_email(product_name, current_price, threshold):
    """Send an email notification when the price drops below the threshold."""
    sender = "your_email@example.com"
    receiver = "user_email@example.com"
    password = "your_password"

    subject = f"Price Alert: {product_name}"
    body = f"The price of {product_name} has dropped to ${current_price}, which is below your threshold of ${threshold}."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        logging.info(f"Email sent for {product_name}.")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def send_desktop_notification(product_name, current_price, threshold):
    """Send a desktop notification."""
    notification.notify(
        title="Price Alert",
        message=f"{product_name} is now ${current_price} (below ${threshold})",
        timeout=10,
    )
    logging.info(f"Desktop notification sent for {product_name}.")