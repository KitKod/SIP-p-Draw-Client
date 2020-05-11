import sys

from PySide2.QtCore import Slot
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QApplication, QMainWindow

from SippDrawConf import getMainWindow, getUI
from gui.ui_mainwindow import Ui_MainWindow
from gui.TableBlock import TableBlock


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def myInvestigationOfUIWidgets():
    ui = getUI()
    ui.table_constructor.setColumnCount(3)
    ui.table_constructor.setHorizontalHeaderLabels(('recv', 'action', 'send'))

    def cell_was_clicked(row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = ui.table_constructor.currentItem()
        print(type(item))
        if item is None:
            return

    @Slot()
    def addItemToTable(button_name):
        pos = ui.table_constructor.rowCount()
        ui.table_constructor.insertRow(pos)

        if 'pushButton_add_recv' in button_name:
            item = TableBlock('200 OK', None)
            item.setBackgroundColor(QColor('red'))
            ui.table_constructor.setItem(pos, 0, item)
        elif 'pushButton_add_send' in button_name:
            item = TableBlock('INVITE', None)
            item.setBackgroundColor(QColor('green'))
            ui.table_constructor.setItem(pos, 2, item)
        else:
            item = TableBlock('Nop', None)
            item.setBackgroundColor(QColor('white'))
            ui.table_constructor.setItem(pos, 1, item)

    ui.table_constructor.cellClicked.connect(cell_was_clicked)

    ui.pushButton_add_recv.clicked.connect(lambda: addItemToTable(ui.pushButton_add_recv.objectName()))
    ui.pushButton_add_send.clicked.connect(lambda: addItemToTable(ui.pushButton_add_send.objectName()))
    ui.pushButton_add_action.clicked.connect(
        lambda: addItemToTable(ui.pushButton_add_action.objectName()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myInvestigationOfUIWidgets()

    getMainWindow().show()
    sys.exit(app.exec_())

