# -*- coding: utf-8 -*-
import telegram
import configparser
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


partiteincorso = list()


class Game:
    groupid = int()
    adminid = int()
    players = list()
    tokill = list()
    joinphase = True

    def __del__(self):
        print("Partita {0} eliminata.\n".format(self.groupid))

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
                telegram.sendmessage("\U0001F608: " + text, player.telegramid)
        telegram.sendmessage("\U0001F608: " + text, self.adminid)

    def status(self) -> str:
        """Restituisci lo stato attuale della partita in una stringa"""
        tosend = "Stato attuale del gioco: \n"
        for player in self.players:
            if not player.alive:
                tosend += "\U0001F480 "
            else:
                tosend += "\U0001F636 "
            tosend += player.username + "\n"
        return tosend

    def mifiastatus(self) -> str:
        """Restituisci lo stato attuale della partita (per mifiosi) in una stringa"""
        tosend = "Stato attuale del gioco: \n"
        for player in self.players:
            if not player.alive:
                tosend += "\U0001F480 "
            elif player.role == 1:
                tosend += "\U0001F608 "
            else:
                tosend += "\U0001F610 "
            tosend += player.username + "\n"
        return tosend

    def fullstatus(self) -> str:
        """Restituisci lo stato attuale della partita (per admin?) in una stringa"""
        tosend = str(self.groupid) + "\n"
        for player in self.players:
            if not player.alive:
                tosend += "\U0001F480 "
            elif player.role == 1:
                tosend += "\U0001F608 "
            elif player.role == 2:
                tosend += "\U0001F575 "
            else:
                tosend += "\U0001F610 "
            tosend += player.username + "\n"
        return tosend

    def findusername(self, fusername) -> Player:
        """Trova un giocatore con un certo nome utente
        :param fusername: Nome utente da cercare
        """
        for player in self.players:
            if player.username == fusername.capitalize():
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
            if player.votedfor != str() and player.alive:
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
        if mostvoted is not None:
            return self.findusername(mostvoted)
        else:
            return None

    def endday(self):
        votedout = self.mostvoted()
        self.message(votedout.username + " è il più votato del giorno e sarà ucciso.")
        self.tokill.append(votedout)
        for killed in self.tokill:
            self.message(killed.username + " è stato ucciso.\n")
            if killed.role == 0:
                self.message("Era un \U0001F610 Royal.")
            elif killed.role == 1:
                self.message("Era un \U0001F608 Mifioso!")
            elif killed.role == 2:
                self.message("Era un \U0001F575 Detective!")
            killed.alive = False
        for player in self.players:
            player.votedfor = str()
            if player.role != 0:
                player.special = True
        self.message(self.displaycount())
        # Controlla se la Royal Games ha vinto
        zero = 0
        uno = 0
        for player in self.players:
            if player.alive:
                if player.role == 0 or player.role == 2:
                    zero += 1
                elif player.role == 1:
                    uno += 1
        if uno == 0:
            self.message("*Il Team Royal ha vinto!*\n"
                         "Tutti i Mifiosi sono stati eliminati.")
            partiteincorso.remove(findgame(self.groupid))
        if uno >= zero:
            self.message("*Il Team Mifia ha vinto!*\n"
                         "I Mifiosi rimasti sono più dei Royal.")
        self.tokill = list()

    def displaycount(self) -> str:
        zero = 0
        uno = 0
        for player in self.players:
            if player.alive:
                if player.role == 0 or player.role == 2:
                    zero += 1
                elif player.role == 1:
                    uno += 1
        msg = "*Royal*: {0} persone rimaste\n" \
              "*Mifia*: {1} persone rimaste".format(str(zero), str(uno))
        return msg

    def save(self):
        status = configparser.ConfigParser()
        status['General'] = {
            "groupid": self.groupid,
            "adminid": self.adminid,
        }
        for player in self.players:
            status[player.username] = {
                "telegramid": player.telegramid,
                "role": player.role,
                "alive": player.alive,
            }
        try:
            f = open(str(self.groupid) + ".ini", "w")
        except OSError:
            open(str(self.groupid) + ".ini", "x")
            f = open(str(self.groupid) + ".ini", "w")
        status.write(f)

    def endjoin(self):
        self.message("La fase di join è finita.")
        self.joinphase = False


