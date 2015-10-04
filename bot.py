# -*- coding: utf-8 -*-
import telegram
import steam

while(True):
	#Guarda il comando ricevuto.
	msg = telegram.getUpdates()
	print(msg['text'])
	cmd = msg['text'].split(' ')
	sby = msg['chat']['id']
	if(cmd[0].startswith('/ahnonlosoio')):
		telegram.sendMessage("Ah, non lo so nemmeno io!", sby)
	elif(cmd[0].startswith('/ehoh')):
		telegram.sendMessage("Eh, oh. Sono cose che capitano.", sby)
	elif(cmd[0].startswith('/start')):
		telegram.sendMessage("Ascolta, io mi starto quando mi pare. Anzi, quando @Steffo ha voglia di aprirmi.", sby)
	elif(cmd[0].startswith('/playing')):
		if(cmd[1] is not None):
			n = steam.getNumberOfCurrentPlayers(cmd[1])
			if(n == None):
				telegram.sendMessage(chr(9888) + " L'app specificata non esiste!", sby)
			else:
				telegram.sendMessage("In questo momento, " + str(n) + " persone stanno giocando a *ID: " + cmd[1] + "*", sby)
		else:
			telegram.sendMessage(chr(9888) + " Non hai specificato un AppID!\nLa sintassi corretta è /playing <AppID>.", sby)