# -*- coding: utf-8 -*-
import requests
import filemanager

# Per far funzionare questa libreria serve un file "steamapi.txt" contenente la Steam Api Key ottenibile a
# http://steamcommunity.com/dev/apikey
steamtoken = filemanager.readfile('steamapi.txt')


def getplayersummaries(steamid):
    """Ottieni i dati dei profili steam dei giocatori di cui è stato specificato lo SteamID 32.
    :param steamid: SteamID 32 dei giocatori, separato da virgola
    """
    # Parametri della richiesta
    parametri = {
        'key': steamtoken,
        'steamids': steamid,
    }
    # Manda la richiesta ai server di Steam.
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=parametri).json()
    if len(r['response']['players']) == 1:
        return r['response']['players'][0]
    elif len(r['response']['players']) > 1:
        return r['response']['players']
    else:
        raise NameError("Lo steamid specificato non esiste.")


def getnumberofcurrentplayers(appid):
    """Ottieni il numero di giocatori che stanno giocando a un certo gioco.
    :param appid: ID Steam dell'applicazione
    """
    # Parametri della richiesta
    parametri = {
        'key': steamtoken,
        'appid': appid,
    }
    # Manda la richiesta ai server di Steam.
    r = requests.get("http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v0001/",
                     params=parametri).json()
    if 'player_count' in r['response']:
        return r['response']['player_count']
    else:
        return None


def getplayerachievements(appid, steamid):
    """Ottieni gli achievement del giocatore e del gioco specificato.
    :param appid: ID dell'applicazione
    :param steamid: SteamID 32 del giocatore
    """
    # Parametri della richiesta
    parametri = {
        'key': steamtoken,
        'steamid': steamid,
        'appid': appid,
        'l': 'IT'  # Mettendo questo vengono in inglese...? What.
    }
    # Manda la richiesta ai server di Steam.
    r = requests.get("http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/",
                     params=parametri).json()
    return r['playerstats']


def getsteamlevel(steamid):
    """Ottieni il livello del profilo di Steam.
    :param steamid: SteamID 32 del giocatore
    """
    parametri = {
        'key': steamtoken,
        'steamid': steamid,
    }
    # Manda la richiesta ai server di Steam.
    r = requests.get("http://api.steampowered.com/IPlayerService/GetSteamLevel/v0001/", params=parametri).json()
    return r['response']['player_level']


def isplayingsharedgame(appid, steamid):
    """Guarda se il gioco a cui sta giocando qualcuno è condiviso.
    Ah, Steam vuole sapere l'ID del gioco a cui sta giocando, quindi mettetecelo.
    :param appid: ID dell'applicazione
    :param steamid: SteamID 32 del giocatore"""
    parametri = {
        'key': steamtoken,
        'steamid': steamid,
        'appid_playing': appid,
    }
    # Manda la richiesta ai server di Steam.
    r = requests.get("http://api.steampowered.com/IPlayerService/IsPlayingSharedGame/v0001/", params=parametri).json()
    return r  # Non posso provare il comando; cambiare quando possibile?


def getschemaforgame(appid):
    """Trova il nome, gli achievement e le statistiche corrispondenti al numero di applicazione specificato.
    :param appid: ID dell'applicazione
    """
    parametri = {
        'key': steamtoken,
        'appid': appid,
    }
    # Manda la richiesta ai server di Steam.
    r = requests.get("http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/", params=parametri).json()
    return r


