import pytest
from etl.controller.pipeline import ExecutePipeline

def test_pipelines_params_with_unique_param():
    ExecutePipeline("USD-BRL")

def test_pipelines_params_with_two_param():
    ExecutePipeline("USD-BRL", "USD-BRLT")

def test_pipelines_params_with_one_invalid_params():
    with pytest.raises(TypeError):
        ExecutePipeline(1)

def test_pipelines_params_with_all_invalid_params():
    with pytest.raises(TypeError):
        ExecutePipeline(1, 1, 1)

def test_pipelines_params_with_all_invalid_keys_params():
    with pytest.raises(KeyError):
        ExecutePipeline("INVALID-QUOTE", "INVALID-QUOTE2")