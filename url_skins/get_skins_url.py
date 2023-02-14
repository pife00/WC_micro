from get_html_raw import champions_html
from bs4 import BeautifulSoup
import requests
import json

champions_skins = []

def findImg(div_elements,):
    img_src = []
    for i in div_elements:
        img_element = i.find('img')
        img_src.append(img_element['src'])
    return img_src
    
def convert(html):
    img_src = []
    myList = []
    soup =  BeautifulSoup(html.text, "html.parser")
    labels = soup.find_all("label", class_="style__CarouselItemText-gky2mu-16 eicHWu")  
    div_elements = soup.find_all("div",class_="style__CarouselItemThumb-gky2mu-15 dmGeeS")   
   
    img_src.append(findImg(div_elements))
    
    for index,value in enumerate(labels):
        file = {value.text:img_src[0][index]}
        myList.append(file)
        
    return myList

#html = requests.get('https://www.leagueoflegends.com/en-us/champions/ahri/')

for html in champions_html:
    champions_skins.append(convert(html)) 

""" with open("sample.json","w") as f:
    json.dump(champions_skins,f) """



