from get_champions_url import champions_url
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import httpx
import asyncio

champions_skins = []

async def download_url(client = url):
   ## result = requests.get(url)
    result = 
    soup = BeautifulSoup(result.text, "html.parser")    
    labels = soup.find_all("label", class_="style__CarouselItemText-gky2mu-16 eicHWu") 
    return [j.text for j in labels]
    

async def main():
    async with httpx.AsyncClient() as client:
        task = []
        for url in champions_url:
            task.append(asyncio.create_task(download_url(client,url)))
            
        result = await asyncio.gather(*task)
    return result
    
    """ for i in champions_url:
        champions_skins.append(download_url(i)) """
main()

result = asyncio.run(main())

print(result)
