
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    """docstring for MainWindow."""
    def __init__(self, title, minw, minh):
        super(MainWindow, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(minw, minh)
