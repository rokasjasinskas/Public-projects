from bs4 import BeautifulSoup
import requests
import csv
from datetime import date
import re
from urllib.parse import urljoin
import sys
import getpass
import os
from dotenv import load_dotenv
import json

DOMAINS = ['www.supergarden.lt', 'www.trusthemp.eu']

load_dotenv()

# Program structure: 
# Log in to program with username and pasword hardcoded in the program. It is Local variables. 

class Login:
    def __init__(self):
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")

    def greet_user(self):

# * Greets user with random anime quote by https://animechan.xyz/docs API 
# Added simple API to greet user with random anime qoutes 
        try:
            response = requests.get("https://animechan.xyz/api/random")
            quote = response.json()

            anime = quote["anime"]
            character = quote["character"]
            quote_text = quote["quote"]
        except (requests.RequestException, KeyError, ValueError, ):
            pass

        try:
            quote_str = f'''-------------
{anime}
{character}: 
{quote_text}
-------------
    '''
            print(quote_str)
        except (UnboundLocalError): 
            pass

        print("Welcome to the program!")
        print("Please log in to continue.")

    def login(self):
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if username == self.username and password == self.password:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials. Login failed.")
            return False

class Web_Names:
    @staticmethod
    def get_cleaned_links(web_url):
        main_url = f"https://{web_url}"  # Replace with the main website URL

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

        return full_links


class Product:
    def __init__(self, name, item_id, id, price, old_price, url):
        self.name = name
        self.item_id = item_id
        self.id = id
        self.price = price
        self.old_price = old_price
        self.url = url

    def __str__(self):
        return f"Product: {self.name}\nItem ID: {self.item_id}\nID: {self.id}\nPrice: {self.price}\nOld price: {self.old_price}\nURL: {self.url}\n"

class Scraper: 
    def __init__(self, urls):
        self.urls = urls
        self.products = []

    def scrape_all(self, domain):
        if domain == DOMAINS[0]:
            self.scrape_supergarden()
        elif domain == DOMAINS[1]:
            self.scrape_trusthemp()
        else: 
            print("Error in domain name")
        

    def scrape_supergarden(self):
        for url in self.urls:
            response = requests.get(url)
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')
            product_elements = soup.find_all('span', class_='item')

            for product_element in product_elements:
                product_name_element = product_element.find_previous('div', class_=['texts-wrp item-rows-1', 'texts-wrp item-rows-2'])
                product_name = product_name_element.find('span', class_='').text.strip() if product_name_element else None
                data_id = product_element.get('data-id')
                product_id_name = product_element.get('data-name')
                data_old_price = product_element.get('data-old-price')

                product_url = product_element.get('data-url')
                product_price = product_element.get('data-price')

                product = Product(product_name, product_id_name, data_id, product_price, data_old_price, product_url)
                self.products.append(product)

    def scrape_trusthemp(self):
        for url in self.urls:
            response = requests.get(url)
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')
            product_elements = soup.find_all('div', class_='ProductItem__Info ProductItem__Info--center')

            for product_element in product_elements:
                product_name_element = product_element.find('a', href=True)
                product_name = product_name_element.text.strip() if product_name_element else None

                product_price_element = product_element.find('span', class_='ProductItem__Price Price Price--highlight Text--subdued')
                product_price = product_price_element.text.strip() if product_price_element else None

                product_old_price_element = product_element.find('span', class_=['ProductItem__Price Price Price--compareAt Text--subdued', 'ProductItem__Price Price Text--subdued'])
                product_old_price = product_old_price_element.text.strip() if product_old_price_element else None

                product_url_ending = product_name_element['href']
                product_url = urljoin(url, product_url_ending)

                data_element = product_element.find('img', class_='data-media-id')
                data_id = data_element.get('data-media-id') if data_element else None

                product_id_name = None

                product = Product(product_name, product_id_name, data_id, product_price, product_old_price, product_url)
                self.products.append(product)

    # def save_to_csv(self, domain):
    #     domain_name = re.sub(r'^www\.|\..*', '', self.urls[0].split('//')[1].split('/')[0])
    #     today = date.today().strftime("%Y-%m-%d")
    #     filename = f"{domain_name}_{today}.csv"

    #     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    #         fieldnames = ["Product Name", "Item ID", "ID", "Price", "Old Price", "URL"]
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         writer.writeheader()

    #         for product in self.products:
    #             writer.writerow({
    #                 "Product Name": product.name,
    #                 "Item ID": product.item_id,
    #                 "ID": product.id,
    #                 "Price": product.price,
    #                 "Old Price": product.old_price,
    #                 "URL": product.url
    #             })

    #     return filename


    def save_to_json(self, domain):
        domain_name = re.sub(r'^www\.|\..*', '', self.urls[0].split('//')[1].split('/')[0])
        today = date.today().strftime("%Y-%m-%d")
        filename = f"{domain_name}_{today}.json"

        data = []
        for product in self.products:
            data.append({
                "Product Name": product.name,
                "Item ID": product.item_id,
                "ID": product.id,
                "Price": product.price,
                "Old Price": product.old_price,
                "URL": product.url
            })

        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return filename
    

    def scrape_from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        for product_data in data:
            product = Product(
                product_data.get("Product Name"),
                product_data.get("Item ID"),
                product_data.get("ID"),
                product_data.get("Price"),
                product_data.get("Old Price"),
                product_data.get("URL")
            )
            self.products.append(product)

        return self.products

    def display_products(self):
        for product in self.products:
            print(product)


class FileManager:
    def __init__(self, file_list):
        self.file_list = file_list

