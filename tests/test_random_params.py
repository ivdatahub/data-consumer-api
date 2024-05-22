from etl.main import GenerateRandomParams


def test_generate_random_params():
    params_qty = 3
    result = GenerateRandomParams(params_qty)

    assert isinstance(result, list)
    assert len(result) == params_qty
    # Add more assertions to validate the generated parameters as needed
