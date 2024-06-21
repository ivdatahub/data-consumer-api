import time
import threading
import queue

from tqdm import tqdm

from etl.models.extract.api_data_extractor import APIExtraction
from etl.models.transform.publisher import ResponseTransformation
from etl.models.load.parquet_loader import ParquetLoader
from etl.views.make_dataset import DatasetSerializer


class PipelineExecutor:
    def __init__(self, *xargs):
        self.params = list(xargs)
        self.files_to_dataset = []
        self.controller_queue = queue.Queue()

    def pipeline_run(self):
        total_invalid_params = 0
        for arg in self.params:
            if not isinstance(arg, str):
                total_invalid_params += 1

        if total_invalid_params == len(self.params):
            raise TypeError(f"Invalid parameters >>>> {self.params}")

        response, valid_params = APIExtraction.run(self.params)

        try:
            def produce():
                transformer = ResponseTransformation(
                    json_response=response,
                    params=valid_params,
                    queue=self.controller_queue,
                )
                transformer.publish()
                # The production is finished
                self.controller_queue.put(None)

            def consume():
                with tqdm(
                    desc="Consuming Data",
                    unit=" item",
                    total=len(valid_params),
                ) as pbar:
                    while True:
                        item = self.controller_queue.get()
                        if item is None:
                            self.controller_queue.task_done()
                            break
                        self.files_to_dataset.append(ParquetLoader.run(item)[0])
                        self.controller_queue.task_done()
                        pbar.update()

            thread_producer = threading.Thread(target=produce)
            thread_consumer = threading.Thread(target=consume)

            thread_producer.start()

            thread_consumer.start()

            thread_producer.join()
            thread_consumer.join()
            self.controller_queue.join()
            
            DatasetSerializer.serialize(self.files_to_dataset)
            
            return valid_params

        except Exception as e:
            raise e
