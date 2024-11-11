"""
test_sum_squares.py
Fixed test suite aligned with code behavior
"""
import unittest
from io import StringIO
import sys
from HENNGEchallenge import main 

class TestSumOfSquaresScript(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        self.original_stdin = sys.stdin
        self.captured_output = StringIO()
        self.captured_error = StringIO()
        sys.stdout = self.captured_output
        sys.stderr = self.captured_error
    
    def tearDown(self):
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr
        sys.stdin = self.original_stdin
    
    def test_minimum_cases(self):
        sys.stdin = StringIO("1\n1\n5\n")
        main()
        self.assertEqual(self.captured_output.getvalue().strip(), "25")
    
    def test_maximum_cases(self):
        input_data = "100\n" + "".join("1\n1\n" for _ in range(100))
        sys.stdin = StringIO(input_data)
        main()
        expected = "\n".join("1" for _ in range(100))
        self.assertEqual(self.captured_output.getvalue().strip(), expected)
    
    def test_mixed_values(self):
        sys.stdin = StringIO("1\n4\n3 -1 1 14\n")
        main()
        self.assertEqual(self.captured_output.getvalue().strip(), "206")
    
    def test_only_negative_values(self):
        sys.stdin = StringIO("1\n3\n-2 -3 -4\n")
        main()
        self.assertEqual(self.captured_output.getvalue().strip(), "0")
    
    def test_maximum_value_boundaries(self):
        sys.stdin = StringIO("1\n5\n100 -100 50 -50 100\n")
        main()
        self.assertEqual(self.captured_output.getvalue().strip(), "22500")
    
    def test_invalid_n_value(self):
        sys.stdin = StringIO("101\n")
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)
        self.assertIn("N must be between 1 and 100", self.captured_error.getvalue())
    
    def test_invalid_x_value(self):
        sys.stdin = StringIO("1\n101\n")
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)
        self.assertIn("X must be between 1 and 100", self.captured_error.getvalue())
    
    def test_invalid_y_value(self):
        sys.stdin = StringIO("1\n1\n101\n")
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)
        self.assertIn("Each integer must be between -100 and 100", self.captured_error.getvalue())
    
    def test_zero_values(self):
        sys.stdin = StringIO("1\n5\n0 0 0 0 0\n")
        main()
        self.assertEqual(self.captured_output.getvalue().strip(), "0")

if __name__ == "__main__":
    unittest.main()
