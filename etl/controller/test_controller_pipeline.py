import pytest
from etl.controller.pipeline import PipelineExecutor


def test_pipelines_params_with_unique_param():
    NewExec = PipelineExecutor("USD-BRL")
    NewExec.pipeline_run()


def test_pipelines_params_with_two_param():
    NewExec = PipelineExecutor("USD-BRL", "USD-BRLT")
    NewExec.pipeline_run()


def test_pipelines_params_with_one_invalid_params():
    with pytest.raises(TypeError):
        newExec = PipelineExecutor(1)
        newExec.pipeline_run()



def test_pipelines_params_with_all_invalid_params():
    with pytest.raises(TypeError):
        newExec = PipelineExecutor(1, 1, 1)
        newExec.pipeline_run()


def test_pipelines_params_with_all_invalid_keys_params():
    validator = None
    try:
        with pytest.raises(KeyError):
            validator = PipelineExecutor("INVALID-QUOTE", "INVALID-QUOTE2")
            validator.pipeline_run()
    finally:
        validator = None
