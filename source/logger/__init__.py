import os, sys
import logging
from datetime import datetime


LOG_DIR = "logs" #all the logs will be stored in the directory
#now we have to join the paths main (root) directory to current working directory(src)

LOG_DIR = os.path.join(os.getcwd(),LOG_DIR)
os.makedirs(LOG_DIR,exist_ok=True)

#creating a input log file with .log extension with time stamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

#creating a output log file

log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(filename = log_file_path, filemode="w", format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s' ,level=logging.INFO)

