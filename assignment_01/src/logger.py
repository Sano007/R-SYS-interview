import logging
import os

from config import *


LOG_COLORS = {
    "DEBUG": "\033[36m",    # Cyan
    "INFO": "\033[32m",     # Green
    "WARNING": "\033[33m",  # Yellow
    "ERROR": "\033[31m",    # Red
    "CRITICAL": "\033[35;1m"  # Bright Magenta
}
# Ensure Logs directory exists
os.makedirs("Logs", exist_ok=True)


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        # Add color to the log level name
        log_color = LOG_COLORS.get(record.levelname, "")
        reset = "\033[0m"

        # Format the log message
        record.levelname = f"{log_color}{record.levelname}{reset}"
        return super().format(record)

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
fileHandler = logging.FileHandler(LOG_PATH)
fileHandler.setLevel(logging.DEBUG)
fileFormatter = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
fileHandler.setFormatter(fileFormatter)

# Create a console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.WARNING)
consoleFormatter = ColoredFormatter("[%(levelname)s] %(message)s")
consoleHandler.setFormatter(consoleFormatter)

# Add handlers to the logger
logger.handlers.clear()
logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)