class FileManager:
    def __init__(self, file_list):
        self.file_list = file_list

    def save_file_list(self):
        filename = "scraped_files_list.json"

        existing_entries = set()
        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as json_file:
                try:
                    existing_data = json.load(json_file)
                    for entry in existing_data:
                        if isinstance(entry, dict):
                            file_name = entry.get("filename")
                            date = entry.get("date")
                            if file_name and date:
                                existing_entries.add((file_name, date))
                        else:
                            print("Invalid entry in existing_data:", entry)
                except json.JSONDecodeError as e:
                    print("Error decoding existing data:", e)

        with open(filename, "a", encoding="utf-8") as json_file:
            for file_data in self.file_list:
                file_name = file_data.get("filename")
                date = file_data.get("date")
                if file_name and date and (file_name, date) not in existing_entries:
                    existing_entries.add((file_name, date))
                    json.dump(file_data, json_file)
                    json_file.write("\n")




# class ViewData:
#     @staticmethod
#     def choose_file(files):
#         print("Choose a file to view:")
#         for index, file in enumerate(files):
#             print(f"{index + 1}. {file['filename']} - {file['date']}")

#         choice = int(input("Enter the file number: "))

#         if 1 <= choice <= len(files):
#             selected_file = files[choice - 1]
#             file_path = f"{selected_file['filename']}_{selected_file['date']}"
#             ViewData.view_file(file_path)
#         else:
#             print("Invalid choice.")

#     @staticmethod
#     def view_file(file_path):
#         choice = input("Choose an option:\n1. Generate CSV file\n2. View in terminal (Print)\nEnter your choice: ")

#         if choice == "1":
#             ViewData.generate_csv(file_path)
#         elif choice == "2":
#             ViewData.print_file(file_path)
#         else:
#             print("Invalid choice.")

#     @staticmethod
#     def generate_csv(file_path):
#         csv_filename = f"{file_path}.csv"
#         json_filename = f"{file_path}.json"

#         with open(json_filename, 'r', encoding='utf-8') as json_file:
#             data = json.load(json_file)

#         with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
#             fieldnames = ["Product Name", "Item ID", "ID", "Price", "Old Price", "URL"]
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()

#             for product in data:
#                 writer.writerow(product)

#         print(f"CSV file generated: {csv_filename}")

#     @staticmethod
#     def print_file(file_path):
#         json_filename = f"{file_path}.json"

#         with open(json_filename, 'r', encoding='utf-8') as json_file:
#             data = json.load(json_file)

#         for product in data:
#             print(f"Product Name: {product['Product Name']}")
#             print(f"Item ID: {product['Item ID']}")
#             print(f"ID: {product['ID']}")
#             print(f"Price: {product['Price']}")
#             print(f"Old Price: {product['Old Price']}")
#             print(f"URL: {product['URL']}")
#             print("-" * 20)



class ExitProgram:
    def __init__(self):
        self.message = "Exiting the program..."

    def exit(self):
        print(self.message)
        sys.exit(0)

    
def main():

    try:
        login = Login()
        login.greet_user()

        if login.login():
            # Continue with the program
            while True:
                print("\nSelect an option:")
                print("A. Gather information from website")
                print("B. View stored information")
                print("C. Quit")
                choice = input("Enter your choice: ")

                if choice.lower() == "a":
                    domain = input(f"What domain would you like to scrape? ({', '.join(DOMAINS)}) ")

                    if domain not in DOMAINS:
                        print("\nInvalid domain.")
                        continue

                    urls = []

                    if domain == DOMAINS[0]:
                        web_names = Web_Names
                        urls = web_names.get_cleaned_links(DOMAINS[0])

                    elif domain == DOMAINS[1]:
                        web_names = Web_Names
                        urls = web_names.get_cleaned_links(DOMAINS[1])

                    scraper = Scraper(urls)
                    scraper.scrape_all(domain)
                    # scraper.display_products()
                    filename = scraper.save_to_json(domain)

                    file_list = [{"filename": filename.split('_')[0], "date": filename.split('_')[1].split('.')[0]}]
                    file_manager = FileManager(file_list)
                    file_manager.save_file_list()


                elif choice.lower() == "b":
                    while True:
                        print("\nSelect next action:")
                        print("A. Print stored information:")
                        print("B. Covert file to .csv: ")
                        print("C. Quit")
                        choice = input("Enter your choice: ")

                            # if choice.lower() == "a":
                            #     pass
                        
                            # elif choice.lower() == "b":
                            #     pass

                    # file_manager = FileManager([])
                    # files = file_manager.load_file_list()
                    # ViewData.choose_file(files)


                elif choice.lower() == "c":
                    
                    exit_program = ExitProgram()
                    exit_program.exit()

                else:
                    print("Invalid choice.")
        else:
            # Handle login failure or exit the program
            exit_program = ExitProgram()
            exit_program.exit()

    except KeyboardInterrupt:
        exit_program = ExitProgram()
        exit_program.exit()


# * if a (gather):
#     -URL input by user
#     -User input check with regular expresions 
#     -Gather information from website (scraping) + 
#     -Data cleaning +
#     -Data stored in separate files with date stamp +
#     -/File name and date is added to separate file which stores all files names+ 
# * if b (view)
#     -Choose website from the list (stored files names)
#     -Choose date from the list
#     -Print file in user friendly form
# * if c (compare)
#     -Choose website 1
#         -Check if such is already tested today
#         -if not do gather info
#     -Choose website 2 
#         -Check if such is already tested today
#         -if not do gather info
#     -Compare gathered information
#     -Print differences
# * if d (exit)
#     -exit program 


if __name__ == "__main__":
    main()
