# -*- coding: utf-8 -*-
import telegram
import steam

while(True):
	#Guarda il comando ricevuto.
	msg = telegram.getUpdates()
	cmd = msg['text'].split(' ')
	if(cmd[0].startswith('/ahnonlosoio')):
		telegram.sendMessage("Ah, non lo so nemmeno io!\n¯\_(ツ)_/¯")