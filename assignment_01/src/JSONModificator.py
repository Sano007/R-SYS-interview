import json
import requests
import os

from config import *
from logger import logger


class JSONModificator:
	"""
	Class designed to fetch, process, and store JSON data from given URLs 
	"""

	_completeJSON: dict
	_successRate: dict

	def __init__(self) -> None:
		self._completeJSON = {}
		self._successRate = {"Success": 0, "Fail": 0}

	def processJSON(self, url: str, modul: str = "main") -> None:
		"""
		Fetches JSON data from a given URL and stores it in self under **modul name**.

		:param `url`: The URL to fetch JSON data from.
		:param `modul`: The module name under which to store the fetched `JSON`. Defaults to `"main"`.
		"""
		try:
			result = requests.get(url)
			if(result.ok):
				logger.info(f"Request's result for modul {modul}: {result.status_code}")
				self._successRate["Success"] += 1
			else:
				logger.warning(f"Request's result for modul {modul}: {result.status_code}")
				self._successRate["Fail"] += 1
				return
		except Exception as e:
			logger.error(e)
			self._successRate["Fail"] += 1
			return
		
		self._completeJSON[modul] = result.json()

	def printSuccessRate(self) -> None:
		"""
		Logs the current success and failure rates of the JSON processing operations.
		"""
		logger.info(f"Success: {self._successRate["Success"]}, Fails: {self._successRate["Fail"]}")

	def saveToFile(self, path=JSON_MERGED_PATH) -> None:
		"""
		Saves the processed JSON data to a specified file, creating necessary directories if they don’t exist.

		:param `path`: The file path where the JSON should be saved. Defaults to `JSON_MERGED_PATH`.
		"""
		directory = os.path.dirname(path)
		try:
			if directory:
				os.makedirs(directory, exist_ok=True)
	
			with open(path, "w") as newJSON:
				json.dump(self._completeJSON, newJSON, indent="\t")
			logger.info(f"Successfuly wrote JSON into '{path}'")
		except Exception as e:
			logger.error(e)
			raise e
			