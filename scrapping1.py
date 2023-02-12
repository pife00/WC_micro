import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com/"
website2 = "https://www.leagueoflegends.com/en-us/champions/"
result = requests.get(website2)
content = result.text
patron = r"/en-us/champions/[\w-]*"

champios_repetidos = re.findall(patron,content)
champios_no_duplicados = list(set(champios_repetidos))

champions = []
no_space = []
for i in champios_repetidos:
    filtro = i.replace("/en-us/champions/","").replace("page-data","").replace("-","")
    champions.append(filtro)


for j in champions:
    if j != '':
        no_space.append(j)

