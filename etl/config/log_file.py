import os


def log_file_name(file: str) -> str:
    current_dir = os.path.dirname(os.path.relpath(file))
    return current_dir.split("/")[-1:][0]
