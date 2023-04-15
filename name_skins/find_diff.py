import json
from deepdiff import DeepDiff
# Cargar los dos archivos JSON en variables
with open('sample1.json', 'r') as f:
    json1 = json.load(f)

with open('sample2.json', 'r') as f:
    json2 = json.load(f)
    
# Comparar los archivos y guardar las diferencias en una variable
diff = DeepDiff(json1, json2)
# Imprimir las diferencias

#print(diff)
 

with open('diff.json','w') as f:
    json.dump(diff,f)
