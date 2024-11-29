import os

from config import *
from JSONModificator import JSONModificator
from logger import logger




if __name__ == "__main__":
	# Initialisation
	os.makedirs("Logs", exist_ok=True)
	mergedJSON = JSONModificator()
	
	# Merging data from defined locations
	mergedJSON.processJSON(URL_MAIN_LOCALISATION_KEY)
	for modul in MODULS:
		mergedJSON.processJSON(f"{URL_MODUL_LOCALISATION_KEY}{modul}/locale/en.json", modul)
	mergedJSON.printSuccessRate()
	try:
		mergedJSON.saveToFile()
	except Exception:
		exit(1)