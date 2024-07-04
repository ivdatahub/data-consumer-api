import logging
import os
from etl.common.utils.common import default_output_log_folder


class CustomLogger:
    def __init__(self, module) -> None:
        self.module = module
        self._log_format = "%(asctime)s :: %(levelname)s :: %(message)s"

    def make_file_log(self):
        dir_name = default_output_log_folder()
        os.makedirs(dir_name, exist_ok=True)

        with open(dir_name + f"{self.module}.log", "w", encoding="UTF-8") as f:
            f.write("")

        return dir_name + f"{self.module}.log"

    def logger(self):
        file_log = self.make_file_log()

        logging.basicConfig(
            filename=file_log,
            level=logging.DEBUG,
            format=self._log_format,
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_log = logging.getLogger("consoleLogger")

        console_log.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(self._log_format)
        ch.setFormatter(formatter)

        console_log.addHandler(ch)

        return console_log

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
            logger = CustomLogger(module=self.module).logger()

        logger.info(msg=msg)

        return True

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
            logger = CustomLogger(module=self.module).logger()

        logger.error(msg=msg)

        return True

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
            logger = CustomLogger(module=self.module).logger()

        logger.warning(msg=msg)

        return True
