# -*- coding: utf-8 -*-
import requests
import filemanager

##Per far funzionare questa libreria serve un file "steamapi.txt" contenente la Steam Api Key ottenibile a http://steamcommunity.com/dev/apikey
steamtoken = filemanager.readFile('steamapi.txt')

def getPlayerSummaries(steamid):
	"""Ottieni i dati del profilo steam del giocatore di cui è stato specificato lo SteamID 32."""
	#Parametri della richiesta
	parametri = {
		'key': steamtoken,
		'steamids': steamid,
	}
	#Manda la richiesta ai server di Steam.
	r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=parametri).json()
	return r['response']['players'][0]

def getNumberOfCurrentPlayers(appid):
	"""Ottieni il numero di giocatori che stanno giocando a un certo gioco."""
	#Parametri della richiesta
	parametri = {
		'key': steamtoken,
		'appid': appid,
	}
	#Manda la richiesta ai server di Steam.
	r = requests.get("http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v0001/", params=parametri).json()
	if('player_count' in r['response']):
		return r['response']['player_count']
	else:
		return None
	
def getPlayerAchievements(appid, steamid):
	"""Ottieni gli achievement del giocatore e del gioco specificato."""
	#Parametri della richiesta
	parametri = {
		'key': steamtoken,
		'steamid': steamid,
		'appid': appid,
		'l': 'IT' #Mettendo questo vengono in inglese...? What.
	}
	#Manda la richiesta ai server di Steam.
	r = requests.get("http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/", params=parametri).json()
	return r['playerstats']

def getSteamLevel(steamid):
	"""Ottieni il livello del profilo di Steam."""
	parametri = {
		'key': steamtoken,
		'steamid': steamid,
	}
	#Manda la richiesta ai server di Steam.
	r = requests.get("http://api.steampowered.com/IPlayerService/GetSteamLevel/v0001/", params=parametri).json()
	return r['response']['player_level']

def isPlayingSharedGame(appid, steamid):
	"""Guarda se il gioco a cui sta giocando qualcuno è condiviso.\nAh, Steam vuole sapere l'ID del gioco a cui sta giocando, quindi mettetecelo."""
	parametri = {
		'key': steamtoken,
		'steamid': steamid,
		'appid_playing': appid,
	}
	#Manda la richiesta ai server di Steam.
	r = requests.get("http://api.steampowered.com/IPlayerService/IsPlayingSharedGame/v0001/", params=parametri).json()
	return r #Non posso provare il comando; cambiare quando possibile?