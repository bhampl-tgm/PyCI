"""
Script for controlling the program
"""
from PyCSVModel import PyCSVModel


class PyCSVController:
    """
    Class for controlling the program
    """
    def __init__(self, csvpath=None):
        """
        Constructor for initialising the program
        :param csvpath: the path of the csv
        """
        self.pycsvguimodel = PyCSVModel(csvpath=csvpath)
        self.pycsvguimodel.read_file()
