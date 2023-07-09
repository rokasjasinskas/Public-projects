from bs4 import BeautifulSoup
import requests
import csv
from datetime import date
import re
from urllib.parse import urljoin
import sys

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

    def scrape_all(self, domain, urls):
        if domain == "supergarden":
            for url in urls:
                # Call the scrape_SG for each URL
                scrape_sg(url)

        elif domain == "trusthemp":
            for url in urls:
                # Call the scrape_SG for each URL
                scrape_trusthemp(url)
        else: 
            print("Error in domain name")
        

    def display_products(self):
        for product in self.products:
            # Display each product
            print(product)

    def save_to_csv(self):
        domain_name = re.sub(r'^www\.|\..*', '', self.urls[0].split('//')[1].split('/')[0])
        today = date.today().strftime("%Y-%m-%d")
        filename = f"{domain_name}_{today}.csv"

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Product Name", "Item ID", "ID", "Price", "Old Price", "URL"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the CSV header
            writer.writeheader()
            for product in self.products:
                # Write each product as a row in the CSV
                writer.writerow({
                    "Product Name": product.name,
                    "Item ID": product.item_id,
                    "ID": product.id,
                    "Price": product.price,
                    "Old Price": product.old_price,
                    "URL": product.url
                })
        return filename  # Return the generated CSV filename

    def scraping_saving (self, urls):
        #It call scraper functions and save all info into files. Name of files is saved in separate file.

        scraper = Scraper(urls)
        scraper.scrape_all()
        #scraper.display_products()
        filename = scraper.save_to_csv()
        filename_list = [
            {"filename": filename.split('_')[0], "date": filename.split('_')[1].split('.')[0]}
        ]
        file_manager = FileManager(filename_list)
        file_manager.save_file_list()

class SuperGarden(Scraper):

    def scrape_SG(self, url):
        response = requests.get(url)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        product_elements = soup.find_all('span', class_='item')

        for product_element in product_elements:
            # Scrape product information
            product_name_element = product_element.find_previous('div', class_=['texts-wrp item-rows-1', 'texts-wrp item-rows-2'])
            product_name = product_name_element.find('span', class_='').text.strip() if product_name_element else None
            data_id = product_element.get('data-id')
            product_id_name = product_element.get('data-name')
            data_old_price = product_element.get('data-old-price')

            product_url = product_element.get('data-url')
            product_price = product_element.get('data-price')

            # Create a Product object and add it to the products list
            product = Product(product_name, product_id_name, data_id, product_price, data_old_price, product_url)
            self.products.append(product)

    # def scrape_all(self):
    #     for url in self.urls:
    #         # Call the scrape_SG method for each URL
    #         self.scrape_SG(url)

    # def display_products(self):
    #     for product in self.products:
    #         # Display each product
    #         print(product)

    # def save_to_csv(self):
    #     domain_name = re.sub(r'^www\.|\..*', '', self.urls[0].split('//')[1].split('/')[0])
    #     today = date.today().strftime("%Y-%m-%d")
    #     filename = f"{domain_name}_{today}.csv"

    #     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    #         fieldnames = ["Product Name", "Item ID", "ID", "Price", "Old Price", "URL"]
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #         # Write the CSV header
    #         writer.writeheader()
    #         for product in self.products:
    #             # Write each product as a row in the CSV
    #             writer.writerow({
    #                 "Product Name": product.name,
    #                 "Item ID": product.item_id,
    #                 "ID": product.id,
    #                 "Price": product.price,
    #                 "Old Price": product.old_price,
    #                 "URL": product.url
    #             })
    #     return filename  # Return the generated CSV filename


class Trusthemp(Scraper) :

    def scrape_trusthemp(self, url):
        response = requests.get(url)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        product_elements = soup.find_all('div', class_='ProductItem__Info ProductItem__Info--center')

        for product_element in product_elements:
            # Scrape product information
            product_name_element = product_element.find('a', href=True)
            product_name = product_name_element.text.strip() if product_name_element else None

            product_price_element = product_element.find('span', class_='ProductItem__Price Price Price--highlight Text--subdued')
            product_price = product_price_element.text.strip() if product_price_element else None

            product_old_price_element = product_element.find('span', class_=['ProductItem__Price Price Price--compareAt Text--subdued', 'ProductItem__Price Price Text--subdued'])
            product_old_price = product_old_price_element.text.strip() if product_old_price_element else None

            product_url_ending = product_name_element['href']
            product_url = urljoin(url, product_url_ending)

            # Extract data-id
            data_element = product_element.find('img', class_='data-media-id')
            data_id = data_element.get('data-media-id') if data_element else None

            product_id_name = None

            # Create a Product object and add it to the products list
            product = Product(product_name, product_id_name, data_id, product_price, product_old_price, product_url)
            self.products.append(product)


    # def scrape_all(self):
    #     for url in self.urls:
    #         # Call the scrape_SG method for each URL
    #         self.scrape_trusthemp(url)

    # def display_products(self):
    #     for product in self.products:
    #         # Display each product
    #         print(product)

    # def save_to_csv(self):
    #     domain_name = re.sub(r'^www\.|\..*', '', self.urls[0].split('//')[1].split('/')[0])
    #     today = date.today().strftime("%Y-%m-%d")
    #     filename = f"{domain_name}_{today}.csv"

    #     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    #         fieldnames = ["Product Name", "Item ID", "ID", "Price", "Old Price", "URL"]
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #         # Write the CSV header
    #         writer.writeheader()
    #         for product in self.products:
    #             # Write each product as a row in the CSV
    #             writer.writerow({
    #                 "Product Name": product.name,
    #                 "Item ID": product.item_id,
    #                 "ID": product.id,
    #                 "Price": product.price,
    #                 "Old Price": product.old_price,
    #                 "URL": product.url
    #             })
    #     return filename  # Return the generated CSV filename
    

class FileManager:
    def __init__(self, file_list):
        self.file_list = file_list

    def save_file_list(self):
        filename = f"scraped_files_list_.csv"

        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["File Name", "Date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

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
    domains = ['supergarden', 'trusthemp']
    try:
        while True:
            print("Select an option:")
            print("A. gather information from website")
            print("B. View stored information")
            print("C. Compare files information")
            print("D. Quit")
            choice = input("Enter your choice: ")

            if choice.lower() == "a":
                domain = print("What domain would you like to scrap? ")
                if domain == domains [0]:
                    scrap = Scraper
                    supergarden = SuperGarden
                elif domain == domains [1]:
                    scrap = Scraper
                    trusthemp = Trusthemp
            elif choice.lower() == "b":
# View
                pass
            elif choice.lower() == "c":
# Compare
                pass
            elif choice.lower() == "d":
                exit_program = ExitProgram()
                exit_program.exit()
            else:
                print("Invalid choice.")
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



if __name__ == "__main__":
    main()
