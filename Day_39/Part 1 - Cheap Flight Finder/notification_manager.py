from email.mime.text import MIMEText
import smtplib
import os


class NotificationManager:

    def send_email(self, message):

        msg = MIMEText(message, "plain", "utf-8")

        msg["Subject"] = "Cheap Flight Alert!"
        msg["From"] = os.getenv("EMAIL")
        msg["To"] = os.getenv("TO_EMAIL")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()

            connection.login(user=os.getenv("EMAIL"),password=os.getenv("EMAIL_PASSWORD"))

            connection.send_message(msg)