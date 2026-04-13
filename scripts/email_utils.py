import smtplib
import os
from email.mime.text import MIMEText

def send_email(subject, body):
    sender = os.environ["EMAIL_USER"]
    password = os.environ["EMAIL_PASS"]

    receivers = [
        "teammember1@gmail.com",
        "teammember2@gmail.com"
    ]

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receivers, msg.as_string())

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Email failed:", str(e))