from PySide.QtGui import *

from PyCSVModel import PyCSVModel


class PyCSVController(QWidget):
    def __init__(self, parent=None, csvpath=None):
        super().__init__(parent)
        self.pycsvguimodel = PyCSVModel(csvpath=csvpath)
        self.pycsvguimodel.read_file()
