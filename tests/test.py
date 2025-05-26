import unittest
import os

def read_file_strip(filename):
    with open(filename, 'r') as f:
        # Read all lines, strip trailing whitespace
        return [line.rstrip() for line in f.readlines()]

class TestCSVOutput(unittest.TestCase):
    def test_visitor_csv(self):
        expected = read_file_strip('tests/visitor.test.csv')
        result = read_file_strip('visitor.csv')
        self.assertEqual(result, expected, 'visitor.csv does not match visitor.test.csv')

    def test_home_csv(self):
        expected = read_file_strip('tests/home.test.csv')
        result = read_file_strip('home.csv')
        self.assertEqual(result, expected, 'home.csv does not match home.test.csv')

if __name__ == '__main__':
    unittest.main()