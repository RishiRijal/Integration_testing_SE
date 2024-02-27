import sensors_main
import unittest
from unittest.mock import patch
import sys

class TestIntegration(unittest.TestCase):

    @patch('builtins.print')
    def test_integration_check_limits(self, mock_print):
        sys.argv = ['sensors_main.py', '16', '16']
        expected_output = "Error: Incorrect command line arguments.\n"
        
        sensors_main.main()
        output = mock_print.call_args[0][0]

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
