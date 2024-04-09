# Auxiliar Dependencies
import pyarrow
import requests
# Custom Logs
from etl.utils.logs import ConsoleInfo, ConsoleError, ConsoleWarning
from etl.utils.common import DefaultTimestampStr, DefaultOutputFolder
from etl.config.beam import CustomBeam
from etl.utils.constants import ENDPOINT_LIST_AVALIABLE_PARITYS, ENDPOINT_QUOTES_AWESOME_API