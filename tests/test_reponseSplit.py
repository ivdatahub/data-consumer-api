# import pytest
# from etl.models.transform.ResponseSplit import transformation

# @pytest.fixture
# def json_response():
#     return {
#         "param1": {"key1": "value1"},
#         "param2": {"key2": "value2"},
#         "param3": {"key3": "value3"}
#     }

# @pytest.fixture
# def valid_params():
#     return ["param1", "param2", "param3"]

# def test_transformation_process_param(json_response, valid_params):
#     # Create an instance of the transformation class
#     transform = transformation(json_response, valid_params)

#     # Assert that the extracted_files list is populated correctly
#     assert transform.extracted_files == [
#         "/path/to/output/param1-20220101.parquet",
#         "/path/to/output/param2-20220101.parquet",
#         "/path/to/output/param3-20220101.parquet"
#     ]

#     # Assert that the number of extracted files is correct
#     assert len(transform.extracted_files) == 3

#     # Assert that the files are written in the correct format
#     assert transform.extracted_files[0].endswith(".parquet")
#     assert transform.extracted_files[1].endswith(".parquet")
#     assert transform.extracted_files[2].endswith(".parquet")