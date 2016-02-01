# -*- coding: utf-8 -*-
import time
import filemanager
import telegram
import steam
import random
import osu
import hearthstone
import sys
import mumbleboxes


# Check per la modalità votazione del bot, corrisponde al numero della chat in cui è attiva la votazione
# 0 per disattivare la votazione
class Votazione:
    chat = int()
    domanda = str()
    # 0: non votato
    # 1: sì
    # 2: no
    # 3: astenuto
    voto = {
        'steffo': int(0),
        'alby1': int(0),
        'boni3099': int(0),
        'maxsensei': int(0),
        'cosimo03': int(0),
        'frankrekt': int(0),
        'heisendoc': int(0),
        'acterryg': int(0),
        'adry99': int(0),
        'alleanderl': int(0),
        'thevagginadestroyer': int(0),
        'tiztiztiz': int(0),
        'fultz': int(0),
        'gotob': int(0),
        'enribenassati': int(0),
        'iemax': int(0),
        'peraemela99': int(0),
        'ilgattopardo': int(0),
        'mrdima98': int(0),
        'ruozir': int(0),
        'supersmurf': int(0),
        'tauei': int(0),
        'voltaggio': int(0),
        'gibait': int(0),
    }

    def __init__(self, question, askin):
        self.domanda = question
        self.chat = askin

    def ask(self):
        telegram.sendmessage(self.domanda, self.chat)

    def register(self, utente, voto):
        self.voto[utente] = voto

    def showresults(self):
        lista = str()
        si = 0
        no = 0
        astenuti = 0
        for membro in self.voto:
            if self.voto[membro] == 0:
                lista += chr(9898)
            elif self.voto[membro] == 1:
                si += 1
                lista += chr(128309)
            elif self.voto[membro] == 2:
                no += 1
                lista += chr(128308)
            elif self.voto[membro] == 3:
                astenuti += 1
                lista += chr(9899)
            lista += " @" + membro + "\n"
        telegram.sendmessage(self.domanda + "\n"
                             "*Risultati:*\n"
                             "Sì: " + str(si) + " (" + str(round(si / (si + no + astenuti) * 100, 2)) + "%)\n"
                             "No: " + str(no) + " (" + str(round(no / (si + no + astenuti) * 100, 2)) + "%)\n"
                             "Astenuti: " + str(astenuti) + "\n\n" + lista, self.chat)

# Votazione in corso
incorso = None

# Playlist di /rage, si riempie quando è vuota
rage = []

# TODO: Rimettere gli audio di Wololo
# wololo = []

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

# Elenco di username dei membri della RYG
telegramnames = ['steffo', 'alby1', 'boni3099', 'maxsensei', 'cosimo03', 'frankrekt', 'heisendoc', 'acterryg', 'adry99',
                 'alleanderl', 'thevagginadestroyer', 'tiztiztiz', 'fultz', 'gotob', 'enribenassati', 'iemax',
                 'peraemela99', 'ilgattopardo', 'mrdima98', 'ruozir', 'supersmurf', 'tauei', 'voltaggio', 'gibait']

