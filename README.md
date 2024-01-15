# Awesome ETL Project

This repository houses the Awesome project, dedicated to the ETL process of currency quotes data.

## Project Structure

- `config/`: Contains project configuration files.
- `data/raw/`: Stores raw data in Parquet format.
  - `BTC-USD-1705097387-00000-of-00001.parquet`: Raw data for BTC-USD quotes.
  - `ETH-USD-1705097387-00000-of-00001.parquet`: Raw data for ETH-USD quotes.
  - `USD-BRL-1705097387-00000-of-00001.parquet`: Raw data for USD-BRL quotes.
- `notebooks/`: Contains the `data_explorer.ipynb` notebook for data exploration.
- `src/`: Holds the project source code.
  - `etl/`: ETL module.
    - `extract.py`: Functions for data extraction.
    - `transform.py`: Functions for data transformation.
    - `load.py`: Functions for data loading.
    - `logs.py`: Module for managing logs.
  - `main.py`: Main script of the project.
- `tests/`: Contains tests for the ETL module.

## How to Run

1. Install project dependencies using `poetry`:

   ```bash
   poetry install

2. Run de main.py script

  ```python
  python -m main.py
