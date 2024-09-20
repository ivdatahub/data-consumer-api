# Data Consumer Pipeline Project: ETL Process for Currency Quotes Data

![Project Status](https://img.shields.io/badge/status-done-brightgreen?style=for-the-badge&logo=github)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=mit)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/ivdatahub/data-consumer-api?style=for-the-badge&logo=github)
![Python Version](https://img.shields.io/badge/python-3.10-blue?style=for-the-badge&logo=python)

![Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge&logo=python)
![pylint](https://img.shields.io/badge/pylint-10.00-green?style=for-the-badge&logo=python)

[![CI-CD](https://img.shields.io/github/actions/workflow/status/ivdatahub/data-consumer-api/CI-CD.yaml?&style=for-the-badge&logo=githubactions&cacheSeconds=60&label=CI-CD)](https://github.com/ivdatahub/data-consumer-api/actions/workflows/CI-CD.yml)
[![DOCKER-DEPLOY](https://img.shields.io/github/actions/workflow/status/ivdatahub/data-consumer-api/deploy-image.yml?&style=for-the-badge&logo=githubactions&cacheSeconds=60&label=DOCKER-DEPLOY)](https://github.com/ivdatahub/data-consumer-api/actions/workflows/deploy-image.yml)

[![Codecov](https://img.shields.io/codecov/c/github/ivdatahub/data-consumer-api?style=for-the-badge&logo=codecov)](https://app.codecov.io/gh/ivdatahub/data-consumer-api)

## Code Coverage KPI Graph

[![codecov](https://codecov.io/gh/ivdatahub/data-consumer-api/graphs/sunburst.svg?token=GEGNHFM6PS)](https://codecov.io/gh/ivdatahub/data-consumer-api)

## Project Stack

<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" Alt="Python" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" Alt="Docker" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/poetry/poetry-original.svg" Alt="Poetry" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/pandas/pandas-original.svg" Alt="Pandas" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/jupyter/jupyter-original.svg" Alt="Jupyter" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/matplotlib/matplotlib-original.svg" Alt="Matplotlib" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/githubactions/githubactions-original.svg" Alt="GitHub Actions" width="50" height="50">

## Project description

ETL Process for Currency Quotes Data" project is a complete solution dedicated to extracting, transforming and loading (ETL) currency quote data. This project uses several advanced techniques and architectures to ensure the efficiency and robustness of the ETL process.

## Contributing

See the following docs:

- [Contributing Guide](https://github.com/ivdatahub/data-consumer-api/blob/main/CONTRIBUTING.md)
- [Code Of Conduct](https://github.com/ivdatahub/data-consumer-api/blob/main/CODE_OF_CONDUCT.md)

## Project Highlights:

- MVC Architecture: Implementation of the Model-View-Controller (MVC) architecture, separating business logic, user interface and data manipulation for better organization and code maintenance.

- Comprehensive Testing: Development of tests to ensure the quality and robustness of the code at various stages of the ETL process

- Parallelism in Models: Use of parallelism in the data transformation and loading stages, increasing efficiency and reducing processing time.

- Fire-Forget Messaging: Use of messaging (queue.queue) in the fire-forget model to manage files generated between the transformation and loading stages, ensuring a continuous and efficient data flow.

- Parameter Validation: Sending valid parameters based on the request data source itself, ensuring the integrity and accuracy of the information processed.

- Configuration Management: Use of a configuration module to manage endpoints, retry times and number of attempts, providing flexibility and ease of adjustment.

- Common Module: Implementation of a common module for code reuse across the project, promoting consistency and reducing redundancies.

- Dynamic Views: Generation of views with index.html using nbConvert, based on consolidated data from a Jupyter Notebook that integrates the generated files into a single dataset for exploration and analysis.

# ETL Process:

- Extraction: A single request is made to a specific endpoint to obtain quotes from multiple currencies.
- Transformation: The request response is processed, separating each currency quote and storing it in individual files in Parquet format, facilitating data organization and retrieval.
- Upload: Individual Parquet files are consolidated into a single dataset using a Jupyter Notebook, allowing for comprehensive analysis and valuable insights into currency quotes.

In summary, this project offers a robust and efficient solution for collecting, processing and analyzing currency quote data, using advanced architecture and parallelism techniques to optimize each step of the ETL process.

 <details>
 <summary>Repository structure</summary>

- [`data/`](https://github.com/ivdatahub/data-consumer-api/tree/main/data): Stores raw data in Parquet format.
  - ETH-EUR-1713658884.parquet: Example: Raw data for ETH-EUR quotes. file_name = symbol + extraction unix timestamp
- [`notebooks/`](https://github.com/ivdatahub/data-consumer-api/tree/main/notebooks): Contains the `data_explorer.ipynb` notebook for data exploration.
- [`etl/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl): Contains the project's source code.
  - [`run.py`](https://github.com/ivdatahub/data-consumer-api/blob/main/etl/run.py): Entrypoint of the application
- [`common/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl/common): Library for code reuse and standardization.
  - [`utils/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl/utils)
    - [`logs.py`](https://github.com/ivdatahub/data-consumer-api/blob/main/etl/utils/logs.py): Package for log management.
  - [`common.py`](https://github.com/ivdatahub/data-consumer-api/blob/main/etl/utils/common.py): Package for common code tasks like output directory retrieval or default timestamp.
  - [`logs/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl/common/logs): For storing debug logs.
- [`controller/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl/controller)
  - [`pipeline.py`](https://github.com/ivdatahub/data-consumer-api/blob/main/etl/controller/pipeline.py): Receives data extraction requests and orchestrates ETL models .
- [`models/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl/models):
  - [`extract/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl/models/extract)
    - [`api_data_extractor.py`](https://github.com/ivdatahub/data-consumer-api/blob/main/etl/models/extract/api_data_extractor.py): Receives the parameters from the controller, sends the request and returns in JSON.
  - [`transform/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl/models/transform)
    - [`publisher.py`](https://github.com/ivdatahub/data-consumer-api/blob/main/etl/models/transform/publisher.py): Receives the JSON from the extractor, separates the dictionary by currency and publishes each of them to a queue to be processed individually.
  - [`load/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl/models/load)
    - [`parquet_loader.py`](https://github.com/ivdatahub/data-consumer-api/blob/main/etl/models/load/parquet_loader.py): In a separate thread, receive a new dictionary from queue that the transformer is publishing and generates .parquet files in the default directory.
- [`views/`](https://github.com/ivdatahub/data-consumer-api/tree/main/etl/views): For storing data analysis and visualization.

</details>

 <summary>How to run the application locally</summary>

## Step by Step

Ensure Python 3.10 or higher is installed on your machine

- Clone the repository:

```sh
$ git clone https://github.com/ivdatahub/data-consumer-api.git
```

- Go to directory

```sh
$ cd data-consumer-api
```

- Install dependencies and execute project

```sh
$ poetry install && poetry run python etl/run.py
```

Learn more about [`poetry`](https://python-poetry.org/)

## ETL and Data Analysis Results:

You can see the complete data analysis, the Jupyter Notebook is deployed in [GitHub Pages](https://ivdatahub.github.io/data-consumer-api/)
