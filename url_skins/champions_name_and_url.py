import re
import requests
from bs4 import BeautifulSoup

champions_url = []

website = "https://www.leagueoflegends.com/en-us/champions/"
url = requests.get(website)
soup = BeautifulSoup(url.text, 'html.parser')
champions_raw_url = soup.find_all(
    "a", class_="style__Wrapper-n3ovyt-0 style__ResponsiveWrapper-n3ovyt-4 ehjaZK elVPdk style__Item-sc-13btjky-3 CanXV isVisible isFirstTime")
links = [link.get('href') for link in champions_raw_url]

for i in links:
    url = "https://www.leagueoflegends.com{}".format(i)
    champions_url.append(url)
