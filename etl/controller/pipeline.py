import time
import threading
import queue

from tqdm import tqdm

from etl.models.extract.api_data_extractor import extraction
from etl.models.transform.publisher import transformation
from etl.models.load.parquet_loader import load
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

        extractor = extraction(self.params)
        response, valid_params = extractor.run

        try:
            def produce():
                transformer = transformation(
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
                        time.sleep(0.2)
                        item = self.controller_queue.get()
                        if item is None:
                            self.controller_queue.task_done()
                            break
                        loader = load(item)
                        self.files_to_dataset.append(loader.run()[0])
                        self.controller_queue.task_done()
                        pbar.update()

            thread_producer = threading.Thread(target=produce)
            thread_consumer = threading.Thread(target=consume)

            thread_producer.start()

            thread_consumer.start()

            thread_producer.join()
            thread_consumer.join()
            self.controller_queue.join()
            
            DatasetSerializer(self.files_to_dataset).serialize()

        except Exception as e:
            raise e
