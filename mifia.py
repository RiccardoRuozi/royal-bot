# -*- coding: utf-8 -*-
import telegram


class Player:
    telegramid = int()
    username = str()
    role = 0 # 0 = normale, 1 = mifia
    alive = True

    def message(self, text):
        """Manda un messaggio al giocatore
        :param text: Testo del messaggio
        """
        telegram.sendmessage(text, self.telegramid)

    def kill(self):
        """Uccidi il giocatore"""
        self.alive = False


class Game:
    chat = int()
    players = list()

    def message(self, text):
        """Manda un messaggio alla chat generale del gioco
        :param text: Testo del messaggio
        """
        telegram.sendmessage(text, self.chat)

    def mifiamessage(self, text):
        """Manda un messaggio alla chat generale del gioco
        :param text: Testo del messaggio
        """
        for player in self.players:
            if player.role == 1:
                telegram.sendmessage(text, player.telegramid)

    def displaystatus(self):
        """Visualizza lo stato attuale della partita"""
        tosend = "Stato attuale del gioco: \n"
        for player in self.players:
            if not player.alive:
                tosend += "\U0001F480 "
            else:
                tosend += "\U0001F636 "
            tosend += player.username + "\n"
        self.message(tosend)

    def displayfullstatus(self):
        """Visualizza lo stato attuale della partita (per admin?)"""
        tosend = "Stato attuale del gioco: \n"
        for player in self.players:
            if not player.alive:
                tosend += "_Morto_ "
            elif player.role == 1:
                tosend += "_Mifia_ "
            else:
                tosend += "_Civile_ "
            tosend += player.username + "\n"
        self.message(tosend)

    def addplayer(self, player):
        """Aggiungi un giocatore alla partita
        :param player: Oggetto del giocatore da aggiungere
        """
        self.players.append(player)
