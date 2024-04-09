import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class CustomBeam:
    def BeamObj(): return beam
    
    def PipelineDirectRunner():
        return PipelineOptions([f"--runner", "Direct", f"--direct_num_workers={1}"])
