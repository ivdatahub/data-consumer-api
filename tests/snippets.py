from enum import Enum
from datetime import datetime, timezone
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import logging

logging.getLogger("__name__")

def logger(function):
    def inner(*args, **kwargs):
        print(f"{datetime.now(timezone.utc)} ::: Antes de chamar a função:  {function.__name__}")
        result = function(*args, **kwargs)
        print(f"{datetime.now(timezone.utc)} ::: Depois de chamar a função:  {function.__name__}")
        return result
    return inner

class pipelineType(Enum):
    EXTRACT = 1
    TRANSFORM = 2
    LOAD = 3
    
class pipeline:
    def __init__(self, type: pipelineType) -> None:
        pass
    
    @logger
    def BeamObj(self):
        return beam
    
    @logger        
    def PipelineDirectRunner(self):
        opts = PipelineOptions([f"--runner", "Direct", f"--direct_num_workers={1}"])
        return beam.Pipeline(options=opts) # type: ignore
    
    
NewPipeline = pipeline(type=pipelineType.EXTRACT)
beamObj = NewPipeline.BeamObj()
beamOpts = NewPipeline.PipelineDirectRunner()