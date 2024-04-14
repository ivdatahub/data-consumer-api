# Auxiliar Dependencies
import pyarrow
import requests
# Custom Logs
from etl.utils.logs import loggingInfo, loggingError, loggingWarn
from etl.utils.common import DefaultTimestampStr, DefaultOutputFolder, DefaultQuotesAPISchema
from etl.config.beam import CustomBeam
from etl.utils.constants import ENDPOINT_QUOTES_AWESOME_API
import os

current_dir = os.path.dirname(os.path.relpath(__file__))
WORK_DIR = current_dir.split("/")[-1:][0]
