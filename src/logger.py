import logging
import os
from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# os.makedirs(logs_path, exist_ok=True)
#
# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
#
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
#
# )

# Set the name of the log directory
LOG_DIRECTORY = "logs"

# Create the log directory if it doesn't exist
os.makedirs(LOG_DIRECTORY, exist_ok=True)

# Set the name of the log file using the current timestamp
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Set the full path to the log file
LOG_FILE_PATH = os.path.join(LOG_DIRECTORY, LOG_FILE_NAME)

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# if __name__ == "__main__":
#     logging.info("Logger has started")
