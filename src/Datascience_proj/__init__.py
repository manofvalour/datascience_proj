import os
import sys
import logging
from datetime import datetime

logging_str= "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

LOG_FILE_NAME= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_filepath= os.path.join(log_dir, LOG_FILE_NAME)
os.makedirs(log_filepath)

log_filename = os.path.join(log_filepath, LOG_FILE_NAME)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger('datasciencelogger')