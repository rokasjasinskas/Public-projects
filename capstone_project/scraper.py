from bs4 import BeautifulSoup
import requests

# Define the URL of the website to scrape
url = 'https://www.supergarden.lt/lt/katalogas'

# Send an HTTP GET request to the website and retrieve the HTML content
response = requests.get(url)
content = response.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all product elements on the page
product_elements = soup.find_all('div', class_='product_element')

# Iterate over the product elements and extract the desired information
for product_element in product_elements:
    # Extract product URL
    product_url = product_element.find('a', class_='photo-wrp')['href']

    # Extract product name
    span_element = product_element.find('span', class_='')
    product_name = span_element.text.strip()

    # Extract product price
    product_price = product_element.find('span', class_='price').text.strip()

    # Print the extracted information for each product
    print("Product URL:", product_url)
    print("Product Name:", product_name)
    print("Product Price:", product_price)
    print("------------------------")
