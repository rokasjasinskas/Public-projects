import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

main_url = "https://www.supergarden.lt"  # Replace with the main website URL

response = requests.get(main_url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
links = []

for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)

# Clean the links
links = list(set(links))
links = [link for link in links if link]
irrelevant_keywords = ["facebook", "instagram", "mailto", "tel:"]
cleaned_links = [link for link in links if not any(keyword in link for keyword in irrelevant_keywords)]

# Join cleaned links with the main URL
full_links = [urljoin(main_url, link) for link in cleaned_links]

print("Full URLs:")
for link in full_links:
    print(link)