# -*- coding: utf-8 -*-
import telegram
import pickle
import random

class Player:
    telegramid = int()
    username = str()
    role = 0  # 0 normale | 1 rryg | 2 resistenza
    alive = True
    votedfor = str()
    special = False

    def message(self, text):
        """Manda un messaggio al giocatore
        :param text: Testo del messaggio
        """
        telegram.sendmessage(text, self.telegramid)


class Game:
    groupid = int()
    adminid = int()
    players = list()
    tokill = list()
    joinphase = True

    def message(self, text):
        """Manda un messaggio alla chat generale del gioco
        :param text: Testo del messaggio
        """
        telegram.sendmessage(text, self.groupid)

    def adminmessage(self, text):
        """Manda un messaggio all'admin del gioco
        :param text: Testo del messaggio
        """
        telegram.sendmessage(text, self.adminid)

    def evilmessage(self, text):
        """Manda un messaggio al team dei nemici del gioco
        :param text: Testo del messaggio
        """
        for player in self.players:
            if player.role == 1:
                telegram.sendmessage(text, player.telegramid)

    def status(self) -> str:
        """Restituisci lo stato attuale della partita in una stringa unicode"""
        tosend = "Stato attuale del gioco: \n"
        for player in self.players:
            if not player.alive:
                tosend += "\U0001F480 "
            else:
                tosend += "\U0001F636 "
            tosend += player.username + "\n"
        return tosend

    def fullstatus(self) -> str:
        """Restituisci lo stato attuale della partita (per admin?) in una stringa unicode"""
        tosend = "Stato attuale del gioco: \n"
        for player in self.players:
            if not player.alive:
                tosend += "\U0001F480 "
            elif player.role == 1:
                tosend += "\U0001F608 "
            elif player.role == 2:
                tosend += "Detective "
            else:
                tosend += "\U0001F636 "
            tosend += player.username + "\n"
        return tosend

    def findusername(self, username) -> Player:
        """Trova un giocatore con un certo nome utente
        :param username: Nome utente da cercare
        """
        for player in self.players:
            if player.username == username:
                return player
        else:
            return None

    def findid(self, telegramid) -> Player:
        """Trova un giocatore con un certo ID di telegram
        :param telegramid: ID da cercare
        """
        for player in self.players:
            if player.telegramid == telegramid:
                return player
        else:
            return None

    def addplayer(self, player):
        """Aggiungi un giocatore alla partita
        :param player: Oggetto del giocatore da aggiungere
        """
        self.players.append(player)

    def mostvoted(self) -> Player:
        """Trova il giocatore più votato"""
        votelist = dict()
        for player in self.players:
            if player.votedfor != str():
                if player.votedfor not in votelist:
                    votelist[player.votedfor] = 1
                else:
                    votelist[player.votedfor] += 1
        mostvoted = str()
        mostvotes = int()
        for player in votelist:
            if mostvoted == str():
                mostvoted = player
                mostvotes = votelist[player]
            else:
                if votelist[player] > mostvotes:
                    mostvoted = player
                    mostvotes = votelist[player]
        return self.findusername(mostvoted)

    # def save(self):
    #    """Salva in un file di testo con il numero del gruppo lo stato attuale del gioco"""
    #    file = open(str(self.groupid) + ".txt", "x")
    #    pickle.dump(self, file)

    def endday(self):
        self.message(self.mostvoted().username + " è stato il più votato del giorno.")
        self.tokill.append(self.mostvoted())
        for killed in self.tokill:
            self.message(killed.username + " è stato ucciso.")
            killed.alive = False
        for player in self.players:
            player.votedfor = str()
            if player.role != 0:
                player.special = True


def load(filename) -> Game:
    """Restituisci da un file di testo con il numero del gruppo lo stato del gioco (Funzione non sicura, non importare
    file a caso pls)
    :param filename: Nome del file da cui caricare lo stato"""
    try:
        file = open(str(filename) + ".txt", "r")
    except OSError:
        return None
    else:
        return pickle.load(file)


partiteincorso = list()


def findgame(chatid) -> Game:
    for game in partiteincorso:
        if game.groupid == chatid:
            return game
    else:
        return None


while True:
    t = telegram.getupdates()
    if 'text' in t:
        g = findgame(t['chat']['id'])
        if g is None:
            if t['text'].startswith("/newgame"):
                g = Game()
                g.groupid = t['chat']['id']
                g.adminid = t['from']['id']
                partiteincorso.append(g)
                g.message("Partita creata!")
            # elif t['text'].startswith("/load"):
            #     g = load(t['chat']['id'])
            elif t['text'].startswith("/status"):
                telegram.sendmessage("Nessuna partita in corso.", t['chat']['id'], t['message_id'])
            else:
                xtra = t['text'].split(' ')
                try:
                    g = findgame(int(xtra[0]))
                except ValueError:
                    g = None
                if g is not None:
                    if xtra[1] == "SPECIAL":
                        if g.findid(t['from']['id']).role == 1 and g.findid(t['from']['id']).special:
                            target = g.findusername(xtra[2])
                            if target is not None:
                                g.tokill.append(target)
                                g.findid(t['from']['id']).special = False
                                g.evilmessage("Il bersaglio di " + t['from']['username'] + " è " + target.username +
                                              ".")
        else:
            if t['text'].startswith("/join"):
                if g.joinphase:
                    p = Player()
                    p.telegramid = t['from']['id']
                    # Qui crasha se non è stato impostato un username. Fare qualcosa?
                    p.username = t['from']['username']
                    # Assegnazione dei ruoli
                    # Spiegare meglio cosa deve fare ogni ruolo?
                    balanced = random.randrange(0, 100, 1)
                    if balanced <= 100:
                        p.role = 1
                        p.special = True
                        p.message("Sei stato assegnato alla squadra *MIFIA*.")
                        p.message("L'ID della partita è " + str(g.groupid) + ".\n"
                                  "Non dimenticarlo. ")
                    elif balanced >= 95:
                        p.role = 2
                        p.special = True
                        p.message("Sei stato assegnato alla squadra *ROYAL*.")
                        p.message("Hai il ruolo speciale di detective.")
                    else:
                        p.role = 0
                        p.message("Sei stato assegnato alla squadra *ROYAL*.")
                    g.addplayer(p)
                    g.message(p.username + " si è unito alla partita!")
                else:
                    g.message("La fase di iscrizione è terminata.")
            # elif t['text'].startswith("/save"):
            #     g.save()
            elif t['text'].startswith("/status"):
                if t['from']['id'] == g.adminid:
                    g.adminmessage(g.fullstatus())
                else:
                    g.message(g.status())
            elif t['text'].startswith("/endjoin"):
                if t['from']['id'] == g.adminid:
                    g.message("Fase di iscrizione chiusa.")
                    g.message(g.status())
            elif t['text'].startswith("/endday"):
                if t['from']['id'] == g.adminid:
                    g.endday()
                    g.message(g.status())
            elif t['text'].startswith("/vote"):
                username = t['text'].split(' ')
                if g.findusername(username[1]) is not None:
                    voter = g.findid(t['from']['id'])
                    voter.votedfor = username[1]
                    g.message("Hai votato per " + username[1] + ".")
                else:
                    g.message("La persona selezionata non esiste.")