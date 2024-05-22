import pytest
import requests
from etl.main import GenerateRandomParams


def test_generate_random_params():
    # Mock the response from the API
    mock_response = ["param1", "param2", "param3", "param4", "param5"]
    requests.get = lambda url: MockResponse(mock_response)

    params_qty = 3
    result = GenerateRandomParams(params_qty)

    assert isinstance(result, list)
    assert len(result) == params_qty - 1
    assert all(param in mock_response for param in result)


class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data
