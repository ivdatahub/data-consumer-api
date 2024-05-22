import pytest
from etl.models.extract.ApiToParquetFile import extraction


def test_extraction_init():
    params = ["USD-BRL", "USD-BRLT", "CAD-BRL"]
    ext = extraction(params)
    assert ext.ValidParams == params


def test_extraction_run_success():
    params = ["USD-BRL", "USD-BRLT", "CAD-BRL"]
    ext = extraction(params)
    json_data = ext.__run__(ext.ValidParams)
    assert isinstance(json_data, dict)


def test_extraction_run_failure():
    try:
        params = []
        ext = extraction(params)
    except Exception:
        assert pytest.raises(KeyError)
