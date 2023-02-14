# first get champions name from get_champions_name
# second generate champions url for scrapping from get_champions_url
# third scrapping to every url to get all skins from get_skins_name
# fourth create a json where inside are name and skins's champion from main

from get_skins_url import champions_skins
import json
""" with open('data.json') as json_file:
    data = json.load(json_file)

key = list(data[161][0].keys())
print(key) """

ultimate_list = []

#print(champions_skins)

for index, value in enumerate(champions_skins):
    keyList = list(champions_skins[index][0].keys())
    myChampion = {
        "name": keyList,
        "skins": value
    }
    ultimate_list.append(myChampion)
    
print()

sorted_list = sorted(ultimate_list, key=lambda x: x['name'])

ruta = "url_skins/sample1.json"
with open(ruta, "w") as outfile:
    json.dump(sorted_list, outfile, indent=4) 
