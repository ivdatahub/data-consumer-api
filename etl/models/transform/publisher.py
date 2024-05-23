import time
from tqdm import tqdm
from etl.common.utils.logs import loggingInfo
from etl.config.logFile import logFileName


WORK_DIR = logFileName(file=__file__)


class transformation:
    def __init__(self, json_response: dict, params, fila: object):
        self.json_response = json_response
        self.validParams = params
        self.fila = fila

    def publish(self):
        for param in tqdm(
            self.validParams, total=len(self.validParams), desc="Producing Data"
        ):
            dic = self.json_response[param.replace("-", "")]
            time.sleep(0.5)
            self.fila.put(dic)  # type: ignore
