import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from etl.jobs.extract.ApiToParquetFile import extraction

def main():
    extraction("USD-BRL", "BTC-BRL")

if __name__ == "__main__":
    main()
    