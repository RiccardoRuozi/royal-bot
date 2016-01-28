import requests


def getserverstatus(url):
    r = requests.get(url)
    return r
