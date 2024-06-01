from etl.common.utils.logs import CustomLogger
from etl.common.utils.common import DefaultOutputLogFolder
import logging
import os

def test_custom_logger_contructor():
    new_logger = CustomLogger("test")
    assert new_logger.module == "test"
    
def test_custom_logger():
    new_logger = CustomLogger("test")
    logger = new_logger._logger()
    assert isinstance(logger, logging.Logger)

def test_make_file_log():
    default_folder = DefaultOutputLogFolder()
    expected_file_log = "test.log"
    expected_path = f"{default_folder}/{expected_file_log}"
    
    new_logger = CustomLogger("test")
    result_path = new_logger._make_file_log()
    
    assert result_path == expected_path
    assert os.path.isfile(expected_path)
