# -*- coding: utf-8 -*-

def readFile(name):
	"""Leggi i contenuti di un file."""
	file = open(name, 'r')
	content = file.read()
	file.close()
	return content
	
def writeFile(name, content):
	"""Scrivi qualcosa su un file, sovrascrivendo qualsiasi cosa ci sia al suo interno."""
	file = open(name, 'w')
	file.write(content)
	file.close()