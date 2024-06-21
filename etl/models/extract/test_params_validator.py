import pytest
from etl.models.extract.params_validator import ParamsValidator


@pytest.fixture
def valid_params() -> list:
    return ["BRL-COP", "BRL-PEN"]


@pytest.fixture
def invalid_params() -> list:
    return ["param1", "param2"]


@pytest.fixture
def mixed_params():
    return ["BRL-COP", "BRL-PEN", "param1", "param2"]


def test_valid_params(valid_params):
    valid = ParamsValidator.valid_params_for_call(valid_params)
    assert valid_params == valid


def test_invalid_params(invalid_params):
    with pytest.raises(KeyError):
        ParamsValidator.valid_params_for_call(invalid_params)


def test_mixed_params(mixed_params, valid_params):
    validated = ParamsValidator.valid_params_for_call(mixed_params)
    assert validated == valid_params
