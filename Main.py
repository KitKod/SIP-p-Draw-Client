import sys

from PySide2.QtWidgets import QApplication

from SippDrawConf import getMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    getMainWindow().show()
    sys.exit(app.exec_())
