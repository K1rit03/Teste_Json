import json 

with open('heroes.json','r',encoding='utf-8') as arquivo:
    dicionario = json.load(arquivo)
for item in dicionario['members']:
    print(item['name'])

    