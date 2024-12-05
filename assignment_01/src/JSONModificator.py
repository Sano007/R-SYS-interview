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
	_duplicitKeys: dict
	_uniqueKeys: dict
	_successRate: dict

	def __init__(self) -> None:
		self._completeJSON = {}
		self._uniqueKeys = {}
		self._duplicitKeys = {}
		self._successRate = {"Success": 0, "Fail": 0}

	def _getFromURL(self, url: str, modul: str) -> dict:
		"""
		Function for getting data in JSON format from REST API.

		:param `url`: URL address for request.
		:param `modul`: Name of the modul for log info.
		:returns `dict`: json data saved into dictionary if operation success, otherwise `None`. 
		"""
		try:
			result = requests.get(url)
			if(result.ok):
				logger.info(f"Request's result for modul {modul}: {result.status_code}")
			else:
				logger.error(f"Request's result for modul {modul}: {result.status_code}")
				return None
		except Exception as e:
			logger.critical(e)
			return None
		return result.json()
	
	def _findDuplicates(self, values: dict) -> None:
		"""
		Finds duplicit keys by saving unique ones into separate dictionary. In case 
		the key already exists, it is stored also with its value into dictionary with duplicates.

		:param `values`: dictionary with new entry for comparing.
		"""
		for key, value in values.items():
			if(not key in self._uniqueKeys):
				self._uniqueKeys[key] = value
			elif(not key in self._duplicitKeys):
				self._duplicitKeys[key] = value
			elif(isinstance(self._duplicitKeys[key], list)):
				self._duplicitKeys[key].append(value)
			else:
				self._duplicitKeys[key] = [self._duplicitKeys[key], value]


	def processJSON(self, url: str, modul: str = "main") -> None:
		"""
		Fetches JSON data from a given URL and stores it in self under **modul name**.

		:param `url`: The URL to fetch JSON data from.
		:param `modul`: The module name under which to store the fetched `JSON`. Defaults to `"main"`.
		"""
		result = self._getFromURL(url, modul)
		if(result is None):
			self._successRate["Fail"] += 1
		else:
			if(len(result) == 0):
				logger.warning(f"Modul {modul} is empty!")
			if(ALLOW_EMPTY_KEYS):
				self._completeJSON[modul] = result
				self._successRate["Success"] += 1
			elif(len(result) > 0):
				self._completeJSON[modul] = result
				self._successRate["Success"] += 1
			else:
				self._successRate["Fail"] += 1


			self._findDuplicates(result)

	def printSuccessRate(self) -> None:
		"""
		Logs the current success and failure rates of the JSON processing operations.
		"""
		logger.info(f"Success: {self._successRate["Success"]}, Fails: {self._successRate["Fail"]}")

	def saveToFile(self, pathMerged: str = JSON_MERGED_PATH, pathDuplicit: str = JSON_DUPLICIT_PATH) -> None:
		"""
		Saves the processed JSON data to a specified file, creating necessary directories if they don’t exist.

		:param `path`: The file path where the JSON should be saved. Defaults to `JSON_MERGED_PATH`.
		"""
		directory = os.path.dirname(pathMerged)
		try:
			if directory:
				os.makedirs(directory, exist_ok=True)
	
			with open(pathMerged, "w") as newJSON:
				json.dump(self._completeJSON, newJSON, indent="\t")
			logger.info(f"Successfuly wrote JSON into '{pathMerged}'")
			with open(pathDuplicit, "w") as newJSON:
				json.dump(self._duplicitKeys, newJSON, indent="\t")
			logger.info(f"Successfuly wrote JSON into '{pathDuplicit}'")

		except Exception as e:
			logger.error(e)
			raise e
			