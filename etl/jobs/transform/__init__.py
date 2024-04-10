import psycopg2
import pyarrow.parquet as pyArrowParquet

from etl.config.beam import CustomBeam
from etl.utils.common import DefaultOutputFolder
from etl.utils.logs import ConsoleInfo, ConsoleError, ConsoleWarning
