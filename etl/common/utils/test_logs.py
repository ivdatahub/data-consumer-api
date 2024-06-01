from .logs import CustomLogger
import logging
import os

def test_custom_logger_contructor():
    new_logger = CustomLogger("test")
    
    assert new_logger.module == "test"
    return new_logger
    
def test_custom_logger():
    new_logger = CustomLogger("test")
    
    logger = new_logger._logger()
    
    assert isinstance(logger, logging.Logger)

def test_make_file_log():
    new_logger = CustomLogger("test")
    
    
    new_logger._make_file_log()
    
    assert os.path.exists()
    
    