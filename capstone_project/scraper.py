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

# List of domains
DOMAINS = ["www.supergarden.lt", "www.trusthemp.eu"]

# Load environment variables from .env file
load_dotenv()

# Program structure:
# Log in to program with username and pasword hardcoded in the program. It is Local variables.


class Login:
    def __init__(self):
    # Get the username and password from environment variables

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
        except (
            requests.RequestException,
            KeyError,
            ValueError,
        ):
            pass

        try:
            quote_str = f"""-------------
{anime}
{character}: 
{quote_text}
-------------
    """
            print(quote_str)
        except UnboundLocalError:
            pass

        print("Welcome to the program!")
        print("Please log in to continue.")
# 
    def login(self):
        #Login with username and password

        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if username == self.username and password == self.password:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials. Login failed.")
            return False


class Web_Names:
    #Gather urls from the main domain so scraper could scan as much urls as he can 
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
        cleaned_links = [
            link
            for link in links
            if not any(keyword in link for keyword in irrelevant_keywords)
        ]

        # Join cleaned links with the main URL
        full_links = [urljoin(main_url, link) for link in cleaned_links]

        return full_links

#Save product info in onle place. Is used for scrape program 
class Product:
    def __init__(self, name, item_id, id, price, old_price, url):
        self.name = name
        self.item_id = item_id
        self.id = id
        self.price = price
        self.old_price = old_price
        self.url = url
#return string with desction of product
    def __str__(self):
        return f"Product: {self.name}\nItem ID: {self.item_id}\nID: {self.id}\nPrice: {self.price}\nOld price: {self.old_price}\nURL: {self.url}\n"


class Scraper:
    def __init__(self, urls):
        self.urls = urls
        self.products = []

#Defines which domain it should scrape. It it will be more domain this part should be extended 
    def scrape_all(self, domain):
        #Supergarden
        if domain == DOMAINS[0]:
            self.scrape_supergarden()
            #Trusthemp
        elif domain == DOMAINS[1]:
            self.scrape_trusthemp()
        else:
            print("Error in domain name")

#Scrape logic made according Supergarden website.
    def scrape_supergarden(self):
        for url in self.urls:
            #Retrieves info from website via response and BeutifulSoup
            response = requests.get(url)
            content = response.text
            soup = BeautifulSoup(content, "html.parser")

            #Defines where it should look info 
            product_elements = soup.find_all("span", class_="item")

            #Defines what should look like
            for product_element in product_elements:

                #product name 
                product_name_element = product_element.find_previous(
                    "div", class_=["texts-wrp item-rows-1", "texts-wrp item-rows-2"]
                )
                product_name = (
                    product_name_element.find("span", class_="").text.strip()
                    if product_name_element
                    else None
                )
                #Product ID
                data_id = product_element.get("data-id")
                
                #Product ID Name
                product_id_name = product_element.get("data-name")

                #Product old price or price without discount
                data_old_price = product_element.get("data-old-price")

                #Product URL
                product_url = product_element.get("data-url")

                #Product current price
                product_price = product_element.get("data-price")

                #Creates product (item)
                product = Product(
                    product_name,
                    product_id_name,
                    data_id,
                    product_price,
                    data_old_price,
                    product_url,
                )

                #Appent product to all product list
                self.products.append(product)

