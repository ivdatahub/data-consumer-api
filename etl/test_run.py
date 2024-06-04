from unittest.mock import patch
from etl.run import main


@patch("etl.run.PipelineExecutor", autospec=True)
def test_main(MockPipelineExecutor):
    main()
    mock_executor_instance = MockPipelineExecutor.return_value
    MockPipelineExecutor.assert_called_once_with("USD-BRL")
    mock_executor_instance.pipeline_run.assert_called_once()


if __name__ == "__main__":
    test_main()
