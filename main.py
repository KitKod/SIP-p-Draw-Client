import sys

from PySide2.QtCore import Slot
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QApplication, QMainWindow, QHeaderView

from SippDrawConf import getMainWindow, getUI
from gui.ui_mainwindow import Ui_MainWindow
from gui.TableBlock import TableBlock
from models.SIPpCommands import SendCommand, RecvCommand, NopCommand
from slots import slotAddRecvCommand, slotBlockWasClicked


@Slot()
def addItemToTable(button_name):
    ui = getUI()
    pos = ui.table_constructor.rowCount()
    ui.table_constructor.insertRow(pos)

    if 'pushButton_add_recv' in button_name:
        item = TableBlock('200 OK', RecvCommand())
        item.setBackgroundColor(QColor('red'))
        ui.table_constructor.setItem(pos, 0, item)
    elif 'pushButton_add_send' in button_name:
        item = TableBlock('INVITE', SendCommand())
        item.setBackgroundColor(QColor('green'))
        ui.table_constructor.setItem(pos, 2, item)
    else:
        item = TableBlock('Nop', NopCommand())
        item.setBackgroundColor(QColor('white'))
        ui.table_constructor.setItem(pos, 1, item)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__initChildWidgets()

    def __initChildWidgets(self):
        self.__initConstructorTable()
        self.__initToolBox()
        self.__initButtons()

    def __initConstructorTable(self):
        self.ui.table_constructor.setColumnCount(3)
        self.ui.table_constructor.setHorizontalHeaderLabels(('recv', 'action', 'send'))
        header = self.ui.table_constructor.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table_constructor.cellClicked.connect(slotBlockWasClicked)

    def __initToolBox(self):
        self.ui.toolBox.setCurrentIndex(0)

    def __initButtons(self):
        self.ui.pushButton_add_recv.clicked.connect(slotAddRecvCommand)
        self.ui.pushButton_add_send.clicked.connect(
            lambda: addItemToTable(self.ui.pushButton_add_send.objectName()))
        self.ui.pushButton_add_action.clicked.connect(
            lambda: addItemToTable(self.ui.pushButton_add_action.objectName()))

        self.ui.attr_com_rtd_spinBox.setSpecialValueText('-')
        self.ui.attr_com_chance_doubleSpinBox.setSpecialValueText('-')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    getMainWindow().show()
    sys.exit(app.exec_())

