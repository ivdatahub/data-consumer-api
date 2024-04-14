import os
from datetime import datetime
import pyarrow

def DefaultOutputFolder():
    return os.path.join(os.path.dirname(__file__), "../../data/")

def DefaultTimestampStr() -> str:
    current = datetime.now().timestamp()
    return str(int(current))

def DefaultQuotesAPISchema():
    api_header = [
        "code",
        "codein",
        "name",
        "high",
        "low",
        "varBid",
        "pctChange",
        "bid",
        "ask",
        "timestamp",
        "create_date"]

    schema = []
    for field in api_header:
        schema += [(field, pyarrow.string())]

    return pyarrow.schema(schema)