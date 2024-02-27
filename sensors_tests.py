import unittest
import sensors_main
from unittest.mock import patch

class TestIntegration(unittest.TestCase):
    @patch('builtins.print')
    def test_integration_check_limits(self, mock_print):
        # Set up
        sys.argv = ['sensors_main.py', '18', '22']  # Command line parameters
        expected_output = "21.2, 18.2, 18.2, 22.2\n-5.0, -4.2, -3.9, -4.5\n1.2, 0.0, 0.5, -0.8, -1.0\n25.0, -4.2, -13.9, 4.5\n"
        
        # Execution
        sensors_main.main()
        output = mock_print.call_args[0][0]

        # Assertion
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
