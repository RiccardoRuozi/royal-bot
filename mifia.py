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
