
from PyQt5.QtWidgets import QMainWindow

from ui.main_window import Ui_MainWindow


class PDWindow(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(PDWindow, self). __init__()

        self.setupUi(self)

        self.show()
