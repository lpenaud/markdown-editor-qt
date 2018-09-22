
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    """docstring for MainWindow."""
    def __init__(self, title, min_x, min_y):
        super(MainWindow, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(QSize(min_x, min_y))
