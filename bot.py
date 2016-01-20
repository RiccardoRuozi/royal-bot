# -*- coding: utf-8 -*-
import telegram
import steam
import random
import osu
import hearthstone
import sys

# Playlist di /rage, si riempie quando è vuota
rage = []

# TODO: Rimettere gli audio di Wololo
wololo = []

# Dizionario con i nomi utenti di osu!
# Se qualcuno cambia nome utente di Telegram, lo cambi anche QUI.
osunames = {
    'steffo': 'SteffoRYG',
    'evilbalu': 'NemesisRYG',
    'fultz': 'ftz99',
    'ilgattopardo': 'gattopardo',
    'frankrekt': 'FrankezRYG',
    'tiztiztiz': 'fedececco',
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

# Ciclo principale del bot
print("Bot avviato!")
while True:
    # Guarda il comando ricevuto.
    msg = telegram.getupdates()
    # Se il messaggio non è una notifica di servizio...
    if 'text' in msg:
        # Salvatelo in una stringa
        text = msg['text']
        # Guarda l'ID della chat in cui è stato inviato
        sentin = msg['chat']['id']
        # Nome da visualizzare nella console per capire chi accidenti è che invia messaggi strani
        if 'username' in msg['from']:
            # Salva l'username se esiste
            username = msg['from']['username']
        else:
            # Altrimenti, salva l'userID
            username = str(msg['from']['id'])
        # Riconosci il comando.
        # Viene usato startswith perchè il comando potrebbe anche essere inviato in forma /ciao@RoyalBot.
        if text.startswith('/ahnonlosoio'):
            print("@" + username + ": /ahnonlosoio")
            telegram.sendmessage("Ah, non lo so nemmeno io!", sentin)
        elif text.startswith('/ehoh'):
            print("@" + username + ": /ehoh")
            telegram.sendmessage("Eh, oh. Sono cose che capitano.", sentin)
        elif text.startswith('/playing'):
            print("@" + username + ": /playing")
            cmd = text.split(" ")
            # Se è stato specificato un AppID...
            if len(cmd) >= 2:
                n = steam.getnumberofcurrentplayers(cmd[1])
                # Se viene ricevuta una risposta...
                if n is None:
                    telegram.sendmessage(chr(9888) + " L'app specificata non esiste!", sentin)
                else:
                    telegram.sendmessage('In questo momento, ' + str(n) + ' persone stanno giocando a [' + cmd[1] +
                                         '](https://steamdb.info/app/' + cmd[1] + '/graphs/)', sentin)
            else:
                telegram.sendmessage(chr(9888) + ' Non hai specificato un AppID!\n'
                                     'La sintassi corretta è /playing <AppID>.', sentin)
        elif text.startswith('/saldi'):
            print("@" + username + ": /saldi")
            cmd = text.split(" ", 1)
            if len(cmd) == 2:
                telegram.sendmessage(
                    'Visualizza le offerte di '
                    '[' + cmd[1] + '](https://isthereanydeal.com/#/search:' + cmd[1].replace(' ', '%20') +
                    ";/scroll:%23gamelist).", sentin)
            else:
                telegram.sendmessage(chr(9888) +
                                     "Non hai specificato un gioco!"
                                     "[Visualizza tutte le offerte]"
                                     "(https://isthereanydeal.com/#/search:.;/scroll:%23gamelist).",
                                     sentin)
        # elif text.startswith('/audio'):
        #     # Se qualcuno ne ha voglia, qui si potrebbe aggiungere la selezione degli audio come argomento,
        #     # invece che fare una playlist casuale...
        #     # Se non ci sono rage nella playlist, riempila e mescolala!
        #     if len(rage) <= 0:
        #         # TODO: Rimettere gli audio di /audio
        #         rage = []
        #         random.shuffle(rage)
        #     # Estrai un audio a caso tra quelli nella playlist e rimuovilo.
        #     ragesend = rage.pop()
        #     print("@" + username + ": /audio")
        #     telegram.senddocument(ragesend, sentin)
        elif text.startswith('/sbam'):
            print("@" + username + ": /sbam")
            telegram.senddocument('BQADAgADBwMAAh8GgAGSsR4rwmk_LwI', sentin)
        # elif text.startswith('/wololo'):
        #     print("@" + username + ": /wololo")
        #     if len(cmd) >= 2:
        #         telegram.senddocument(wololo[int(cmd[1]) - 1], sentin)
        #     else:
        #         telegram.senddocument('BQADAgADZwIAAh8GgAF3etjqkzFDxAI', sentin)
        elif text.startswith('/osu'):
            print("@" + username + ": /osu")
            # Trova il nome utente
            cmd = text.split(' ', 1)
            if len(cmd) >= 2:
                # Trova la modalità
                cmd = text.split(' ', 2)
                if len(cmd) >= 3:
                    # Modalità specificata
                    mode = int(cmd[2])
                else:
                    # Osu! normale
                    mode = 0
                r = osu.getuserrecent(cmd[1], mode)
                if mode == 0:
                    telegram.sendmessage("*Osu!*\n"
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n"
                                         "*Combo* x" + r['maxcombo'] + "\n"
                                         "*300*: " + r['count300'] + "\n"
                                         "*100*: " + r['count100'] + "\n"
                                         "*50*: " + r['count50'] + "\n"
                                         "*Awesome*: " + r['countkatu'] + "\n"
                                         "*Good*: " + r['countgeki'] + "\n"
                                         "*Miss*: " + r['countmiss'], sentin)
                elif mode == 1:
                    telegram.sendmessage("*Taiko*\n"
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n"
                                         "*Combo* x" + r['maxcombo'] + "\n"
                                         "*Great*: " + r['count300'] + "\n"
                                         "*Good*: " + r['count100'] + "\n"
                                         "_Large_ *Great*: " + r['countkatu'] + "\n"
                                         "_Large_ *Good*: " + r['countgeki'] + "\n"
                                         "*Bad*: " + r['countmiss'], sentin)
                elif mode == 2:
                    telegram.sendmessage("*Catch the Beat*\n"
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n"
                                         "*Combo* x" + r['maxcombo'] + "\n"
                                         "*Fruit*: " + r['count300'] + "\n"
                                         "*Droplet* _tick_: " + r['count100'] + "\n"
                                         "*Droplet* _trail_: " + r['count50'] + "\n"
                                         "*Miss*: " + r['countmiss'], sentin)
                elif mode == 3:
                    telegram.sendmessage("*Osu!mania*\n" +
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] + ")\n*" + r['rank'] +
                                         "*\n*Punti*: " + r['score'] + "\n"
                                         "*Combo* x" + r['maxcombo'] + "\n"
                                         "_Rainbow_ *300*: " + r['countgeki'] + "\n"
                                         "*300*: " + r['count300'] + "\n"
                                         "*100*: " + r['count100'] + "\n"
                                         "*200*: " + r['countkatu'] + "\n"
                                         "*50*: " + r['count50'] + "\n"
                                         "*Miss*: " + r['countmiss'], sentin)
            else:
                # E' un po' una scorciatoia eh, peeerò...
                if username.lower() in osunames:
                    r = osu.getuserrecent(osunames[username.lower()], 0)
                    telegram.sendmessage("*Osu!*\n"
                                         "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                             'beatmap_id'] +
                                         ")\n*" + r['rank'] + "*\n*Punti*: " + r['score'] + "\n"
                                         "*Combo* x" + r['maxcombo'] + "\n"
                                         "*300*: " + r['count300'] + "\n"
                                         "*100*: " + r['count100'] + "\n"
                                         "*50*: " + r['count50'] + "\n"
                                         "*Awesome*: " + r['countkatu'] + "\n"
                                         "*Good*: " + r['countgeki'] + "\n"
                                         "*Miss*: " + r['countmiss'], sentin)
        elif text.startswith('/roll'):
            print("@" + username + ": /roll")
            cmd = text.split(' ', 1)
            if len(cmd) >= 2:
                m = int(cmd[1])
            else:
                m = 100
            n = random.randrange(m) + 1
            telegram.sendmessage("Numero casuale da 1 a " + str(m) + ":\n*" + str(n) + "*", sentin)
        elif text.startswith('/automah'):
            print("@" + username + ": /automah")
            # TODO: Mettere l'audio di Tobia
            telegram.sendmessage("Automaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa! Devi funzionare, cavolo!", sentin)
        elif text.startswith('/hs'):
            print(username + ": /hs")
            cmd = text.split(" ", 1)
            r = None
            try:
                r = hearthstone.card(cmd[1])
                # Se ci sono più carte, prendine una a caso!
                r = r[random.randrange(len(r))]
            except ValueError:
                telegram.sendmessage(chr(9888) + "La carta specificata non esiste!", sentin)
            else:
                # Si trova nelle bustine
                if 'howToGet' not in r:
                    if 'cardSet' in r:
                        r['howToGet'] = "Trovala in " + r['cardSet'] + "."
                    else:
                        r['howToGet'] = "Inottenibile."
                # Nessuna classe
                if 'playerClass' not in r:
                    r['playerClass'] = "Neutral"
                # Nessun effetto
                if 'text' not in r:
                    r['text'] = ""
                # HTML nella descrizione
                r['text'] = r['text'].replace("<b>", "*")
                r['text'] = r['text'].replace("</b>", "*")
                r['text'] = r['text'].replace("<i>", "_")
                r['text'] = r['text'].replace("</i>", "_")
                r['text'] = r['text'].replace("$", "")
                # Nessuna rarità
                if 'rarity' not in r:
                    r['rarity'] = "None"
                # Nessuna descrizione
                if 'flavor' not in r:
                    r['flavor'] = ""
                # Testo principale
                text = None
                # Magie
                if r['type'] == "Spell":
                    text = str("[" + r['name'] + "](" + r['img'] + ") "
                               "(" + r['rarity'] + ")\n" +
                               r['playerClass'] + "\n" +
                               str(r['cost']) + " mana\n" +
                               r['text'] + "\n" +
                               r['howToGet'] + "\n\n_" +
                               r['flavor'] + "_\n")
                # Servitori
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
                # Armi
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
                # Potere Eroe
                elif r['type'] == "Hero Power":
                    text = str("[" + r['name'] + "](" + r['img'] + ")\n" +
                               r['playerClass'] + "\n" +
                               str(r['cost']) + " mana\n" +
                               r['text'] + "\n")
                # Eroe
                elif r['type'] == "Hero":
                    text = str("[" + r['name'] + "](" + r['img'] + ")\n" +
                               str(r['health']) + " salute\n")
                telegram.sendmessage(text, sentin)
        elif text.startswith('/restart'):
            if username == "Steffo":
                telegram.sendmessage("Riavvio accettato.", sentin)
                sys.exit(0)
