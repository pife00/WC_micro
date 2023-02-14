from champions_name_and_url import champions_url
import requests
from bs4 import BeautifulSoup
import concurrent.futures

champions_html = []

def download_url(url):
    result = requests.get(url)
    champions_html.append(result)
    
with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
    for url in champions_url:
        executor.submit(download_url, url)
