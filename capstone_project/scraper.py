from bs4 import BeautifulSoup
import requests

# Define the URLs of the websites to scrape
urls = ['https://www.supergarden.lt/lt/katalogas', 'https://www.supergarden.lt/lt/katalogas?&page=2']

def scrape(url):
    # Send an HTTP GET request to the website and retrieve the HTML content
    response = requests.get(url)
    content = response.text

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # Find all product elements on the page
    product_elements = soup.find_all('div', class_='product_element')

    # Create an empty list to store the products
    product_list = []

    # Iterate over the product elements and extract the desired information
    for product_element in product_elements:
        # Extract product URL
        product_url = product_element.find('a', class_='photo-wrp')['href']

        # Extract product name
        span_element = product_element.find('span', class_='')
        product_name = span_element.text.strip()

        # Extract product price
        product_price = product_element.find('span', class_='price').text.strip()

        # Create a dictionary to store the product information
        product = {
            "Product Name": product_name,
            "Product Price": product_price,
            "Product URL": product_url
        }

        # Add the product to the product list
        product_list.append(product)

    # Return the product list
    return product_list

def main():
    # Create an empty list to store all products from different pages
    all_products = []

    # Iterate over the URLs and call the scrape function for each URL
    for url in urls:
        products = scrape(url)
        all_products.extend(products)

    # Print the extracted information for each product
    for product in all_products:
        print("Product URL:", product["Product URL"])
        print("Product Name:", product["Product Name"])
        print("Product Price:", product["Product Price"])
        print("------------------------")


if __name__ == "__main__":
    main()
