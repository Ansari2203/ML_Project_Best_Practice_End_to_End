# Generic Function to Log Each Errors into log file
import logging
import os
from datetime import datetime

LOG_FILE = "{}.log".format(datetime.now().strftime('%m_%d_%Y_%H_%M_%S'))
logs_path = os.path.join(os.getcwd(), "logs")

try:
    os.makedirs(logs_path)
except OSError as e:
    if e.errno != os.errno.EEXIST:
        raise

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Uncomment below two line if you want to check this file code is working properly or not 
# if __name__ == "__main__":
#     logging.info("Logging has started")
