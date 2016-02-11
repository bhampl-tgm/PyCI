"""
Script for testing PyCSV
"""
from unittest import TestCase
from PyCSVModel import PyCSVModel


class Tests(TestCase):
    """
    Test class of PyCSV
    """
    def test_read_csv(self):
        """
        Testing of a successful csv read
        """
        expecteddict = [{'titel': 'TestTitel', 'id': '0', 'content': 'TestContent'}]
        model = PyCSVModel(csvpath='testcsvs/testcsv1.csv')
        model.read_file()
        self.assertEqual(expecteddict, model.data)

    def test_tworows(self):
        """
        Testing of a successful csv read with two rows
        """
        expecteddict = [{'titel': 'TestTitel', 'id': '0', 'content': 'TestContent'},
                        {'titel': 'bla', 'id': '1', 'content': 'blub'}]
        model = PyCSVModel(csvpath='testcsvs/testcsv2.csv')
        model.read_file()
        self.assertEqual(expecteddict, model.data)

    def test_only_title(self):
        """
        Testing of a csv file with only a title
        """
        expecteddict = []
        model = PyCSVModel(csvpath='testcsvs/testcsv3.csv')
        model.read_file()
        self.assertEqual(expecteddict, model.data)

    def test_empty(self):
        """
        Testing of a empty csv
        """
        with self.assertRaises(ValueError):
            model = PyCSVModel(csvpath='testcsvs/testcsv4.csv')
            model.read_file()

    def test_wrong_delimiter(self):
        """
        Testing a csv with wrong delimiter
        """
        with self.assertRaises(ValueError):
            model = PyCSVModel(csvpath='testcsvs/testcsv5.csv')
            model.read_file()
            self.assertEqual([], model.data)
