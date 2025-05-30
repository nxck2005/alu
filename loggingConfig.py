# Logging config, so all module level loggers can inherit
# vibe coded, please use w caution. i could not be arsed lol

import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from constants import __version__
import sys

def loggingConfigure():
    
    # make the path directory if it doesnt exist
    os.makedirs("logs", exist_ok=True)
    
    # formatted date for filename
    dtfmt = datetime.now().strftime("%Y%m%d_%H%M%S")
    logfname = f"logs/alu_{__version__}_{dtfmt}.log"
    
    # 10 MB per file, 5 log files
    rtHandler = RotatingFileHandler(
        logfname,
        maxBytes=10*1024*1024,
        backupCount=5,
        encoding='utf-8'
    )

    # change level as needed
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            rtHandler,
            logging.StreamHandler(sys.stdout)
        ],
    )
    return
