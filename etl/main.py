import sys
import os

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(WORK_DIR))

from etl import ExecutePipeline

def main():
    ExecutePipeline("USD-BRL", "BTC-BRL")

if __name__ == "__main__":
    main()
    