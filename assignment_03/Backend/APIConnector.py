import http.client, json

from Backend.config import RAPID_API
from Backend.logger import logger

# Modul initialisation
try:
	apiConnection = http.client.HTTPSConnection(RAPID_API["url"])
except Exception:
	logger.fatal("Could not connect to the RapidAPI. Terminating...")
	exit(1)

REQUEST_ADDRESES = {
	"getCity": "/v1/geo/cities?namePrefix={cityName}&limit=1"
}
HEADERS = {
	'x-rapidapi-key': RAPID_API['key'],
	'x-rapidapi-host': RAPID_API["url"]
}


def getCityID(city: str) -> str:
	apiConnection.request(
		"GET", 
		REQUEST_ADDRESES['getCity'].format(cityName = city),
		headers = HEADERS
	)
	result = apiConnection.getresponse()
	if(result.getcode() > 400 ):
		raise ValueError
	else:
		return json.loads(result.read().decode("utf-8"))['id']

def getDistance(ctiyA: str, cityB: str) -> int:
	"""_summary_

	Args:
		ctiyA (str): _description_
		cityB (str): _description_

	Returns:
		int: _description_
	"""
	
	
	return 0