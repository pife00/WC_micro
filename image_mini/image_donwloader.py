import requests
from bs4 import BeautifulSoup

alt_name = []
urls_img = []
with open("index.html","r",encoding='utf-8') as f:
    url = f.read()

soup = BeautifulSoup(url, 'html.parser')
images = soup.find_all("img",class_="bg-image")
for img in images:
    alt_name.append(img['alt'])
    urls_img.append(img['src'])
    
for index,img in  enumerate(urls_img):
    img_data = requests.get(img).content
    with open('{}.png'.format(alt_name[index]), 'wb') as f:
        f.write(img_data)
        
        



""" image_url = "https://static.bigbrain.gg/assets/lol/riot_static/13.3.1/img/champion/XinZhao.png"
img_data = requests.get(image_url).content
with open('image_name.png', 'wb') as handler:
    handler.write(img_data) """