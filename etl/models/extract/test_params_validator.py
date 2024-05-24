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
    validator = ParamsValidator(valid_params)
    valid = validator.valid_params_for_call()
    assert validator.params == valid_params
    assert valid_params == valid


def test_invalid_params(invalid_params):
    validator = ParamsValidator(invalid_params)
    with pytest.raises(KeyError):
        validator.valid_params_for_call()


def test_mixed_params(mixed_params, valid_params):
    validator = ParamsValidator(mixed_params)
    validated = validator.valid_params_for_call()
    assert validator.params == mixed_params
    assert validated == valid_params
