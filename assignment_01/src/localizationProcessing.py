import os

from config import *
from JSONModificator import JSONModificator
from logger import logger




if __name__ == "__main__":
	# Initialization
	os.makedirs("Logs", exist_ok=True)
	logger.info("Running script...")
	mergedJSON = JSONModificator()
	
	# Merging data from defined locations
	mergedJSON.processJSON(URL_MAIN_LOCALISATION_KEY)
	for modul in MODULS:
		mergedJSON.processJSON(f"{URL_MODUL_LOCALISATION_KEY}{modul}/locale/en.json", modul)
	mergedJSON.printSuccessRate()
	try:
		mergedJSON.saveToFile()
	except Exception:
		# In case writing to file is permitted, terminate with exit code 1
		exit(1)