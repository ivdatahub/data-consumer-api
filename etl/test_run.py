from unittest.mock import patch
from etl.run import main


@patch("etl.run.PipelineExecutor", autospec=True)
def test_main(mock_pipeline_executor):
    main()
    mock_executor_instance = mock_pipeline_executor.return_value
    mock_pipeline_executor.assert_called_once_with("USD-BRL")
    mock_executor_instance.pipeline_run.assert_called_once()
