from champions_name_and_url import champions_url
import requests
from bs4 import BeautifulSoup
import concurrent.futures

champions_html = []

def download_url(url):
    result = requests.get(url)
    champions_html.append(result)
    #soup =  BeautifulSoup(result.text, "html.parser")
    """ labels = soup.find_all(
        "label", class_="style__CarouselItemText-gky2mu-16 eicHWu") """
    #return [j for j in soup]
 
""" for i in champions_url:
    champions_html.append(download_url(i))  """
    
with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
    for url in champions_url:
        executor.submit(download_url, url)
    
""" with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_url,champions_url)
 """
