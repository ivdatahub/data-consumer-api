import os
from datetime import datetime, timezone, timedelta

def DefaultOutputFolder():
    return os.path.join(os.path.dirname(__file__), "../../data/")

def DefaultTimestampStr() -> str:
    current = datetime.now().timestamp()
    return str(int(current))

def DefaultUTCDatetime() -> str:    
    return (datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M:%S")
