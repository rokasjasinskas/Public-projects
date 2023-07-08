import requests
from bs4 import BeautifulSoup

main_url = "https://www.supergarden.lt"  # Replace with the main website URL

response = requests.get(main_url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
links = []

for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)

# Process the extracted links as needed
print(links)
