import requests
from bs4 import BeautifulSoup
from get_champions_name import champions_name
import json

myNewList = []


def get_skins_names():
    for i in champions_name:
        websiteChampion = "https://www.leagueoflegends.com/en-us/champions/{}/".format(
            i)
        result = requests.get(websiteChampion)
        soup = BeautifulSoup(result.text, "html.parser")
        labels = soup.find_all(
            "label", class_="style__CarouselItemText-gky2mu-16 eicHWu")
        champions_skins = []
        for label in labels:
            champions_skins.append(label.text)
        myList = {
            "name": i,
            "skins": champions_skins
        }
        myNewList.append(myList)

get_skins_names()

with open("sample.json", "w") as outfile:
    json.dump(myNewList, outfile, indent=4)
