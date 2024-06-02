import pytest
from etl.controller.pipeline import PipelineExecutor

def test_pipelines_params_with_two_param():
    expected_result = ["USD-BRL", "USD-BRLT"]
    new_executor = PipelineExecutor("USD-BRL", "USD-BRLT")
    result = new_executor.pipeline_run()
    assert result == expected_result  
    
def test_pipelines_params_with_two_param_and_one_invalid():
    expected_result = ["USD-BRL", "USD-BRLT"]
    new_executor = PipelineExecutor("USD-BRL", "USD-BRLT", "invalid_param")
    result = new_executor.pipeline_run()
    assert result == expected_result  

def test_pipelines_params_with_all_invalid_params():
    with pytest.raises(TypeError):
        new_executor = PipelineExecutor(1, 1, 1)
        new_executor.pipeline_run()


def test_pipelines_params_with_all_invalid_keys_params():
    with pytest.raises(KeyError):
        validator = PipelineExecutor("INVALID-QUOTE", "INVALID-QUOTE2")
        validator.pipeline_run()
