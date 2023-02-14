import requests
import os
import json
import re
ruta_archivo = 'c:/Users/xeon-2690/Documents/WC_micro/download_skins/sample1.json'

with open(ruta_archivo) as f:
    datos_json = json.load(f)


""" for index,value in enumerate(datos_json):
    ruta = f'c:/Users/xeon-2690/Documents/WC_micro/download_skins/{value["name"][0]}'
    for inside in datos_json[index]["skins"]:
        for clave,url in inside.items():
            img_data = requests.get(url).content
            with open('{}.png'.format(clave), 'wb') as f:
                f.write(img_data) """


for i in datos_json[1]["skins"]:
    
    for clave,url in i.items():
        clave = clave.replace('/','')
        ruta = f'c:/Users/xeon-2690/Documents/WC_micro/download_skins/Aatrox/{clave}.png'
        img_data = requests.get(url).content
        with open(ruta, 'wb') as f:
            f.write(img_data)
        print(f"la clave es:{clave} y la url:{url}")         
 
"""   
for i in datos_json:
    print()
    os.mkdir('c:/Users/xeon-2690/Documents/WC_micro/download_skins/{}'.format(i["name"][0]))  """
