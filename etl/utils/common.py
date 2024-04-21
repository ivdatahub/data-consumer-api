import os
from datetime import datetime, timezone, timedelta

def DefaultOutputFolder():
    """
    Returns the default output folder path.

    Returns:
        str: The default output folder path.
    """
    return os.path.join(os.path.dirname(__file__), "../../data/")

def DefaultTimestampStr() -> str:
    """
    Returns the current timestamp as a string.

    Returns:
        str: The current timestamp as a string.
    """
    current = datetime.now().timestamp()
    return str(int(current))

def DefaultUTCDatetime() -> str:
    """
    Returns the current UTC datetime as a string.

    Returns:
        str: The current UTC datetime as a string in the format "%Y-%m-%d %H:%M:%S".
    """
    return (datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M:%S")
