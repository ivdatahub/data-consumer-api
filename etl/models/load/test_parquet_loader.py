from etl.models.load.parquet_loader import ParquetLoader


def test_load_to_parquet():
    # Create a sample item
    item = {"code": "USD", "codein": "BRL", "value": 5.0}

    # Call the load method
    extracted_files = ParquetLoader.run(item)

    # Assert that the extracted_files list contains the expected file path
    assert len(extracted_files) == 1

    for extracted_file in extracted_files:
        assert extracted_file.startswith("USD-")
        assert extracted_file.endswith(".parquet")
