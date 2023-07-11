import smtplib
from email.mime.text import MIMEText
from google.oauth2 import service_account
from google.auth.transport.requests import Request

def send_email(subject, body, sender, recipients, credentials_file):
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = ', '.join(recipients)

    credentials = service_account.Credentials.from_service_account_file(
        credentials_file,
        scopes=['https://www.googleapis.com/auth/gmail.send']
    )

    # Use the credentials to authorize a connection to the Gmail API
    credentials.refresh(Request())

    # Create an SMTP client and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_client:
        smtp_client.ehlo()
        smtp_client.starttls()
        smtp_client.login(sender, credentials_file)
        smtp_client.sendmail(sender, recipients, message.as_string())

    print("Email sent successfully!")

# Example usage
subject = "Email Subject"
body = "This is the body of the text message"
sender = "burundukas.plieninis@gmail.com"
recipients = ["jasinskas.rokas@gmail.com"]
credentials_file = "/workspaces/125792805/APIs_to_Email/credentials.json"

send_email(subject, body, sender, recipients, credentials_file)
