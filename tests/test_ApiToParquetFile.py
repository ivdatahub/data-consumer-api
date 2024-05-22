# import pytest
# from etl.models.extract.ApiToParquetFile import extraction

# def test_extraction_init():
#     params = ["param1", "param2", "param3"]
#     ext = extraction(params)
#     assert ext.ValidParams == params

# def test_extraction_run_success():
#     params = ["param1", "param2", "param3"]
#     ext = extraction(params)
#     json_data = ext.__run__(ext.ValidParams)
#     assert isinstance(json_data, dict)

# def test_extraction_run_failure():
#     params = ["param1", "param2", "param3"]
#     ext = extraction(params)
#     ext.ValidParams = []
#     json_data = ext.__run__(ext.ValidParams)
#     assert json_data == {}