import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def send_email(subject, body, sender, recipients, credentials_file):
    flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=creds)
    message = MIMEText(body)
    message['to'] = ', '.join(recipients)
    message['subject'] = subject
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        sent_message = service.users().messages().send(userId="me", body=create_message).execute()
        print(f"Sent message to {sent_message['to']}. Message ID: {sent_message['id']}")
    except HttpError as error:
        print(f"An error occurred: {error}")
        sent_message = None

# Example usage
subject = "Email Subject"
body = "This is the body of the email"
sender = "burundukas.plieninis@gmail.com"
recipients = ["jasinskas.rokas@gmail.com"]
credentials_file = "/workspaces/125792805/APIs_to_Email/credentials.json"

send_email(subject, body, sender, recipients, credentials_file)
