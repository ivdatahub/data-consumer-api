import time
import threading
import queue

from tqdm import tqdm

from etl.models.extract.api_data_extractor import extraction
from etl.models.transform.publisher import transformation
from etl.models.load.parquet_loader import load


class PipelineExecutor:
    def __init__(self, *xargs):
        self.params = list(xargs)
        self.controller_queue = queue.Queue()

        totalInvalidParams = 0
        for arg in self.params:
            if not isinstance(arg, str):
                totalInvalidParams += 1

        if totalInvalidParams == len(self.params):
            raise TypeError(f"Invalid parameters >>>> {self.params}")

    def pipeline_run(self):
        extractor = extraction(self.params)

        try:
            # Define a função que será executada pelo thread do produtor
            def produce():
                transformer = transformation(
                    extractor.json_data, extractor.ValidParams, self.controller_queue
                )
                transformer.publish()
                # Sinaliza que a produção está completa
                self.controller_queue.put(None)

            # Define a função que será executada pelo thread do consumidor
            def consume():
                with tqdm(
                    desc="Consuming Data", unit=" item", total=len(extractor.ValidParams)
                ) as pbar:
                    while True:
                        time.sleep(0.5)
                        item = self.controller_queue.get()
                        if item is None:
                            self.controller_queue.task_done()
                            break
                        loader = load(item)
                        loader.run()
                        self.controller_queue.task_done()
                        pbar.update()

            # Criação dos threads
            thread_producer = threading.Thread(target=produce)
            thread_consumer = threading.Thread(target=consume)

            # Inicia os threads
            thread_producer.start()

            thread_consumer.start()

            thread_producer.join()
            thread_consumer.join()
            self.controller_queue.join()

        except Exception as e:
            # Tratamento genérico para outras exceções
            print(f"Erro durante a execução do pipeline: {e}")
            raise e
