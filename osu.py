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
    return r[0]


def getuser(user, mode=0):
    """Ottieni informazioni su un utente.
    :param user: Username o ID dell'utente
    :param mode: Modalità (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania)
    """
    parametri = {
        'k': apikey,
        'u': user,
        'm': mode
    }
    r = requests.get("https://osu.ppy.sh/api/get_user", params=parametri).json()
    return r[0]


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
    return r[0]
