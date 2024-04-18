import sys
import os
import unittest
from unittest.mock import patch

# Add the parent directory to the sys.path
WORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(WORK_DIR))

from etl.main import ExecutePipeline

class TestMain(unittest.TestCase):

    @patch('etl.main.ExecutePipeline')
    def test_main(self, mock_execute_pipeline):
        # Arrange
        expected_source = "USD-BRL"
        expected_target = "USD-BRLT"

        # Act
        ExecutePipeline("USD-BRL", "USD-BRLT")

        # Assert
        mock_execute_pipeline.assert_called_once_with(expected_source, expected_target)

if __name__ == '__main__':
    unittest.main()