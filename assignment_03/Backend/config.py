import json


try:
	with open("config.json", 'r') as cfgFile:
		configuration = json.load(cfgFile)
	LOG_PATH = configuration["log-path"]
	RAPID_API = configuration["RapidAPI"]
except Exception:
	print("Config file was not loaded! Terminating...")
	exit(1)

# RapidAPI constants