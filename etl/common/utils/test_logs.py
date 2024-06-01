from .logs import CustomLogger
import logging

def test_custom_logger_contructor():
    new_logger = CustomLogger("test")
    
    assert new_logger.module == "test"
    return new_logger
    
def test_custom_logger():
    new_logger = CustomLogger("test")
    
    logger = new_logger._logger()
    
    assert isinstance(logger, logging.Logger)

    