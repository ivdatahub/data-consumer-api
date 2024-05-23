import pytest
from etl.models.load.parquet_loader import load


def test_load_to_parquet():
    # Create a sample item
    item = {"code": "USD", "codein": "BRL", "value": 5.0}

    # Instantiate the loadToParquet class
    loader = load(item)

    # Call the load method
    extracted_files = loader.run()

    # Assert that the extracted_files list contains the expected file path
    assert len(extracted_files) == 1

    for extracted_file in extracted_files:
        assert extracted_file.startswith("USD-")
        assert extracted_file.endswith(".parquet")
