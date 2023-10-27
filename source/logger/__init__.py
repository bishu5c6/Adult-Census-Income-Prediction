'''
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
'''
import logging
import os
from datetime import datetime
import os

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

#https://docs.python.org/3/library/logging.html for more logging information

