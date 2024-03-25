# Apache Beam Dependencies
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# Auxiliar Dependencies
import pyarrow
import requests
from datetime import datetime
import os

# Custom Logs
from utils.logs import ConsoleInfo, ConsoleError, ConsoleWarning