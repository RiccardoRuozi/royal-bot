import filemanager
import requests

# No, non ci sto nemmeno più provando a scrivere decentemente il bot. E' una schifezza e andrebbe rifatto da capo.
def getwidgetdata(token):
    r = requests.get("https://discordapp.com/api/servers/{0}/widget.json".format(token))
    if r.status_code == 200:
        return r.json()
    else:
        # Sì, dovrei fare una DiscordException
        raise Exception("Qualcosa di discord non va")

def getchannelname(r, id):
    for channel in r['channels']:
        if id == channel['id']:
            return channel['name']
