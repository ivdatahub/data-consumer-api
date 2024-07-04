import pytest
from etl.models.transform.publisher import ResponseTransformation
import queue

fila = queue.Queue()


@pytest.fixture
def json_response() -> dict:
    return {
        "BRLCOP": {
            "code": "BRL",
            "codein": "COP",
            "name": "Real Brasileiro/Peso Colombiano",
            "high": "746.23",
            "low": "741.33",
            "varBid": "-8.36",
            "pctChange": "-1.11",
            "bid": "742.44",
            "ask": "743.12",
            "timestamp": "1716386175",
            "create_date": "2024-05-22 10:56:15",
        },
        "BRLPEN": {
            "code": "BRL",
            "codein": "PEN",
            "name": "Real Brasileiro/Sol do Peru",
            "high": "0.7319",
            "low": "0.7253",
            "varBid": "-0.0098",
            "pctChange": "-1.33",
            "bid": "0.7116",
            "ask": "0.7403",
            "timestamp": "1716386118",
            "create_date": "2024-05-22 10:55:18",
        },
    }


@pytest.fixture
def valid_params() -> list:
    return ["BRL-COP", "BRL-PEN"]


def test_transformation_process_param(json_response, valid_params):
    # Create an instance of the transformation class
    transform = ResponseTransformation(json_response, valid_params, fila)
    transform.publish()

    assert fila.qsize() == 2
