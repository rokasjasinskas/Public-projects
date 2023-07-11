import requests
import json
from bs4 import BeautifulSoup

def scrape_price():
    url = "https://www.summmer.lt/en/freeze-dried-fruits-and-berries"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    price_element = soup.find(class_="product-item-price")
    if price_element is not None:
        price = price_element.text.strip()
    else:
        price = "Price not found"
    return price

price = scrape_price()

data = {"price": price}

with open("data.json", "w") as json_file:
    json.dump(data, json_file)
