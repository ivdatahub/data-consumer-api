from etl.models.extract.fromAPI import extraction


def test_extraction_init():
    params = ["USD-BRL", "USD-BRLT", "CAD-BRL"]
    ext = extraction(params)
    assert ext.ValidParams == params


def test_extraction_run_success():
    params = ["USD-BRL", "USD-BRLT", "CAD-BRL"]
    ext = extraction(params)
    json_data = ext.__run__(ext.ValidParams)
    assert isinstance(json_data, dict)
