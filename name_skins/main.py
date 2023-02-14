# first get champions name from get_champions_name
# second generate champions url for scrapping from get_champions_url
# third scrapping to every url to get all skins from get_skins_name
# fourth create a json where inside are name and skins's champion from main

from get_skins_name import champions_skins
import json

ultimate_list = []

for index, value in enumerate(champions_skins):
    myChampion = {
        "name": value[0],
        "skins": value
    }
    ultimate_list.append(myChampion)

sorted_list = sorted(ultimate_list,key=lambda x:x['name']) 
 
ruta = "name_skins/sample1.json"
with open(ruta, "w") as outfile:
    json.dump(ultimate_list, outfile, indent=4)
