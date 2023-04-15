import re
import requests
from bs4 import BeautifulSoup
import json

website = "https://leagueoflegends.fandom.com/wiki/Champion_(Wild_Rift)"
url = requests.get(website)
soup = BeautifulSoup(url.text, 'html.parser')

champions_text = []

divs = soup.find_all(
    "div", class_="columntemplate")
exclusive_skins = divs[5]
links = exclusive_skins.findAll("span", style="white-space:normal;")

for i in links:
    _i = i.text.replace(" ","_")
    champions_text.append(_i) 
    
ruta = "wildrift_champions/exclusive.json"

with open(ruta, "w") as outfile:
    json.dump(champions_text, outfile, indent=4)



