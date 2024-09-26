import json

with open("notas.txt","r",encoding="utf-8") as arquivoteste:
    y = json.load(arquivoteste)
print(y)