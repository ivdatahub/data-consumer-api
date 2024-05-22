import pytest
from etl.models.extract.ParamsValidator import ParamsValidator


def test_params_validator_invalid_params():
    params = ["param1", "param2", "param3"]
    with pytest.raises(KeyError):
        ParamsValidator(params)


def test_params_validator_two_valid_params_for_call():
    params = ["USD-BRL", "INVALID_PARAM", "CAD-BRL"]
    validator = ParamsValidator(params)
    valid_params = validator.__ValidParamsForCall__()
    # Garantindo os parametros validos
    assert valid_params == ["USD-BRL", "CAD-BRL"]
    # Garantindo que os parametros validos estão no atributo validParams
    assert validator.validParams == valid_params


def test_params_validator_all_valid_params_for_call():
    params = ["USD-BRL", "CAD-BRL"]
    validator = ParamsValidator(params)
    assert validator.validParams == params
