import requests
import re

# Define the website URL
website_url = "https://www.supergarden.lt/lt/verslui"  # Replace with the desired website URL

# Send an HTTP GET request to the website
response = requests.get(website_url)
html_content = response.text

# Use regular expressions to extract email addresses
email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email_matches = re.findall(email_regex, html_content, re.IGNORECASE)

# Print the extracted email addresses
for email in email_matches:
    print(email)