# Dizionario con gli steamID
# Vedi sopra
steamids = {
    'steffo': 76561198034314260,
    'alby1': 76561198071383448,
    'boni3099': 76561198131868211,
    'maxsensei': 76561198121094516,
    'cosimo03': 76561198062778224,
    'frankrekt': 76561198071099951,
    'heisendoc': 76561198080377213,
    'acterryg': 76561198146704979,
    'adry99': 76561198230034568,
    'alleanderl': 76561198154175301,
    'thevagginadestroyer': 76561198128738388,
    'tiztiztiz': 76561198109189938,
    'fultz': 76561198035547490,
    'gattino02': 76561198071069550,
    'gotob': 76561198096658890,
    'enribenassati': 76561198123018368,
    'iemax': 76561198149695151,
    'peraemela99': 76561198161867082,
    'ilgattopardo': 76561198111021344,
    'mrdima98': 76561198140863530,
    'ruozir': 76561198117708290,
    'supersmurf': 76561198115852550,
    'tauei': 76561198104305298,
    'voltaggio': 76561198147601821,
    'gibait': 76561198157721704,
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
        # ID del messaggio ricevuto
        source = msg['message_id']
        # Nome da visualizzare nella console per capire chi accidenti è che invia messaggi strani
        if 'username' in msg['from']:
            # Salva l'username se esiste
            username = msg['from']['username']
        else:
            # Altrimenti, salva l'userID
            username = str(msg['from']['id'])
        # Se sei un membro della Royal Games
        if username.lower() in telegramnames:
            # Riconosci il comando.
            # Viene usato startswith perchè il comando potrebbe anche essere inviato in forma /ciao@RoyalBot.
            if text.startswith('/ahnonlosoio'):
                print("@" + username + ": /ahnonlosoio")
                telegram.sendmessage("Ah, non lo so nemmeno io!", sentin, source)
            elif text.startswith('/ehoh'):
                print("@" + username + ": /ehoh")
                telegram.sendmessage("Eh, oh. Sono cose che capitano.", sentin, source)
            elif text.startswith('/playing'):
                print("@" + username + ": /playing")
                # Informa Telegram che il messaggio è stato ricevuto.
                telegram.sendchataction(sentin)
                cmd = text.split(" ")
                # Se è stato specificato un AppID...
                if len(cmd) >= 2:
                    n = steam.getnumberofcurrentplayers(cmd[1])
                    # Se viene ricevuta una risposta...
                    if n is None:
                        telegram.sendmessage(chr(9888) + " L'app specificata non esiste!", sentin, source)
                    else:
                        telegram.sendmessage('In questo momento, ' + str(n) + ' persone stanno giocando a [' + cmd[1] +
                                             '](https://steamdb.info/app/' + cmd[1] + '/graphs/)', sentin, source)
                else:
                    telegram.sendmessage(chr(9888) + ' Non hai specificato un AppID!\n'
                                         'La sintassi corretta è /playing <AppID>.', sentin, source)
            elif text.startswith('/saldi'):
                print("@" + username + ": /saldi")
                # Informa Telegram che il messaggio è stato ricevuto.
                telegram.sendchataction(sentin)
                cmd = text.split(" ", 1)
                if len(cmd) == 2:
                    telegram.sendmessage(
                        'Visualizza le offerte di '
                        '[' + cmd[1] + '](https://isthereanydeal.com/#/search:' + cmd[1].replace(' ', '%20') +
                        ";/scroll:%23gamelist).", sentin, source)
                else:
                    telegram.sendmessage(chr(9888) +
                                         " Non hai specificato un gioco!"
                                         "[Visualizza tutte le offerte]"
                                         "(https://isthereanydeal.com/#/search:.;/scroll:%23gamelist).",
                                         sentin, source)
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
            #     telegram.senddocument(ragesend, sentin, source)
            elif text.startswith('/sbam'):
                print("@" + username + ": /sbam")
                telegram.senddocument('BQADAgADBwMAAh8GgAGSsR4rwmk_LwI', sentin)
            # elif text.startswith('/wololo'):
            #     print("@" + username + ": /wololo")
            #     if len(cmd) >= 2:
            #         telegram.senddocument(wololo[int(cmd[1]) - 1], sentin, source)
            #     else:
            #         telegram.senddocument('BQADAgADZwIAAh8GgAF3etjqkzFDxAI', sentin, source)
            elif text.startswith('/osu'):
                print("@" + username + ": /osu")
                # Informa Telegram che il messaggio è stato ricevuto.
                telegram.sendchataction(sentin)
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
                    try:
                        r = osu.getuserrecent(cmd[1], mode)
                    except NameError:
                        telegram.sendmessage(chr(9888) + " Errore nella richiesta ai server di Osu!", sentin, source)
                    else:
                        if "enabled_mods" in r:
                            mods = "*Mod:*"
                            # Adoro SE
                            # Dividi in bit l'ID delle mod selezionate
                            if int(r['enabled_mods']) & 0b1:
                                mods += " NoFail"
                            if int(r['enabled_mods']) & 0b10:
                                mods += " Easy"
                            if int(r['enabled_mods']) & 0b100:
                                mods += " NoVideo (?)"
                            if int(r['enabled_mods']) & 0b1000:
                                mods += " Hidden"
                            if int(r['enabled_mods']) & 0b10000:
                                mods += " HardRock"
                            if int(r['enabled_mods']) & 0b100000:
                                mods += " SuddenDeath"
                            if int(r['enabled_mods']) & 0b1000000:
                                mods += " DoubleTime"
                            if int(r['enabled_mods']) & 0b10000000:
                                mods += " Relax"
                            if int(r['enabled_mods']) & 0b100000000:
                                mods += " HalfTime"
                            if int(r['enabled_mods']) & 0b1000000000:
                                mods += " Nightcore"
                            if int(r['enabled_mods']) & 0b10000000000:
                                mods += " Flashlight"
                            if int(r['enabled_mods']) & 0b100000000000:
                                mods += " Autoplay"
                            if int(r['enabled_mods']) & 0b1000000000000:
                                mods += " SpunOut"
                            if int(r['enabled_mods']) & 0b10000000000000:
                                mods += " Autopilot"
                            if int(r['enabled_mods']) & 0b100000000000000:
                                mods += " Perfect"
                            if int(r['enabled_mods']) & 0b1000000000000000:
                                mods += " 4K"
                            if int(r['enabled_mods']) & 0b10000000000000000:
                                mods += " 5K"
                            if int(r['enabled_mods']) & 0b100000000000000000:
                                mods += " 6K"
                            if int(r['enabled_mods']) & 0b1000000000000000000:
                                mods += " 7K"
                            if int(r['enabled_mods']) & 0b10000000000000000000:
                                mods += " 8K"
                            if int(r['enabled_mods']) & 0b100000000000000000000:
                                mods += " FadeIn"
                            if int(r['enabled_mods']) & 0b1000000000000000000000:
                                mods += " Random"
                            if int(r['enabled_mods']) & 0b1000000000000000000000000:
                                mods += " 9K"
                            if int(r['enabled_mods']) & 0b10000000000000000000000000:
                                mods += " 10K"
                            if int(r['enabled_mods']) & 0b100000000000000000000000000:
                                mods += " 1K"
                            if int(r['enabled_mods']) & 0b1000000000000000000000000000:
                                mods += " 3K"
                            if int(r['enabled_mods']) & 0b10000000000000000000000000000:
                                mods += " 2K"
                            mods += '\n'
                        else:
                            mods = '\n'
                        if mode == 0:
                            telegram.sendmessage("*Osu!*\n"
                                                 "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                                     'beatmap_id'] +
                                                 ")\n*" + r['rank'] + "*\n" + mods +
                                                 "*Punti*: " + r['score'] + "\n"
                                                 "*Combo* x" + r['maxcombo'] + "\n"
                                                 "*300*: " + r['count300'] + "\n"
                                                 "*100*: " + r['count100'] + "\n"
                                                 "*50*: " + r['count50'] + "\n"
                                                 "*Awesome*: " + r['countkatu'] + "\n"
                                                 "*Good*: " + r['countgeki'] + "\n"
                                                 "*Miss*: " + r['countmiss'], sentin, source)
                        elif mode == 1:
                            telegram.sendmessage("*Taiko*\n"
                                                 "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                                     'beatmap_id'] +
                                                 ")\n*" + r['rank'] + "*\n" + mods +
                                                 "\n*Punti*: " + r['score'] + "\n"
                                                 "*Combo* x" + r['maxcombo'] + "\n"
                                                 "*Great*: " + r['count300'] + "\n"
                                                 "*Good*: " + r['count100'] + "\n"
                                                 "_Large_ *Great*: " + r['countkatu'] + "\n"
                                                 "_Large_ *Good*: " + r['countgeki'] + "\n"
                                                 "*Bad*: " + r['countmiss'], sentin, source)
                        elif mode == 2:
                            telegram.sendmessage("*Catch the Beat*\n"
                                                 "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                                     'beatmap_id'] +
                                                 ")\n*" + r['rank'] + "*\n" + mods +
                                                 "\n*Punti*: " + r['score'] + "\n"
                                                 "*Combo* x" + r['maxcombo'] + "\n"
                                                 "*Fruit*: " + r['count300'] + "\n"
                                                 "*Droplet* _tick_: " + r['count100'] + "\n"
                                                 "*Droplet* _trail_: " + r['count50'] + "\n"
                                                 "*Miss*: " + r['countmiss'], sentin, source)
                        elif mode == 3:
                            telegram.sendmessage("*Osu!mania*\n" +
                                                 "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                                     'beatmap_id'] + ")\n*" + r['rank'] + "*\n" + mods +
                                                 "\n*Punti*: " + r['score'] + "\n"
                                                 "*Combo* x" + r['maxcombo'] + "\n"
                                                 "_Rainbow_ *300*: " + r['countgeki'] + "\n"
                                                 "*300*: " + r['count300'] + "\n"
                                                 "*100*: " + r['count100'] + "\n"
                                                 "*200*: " + r['countkatu'] + "\n"
                                                 "*50*: " + r['count50'] + "\n"
                                                 "*Miss*: " + r['countmiss'], sentin, source)
                else:
                    # TODO: Mettere a posto sto schifo.
                    if username.lower() in osunames:
                        r = osu.getuserrecent(osunames[username.lower()], 0)
                        if "enabled_mods" in r:
                            mods = "*Mod:*"
                            # Adoro SE
                            # Dividi in bit l'ID delle mod selezionate
                            if int(r['enabled_mods']) & 0b1:
                                mods += " NoFail"
                            if int(r['enabled_mods']) & 0b10:
                                mods += " Easy"
                            if int(r['enabled_mods']) & 0b100:
                                mods += " NoVideo (?)"
                            if int(r['enabled_mods']) & 0b1000:
                                mods += " Hidden"
                            if int(r['enabled_mods']) & 0b10000:
                                mods += " HardRock"
                            if int(r['enabled_mods']) & 0b100000:
                                mods += " SuddenDeath"
                            if int(r['enabled_mods']) & 0b1000000:
                                mods += " DoubleTime"
                            if int(r['enabled_mods']) & 0b10000000:
                                mods += " Relax"
                            if int(r['enabled_mods']) & 0b100000000:
                                mods += " HalfTime"
                            if int(r['enabled_mods']) & 0b1000000000:
                                mods += " Nightcore"
                            if int(r['enabled_mods']) & 0b10000000000:
                                mods += " Flashlight"
                            if int(r['enabled_mods']) & 0b100000000000:
                                mods += " Autoplay"
                            if int(r['enabled_mods']) & 0b1000000000000:
                                mods += " SpunOut"
                            if int(r['enabled_mods']) & 0b10000000000000:
                                mods += " Autopilot"
                            if int(r['enabled_mods']) & 0b100000000000000:
                                mods += " Perfect"
                            if int(r['enabled_mods']) & 0b1000000000000000:
                                mods += " 4K"
                            if int(r['enabled_mods']) & 0b10000000000000000:
                                mods += " 5K"
                            if int(r['enabled_mods']) & 0b100000000000000000:
                                mods += " 6K"
                            if int(r['enabled_mods']) & 0b1000000000000000000:
                                mods += " 7K"
                            if int(r['enabled_mods']) & 0b10000000000000000000:
                                mods += " 8K"
                            if int(r['enabled_mods']) & 0b100000000000000000000:
                                mods += " FadeIn"
                            if int(r['enabled_mods']) & 0b1000000000000000000000:
                                mods += " Random"
                            if int(r['enabled_mods']) & 0b1000000000000000000000000:
                                mods += " 9K"
                            if int(r['enabled_mods']) & 0b10000000000000000000000000:
                                mods += " 10K"
                            if int(r['enabled_mods']) & 0b100000000000000000000000000:
                                mods += " 1K"
                            if int(r['enabled_mods']) & 0b1000000000000000000000000000:
                                mods += " 3K"
                            if int(r['enabled_mods']) & 0b10000000000000000000000000000:
                                mods += " 2K"
                            mods += '\n'
                        else:
                            mods = '\n'
                        telegram.sendmessage("*Osu!*\n"
                                             "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                                 'beatmap_id'] +
                                             ")\n*" + r['rank'] + "*\n" + mods +
                                             "\n*Punti*: " + r['score'] + "\n"
                                             "*Combo* x" + r['maxcombo'] + "\n"
                                             "*300*: " + r['count300'] + "\n"
                                             "*100*: " + r['count100'] + "\n"
                                             "*50*: " + r['count50'] + "\n"
                                             "*Awesome*: " + r['countkatu'] + "\n"
                                             "*Good*: " + r['countgeki'] + "\n"
                                             "*Miss*: " + r['countmiss'], sentin, source)
            elif text.startswith('/roll'):
                print("@" + username + ": /roll")
                cmd = text.split(' ', 1)
                if len(cmd) >= 2:
                    try:
                        m = int(cmd[1])
                    except ValueError:
                        telegram.sendmessage(chr(9888) + " Il numero specificato non è un intero.", sentin, source)
                else:
                    m = 100
                try:
                    n = random.randrange(m) + 1
                except ValueError:
                    telegram.sendmessage(chr(9888) + " Il numero specificato non è maggiore o uguale a 0.", sentin, source)
                else:
                    telegram.sendmessage("Numero casuale da 1 a " + str(m) + ":\n*" + str(n) + "*", sentin, source)
            elif text.startswith('/automah'):
                print("@" + username + ": /automah")
                # TODO: Mettere l'audio di Tobia
                telegram.sendmessage("Automaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa! Devi funzionare, cavolo!", sentin,
                                     source)
            elif text.startswith('/hs'):
                print("@" + username + ": /hs")
                # Informa Telegram che il messaggio è stato ricevuto.
                telegram.sendchataction(sentin)
                cmd = text.split(" ", 1)
                r = None
                if len(cmd) >= 2:
                    try:
                        r = hearthstone.card(cmd[1])
                        # Se ci sono più carte, prendine una a caso!
                        r = r[random.randrange(len(r))]
                    except ValueError:
                        telegram.sendmessage(chr(9888) + " La carta specificata non esiste!", sentin, source)
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
                                       "*Eroe*\n" +
                                       str(r['health']) + " salute\n")
                        telegram.sendmessage(text, sentin, source)
                else:
                    telegram.sendmessage(chr(9888) + " Non hai specificato nessuna carta!\n"
                                         "La sintassi corretta è _/hs nomecarta_ .", sentin, source)
            elif text.startswith('/online'):
                # Elenco di tutte le persone online su Steam
                print("@" + username + ": /online ")
                # Informa Telegram che il messaggio è stato ricevuto.
                telegram.sendchataction(sentin)
                cmd = text.split(" ")
                if len(cmd) >= 2:
                    if cmd[1].lower() == "help":
                        telegram.sendmessage(chr(128309) + " Online\n" +
                                             chr(128308) + " In gioco | Occupato\n" +
                                             chr(9899) + " Assente | Inattivo\n" +
                                             chr(128310) + " Disponibile per scambiare\n" +
                                             chr(128311) + " Disponibile per giocare", sentin, source)
                else:
                    # Stringa utilizzata per ottenere informazioni su tutti gli utenti in una sola richiesta a steam
                    userids = str()
                    for nome in steamids:
                        userids += str(steamids[nome]) + ','
                    tosend = "*Online ora:*\n"
                    r = steam.getplayersummaries(userids)
                    for player in r:
                        # In gioco
                        if 'gameextrainfo' in player:
                            tosend += chr(128308) + " _" + player['gameextrainfo'] + "_ |"
                        elif 'gameid' in player:
                            tosend += chr(128308) + " _" + player['gameid'] + "_ |"
                        # Online
                        elif player['personastate'] == 1:
                            tosend += chr(128309)
                        # Occupato
                        elif player['personastate'] == 2:
                            tosend += chr(128308)
                        # Assente o Inattivo
                        elif player['personastate'] == 3 or player['personastate'] == 4:
                            tosend += chr(9899)
                        # Disponibile per scambiare
                        elif player['personastate'] == 5:
                            tosend += chr(128310)
                        # Disponibile per giocare
                        elif player['personastate'] == 6:
                            tosend += chr(128311)
                        if player['personastate'] != 0:
                            tosend += " " + player['personaname'] + "\n"
                    else:
                        telegram.sendmessage(tosend, sentin, source)
            elif text.startswith('/shrekt'):
                print("@" + username + ": /shrekt ")
                telegram.senddocument("BQADBAADsQADiBjiAqYN-EBXASyhAg", sentin)
            elif text.startswith('/restart') and username == "Steffo":
                print("@" + username + ": /restart ")
                telegram.sendmessage("Riavvio accettato.", sentin, source)
                sys.exit(0)
            elif text.startswith('/nuovavotazione') and username == "Steffo":
                print("@" + username + ": /nuovavotazione ")
                cmd = text.split(" ", 1)
                incorso = Votazione(cmd[1], sentin)
            elif text.startswith('/si') and incorso is not None:
                if incorso.chat == sentin:
                    print("@" + username + ": /si ")
                    incorso.register(username.lower(), 1)
                    telegram.sendmessage("Votazione registrata!", sentin, source)
            elif text.startswith('/no') and incorso is not None:
                if incorso.chat == sentin:
                    print("@" + username + ": /no ")
                    incorso.register(username.lower(), 2)
                    telegram.sendmessage("Votazione registrata!", sentin, source)
            elif text.startswith('/astieniti') and incorso is not None:
                if incorso.chat == sentin:
                    print("@" + username + ": /astieniti ")
                    incorso.register(username.lower(), 3)
                    telegram.sendmessage("Votazione registrata!", sentin, source)
            elif text.startswith('/domanda') and incorso is not None:
                if incorso.chat == sentin:
                    print("@" + username + ": /domanda ")
                    incorso.ask()
            elif text.startswith('/risultati') and incorso is not None:
                if incorso.chat == sentin:
                    print("@" + username + ": /risultati ")
                    incorso.showresults()
            elif text.startswith('/cv'):
                print("@" + username + ": /cv ")
                # Informa Telegram che il messaggio è stato ricevuto.
                telegram.sendchataction(sentin)
                r = mumbleboxes.getserverstatus("https://www.mumbleboxes.com/servers/5454/cvp.json").json()
                tosend = "Utenti online: " + str(len(r['root']['users'])) + " / 15\n"
                for u in r['root']['users']:
                    if not u['mute']:
                        if u['selfDeaf']:
                            tosend += chr(128263) + " "
                        elif u['selfMute']:
                            tosend += chr(128264) + " "
                        else:
                            tosend += chr(128266) + " "
                        tosend += u['name'] + "\n"
                telegram.sendmessage(tosend, sentin, source)
            elif text.startswith('/diario'):
                print("@" + username + ": /diario ")
                cmd = text.split(" ", 1)
                d = filemanager.readfile("diario.txt")
                d += str(time.time()) + " | " + cmd[1] + "\n"
                filemanager.writefile("diario.txt", d)
                telegram.sendmessage("Aggiunto al diario RYG.", sentin, source)
        else:
            print("@" + username + " bloccato.")



