import os


def logFileName(file: str) -> str:
    current_dir = os.path.dirname(os.path.relpath(file))
    WORK_DIR = current_dir.split("/")[-1:][0]
    return WORK_DIR
