from bs4 import BeautifulSoup
import requests
import json
html = requests.get('https://www.leagueoflegends.com/en-us/champions/ahri/')
soup =  BeautifulSoup(html.text, "html.parser")
labels = soup.find_all("label", class_="style__CarouselItemText-gky2mu-16 eicHWu")

div_elements = soup.find_all("div",class_="style__CarouselItemThumb-gky2mu-15 dmGeeS")
img_src = []

for i in div_elements:
    img_element = i.find('img')
    img_src.append(img_element['src'])

newList = []
for index,value in enumerate(img_src):
    file = {labels[index].text:img_src[index]}
    newList.append(file)
     
with open("sample.json","w") as f:
    json.dump(newList,f)