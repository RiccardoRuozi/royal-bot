import filemanager
import requests

# Per far funzionare questa libreria serve un file "hearthstoneapi.txt" con l'API key ricevuta da mashape.com
apikey = filemanager.readfile('hearthstoneapi.txt')


def card(name):
    headers = {
        'X-Mashape-Key': apikey
    }
    parametri = {
        'locale': 'itIT'
    }
    # TODO: Controllare che questo non sia exploitabile per un XSS o roba del genere. Anche se dubito.
    r = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/" + name,
                     params=parametri, headers=headers)
    if r.status_code != 404:
        return r.json()
    else:
        parametri = {
            'locale': 'enUS'
        }
        r = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/search/" + name,
                         params=parametri, headers=headers)
        if r.status_code != 404:
            return r.json()
        else:
            raise ValueError("La carta non esiste!")
