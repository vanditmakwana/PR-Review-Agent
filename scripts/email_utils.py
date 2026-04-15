import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, review, repo, pr_number):
    sender = os.environ["EMAIL_USER"]
    password = os.environ["EMAIL_PASS"]

    receivers = [
        "dhruvrathod0730@gmail.com"
    ]

    # 🎨 HTML Email Template
    html_content = f"""
    <html>
    <body style="font-family: Arial; background-color:#f4f4f4; padding:20px;">
        
        <div style="max-width:700px; margin:auto; background:white; padding:20px; border-radius:10px;">
            
            <h2 style="color:#4CAF50;">🚀 PR Review Report</h2>

            <p><b>Repository:</b> {repo}</p>
            <p><b>PR Number:</b> #{pr_number}</p>

            <hr>

            <h3 style="color:#e74c3c;">🔍 Issues & Analysis</h3>
            <div style="background:#fdecea; padding:10px; border-radius:5px; white-space: pre-wrap;">
                {review}
            </div>

            <hr>

            <a href="https://github.com/{repo}/pull/{pr_number}" 
               style="display:inline-block; padding:10px 15px; background:#3498db; color:white; text-decoration:none; border-radius:5px;">
               🔗 View Pull Request
            </a>

        </div>

    </body>
    </html>
    """

    # 📧 Create email
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)

    msg.attach(MIMEText(html_content, "html"))

    # 🚀 Send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receivers, msg.as_string())

        print("✅ Styled email sent successfully")

    except Exception as e:
        print("❌ Email failed:", str(e))