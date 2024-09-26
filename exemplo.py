import json


materiais_escolares = {
    "caderno": {
        "marca": "Tilibra",
        "preco": 25.90,
        "quantidade": 10
    },
    "caneta": {
        "marca": "BIC",
        "preco": 4.50,
        "quantidade": 50
    },
    "lápis": {
        "marca": "Faber-Castell",
        "preco": 3.20,
        "quantidade": 30
    },
    "borracha": {
        "marca": "Mercur",
        "preco": 2.00,
        "quantidade": 20
    },
    "mochila": {
        "marca": "Nike",
        "preco": 150.00,
        "quantidade": 5
    },
    "régua": {
        "marca": "Tris",
        "preco": 1.50,
        "quantidade": 25
    },
    "estojo": {
        "marca": "Sundek",
        "preco": 45.00,
        "quantidade": 15
    },
    "marca-texto": {
        "marca": "Stabilo",
        "preco": 10.00,
        "quantidade": 40
    },
    "papel sulfite": {
        "marca": "Chamex",
        "preco": 15.00,
        "quantidade": 100
    },
    "colar": {
        "marca": "Pritt",
        "preco": 8.00,
        "quantidade": 12
    }
}

with open('estoque.json','w',encoding = 'utf8') as arquivo:
    json.dump(materiais_escolares,arquivo, indent = 4, ensure_ascii = False)