def findgame(chatid) -> Game:
    for game in partiteincorso:
        if game.groupid == chatid:
            return game
    else:
        return None


def loadgame(chatid) -> Game:
    l = Game()
    loaded = configparser.ConfigParser()
    loaded.read(str(chatid) + ".ini")
    # General non è un giocatore, quindi toglilo
    playerlist = loaded.sections()
    playerlist.remove("General")
    for player in playerlist:
        lp = Player()
        lp.alive = bool(loaded[player]['alive'])
        lp.username = player
        lp.role = int(loaded[player]['role'])
        lp.telegramid = int(loaded[player]['telegramid'])
        l.players.append(lp)
    l.groupid = int(loaded['General']['groupid'])
    l.adminid = int(loaded['General']['adminid'])
    return l


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
            elif t['text'].startswith("/loadgame"):
                g = loadgame(t['chat']['id'])
                partiteincorso.append(g)
                g.message("Partita caricata!\n_Forse._")
            elif t['text'].startswith("/status"):
                telegram.sendmessage("Nessuna partita in corso in questo gruppo.", t['chat']['id'], t['message_id'])
            else:
                xtra = t['text'].split(' ', 2)
                try:
                    g = findgame(int(xtra[0]))
                except ValueError:
                    g = None
                if g is not None:
                    if xtra[1].capitalize() == "special":
                        if g.findid(t['from']['id']).role == 1 and g.findid(t['from']['id']).special:
                            target = g.findusername(xtra[2])
                            if target is not None:
                                g.tokill.append(target)
                                g.findid(t['from']['id']).special = False
                                g.evilmessage("Il bersaglio di " + t['from']['username'] + " è *" + target.username +
                                              "*.")
                        elif g.findid(t['from']['id']).role == 2 and g.findid(t['from']['id']).special:
                            target = g.findusername(xtra[2])
                            p = g.findid(t['from']['id'])
                            if target is not None:
                                if target.role == 0:
                                    p.message(target.username + " è un \U0001F610 Royal.")
                                elif target.role == 1:
                                    p.message(target.username + " è un \U0001F608 Mifioso.")
                                elif target.role == 2:
                                    p.message(target.username + " è un \U0001F575 Detective.")
                                p.special = False
                    elif xtra[1].capitalize() == "chat":
                        if g.findid(t['from']['id']).role == 1:
                            g.evilmessage(xtra[2])
        else:
            if t['text'].startswith("/join"):
                if g.joinphase and g.findid(t['from']['id']) is None:
                    p = Player()
                    p.telegramid = t['from']['id']
                    # Qui crasha se non è stato impostato un username. Fare qualcosa?
                    p.username = t['from']['username'].capitalize()
                    # Assegnazione dei ruoli
                    r = random.randrange(0, 100)
                    # Spiegare meglio cosa deve fare ogni ruolo?
                    if r < 15:
                        p.role = 1
                        p.special = True
                        p.message("Sei stato assegnato alla squadra \U0001F608 *MIFIA*."
                                  "Apparirai agli altri come un membro del team ROYAL.\n"
                                  "Depistali e non farti uccidere!\n"
                                  "Il team ROYAL ucciderà la persona più votata di ogni turno.\n"
                                  "Per votare, scrivi `/vote username`!\n"
                                  "Scrivi in questa chat `{0} CHAT messaggio` per mandare un"
                                  " messaggio segreto al tuo team.\n"
                                  "Scrivi in questa chat `{0} SPECIAL username` per uccidere"
                                  " qualcuno alla fine del giorno.\n"
                                  "La squadra Mifia vince se tutta la Royal Games è eliminata.\n"
                                  "Perdi se vieni ucciso."
                                  .format(g.groupid))
                    elif r > 85:
                        p.role = 2
                        p.special = True
                        p.message("Sei stato assegnato alla squadra *ROYAL* con il ruolo di \U0001F575 *DETECTIVE*.\n"
                                  "Apparirai agli altri come un membro del team ROYAL.\n"
                                  "Non attirare l'attenzione dei Mifiosi su di te!\n"
                                  "Il team ROYAL ucciderà la persona più votata di ogni turno.\n"
                                  "Per votare, scrivi `/vote username`!\n"
                                  "Tra di voi si nascondono dei Mifiosi.\n"
                                  "Stanateli e uccideteli votando per le persone giuste!\n"
                                  "La squadra Royal vince se tutti i Mifiosi sono morti.\n"
                                  "La squadra Royal perde se sono vivi solo Mifiosi.\n"
                                  "Scrivi in questa chat `{0} SPECIAL nomeutente` per usare il tuo "
                                  " potere di detective e indagare sul ruolo di qualcuno per un giorno."
                                  .format(g.groupid))
                    else:
                        p.role = 0
                        p.special = True
                        p.message("Sei stato assegnato alla squadra \U0001F610 *ROYAL*.\n"
                                  "Il team ROYAL ucciderà la persona più votata di ogni turno.\n"
                                  "Per votare, scrivi `/vote username`!\n"
                                  "Tra di voi si nascondono dei Mifiosi.\n"
                                  "Stanateli e uccideteli votando per le persone giuste!\n"
                                  "La squadra Royal vince se tutti i Mifiosi sono morti.\n"
                                  "La squadra Royal perde se sono vivi solo Mifiosi.")
                    g.addplayer(p)
                    g.message(p.username + " si è unito alla partita!")
                    g.adminmessage(g.fullstatus())
                    g.save()
                else:
                    g.message("\u26A0\uFE0F Non puoi unirti alla partita.\n"
                              "La fase di unione è terminata o ti sei già unito in precedenza.")
            elif t['text'].startswith("/status"):
                if not g.joinphase:
                    g.message(g.status() + "\n" + g.displaycount())
                else:
                    g.message(g.status())
                p = g.findid(t['from']['id'])
                if p is not None and p.role == 1:
                    p.message(g.mifiastatus())
            elif t['text'].startswith("/fullstatus"):
                if t['from']['id'] == g.adminid:
                    g.adminmessage(g.fullstatus() + "\n" + g.displaycount())
                else:
                    g.message("\u26A0\uFE0F Non sei il creatore della partita; non puoi vedere lo status completo.")
            elif t['text'].startswith("/save"):
                if t['from']['id'] == g.adminid:
                    g.save()
                    g.message("Partita salvata!\n_Funzione instabile, speriamo che non succedano casini..._")
                else:
                    g.message("\u26A0\uFE0F Non sei il creatore della partita; non puoi salvare la partita.")
            elif t['text'].startswith("/endday"):
                if t['from']['id'] == g.adminid:
                    g.endday()
                else:
                    g.message("\u26A0\uFE0F Non sei il creatore della partita; non puoi finire il giorno.")
            elif t['text'].startswith("/vote"):
                if not g.joinphase:
                    username = t['text'].split(' ')
                    if len(username) > 1 and g.findusername(username[1]) is not None:
                        voter = g.findid(t['from']['id'])
                        if voter.alive:
                            voter.votedfor = username[1]
                            g.message("Hai votato per " + username[1] + ".")
                        else:
                            g.message("_La tua votazione riecheggia nel nulla._\n"
                                      "\u26A0\uFE0F Sei morto, e i morti non votano.")
                    else:
                        g.message("\u26A0\uFE0F La persona selezionata non esiste.")
                else:
                    g.message("\u26A0\uFE0F La partita non è ancora iniziata; non puoi votare.")
            elif t['text'].startswith("/endjoin"):
                g.endjoin()