#Scrape logic made according trushemp website.
    def scrape_trusthemp(self):

        #Retrieves info from website via response and BeutifulSoup
        for url in self.urls:

            #Retrieves info from website via response and BeutifulSoup
            response = requests.get(url)
            content = response.text
            soup = BeautifulSoup(content, "html.parser")
            #Defines where it should look info 
            product_elements = soup.find_all(
                "div", class_="ProductItem__Info ProductItem__Info--center"
            )

            #Creates product 
            for product_element in product_elements:
                
                #Search for name
                product_name_element = product_element.find("a", href=True)
                product_name = (
                    product_name_element.text.strip() if product_name_element else None
                )

                #Search for discounted price
                product_price_element = product_element.find(
                    "span",
                    class_="ProductItem__Price Price Price--highlight Text--subdued",
                )
                product_price = (
                    product_price_element.text.strip()
                    if product_price_element
                    else None
                )

                #Search for current price
                product_old_price_element = product_element.find(
                    "span",
                    class_=[
                        "ProductItem__Price Price Price--compareAt Text--subdued",
                        "ProductItem__Price Price Text--subdued",
                    ],
                )
                product_old_price = (
                    product_old_price_element.text.strip()
                    if product_old_price_element
                    else None
                )

                #Search and return url. HTML code of trusthemp did not stored finite URL as supergarden. 
                product_url_ending = product_name_element["href"]
                product_url = urljoin(url, product_url_ending)

                #Search for item ID
                data_element = product_element.find("img", class_="data-media-id")
                data_id = data_element.get("data-media-id") if data_element else None

                #Website do not store product ID name, so it return None 
                product_id_name = None

                #Create product
                product = Product(
                    product_name,
                    product_id_name,
                    data_id,
                    product_price,
                    product_old_price,
                    product_url,
                )

                #Append product to products
                self.products.append(product)


# Define action to store scraped info into jsone file
    def save_to_json(self, domain):

        #Check domain name with regex
        domain_name = re.sub(
            r"^www\.|\..*", "", self.urls[0].split("//")[1].split("/")[0]
        )

        #defines current day
        today = date.today().strftime("%Y-%m-%d")

        #Creates file name 
        filename = f"{domain_name}_{today}.json"

        #Store file in dictionary
        data = []
        for product in self.products:
            data.append(
                {
                    "Product Name": product.name,
                    "Item ID": product.item_id,
                    "ID": product.id,
                    "Price": product.price,
                    "Old Price": product.old_price,
                    "URL": product.url,
                }
            )

        #Write product to jsone file. If same day program is run it will overwrite identical files. 
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return filename

    # Display products in this class. It was mostly used during programing to double check if returned info from url is correct 
    def display_products(self):
        for product in self.products:
            print(product)

