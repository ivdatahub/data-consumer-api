# Awesome API ETL Project
This repository houses the Awesome project, dedicated to the ETL process of currency quotes data.

## Project Structure

- [`data/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/data): Stores raw data in Parquet format.
  - ETH-EUR-1713658884.parquet: Ex: Raw data for ETH-EUR quotes. file-name = symbol + unix timestamp of extraction
- [`notebooks/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/notebooks): Contains the `data_explorer.ipynb` notebook for data exploration.
- [`etl/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl): Holds the project source code.
  - [`main.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/main.py): The  entrypoint for ETL Module
  - [`jobs/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/jobs): ETL Modules   
    - [`ExtractApiData/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/jobs/ExtractApiData): Module for data extraction from API.
      - [`ApiToParquetFile.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/jobs/ExtractApiData/ApiToParquetFile.py): Extract API data to Parquet File and storage in /data
  - [`utils/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/utils)
    - [`logs.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/utils/logs.py): Package for managing logs.
    - [`common.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/utils/common.py): Package for common tasks in the code
    - [`constants.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/utils/constants.py): Constants used in the code

## If you want run this project and verify time of execution:

<details>
  <summary>Click here:</summary>
  
  ## Step by Step
  1. Clone the repository:
    `$ git clone https://github.com/IvanildoBarauna/ETL-awesome-api.git`

  2. Install project dependencies using `poetry`:
    `$ poetry install`
    
  3. Run de main.py script
    `$ poetry run python etl/main.py`
    
  4. This command will execute the main script of the project, initiating the ETL process for currency quotes data.
    Note: Ensure that you have Python 3.9 installed on your system.

  5. Alternatively, you can run the project using Docker or Docker Compose. To build and run the Docker image, use the following command:
     Note: Note: Ensure that you have Docker installed on your system.
     
    `$ docker build -t etl-awesome-api . && docker run etl-awesome-api`
    
    To run the project with Docker Compose, use the following command:

    `$ docker-compose up`

</details>

## The results of ETL and Data Analysis, look the Jupyter Notebook bellow:

You can see the complete Data Analysis [here](notebooks/data_explorer.ipynb)
