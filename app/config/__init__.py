def BeamDirectRunnerOptions(workers: int):
    from apache_beam.options.pipeline_options import PipelineOptions
    
    return PipelineOptions(
        [
            f"--runner", "Direct", f"--direct_num_workers={workers}"
        ]
    )

def OutputFolder():
    import os
    return os.path.join(os.path.dirname(__file__), "../../data/")


