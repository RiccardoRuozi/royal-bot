# -*- coding: utf-8 -*-
import telegram
import steam

print("Bot avviato!")
while(True):
	#Guarda il comando ricevuto.
	msg = telegram.getUpdates()
	cmd = msg['text'].split(' ', 1)
	sby = msg['chat']['id']
	if(cmd[0].startswith('/ahnonlosoio')):
		print('/ahnonlosoio')
		telegram.sendMessage("Ah, non lo so nemmeno io!", sby)
	elif(cmd[0].startswith('/ehoh')):
		print('/ehoh')
		telegram.sendMessage("Eh, oh. Sono cose che capitano.", sby)
	elif(cmd[0].startswith('/start')):
		print('/start')
		telegram.sendMessage("Ascolta, io mi starto quando mi pare. Anzi, quando Steffo ha voglia di aprirmi.", sby)
	elif(cmd[0].startswith('/playing')):
		print('/playing ...')
		if(len(cmd) >= 2):
			n = steam.getNumberOfCurrentPlayers(cmd[1])
			if(n == None):
				telegram.sendMessage(chr(9888) + " L'app specificata non esiste!", sby)
			else:
				telegram.sendMessage("In questo momento, " + str(n) + " persone stanno giocando a [" + cmd[1] + "](https://steamdb.info/app/" + cmd[1] + "/graphs/)", sby)
		else:
			telegram.sendMessage(chr(9888) + " Non hai specificato un AppID!\nLa sintassi corretta è /playing <AppID>.", sby)
	elif(cmd[0].startswith('/saldistim')):
		print('/saldistim ...')
		if(len(cmd) >= 2):
			telegram.sendMessage("Ricerca di offerte di [" + cmd[1] + "](https://isthereanydeal.com/#/search:" + cmd[1].replace(' ', '%20') + ";/scroll:%23gamelist) completata.", sby)
		else:
			telegram.sendMessage(chr(9888) + " Non hai specificato un gioco! [Visualizza tutte le offerte](https://isthereanydeal.com/#/search:.;/scroll:%23gamelist).", sby)
	elif(cmd[0].startswith('/rage')):
		print('/rage')
		telegram.sendDocument("BQADAgAD3wEAAh8GgAE6ZnLP5_gFMwI", sby)