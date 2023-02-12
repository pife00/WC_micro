import requests
from bs4 import BeautifulSoup
from get_champions_name import champions_name
import json

""" websiteChampion = "https://www.leagueoflegends.com/en-us/champions/{}/".format(champions_name[1])
result = requests.get(websiteChampion)

soup = BeautifulSoup(result.text, "html.parser")

labels = soup.find_all("label", class_="style__CarouselItemText-gky2mu-16 eicHWu")
champions_skins = []
for label in labels:
    champions_skins.append (label.text) """
    
myNewList = []
for i in champions_name:
    myList = {
        "name":i,
    }
    myNewList.append(myList)

print(myNewList)
    
""" myList = {
    "name":champions_name[0],
    "skins":champions_skins
} """

with open("sample.json","w") as outfile:
    json.dump(myNewList, outfile, indent=4)