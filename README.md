# Awesome API ETL Project

This repository houses the Awesome project, dedicated to the ETL process of currency quotes data.

## Project Structure

- `config/`: Contains project configuration files.
- `data/`: Stores raw data in Parquet format.
  - `BTC-USD-1705097387-00000-of-00001.parquet`: Ex: Raw data for BTC-USD quotes.
- `notebooks/`: Contains the `data_explorer.ipynb` notebook for data exploration.
- `app/`: Holds the project source code.
  - `extract.py`: Functions for data extraction.
  - `transform.py`: Functions for data transformation.
  - `load.py`: Functions for data loading.
  - `logs.py`: Module for managing logs.
  - `main.py`: Main script of the project.

## How to Run

1. Install project dependencies using `poetry`:
   ```bash
   poetry install

2. Run de main.py script
   ```python
   poetry run python app/main.py

3. This command will execute the main script of the project, initiating the ETL process for currency quotes data.
Note: Ensure that you have Python 3.9 installed on your system.

## Requirements

Python 3.9
Dependencies listed in pyproject.toml, poetry.lock, and requirements.txt.

# Arch
