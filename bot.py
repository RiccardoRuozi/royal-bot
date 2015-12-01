# -*- coding: utf-8 -*-
import telegram
import steam
import random
import osu

# Playlist di /rage, si riempie quando è vuota
rage = []

# Elenco degli audio di /wololo
wololo = ['BQADAgADWAIAAh8GgAGP53EPnRyiYwI', 'BQADAgADWQIAAh8GgAHIF861pVS1aAI', 'BQADAgADWgIAAh8GgAHdq5n4ZJwVBQI',
          'BQADAgADWwIAAh8GgAFBI_HmkOU-PgI', 'BQADAgADXAIAAh8GgAFjAmhg3-IOIQI', 'BQADAgADXQIAAh8GgAFf8P21MBzx3gI',
          'BQADAgADXgIAAh8GgAE5LOgedb-1RQI', 'BQADAgADYAIAAh8GgAFiAcVphkyzRQI', 'BQADAgADYQIAAh8GgAFnZa5sWEQv6QI',
          'BQADAgADYgIAAh8GgAHdnlwB6ATJogI', 'BQADAgADYwIAAh8GgAGMuHLrY94CXwI', 'BQADAgADZAIAAh8GgAE7SxHEvU6pLAI',
          'BQADAgADZQIAAh8GgAFfUK7GPQHLhgI', 'BQADAgADZgIAAh8GgAGDx56hsKHh0wI', 'BQADAgADZwIAAh8GgAF3etjqkzFDxAI',
          'BQADAgADaAIAAh8GgAHCsHs0NNMnAwI', 'BQADAgADaQIAAh8GgAGEQP7WW-gVhAI', 'BQADAgADagIAAh8GgAHrOerh1qI1jgI',
          'BQADAgADawIAAh8GgAFR8ckrXWOw6gI', 'BQADAgADbAIAAh8GgAFaQm4cTda94AI', 'BQADAgADbQIAAh8GgAG2X-qRdGpmewI',
          'BQADAgADbgIAAh8GgAHzrM2auYrj-AI', 'BQADAgADbwIAAh8GgAFq5jafCpl8PAI', 'BQADAgADcAIAAh8GgAGY69r5eir53QI',
          'BQADAgADcQIAAh8GgAH2Uj-JSM-4BwI', 'BQADAgADcgIAAh8GgAFGt6FRsV9kmAI', 'BQADAgADcwIAAh8GgAHSw9dKaqbZjgI',
          'BQADAgADdAIAAh8GgAF0IeDeuxaQ-AI', 'BQADAgADdQIAAh8GgAHJRO6c5-bodwI', 'BQADAgADdgIAAh8GgAEyyCSLdV_dMgI',
          'BQADAgADdwIAAh8GgAHrLJKjv16lWwI', 'BQADAgADeAIAAh8GgAFkaz8qZREelQI', 'BQADAgADeQIAAh8GgAG1rPQHEIjf6AI']

random.seed()

