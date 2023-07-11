# import library
from bs4 import BeautifulSoup
import requests

# Request to website and download HTML contents
url='https://www.summmer.lt/produktai'
req=requests.get(url)
content=req.text
soup=BeautifulSoup(content, features ="html.parser")

# Save soup to a new text file
with open('html_content.txt', 'w', encoding='utf-8') as file:
    file.write(str(soup))

