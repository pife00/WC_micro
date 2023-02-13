import requests

from get_champions_name import champions_name

champions_url = []

for i in champions_name:
    url = "https://www.leagueoflegends.com/en-us/champions/{}/".format(i)
    champions_url.append(url)

