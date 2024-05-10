# Awesome Project: ETL Process for Currency Quotes Data

![Project Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)  ![License](https://img.shields.io/badge/license-MIT-blue)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/IvanildoBarauna/ETL-awesome-api) ![Python Version](https://img.shields.io/badge/python-3.9-blue) 

![GitHub Workflow Status](https://github.com/IvanildoBarauna/ETL-awesome-api/actions/workflows/CI-CD.yaml/badge.svg) 


Project description
This project, called "Awesome Project: ETL Process for Currency Quotes Data", is a solution dedicated to extracting, transforming and loading (ETL) currency quote data. It makes a single request to a specific endpoint to obtain quotes for multiple currencies.

The request response is then processed, where each currency quote is separated and stored in individual files in Parquet format. This makes it easier to organize data and efficiently retrieve it for future analysis.

Additionally, the project includes a Jupyter Notebook for data exploration. This notebook is responsible for consolidating all individual Parquet files into a single dataset. From there, the data can be explored and analyzed to gain valuable insights into currency quotes.

In summary, this project provides a complete solution for collecting, processing and analyzing currency quote data.

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

    `$ docker-compose up --build`

</details>

## The results of ETL and Data Analysis, look the Jupyter Notebook bellow:

You can see the complete Data Analysis [here](notebooks/data_explorer.ipynb)
