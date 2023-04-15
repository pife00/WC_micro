from get_html_raw import champions_html
from bs4 import BeautifulSoup

champions_skins = []

def convert(html):
    soup =  BeautifulSoup(html.text, "html.parser")
    labels = soup.find_all(
    "label", class_="style__CarouselItemText-gky2mu-16 eicHWu")      
    return [j.text for j in labels]

for html in champions_html:
    champions_skins.append(convert(html))

print(champions_skins)