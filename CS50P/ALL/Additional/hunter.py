import requests
import os
from dotenv import load_dotenv

load_dotenv()

hunter_key = os.getenv('HUNTER_KEY')


url = "https://api.hunter.io/v2/domain-search"
domain = "turingcollege.com"
company = "Turing Collage"

params = {
    "domain": domain,
    "company": company,
    "api_key": hunter_key,
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    emails = data['data']['emails']
    for email in emails:
        print(email['value'])
else:
    print(f"Request failed with status code {response.status_code}")
