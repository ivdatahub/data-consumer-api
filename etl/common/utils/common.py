import os
from datetime import datetime, timezone, timedelta


def DefaultOutputFolder():
    """
    Returns the default output folder path.
    """
    return os.path.join(os.path.dirname(__file__), "../../../data/")


def DefaultOutputLogFolder() -> str:
    """
    Returns the default output log folder path.
    """
    return os.path.join(os.path.dirname(__file__), "../logs/")


def DefaultTimestampStr() -> str:
    """
    Returns the current timestamp as a string.
    """
    current = datetime.now().timestamp()
    return str(int(current))


def DefaultUTCDatetime() -> str:
    """
    Returns:
        str: The current UTC datetime as a string in the format "%Y-%m-%d %H:%M:%S".
    """
    return (datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M:%S")
