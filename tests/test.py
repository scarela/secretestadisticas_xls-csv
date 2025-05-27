import unittest
import os
import subprocess

def read_file_strip(filename):
    with open(filename, 'r') as f:
        # Read all lines, strip trailing whitespace
        return [line.rstrip() for line in f.readlines()]

class TestCSVOutput(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Run the CLI app to generate the CSVs in the tests directory
        subprocess.run(['python', '../cli_app.py', 'gamestats.xls'], cwd=os.path.dirname(__file__), check=True)

    def test_visitor_csv(self):
        expected = read_file_strip(os.path.join(os.path.dirname(__file__), 'visitor.test.csv'))
        result = read_file_strip(os.path.join(os.path.dirname(__file__), 'visitor.csv'))
        self.assertEqual(result, expected, 'visitor.csv does not match visitor.test.csv')

    def test_home_csv(self):
        expected = read_file_strip(os.path.join(os.path.dirname(__file__), 'home.test.csv'))
        result = read_file_strip(os.path.join(os.path.dirname(__file__), 'home.csv'))
        self.assertEqual(result, expected, 'home.csv does not match home.test.csv')

if __name__ == '__main__':
    unittest.main()