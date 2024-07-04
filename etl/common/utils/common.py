import os
from datetime import datetime, timezone


def default_output_folder():

    """
    Returns the default output folder path.
    """
    return os.path.join(os.path.dirname(__file__), "../../../data/")


def default_output_log_folder() -> str:
    """
    Returns the default output log folder path.
    """
    return os.path.join(os.path.dirname(__file__), "../logs/")


def default_timestamp_str() -> str:
    """
    Returns the current timestamp as a string.
    """
    current = datetime.now().timestamp()
    return str(int(current))



def default_utc_datetime() -> str:
    """
    Returns:
        str: The current UTC datetime as a string in the format "%Y-%m-%d %H:%M:%S".
    """
    return (datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M:%S")
