import logging
import os
from etl.common.utils.common import DefaultOutputLogFolder


class CustomLogger():
    def __init__(self, module) -> None:
        self.module = module
        self._log_format = "%(asctime)s :: %(levelname)s :: %(message)s"
    
    def _make_file_log(self):
        dir_name = DefaultOutputLogFolder()
        os.makedirs(dir_name, exist_ok=True)
        
        with open(dir_name + f"{self.module}.log", "w") as f:
            f.write("")
            
        return dir_name + f"{self.module}.log"
    
    
    def _logger(self):
        file_log = self._make_file_log()
            
        logging.basicConfig(
            filename=file_log,
            level=logging.DEBUG,
            format=self._log_format,
            datefmt="%Y-%m-%d %H:%M:%S",
            )
        
        consoleLog = logging.getLogger("consoleLogger")
        
        consoleLog.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(self._log_format)
        ch.setFormatter(formatter)

        consoleLog.addHandler(ch)

        return consoleLog


    def info(self, msg: str):
        """
        Logs an informational message.

        Args:
            msg (str): The message to be logged.
            module (str): The name of the module.

        Returns:
            None
        """
        if logging.getLogger("consoleLogger").hasHandlers():
            logger = logging.getLogger("consoleLogger")
        else:
            logger = CustomLogger(module=self.module)._logger()

        logger.info(msg=msg)


    def error(self, msg: str):
        """
        Logs an error message.

        Args:
            msg (str): The message to be logged.
            module (str): The name of the module.

        Returns:
            None
        """
        if logging.getLogger("consoleLogger").hasHandlers():
            logger = logging.getLogger("consoleLogger")
        else:
            logger = CustomLogger(module=self.module)._logger()

        logger.error(msg=msg)


    def warning(self, msg: str):
        """
        Logs a warning message.

        Args:
            msg (str): The message to be logged.
        Returns:
            None
        """
        if logging.getLogger("consoleLogger").hasHandlers():
            logger = logging.getLogger("consoleLogger")
        else:
            logger = CustomLogger(module=self.module)._logger()

        logger.warn(msg=msg)