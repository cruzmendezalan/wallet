import requests
import json

class pJson(object):
	"""Clase para manipular strings json con el fin de formatearlos o volverlos objetos """
	def __init__(self):
		super(pJson, self).__init__()

	def prettyPrint(self, texto):
		parsed = json.loads(texto)
		print(json.dumps(parsed, indent = 4, sort_keys = True))


class Bitso(object):
	""" Esta clase consume de la api publica de bitso """
	def __init__(self):
		super(Bitso, self).__init__()
		self.pJson = pJson()

	def availableBooks(self):
		r = requests.get("https://api.bitso.com/v3/available_books/")
		r.json()
		self.pJson.prettyPrint(r.content)
		

def main():
	b = Bitso()
	b.availableBooks()

if __name__ == "__main__":
    # execute only if run as a script
    main()