from unittest import TestCase

from PyCSVModel import PyCSVModel


class Tests(TestCase):
    def test_read_vsc(self):
        expecteddict = [{'titel': 'TestTitel', 'id': '0', 'content': 'TestContent'}]
        model = PyCSVModel(csvpath='testcsvs/testcsv1.csv')
        model.read_file()
        self.assertEqual(expecteddict, model.data)

    def test_tworows(self):
        expecteddict = [{'titel': 'TestTitel', 'id': '0', 'content': 'TestContent'},
                        {'titel': 'bla', 'id': '1', 'content': 'blub'}]
        model = PyCSVModel(csvpath='testcsvs/testcsv2.csv')
        model.read_file()
        self.assertEqual(expecteddict, model.data)

    def test_only_title(self):
        expecteddict = []
        model = PyCSVModel(csvpath='testcsvs/testcsv3.csv')
        model.read_file()
        self.assertEqual(expecteddict, model.data)

    def test_empty(self):
        with self.assertRaises(ValueError):
            model = PyCSVModel(csvpath='testcsvs/testcsv4.csv')
            model.read_file()

    def test_wrong_delimiter(self):
        with self.assertRaises(ValueError):
            model = PyCSVModel(csvpath='testcsvs/testcsv5.csv')
            model.read_file()
            self.assertEqual([], model.data)
