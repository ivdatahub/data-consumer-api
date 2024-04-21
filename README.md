# Awesome API ETL Project
This repository houses the Awesome project, dedicated to the ETL process of currency quotes data.

## Project Structure

- `data/`: Stores raw data in Parquet format.
  - `BTC-USD-1705097387.parquet`: Ex: Raw data for BTC-USD quotes.
- `notebooks/`: Contains the `data_explorer.ipynb` notebook for data exploration.
- `etl/`: Holds the project source code.
  - `main.py`: The  entrypoint for ETL Module
  - `jobs/`: ETL Modules   
    - `ExtractApiData/`: Module for data extraction from API.
      - `ApiToParquetFile.py`: Extract API data to Parquet File and storage in /data
  - `utils/`
    - `logs.py`: Package for managing logs.
    - `common.py`: Package for common tasks in the code
    - `constants.py`: Constants used in the code

## If you want run this project and verify time of execution:

<details>
  <summary>Click here:</summary>
  
  ## Step by Step
  1. Install project dependencies using `poetry`:
  
    ```bash
    poetry install
    ```

  2. Run de main.py script
  
    ```python
    poetry run python etl/main.py
    ```

  3. This command will execute the main script of the project, initiating the ETL process for currency quotes data.
    Note: Ensure that you have Python 3.9 installed on your system.

  4. Alternatively, you can run the project using Docker or Docker Compose. To build and run the Docker image, use the following command:

    ```bash
    docker build -t etl-awesome-api . && docker run etl-awesome-api
    ```

    To run the project with Docker Compose, use the following command:

    ```bash
    docker-compose up
    ```

  ## Requirements

  Python 3.9
  Dependencies listed in pyproject.toml and requirements.txt.
</details>

## The results of ETL and Data Analysis, look the Jupyter Notebook bellow:

You can see the complete Data Analysis [here](notebooks/data_explorer.ipynb)
