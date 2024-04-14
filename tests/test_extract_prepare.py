import os
import sys 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl import ExecutePipeline
import pytest

def test_pipelines_params_with_unique_param():
    ## Valid Scenarios    
    with pytest.raises(Exception):
        ExecutePipeline("USD-BRL")
    
def test_pipelines_params_with_two_or_more_valid_params():
    with pytest.raises(Exception):
        ExecutePipeline("USD-BRL", "BTC-BRL")
    
def test_pipelines_params_with_one_invalid_params():
    with pytest.raises(Exception):
        ExecutePipeline("USD-BRL", "BTC-BRL", 1)
    
def test_pipelines_params_with_one_invalid_params():
    with pytest.raises(TypeError):
        ExecutePipeline(1)
        
def test_pipelines_params_with_more_invalid_params():
    with pytest.raises(TypeError):
        ExecutePipeline(1,1,1)