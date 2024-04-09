import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from etl import ExecutePipeline

def main():
    ExecutePipeline("USD-BRL", "BTC-BRL")

if __name__ == "__main__":
    main()
    