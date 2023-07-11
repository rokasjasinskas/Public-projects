import base64
import requests
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from urllib.parse import urlparse, parse_qs

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def extract_authorization_code(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    authorization_code = query_params.get("code", [None])[0]
    return authorization_code

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

# Replace the authorization_url with the URL you received
authorization_url = input("Enter the authorization URL: ")
authorization_code = extract_authorization_code(authorization_url)

# Exchange authorization code for access token
flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
flow.redirect_uri = extract_authorization_code(authorization_url)
credentials = flow.fetch_token(code=authorization_code)

# Build the service object with the access token
service = build('gmail', 'v1', credentials=credentials)

# Call the send_email function
send_email

send_email(subject, body, sender, recipients, credentials_file)
