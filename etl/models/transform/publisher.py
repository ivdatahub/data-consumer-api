import time
import queue

from tqdm import tqdm

from etl.config.logFile import log_file_name

WORK_DIR = log_file_name(file=__file__)


class transformation:
    def __init__(self, json_response: dict, params, queue: queue.Queue):
        self.json_response = json_response
        self.valid_params = params
        self.queue = queue

    def publish(self):
        for param in tqdm(
            self.valid_params, total=len(self.valid_params), desc="Producing Data"
        ):
            dic = self.json_response[param.replace("-", "")]
            time.sleep(0.2)
            self.queue.put(dic)
