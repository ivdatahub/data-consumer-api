import queue
from tqdm import tqdm


class ResponseTransformation:
    def __init__(self, json_response: dict, params, etl_queue: queue.Queue):
        self.json_response = json_response
        self.valid_params = params
        self.queue = etl_queue

    def publish(self):
        for param in tqdm(
            self.valid_params, total=len(self.valid_params), desc="Producing Data"
        ):
            dic = self.json_response[param.replace("-", "")]
            self.queue.put(dic)
