import logging
import os
from datetime import datetime

#log file ka name ky hoge
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#folder bana ne ke liye logs name ka
folder_path = os.path.join(os.getcwd(), "logs")
os.makedirs(folder_path,exist_ok=True)

#log file ka complete path
LOG_FILE_PATH = os.path.join(folder_path,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)


if __name__== "__main__":
    logging.info("logging has started")
