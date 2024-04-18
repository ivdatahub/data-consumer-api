import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class NewApacheBeamInstance:
    def BeamObj(self): return beam
    
    def PipelineDirectRunner(self):
        opts = PipelineOptions([f"--runner", "Direct", f"--direct_num_workers={1}"])
        return beam.Pipeline(options=opts) # type: ignore
    
def CustomBeam():
    return NewApacheBeamInstance()
