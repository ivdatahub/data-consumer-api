from etl.models.extract.api_data_extractor import extraction


def test_extraction_init():
    params = ["USD-BRL", "USD-BRLT", "CAD-BRL"]
    extractor = extraction(params)
    response, valid_params = extractor.run
    assert valid_params == params


def test_extraction_run_success():
    params = ["USD-BRL", "USD-BRLT", "CAD-BRL"]
    extractor = extraction(params)
    response, valid_params = extractor.run
    assert isinstance(response, dict)
