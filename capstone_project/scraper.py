from bs4 import BeautifulSoup
import requests
import csv
from datetime import date
import re
from urllib.parse import urljoin
import sys

DOMAINS = ['supergarden', 'trusthemp']

# Program structure: 
# * Log in to program with username and pasword hardcoded in the program. It is Local variables. 

class Login():
# * Greets user with random anime quote by https://animechan.xyz/docs API 
    pass

class Meniu():
    pass
# * Drop down meniu: 
#     a. gather info from website
#     b. View of stored information
#         -Asks if wants short conclusion or not. For conclusion use chatGPT API
#     c. Comparing information from two websites
#         -Asks if wants short conclusion or not. For conclusion use chatGPT API
#     d. Exit 

# Scraper class defined below: 
# * if a (gather):
#     -URL input by user
#     -User input check with regular expresions 
#     -Gather information from website (scraping) + 
#     -Data cleaning +
#     -Data stored in separate files with date stamp +
#     -/File name and date is added to separate file which stores all files names+ 

class Web_Names ():
    pass
# gather all website from main domain 



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
        if domain == "supergarden":
            self.scrape_supergarden()
        elif domain == "trusthemp":
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

    def save_to_csv(self, domain):
        domain_name = re.sub(r'^www\.|\..*', '', self.urls[0].split('//')[1].split('/')[0])
        today = date.today().strftime("%Y-%m-%d")
        filename = f"{domain_name}_{today}.csv"

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Product Name", "Item ID", "ID", "Price", "Old Price", "URL"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for product in self.products:
                writer.writerow({
                    "Product Name": product.name,
                    "Item ID": product.item_id,
                    "ID": product.id,
                    "Price": product.price,
                    "Old Price": product.old_price,
                    "URL": product.url
                })

        return filename


    def display_products(self):
        for product in self.products:
            print(product)

class FileManager:
    def __init__(self, file_list):
        self.file_list = file_list

    def save_file_list(self):
        filename = f"scraped_files_list_.csv"

        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["File Name", "Date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            for file_data in self.file_list:
                writer.writerow({
                    "File Name": file_data["filename"],
                    "Date": file_data["date"]
                })



class ViewData(): 
    pass
# * if b (view)
#     -Choose website from the list (stored files names)
#     -Choose date from the list
#     -Print file in user friendly form

class CompareData(): 
    pass

# * if c (compare)
#     -Choose website 1
#         -Check if such is already tested today
#         -if not do gather info
#     -Choose website 2 
#         -Check if such is already tested today
#         -if not do gather info
#     -Compare gathered information
#     -Print difference

class ExitProgram:
    def __init__(self):
        self.message = "Exiting the program..."

    def exit(self):
        print(self.message)
        sys.exit(0)



    
def main():

    try:
        while True:
            print("Select an option:")
            print("A. Gather information from website")
            print("B. View stored information")
            print("C. Compare files information")
            print("D. Quit")
            choice = input("Enter your choice: ")

            if choice.lower() == "a":
                domain = input("What domain would you like to scrape? ")

                if domain not in DOMAINS:
                    print("Invalid domain.")
                    continue

                urls = []

                if domain == DOMAINS[0]:
                    urls = ['https://www.supergarden.lt/lt/katalogas', 'https://www.supergarden.lt/lt/katalogas?&page=2']
                elif domain == DOMAINS[1]:
                    urls = ['https://www.trusthemp.eu/collections/all']

                scraper = Scraper(urls)
                scraper.scrape_all(domain)
                scraper.display_products()
                filename = scraper.save_to_csv(domain)

                file_list = [{"filename": filename.split('_')[0], "date": filename.split('_')[1].split('.')[0]}]
                file_manager = FileManager(file_list)
                file_manager.save_file_list()

        # sg_urls = ['https://www.supergarden.lt/lt/katalogas', 'https://www.supergarden.lt/lt/katalogas?&page=2']
        # sg_scraper = Scraper_SuperGarden(sg_urls)
        # sg_scraper.scrape_all()
        # #sg_scraper.display_products()
        # sg_filename = sg_scraper.save_to_csv()

        # trusthemp_urls = ['https://www.trusthemp.eu/collections/all']
        # trusthemp_scraper = Scraper_Trusthemp(trusthemp_urls)
        # trusthemp_scraper.scrape_all()
        # #trusthemp_scraper.display_products()
        # trusthemp_filename = trusthemp_scraper.save_to_csv()

        # file_list = [
        #     {"filename": sg_filename.split('_')[0], "date": sg_filename.split('_')[1].split('.')[0]},
        #     {"filename": trusthemp_filename.split('_')[0], "date": trusthemp_filename.split('_')[1].split('.')[0]},
        # ]

        # file_manager = FileManager(file_list)
        # file_manager.save_file_list()





            elif choice.lower() == "b":
                # View stored information
                pass

            elif choice.lower() == "c":
                # Compare files information
                pass

            elif choice.lower() == "d":
                exit_program = ExitProgram()
                exit_program.exit()

            else:
                print("Invalid choice.")
                break

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
