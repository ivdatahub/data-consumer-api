import logging
import os
import sys

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(WORK_DIR))

def LogConfig(module: str):    
    return logging.basicConfig(
        filename=f"etl/logs/{module}.log",
        level=logging.DEBUG, 
        format='%(asctime)s :: %(levelname)s :: %(filename)s :: %(lineno)d :: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S' 
    )

def loggingInfo(msg, module):
    LogConfig(module)
    return logging.info(msg)

def loggingError(msg, module):
    LogConfig(module)
    return logging.error(msg)

def loggingWarn(msg,module):
    LogConfig(module)
    return logging.warning(msg)

