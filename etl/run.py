import time
import sys

from etl.controller.pipeline import PipelineExecutor

start = time.time()


def main(params: str = "USD-BRL"):
    new_exec = PipelineExecutor(params)
    new_exec.pipeline_run()


# pragma: no cover
if __name__ == "__main__":
    if len(sys.argv) > 1:
        params = str(sys.argv[1])
        main(params)
    else:
        main()

print("Elapsed Time: ", round(time.time() - start, 2), "seconds")
