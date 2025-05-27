# Logging config, so all module level loggers can inherit

import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

def loggingConfigure():
    
    # make the path directory if it doesnt exist
    os.makedirs("logs", exist_ok=True)
    
    # formatted date for filename
    dtfmt = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    rfHandler = RotatingFileHandler()
    
    logging.basicConfig(
        filename=f"logs/alu_{dtfmt}.log",
        
    )
    
    
    
    return