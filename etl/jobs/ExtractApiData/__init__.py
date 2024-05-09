# Auxiliar Dependencies
import requests
# Custom Logs
from etl.utils.logs import loggingInfo, loggingError, loggingWarn
from etl.utils.common import DefaultTimestampStr, DefaultOutputFolder, DefaultUTCDatetime
import pandas
import os
from dotenv import load_dotenv

load_dotenv()

SRV_URL = str(os.getenv("SERVER_URL"))
""" Reference for Server URL from enviroment variable """


current_dir = os.path.dirname(os.path.relpath(__file__))
WORK_DIR = current_dir.split("/")[-1:][0]
