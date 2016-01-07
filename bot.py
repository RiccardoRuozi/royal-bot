# -*- coding: utf-8 -*-
import telegram
import steam
import random
import osu
import hearthstone
import sys

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

# Dizionario con i nomi utenti di osu!
# Se qualcuno cambia nome utente di Telegram, lo cambi anche QUI.
osunames = {
    'steffo': 'SteffoRYG',
    'evilbalu': 'NemesisRYG',
    'fultz': 'ftz99',
    'ilgattopardo': 'gattopardo',
    'frankfrankfrank': 'FrankezRYG',
    'fedyal': 'fedececco',
    'acterryg': 'Acter1',
    'maxsensei': 'MaxSensei',
    'heisendoc': 'ImHeisenberg',
    'thevagginadestroyer': 'barboll',
    'cosimo03': 'Cosimo03',
    'albertino04': 'Alby1',
    'voltaggio': 'voltaggio',
    'tauei': 'tauei',
    'boni3099': 'boni3099',
    'mrdima98': 'MRdima98',
}

random.seed()

# Ciclo principale del bot! Mettete qui la roba che deve fare.
print("Bot avviato!")
while True:
    # Guarda il comando ricevuto.
    msg = telegram.getupdates()
    # Se il messaggio è un comando...
    if 'text' in msg:
        # Dividilo con degli spazi e metti il comando in cmd[0] e gli argomenti in cmd[1]
        cmd = msg['text'].split(' ', 1)
        # Guarda l'ID della chat in cui è stato inviato
        sby = msg['chat']['id']
        # Nome da visualizzare nella console per capire chi accidenti è che invia messaggi strani
        if 'username' in msg['from']:
            # Visualizza l'username se esiste
            unm = '@' + msg['from']['username']
        else:
            # Altrimenti, visualizza l'userID
            unm = str(msg['from']['id'])
        # Riconosci il comando.
        # Viene usato startswith perchè il comando potrebbe anche essere inviato in forma /ciao@RoyalBot.
        if cmd[0].startswith('/ahnonlosoio'):
            print(unm + ": /ahnonlosoio")
            telegram.sendmessage("Ah, non lo so nemmeno io!", sby)
        elif cmd[0].startswith('/ehoh'):
            print(unm + ": /ehoh")
            telegram.sendmessage("Eh, oh. Sono cose che capitano.", sby)
        elif cmd[0].startswith('/playing'):
            print(unm + ": /playing")
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
        elif cmd[0].startswith('/saldi'):
            print(unm + ": /saldi")
            if len(cmd) >= 2:
                telegram.sendmessage(
                    'Visualizza le offerte di ' +
                    '[' + cmd[1] + '](https://isthereanydeal.com/#/search:' + cmd[1].replace(' ', '%20') +
                    ";/scroll:%23gamelist).", sby)
            else:
                telegram.sendmessage(chr(9888) +
                                     ' Non hai specificato un gioco! ' +
                                     '[Visualizza tutto](https://isthereanydeal.com/#/search:.;/scroll:%23gamelist).',
                                     sby)
        elif cmd[0].startswith('/audio'):
            # Se qualcuno ne ha voglia, qui si potrebbe aggiungere la selezione degli audio come argomento,
            # invece che fare una playlist casuale...
            # Se non ci sono rage nella playlist, riempila e mescolala!
            if len(rage) <= 0:
                # Elenco degli audio disponibili
                rage = ['BQADAgADEgIAAh8GgAGyLs6mbzxpVAI', 'BQADAgADEwIAAh8GgAGrT-MlTymm5gI',
                        'BQADAgADEQIAAh8GgAH62SrNqgXB6AI', 'BQADAgADEAIAAh8GgAHTLEngwtqr_QI',
                        'BQADAgAD3wEAAh8GgAE6ZnLP5_gFMwI', 'BQADAgAD5AEAAh8GgAGu0FpK_X2DuQI',
                        'BQADAgAD5gEAAh8GgAGvUTJ9meZixwI', 'BQADAgAD5wEAAh8GgAHJSoUnCr9WxwI',
                        'BQADAgAD6QEAAh8GgAExL8N1AWkDjgI', 'BQADAgAD6wEAAh8GgAFtkzazUqUEtwI',
                        'BQADAgAD9AEAAh8GgAE427GcA8FCqQI', 'BQADAgADMgIAAh8GgAEpusE7OCOXYgI',
                        'BQADAgADMwIAAh8GgAFffavzkvOkKAI', 'BQADAgADTAIAAh8GgAEgantYpHT5IwI',
                        'BQADAgADpgIAAh8GgAFu0RmpD3Mw7wI', 'BQADAgADpwIAAh8GgAGUgGD5t1omDwI',
                        'BQADAgADqAIAAh8GgAFNZ_rptavtKAI', 'BQADAgADqQIAAh8GgAGtd74-VO-J1AI',
                        'BQADAgADqgIAAh8GgAGa5MDYCi7viwI', 'BQADAgADqwIAAh8GgAGM3vOELWDm3AI',
                        'BQADAgADrAIAAh8GgAHF15LlwjLMbwI', 'BQADAgADrgIAAh8GgAE2T5cM_TCQVQI',
                        'BQADAgADrwIAAh8GgAGYcc3JtCsZ1AI']
                random.shuffle(rage)
            # Estrai un audio a caso tra quelli nella playlist e rimuovilo.
            ragesend = rage.pop()
            print(unm + ": /audio")
            telegram.senddocument(ragesend, sby)
        elif cmd[0].startswith('/sbam'):
            print(unm + ": /sbam")
            telegram.senddocument('BQADAgADTQIAAh8GgAGj0jKIrpTgvQI', sby)
        elif cmd[0].startswith('/wololo'):
            print(unm + ": /wololo")
            if len(cmd) >= 2:
                telegram.senddocument(wololo[int(cmd[1]) - 1], sby)
            else:
                telegram.senddocument('BQADAgADZwIAAh8GgAF3etjqkzFDxAI', sby)
        elif cmd[0].startswith('/osu'):
            print(unm + ": /osu")
            if len(cmd) >= 2:
                cmd = msg['text'].split(' ', 2)
                if len(cmd) >= 3:
                    mode = int(cmd[2])
                else:
                    mode = 0
                r = osu.getuserrecent(cmd[1], mode)
                if mode == 0:
                    telegram.sendmessage("*Osu!*\n" +
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] +
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
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n" +
                                         "*Combo* x" + r['maxcombo'] + "\n" +
                                         "*Great*: " + r['count300'] + "\n" +
                                         "*Good*: " + r['count100'] + "\n" +
                                         "_Large_ *Great*: " + r['countkatu'] + "\n" +
                                         "_Large_ *Good*: " + r['countgeki'] + "\n" +
                                         "*Bad*: " + r['countmiss'], sby)
                elif mode == 2:
                    telegram.sendmessage("*Catch the Beat*\n" +
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n" +
                                         "*Combo* x" + r['maxcombo'] + "\n" +
                                         "*Fruit*: " + r['count300'] + "\n" +
                                         "*Droplet* _tick_: " + r['count100'] + "\n" +
                                         "*Droplet* _trail_: " + r['count50'] + "\n" +
                                         "*Miss*: " + r['countmiss'], sby)
                elif mode == 3:
                    telegram.sendmessage("*Osu!mania*\n" +
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n" +
                                         "*Combo* x" + r['maxcombo'] + "\n" +
                                         "_Rainbow_ *300*: " + r['countgeki'] + "\n" +
                                         "*300*: " + r['count300'] + "\n" +
                                         "*100*: " + r['count100'] + "\n" +
                                         "*200*: " + r['countkatu'] + "\n" +
                                         "*50*: " + r['count50'] + "\n" +
                                         "*Miss*: " + r['countmiss'], sby)
            else:
                # E' un po' una scorciatoia eh, peeerò...
                if unm[1:].lower() in osunames:
                    r = osu.getuserrecent(osunames[unm[1:].lower()], 0)
                    telegram.sendmessage("*Osu!*\n" +
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n" +
                                         "*Combo* x" + r['maxcombo'] + "\n" +
                                         "*300*: " + r['count300'] + "\n" +
                                         "*100*: " + r['count100'] + "\n" +
                                         "*50*: " + r['count50'] + "\n" +
                                         "*Awesome*: " + r['countkatu'] + "\n" +
                                         "*Good*: " + r['countgeki'] + "\n" +
                                         "*Miss*: " + r['countmiss'], sby)
        elif cmd[0].startswith('/roll'):
            if len(cmd) >= 2:
                m = int(cmd[1])
            else:
                m = 100
            n = random.randrange(m)
            telegram.sendmessage("Numero casuale da 1 a " + str(m) + ":\n*" + str(n) + "*", sby)
        elif cmd[0].startswith('/automah'):
            print(unm + ": /automah")
            # Quando mi manda l'audio GoToB?
            telegram.sendmessage("Automaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa! Devi funzionare, cavolo!", sby)
        elif cmd[0].startswith('/hs'):
            print(unm + ": /hs")
            r = None
            try:
                r = hearthstone.card(cmd[1])[0]
            except ValueError:
                telegram.sendmessage(chr(9888) + "La carta specificata non esiste!", sby)
            else:
                # Si trova nelle bustine
                if 'howToGet' not in r:
                    if 'cardSet' in r:
                        r['howToGet'] = "Trovala nelle bustine " + r['cardSet'] + "."
                    else:
                        r['howToGet'] = "Inottenibile."
                # Nessuna classe
                if 'playerClass' not in r:
                    r['playerClass'] = "Neutral"
                # Nessun effetto
                if 'text' not in r:
                    r['text'] = "_Nessun effetto._"
                # Nessuna rarità
                if 'rarity' not in r:
                    r['rarity'] = "None"
                # Nessuna descrizione
                if 'flavor' not in r:
                    r['flavor'] = "Nessuna descrizione."
                # Testo principale
                text = None
                if r['type'] == "Spell":
                    text = str("[" + r['name'] + "](" + r['img'] + ") "
                               "(" + r['rarity'] + ")\n" +
                               r['playerClass'] + "\n" +
                               str(r['cost']) + " mana\n" +
                               r['text'] + "\n" +
                               r['howToGet'] + "\n\n_" +
                               r['flavor'] + "_\n")
                elif r['type'] == "Minion":
                    text = str("[" + r['name'] + "](" + r['img'] + ") "
                               "(" + r['rarity'] + ")\n" +
                               r['playerClass'] + "\n" +
                               str(r['cost']) + " mana\n" +
                               str(r['attack']) + " attacco\n" +
                               str(r['health']) + " salute\n" +
                               r['text'] + "\n" +
                               r['howToGet'] + "\n\n_" +
                               r['flavor'] + "_\n")
                elif r['type'] == "Weapon":
                    text = str("[" + r['name'] + "](" + r['img'] + ") "
                               "(" + r['rarity'] + ")\n" +
                               r['playerClass'] + "\n" +
                               str(r['cost']) + " mana\n" +
                               str(r['attack']) + " attacco\n" +
                               str(r['durability']) + " integrita'\n" +
                               r['text'] + "\n" +
                               r['howToGet'] + "\n\n_" +
                               r['flavor'] + "_\n")
                elif r['type'] == "Hero Power":
                    text = str("[" + r['name'] + "](" + r['img'] + ")\n" +
                               r['playerClass'] + "\n" +
                               str(r['cost']) + " mana\n" +
                               r['text'] + "\n")
                elif r['type'] == "Hero":
                    text = str("[" + r['name'] + "](" + r['img'] + ")\n" +
                               str(r['health']) + " salute\n")
                telegram.sendmessage(text, sby)
        elif(cmd[0].startswith('/everyonegetinhere')):
            print(unm + ": /everyonegetinhere")
            telegram.sendMessage("@ActerRYG \n@Adry99 \n@Alleanderl \n@Boni3099 \n@Cosimo03 \n@EnriBenassati \n@EvilBalu \n@FrankRekt \n@Fultz \n@GoToB \n@HeisenDoc \n@iEmax \n@IlGattopardo \n@MaxSensei \n@MRdima98 \n@Peramela99 \n@RuoziR \n@SuperSmurf \n@Steffo \n@Tauei \n@thevagginadestroyer \n@Vivalafigliadellortolano \n@Voltaggio", -2141322)
        elif cmd[0].startswith('/restart'):
            if unm == "@Steffo":
                telegram.sendmessage("Riavvio confermato.", sby)
                sys.exit(0)


