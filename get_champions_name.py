import re
import requests
from bs4 import BeautifulSoup
website = "https://www.leagueoflegends.com/en-us/champions/"
url = requests.get(website)

soup = BeautifulSoup(url.text,'html.parser')
champions_raw = soup.find_all("span",class_="style__Text-n3ovyt-3 gMLOLF")
champions_name = []
for span in champions_raw:
    champions_name.append(span.text)
    
    