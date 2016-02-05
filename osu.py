# -*- coding: utf-8 -*-
import requests
import filemanager

# Importa la API key dal file.
apikey = filemanager.readfile("osuapi.txt")


def getbeatmap(num):
    """Ottieni informazioni su una beatmap.
    :param num: ID della beatmap
    """
    parametri = {
        'k': apikey,
        'b': num,
    }
    r = requests.get("https://osu.ppy.sh/api/get_beatmaps", params=parametri).json()
    if len(r) >= 1:
        return r[0]
    else:
        raise NameError


def getuser(user, mode=0):
    """Ottieni informazioni su un utente.
    :param user: Username o ID dell'utente
    :param mode: Modalita' (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania)
    """
    parametri = {
        'k': apikey,
        'u': user,
        'm': mode
    }
    r = requests.get("https://osu.ppy.sh/api/get_user", params=parametri).json()
    if len(r) >= 1:
        return r[0]
    else:
        raise NameError


def getscores(beatmap, mode=0, limit=100, user=None):
    """Ottieni i migliori 100 punteggi di una beatmap O il punteggio dell'utente specificato
    :param beatmap: ID della beatmap
    :param mode: Modalità (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania)
    :param limit: Numero di punteggi da ottenere (max 100)
    :param user: Utente di cui ottenere i punteggi
    """
    parametri = {
        'k': apikey,
        'b': beatmap,
        'u': user,
        'm': mode,
        'limit': limit,
    }
    r = requests.get("https://osu.ppy.sh/api/get_scores", params=parametri).json()
    return r


def getuserbest(user, mode=0):
    """Ottieni i record di un utente. Immagino siano i punteggi con più pp?
    :param user: Username o ID dell'utente
    :param mode: Modalità (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania)
    """
    parametri = {
        'k': apikey,
        'u': user,
        'm': mode,
    }
    r = requests.get("https://osu.ppy.sh/api/get_user_best", params=parametri).json()
    return r


def getuserrecent(user, mode=0):
    """Ottieni il punteggio dell'ultima canzone giocata da un utente.
    :param user: Username o ID dell'utente
    :param mode: Modalità (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania)
    """
    parametri = {
        'k': apikey,
        'u': user,
        'm': mode,
        'limit': 1,
    }
    r = requests.get("https://osu.ppy.sh/api/get_user_recent", params=parametri).json()
    if len(r) >= 1:
        return r[0]
    else:
        raise NameError

def listmods(n):
    """
    Trasforma il valore restituito dall'API di osu! di enabled_mods in una stringa contenente l'elenco corrispondente a
    parole.
    :param n: Valore da trasformare in stringa
    """
    mods = "*Mod:*"
    # Dividi in bit l'ID delle mod selezionate usando un bitwise and
    # Forse si potrebbe rifare usando la forma esadecimale...?
    if int(n) & 0x1:
        mods += " NoFail"
    if int(n) & 0x2:
        mods += " Easy"
    if int(n) & 0x4:
        mods += " NoVideo (?)"
    if int(n) & 0x8:
        mods += " Hidden"
    if int(n) & 0x10:
        mods += " HardRock"
    if int(n) & 0x20:
        mods += " SuddenDeath"
    if int(n) & 0x40:
        mods += " DoubleTime"
    if int(n) & 0x80:
        mods += " Relax"
    if int(n) & 0x100:
        mods += " HalfTime"
    if int(n) & 0x200:
        mods += " Nightcore"
    if int(n) & 0x400:
        mods += " Flashlight"
    if int(n) & 0x800:
        mods += " Autoplay"
    if int(n) & 0x1000:
        mods += " SpunOut"
    if int(n) & 0x2000:
        mods += " Autopilot"
    if int(n) & 0x4000:
        mods += " Perfect"
    if int(n) & 0x8000:
        mods += " 4K"
    if int(n) & 0x10000:
        mods += " 5K"
    if int(n) & 0x20000:
        mods += " 6K"
    if int(n) & 0x40000:
        mods += " 7K"
    if int(n) & 0x80000:
        mods += " 8K"
    if int(n) & 0x100000:
        mods += " FadeIn"
    if int(n) & 0x200000:
        mods += " Random"
    if int(n) & 0x400000:
        mods += " 9K"
    if int(n) & 0x800000:
        mods += " 10K"
    if int(n) & 0x1000000:
        mods += " 1K"
    if int(n) & 0x2000000:
        mods += " 3K"
    if int(n) & 0x4000000:
        mods += " 2K"
    return mods
