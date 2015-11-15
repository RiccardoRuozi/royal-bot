# -*- coding: utf-8 -*-
import telegram
import steam
import random

# Playlist di /rage, si riempie quando è vuota
rage = []

print("Bot avviato!")
while True:
    # Guarda il comando ricevuto.
    msg = telegram.getupdates()
    cmd = msg['text'].split(' ', 1)
    sby = msg['chat']['id']
    if cmd[0].startswith('/ahnonlosoio'):
        print(str(sby) + ": /ahnonlosoio")
        telegram.sendmessage("Ah, non lo so nemmeno io!", sby)
    elif cmd[0].startswith('/ehoh'):
        print(str(sby) + ": /ehoh")
        telegram.sendmessage("Eh, oh. Sono cose che capitano.", sby)
    elif cmd[0].startswith('/start'):
        print(str(sby) + ": /start")
        telegram.sendmessage('Ascolta, io mi starto quando mi pare. Anzi, quando Steffo ha voglia di aprirmi.', sby)
    elif cmd[0].startswith('/playing'):
        print(str(sby) + ": /playing")
        if len(cmd) >= 2:
            n = steam.getNumberOfCurrentPlayers(cmd[1])
            if n is None:
                telegram.sendmessage(chr(9888) + " L'app specificata non esiste!", sby)
            else:
                telegram.sendmessage('In questo momento, ' + str(n) + ' persone stanno giocando a [' + cmd[1] +
                                     '](https://steamdb.info/app/' + cmd[1] + '/graphs/)', sby)
        else:
            telegram.sendmessage(chr(9888) + ' Non hai specificato un AppID!\nLa sintassi corretta è /playing <AppID>.',
                                 sby)
    elif cmd[0].startswith('/saldistim'):
        print(str(sby) + ": /saldistim")
        if len(cmd) >= 2:
            telegram.sendmessage(
                'Ricerca di offerte di ' +
                '[' + cmd[1] + '](https://isthereanydeal.com/#/search:' + cmd[1].replace(' ', '%20') +
                ";/scroll:%23gamelist) completata.", sby)
        else:
            telegram.sendmessage(chr(9888) +
                                 ' Non hai specificato un gioco!' +
                                 '[Visualizza tutto](https://isthereanydeal.com/#/search:.;/scroll:%23gamelist).', sby)
    elif cmd[0].startswith('/rage'):
        if len(rage) <= 0:
            # Elenco degli audio disponibili
            rage = ['BQADAgADEgIAAh8GgAGyLs6mbzxpVAI', 'BQADAgADEwIAAh8GgAGrT-MlTymm5gI',
                    'BQADAgADEQIAAh8GgAH62SrNqgXB6AI', 'BQADAgADEAIAAh8GgAHTLEngwtqr_QI',
                    'BQADAgAD3wEAAh8GgAE6ZnLP5_gFMwI', 'BQADAgAD5AEAAh8GgAGu0FpK_X2DuQI',
                    'BQADAgAD5gEAAh8GgAGvUTJ9meZixwI', 'BQADAgAD5wEAAh8GgAHJSoUnCr9WxwI',
                    'BQADAgAD6QEAAh8GgAExL8N1AWkDjgI', 'BQADAgAD6wEAAh8GgAFtkzazUqUEtwI',
                    'BQADAgAD9AEAAh8GgAE427GcA8FCqQI', 'BQADAgADMgIAAh8GgAEpusE7OCOXYgI',
                    'BQADAgADMwIAAh8GgAFffavzkvOkKAI', 'BQADAgADTAIAAh8GgAEgantYpHT5IwI']
            random.shuffle(rage)
        ragesend = rage.pop()
        print(str(sby) + ": /rage " + ragesend)
        telegram.senddocument(ragesend, sby)
    elif cmd[0].startswith('/sbam'):
        print(str(sby) + ": /sbam ")
        telegram.sendaudio('BQADAgADTQIAAh8GgAGj0jKIrpTgvQI', sby)
