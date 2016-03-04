import requests
import filemanager

lolkey = filemanager.readfile("lolapi.txt")


def getchampionstaticdata(cid, extra=None):
    parametri = {
        'api_key': lolkey,
        'region': "euw",
        'locale': "it_IT",
        'id': cid,
        'champData': extra,
    }
    r = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion/" + str(cid),
                     params=parametri).json()
    return r


def getfreerotation():
    parametri = {
        'freeToPlay': 'true',
        'region': "euw",
        'api_key': lolkey
    }
    r = requests.get("https://euw.api.pvp.net/api/lol/euw/v1.2/champion", params=parametri).json()
    return r['champions']


def getmatchlist(sid):
    parametri = {
        'region': "euw",
        'api_key': lolkey,
    }
    r = requests.get("https://euw.api.pvp.net/api/lol/euw/v2.2/matchlist/by-summoner/" + str(sid), params=parametri)\
        .json()
    return r
