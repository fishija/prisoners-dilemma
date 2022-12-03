from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

import sys

from src.pd import PDWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app_icon = QIcon('res/logger_icon.ico')
    # app.setWindowIcon(app_icon)

    main_window = PDWindow()
    print("cos")
    sys.exit(app.exec_())
