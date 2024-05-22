from etl.common.utils.logs import loggingInfo
from etl.config.logFile import logFileName

WORK_DIR = logFileName(file=__file__)


class transformation:
    def __init__(self, json_response: dict, params, fila: object):
        self.json_response = json_response
        self.validParams = params
        self.fila = fila

    def publish(self):
        for param in self.validParams:
            dic = self.json_response[param.replace("-", "")]
            self.fila.put(dic)  # type: ignore
