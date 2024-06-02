from etl.models.extract.api_data_extractor import extraction


def test_extraction_constructor():
    params = ["USD-BRL", "USD-BRLT", "CAD-BRL"]
    extractor = extraction(params)
    assert extractor.params == params