# Class made to retrieve info from saved files
class FileRetriever:

    #retrieve saves file names 
    @staticmethod
    def retrieve_filenames_and_dates_from_csv(file_path):
        try:
            filenames = []
            with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for entry in csv_reader:
                    filename = entry.get("filename")
                    date = entry.get("date")
                    if filename and date:
                        filenames.append(f"{filename}_{date}")
            return filenames
        except FileNotFoundError:
            print("File not found:", file_path)
            return []
    
    #Converts json to csv files 
    @staticmethod
    def convert_json_to_csv(json_file_path):
        csv_file_path = os.path.splitext(json_file_path)[0] + ".csv"

        if os.path.isfile(csv_file_path):
            print(f"CSV file '{csv_file_path}' already exists. Skipping conversion.")
            return

        try:
            # Read json file
            with open(json_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)

            #Writes csv file
            with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
                fieldnames = list(data[0].keys()) if data else []
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

            print(
                f"JSON file '{json_file_path}' converted to CSV file '{csv_file_path}' successfully."
            )
        except FileNotFoundError:
            print("File not found:", json_file_path)
        except json.JSONDecodeError as e:
            print("Error decoding JSON data:", e)
        except Exception as e:
            print("An error occurred:", e)

    #Print json file content 
    @staticmethod
    def print_json_file(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as json_file:
                products = json.load(json_file)
                for product in products:
                    for key, value in product.items():
                        print(f"{key}: {value}")
                    print("--------------------\n")

        except FileNotFoundError:
            print("File not found:", file_path)
        except json.JSONDecodeError as e:
            print("Error decoding JSON data:", e)

    #Count items in json file
    @staticmethod
    def count_items(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                item_count = len(data)
                return item_count
        except FileNotFoundError:
            print("File not found:", file_path)
        except json.JSONDecodeError as e:
            print("Error decoding JSON data:", e)

    #exit programs
class ExitProgram:
    def __init__(self):
        self.message = "Exiting the program..."

    def exit(self):
        print(self.message)
        sys.exit(0)

    #saves Scraped files names to the csv file, in order to retrieve it in later stages. 
class FileManager:
    def __init__(self, file_list):
        self.file_list = file_list

    #Saves filenames into csv and checks if file with same name exists or not. If not add to the list 
    def save_file_list(self):
        filename = "scraped_files_list.csv"

        existing_entries = set()
        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for entry in csv_reader:
                    file_name = entry.get("filename")
                    date = entry.get("date")
                    if file_name and date:
                        existing_entries.add((file_name, date))

        with open(filename, "a", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["filename", "date"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if csv_file.tell() == 0:
                csv_writer.writeheader()

            for file_data in self.file_list:
                file_name = file_data.get("filename")
                date = file_data.get("date")
                if file_name and date and (file_name, date) not in existing_entries:
                    existing_entries.add((file_name, date))
                    csv_writer.writerow(file_data)


#main was done outside of class 
def main():
    try:
        login = Login()
        login.greet_user()

        #First level of program with a, b, c
        if login.login():
            # Continue with the program
            while True:
                print("\nSelect an option:")
                print("A. Gather information from website")
                print("B. View stored information")
                print("C. Quit")
                choice = input("Enter your choice: ")

                #Call scaper according user input
                if choice.lower() == "a":
                    domain = input(
                        f"What domain would you like to scrape? ({', '.join(DOMAINS)}) "
                    )

                    if domain not in DOMAINS:
                        print("\nInvalid domain.")
                        continue

                    urls = []

                    #First domain from the list
                    if domain == DOMAINS[0]:
                        #Gathers all links from domain and cleans them
                        web_names = Web_Names
                        urls = web_names.get_cleaned_links(DOMAINS[0])

                    #Second domain from the list
                    elif domain == DOMAINS[1]:
                        #Gathers all links from domain and clean them
                        web_names = Web_Names
                        urls = web_names.get_cleaned_links(DOMAINS[1])

                    #Call scraping
                    scraper = Scraper(urls)
                    scraper.scrape_all(domain)

                    #used during programing to check if gathered info is correct
                    # scraper.display_products()

                    #Saves scraped info to json
                    filename = scraper.save_to_json(domain)

                    #save file names to the csv
                    file_list = [
                        {
                            "filename": filename.split("_")[0],
                            "date": filename.split("_")[1].split(".")[0],
                        }
                    ]
                    file_manager = FileManager(file_list)
                    file_manager.save_file_list()

                #View stored info
                elif choice.lower() == "b":
                    while True:
                        print("\nSelect next action:")
                        print("A. Print stored files names:")
                        print("B. Covert file to .csv: ")
                        print("C. Print file content: ")
                        print("D. Print number of products in the file: ")
                        print("E. Go back.")
                        choice = input("Enter your choice: ")

                        #Read filename list from csv and print to user
                        if choice.lower() == "a":
                            fileretriever = FileRetriever()
                            file_path = "/workspaces/war_game/capstone_project/scraped_files_list.csv"
                            filenames = (
                                fileretriever.retrieve_filenames_and_dates_from_csv(
                                    file_path
                                )
                            )
                            print(
                                f"\nAt this moment moment there is following saved files:"
                            )
                            for filename in filenames:
                                print(filename)

                        #Converts files from json to csv. User defines name of file 
                        elif choice.lower() == "b":
                            retrieve = FileRetriever
                            input_str = input(f"\nPlease input file name: ")
                            retrieve.convert_json_to_csv(
                                f"/workspaces/war_game/capstone_project/{input_str}.json"
                            )

                        #Print files content. User defines name of file 
                        elif choice.lower() == "c":
                            retrieve = FileRetriever
                            input_str = input(f"\nPlease input file name: ")
                            retrieve.print_json_file(
                                f"/workspaces/war_game/capstone_project/{input_str}.json"
                            )

                        #Print number of product in file. User defines name of file 
                        elif choice.lower() == "d":
                            retrieve = FileRetriever
                            input_str = input(f"\nPlease input file name: ")
                            print(
                                f"Number of products:",
                                retrieve.count_items(
                                    f"/workspaces/war_game/capstone_project/{input_str}.json"
                                ),
                            )

                        #Get back
                        elif choice.lower() == "e":
                            break
                
                #Exit
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



if __name__ == "__main__":
    main()
