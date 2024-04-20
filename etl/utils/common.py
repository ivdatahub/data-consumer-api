import os
from datetime import datetime

def DefaultOutputFolder():
    return os.path.join(os.path.dirname(__file__), "../../data/")

def DefaultTimestampStr() -> str:
    current = datetime.now().timestamp()
    return str(int(current))