print("Bot avviato!")
while True:
    # Guarda il comando ricevuto.
    msg = telegram.getupdates()
    if 'text' in msg:
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
                n = steam.getnumberofcurrentplayers(cmd[1])
                if n is None:
                    telegram.sendmessage(chr(9888) + " L'app specificata non esiste!", sby)
                else:
                    telegram.sendmessage('In questo momento, ' + str(n) + ' persone stanno giocando a [' + cmd[1] +
                                         '](https://steamdb.info/app/' + cmd[1] + '/graphs/)', sby)
            else:
                telegram.sendmessage(chr(9888) + ' Non hai specificato un AppID!\n' +
                                     'La sintassi corretta è /playing <AppID>.', sby)
        elif cmd[0].startswith('/saldistim'):
            print(str(sby) + ": /saldistim")
            if len(cmd) >= 2:
                telegram.sendmessage(
                    'Ricerca di offerte di ' +
                    '[' + cmd[1] + '](https://isthereanydeal.com/#/search:' + cmd[1].replace(' ', '%20') +
                    ";/scroll:%23gamelist) completata.", sby)
            else:
                telegram.sendmessage(chr(9888) +
                                     ' Non hai specificato un gioco! ' +
                                     '[Visualizza tutto](https://isthereanydeal.com/#/search:.;/scroll:%23gamelist).',
                                     sby)
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
            telegram.senddocument('BQADAgADTQIAAh8GgAGj0jKIrpTgvQI', sby)
        elif cmd[0].startswith('/wololo'):
            print(str(sby) + ": /wololo")
            if len(cmd) >= 2:
                telegram.senddocument(wololo[int(cmd[1]) - 1], sby)
            else:
                telegram.senddocument('BQADAgADZwIAAh8GgAF3etjqkzFDxAI', sby)
        elif cmd[0].startswith('/osunow'):
            print(str(sby) + ": /osunow ")
            if len(cmd) >= 2:
                cmd = msg['text'].split(' ', 2)
                if len(cmd) >= 3:
                    mode = int(cmd[2])
                else:
                    mode = 0
                r = osu.getuserrecent(cmd[1], mode)
                if mode == 0:
                    telegram.sendmessage("*Osu!*\n" +
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r['beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n" +
                                         "*Combo* x" + r['maxcombo'] + "\n" +
                                         "*300*: " + r['count300'] + "\n" +
                                         "*100*: " + r['count100'] + "\n" +
                                         "*50*: " + r['count50'] + "\n" +
                                         "*Awesome*: " + r['countkatu'] + "\n" +
                                         "*Good*: " + r['countgeki'] + "\n" +
                                         "*Miss*: " + r['countmiss'], sby)
                elif mode == 1:
                    telegram.sendmessage("*Taiko*\n" +
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r['beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n" +
                                         "*Combo* x" + r['maxcombo'] + "\n" +
                                         "*Great*: " + r['count300'] + "\n" +
                                         "*Good*: " + r['count100'] + "\n" +
                                         "_Large_ *Great*: " + r['countkatu'] + "\n" +
                                         "_Large_ *Good*: " + r['countgeki'] + "\n" +
                                         "*Bad*: " + r['countmiss'], sby)
                elif mode == 2:
                    telegram.sendmessage("*Catch the Beat*\n" +
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r['beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n" +
                                         "*Combo* x" + r['maxcombo'] + "\n" +
                                         "*Fruit*: " + r['count300'] + "\n" +
                                         "*Droplet* _tick_: " + r['count100'] + "\n" +
                                         "*Droplet* _trail_: " + r['count50'] + "\n" +
                                         "*Miss*: " + r['countmiss'], sby)
                elif mode == 3:
                    telegram.sendmessage("*Osu!mania*\n" +
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r['beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n" +
                                         "*Combo* x" + r['maxcombo'] + "\n" +
                                         "_Rainbow_ *300*: " + r['countgeki'] + "\n" +
                                         "*300*: " + r['count300'] + "\n" +
                                         "*100*: " + r['count100'] + "\n" +
                                         "*200*: " + r['countkatu'] + "\n" +
                                         "*50*: " + r['count50'] + "\n" +
                                         "*Miss*: " + r['countmiss'], sby)
            else:
                # In futuro, il nome utente deve trovarlo da solo in base all'username di provenienza.
                telegram.sendmessage(chr(9888) + " Non hai specificato un nome utente!", sby)
        elif cmd[0].startswith('/roll'):
            if len(cmd) >= 2:
                m = int(cmd[1])
            else:
                m = 100
            n = random.randrange(m)
            telegram.sendmessage("Roll da 1 a " + str(m) + ": *" + str(n) + "*", sby)
        elif cmd[0].startswith('/automah'):
            print(str(sby) + ": /automah ")
            telegram.sendmessage("Automaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", sby)
