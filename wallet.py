import requests
import json
import urllib

class pJson(object):
	"""Clase para manipular strings json con el fin de formatearlos o volverlos objetos """
	def __init__(self):
		super(pJson, self).__init__()

	def prettyPrint(self, texto):
		parsed = json.loads(texto)
		print(json.dumps(parsed, indent = 4, sort_keys = True))


class Bitso(object):
	""" Esta clase consume de la api publica de bitso
		El constructor recibe una varibale boleana, la cual hace un switch
		para cambiar entre modo desarrollo y modo developer
	"""
	def __init__(self, production = False):
		super(Bitso, self).__init__()
		self.pJson 		= pJson()
		self.production = production

	def availableBooks(self):
		r = requests.get(self.getBaseUrl()+"available_books/")
		r.json()
		self.pJson.prettyPrint(r.content)

	def ticker(self, book):
		data 	= {'book' : book}
		r 		= requests.get(self.getBaseUrl()+"ticker/", params = data)
		r.json()
		self.pJson.prettyPrint(r.content)

	def orderBook(self, book):
		data = {'book':book}
		r = requests.get(self.getBaseUrl()+"order_book/", params = data)
		r.json()
		self.pJson.prettyPrint(r.content)

	def trades(self, book):
		data = {'book':book}
		r = requests.get(self.getBaseUrl()+"trades/",params = data)
		r.json()
		self.pJson.prettyPrint(r.content)

	def getBaseUrl(self):
		if self.production == True:
			return "https://api.bitso.com/v3/"
		return "https://api-dev.bitso.com/v3/"
		

def main():
	b = Bitso()
	#b.availableBooks()
	#b.ticker("xrp_mxn")
	#b.orderBook("xrp_mxn")
	b.trades("xrp_mxn")

if __name__ == "__main__":
    # execute only if run as a script
    main()