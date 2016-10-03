import json

db = json.load("db.json")

def findname(name: str):
    for player in db:
        if player == name:
            return db[player]
    else:
        return None

def findbykey(key, value):
    for player in db:
        if player[key] == value:
            return db[player]
    else:
        return None
