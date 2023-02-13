#first get champions name from get_champions_name
#second generate champions url for scrapping from get_champions_url
#third scrapping to every url to get all skins from get_skins_name
#fourth create a json where inside are name and skins's champion from main

from get_skins_names import champions_skins
from get_champions_name import champions_name
import time
import json

start_time = time.time()
ultimate_list = []
for index, value in enumerate(champions_skins):
    myChampion = {
        "name": champions_name[index],
        "skins": value
    }
    ultimate_list.append(myChampion)
    
with open("sample.json", "w") as outfile:
    json.dump(ultimate_list, outfile, indent=4)

end_time = time.time()
total_time = end_time - start_time

