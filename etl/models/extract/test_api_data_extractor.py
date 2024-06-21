from etl.models.extract.api_data_extractor import APIExtraction


def test_extraction_constructor():
    params = ["USD-BRL", "USD-BRLT", "CAD-BRL"]
    extractor = APIExtraction.run(params)
    assert extractor[1] == params
