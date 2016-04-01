# -*- coding: utf-8 -*-
import telegram


class Player:
    telegramid = int()
    username = str()
    role = int()
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
        telegram.sendmessage(text, self.telegramid)

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

    def addplayer(self, player):
        """Aggiungi un giocatore alla partita
        :param player: Oggetto del giocatore da aggiungere
        """
        self.players.append(player)
