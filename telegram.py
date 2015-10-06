# -*- coding: utf-8 -*-
import requests
import filemanager

##Per far funzionare questa libreria serve un file "lastid.txt" contenente l'update ID dell'ultimo messaggio non letto e un file "telegramapi.txt" contenente il token di accesso del bot assegnato da @BotFather.
telegramtoken = filemanager.readFile('telegramapi.txt')

def getUpdates():
	"""Ricevi gli ultimi aggiornamenti dal server di Telegram e restituisci l'ultimo messaggio non letto."""
	parametri = {
		'offset': filemanager.readFile("lastid.txt"), #Update ID del messaggio da leggere
		'limit': 1, #Numero di messaggi da ricevere alla volta, lasciare 1
		'timeout': 300, #Secondi da mantenere attiva la richiesta se non c'e' nessun messaggio
	}
	while(True):	
		data = requests.get("https://api.telegram.org/bot" + telegramtoken + "/getUpdates", params=parametri).json()
		if(data['ok'] == True):
			if(data['result'] != []):
				filemanager.writeFile("lastid.txt", str(data['result'][0]['update_id'] + 1))
				#sporco hack per non far crashare il bot ogni 10 secondi; prima o poi capirò il senso di certe risposte nell'api di telegram
				if('message' in data['result'][0]):
					if('text' in data['result'][0]['message']):
						return data['result'][0]['message']

def sendMessage(content, to):
	"""Manda un messaggio a una chat."""
	#Parametri del messaggio
	parametri = {
		'chat_id': to, #L'ID della chat a cui mandare il messaggio, Royal Games: -2141322
		'text': content, #Il messaggio da mandare
		'parse_mode': 'Markdown', #Formattare il messaggio?
	}
	#Manda il messaggio
	requests.get("https://api.telegram.org/bot" + telegramtoken + "/sendMessage", params=parametri)
	
def forwardMessage(msg, sentby, to):
	"""Inoltra un messaggio mandato in un'altra chat."""
	#Parametri del messaggio
	parametri = {
		'chat_id': to,
		'from_chat_id': sentby,
		'message_id': msg,
	}
	#Manda la richiesta ai server di Telegram.
	requests.get("https://api.telegram.org/bot" + telegramtoken + "/forwardMessage", params=parametri)

def sendAudio(audio, to):
	"""Manda un audio a una chat."""
	parametri = {
		'chat_id': to,
		'audio': audio,
	}
	#Manda la richiesta ai server di Telegram.
	requests.get("https://api.telegram.org/bot" + telegramtoken + "/sendAudio", params=parametri)

def sendLocation(lat, long, to):
	"""Manda una posizione sulla mappa."""
	#Parametri del messaggio
	parametri = {
		'chat_id': to,
		'latitude': lat,
		'longitude': long,
	}
	#Manda la richiesta ai server di Telegram.
	requests.get("https://api.telegram.org/bot" + telegramtoken + "/sendLocation", params=parametri)

def sendChatAction(to, type='typing'):
	"""Visualizza lo stato "sta scrivendo" del bot."""
	#Parametri del messaggio
	parametri = {
		'chat_id': to,
		'action': type,
	}
	#Manda la richiesta ai server di Telegram.
	requests.get("https://api.telegram.org/bot" + telegramtoken + "/sendChatAction", params=parametri)