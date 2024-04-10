# Awesome API ETL Project

This repository houses the Awesome project, dedicated to the ETL process of currency quotes data.

## Project Structure


- `data/`: Stores raw data in Parquet format.
  - `BTC-USD-1705097387-00000-of-00001.parquet`: Ex: Raw data for BTC-USD quotes.
- `notebooks/`: Contains the `data_explorer.ipynb` notebook for data exploration.
- `etl/`: Holds the project source code.
  - `main.py`: The  entrypoint for ETL Module
  - `jobs/`: ETL Modules   
    - `extract/`: Module for data extraction.
      - `ApiToParquetFile.py`: Extract API data to Parquet File and storage in /data
    - `load.py`: Mobule for dynamic data loading.
      - `InsertOnDataBase`: Insert all files in dw-service
    - `main.py`: Main script of the project.
  - `config/`: Contains project configuration files.
    - `beam.py`: Used for get parameters and configs of Apache Beam
    - `database.py`: Used for get parameters and configs of Datawarehouse
  - `utils/`
    - `logs.py`: Package for managing logs.
    - `common.py`: Package for common tasks in the code
    - `constants.py`: Constants used in the code

## How to Run

1. Install project dependencies using `poetry`:
   ```bash
   poetry install

2. Run de main.py script
   ```python
   poetry run python etl/main.py

3. This command will execute the main script of the project, initiating the ETL process for currency quotes data.
Note: Ensure that you have Python 3.9 installed on your system.

## Requirements

Python 3.9
Dependencies listed in pyproject.toml and requirements.txt.

# Arch
