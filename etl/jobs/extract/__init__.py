# Auxiliar Dependencies
import pyarrow
import requests
# Custom Logs
from etl.utils.logs import ConsoleInfo, ConsoleError, ConsoleWarning
from etl.utils.common import datetime, DefaultTimestampStr, DefaultOutputFolder
from etl.config.beam import CustomBeam