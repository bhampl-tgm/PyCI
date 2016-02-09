import csv
from _csv import Error


class PyCSVModel:
    def __init__(self, csvpath=None):
        self.csvpath = csvpath
        self.data = []
        self.columns = []

    def read_file(self):

        with open(self.csvpath) as csvfile:
            try:
                dialect = csv.Sniffer().sniff(csvfile.read(1024))
                csvfile.seek(0)
                reader = csv.DictReader(csvfile, dialect=dialect)
                for row in reader:
                    # print(row)
                    self.data.append(row)
            except Error:
                raise ValueError('Wrong csv delimiter or empty file') from None
