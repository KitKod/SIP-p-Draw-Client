import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QHeaderView

from SippDrawConf import getMainWindow, SippDrawConf
from gui.ui_mainwindow import Ui_MainWindow
from slots import slotAddRecvCommand, slotAddSendCommand, slotAddActionCommand, slotBlockWasClicked


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
        self.__initInputWidgets()

    def __initConstructorTable(self):
        self.ui.table_constructor.setColumnCount(SippDrawConf.COUNT_OF_COLUMN)
        self.ui.table_constructor.setHorizontalHeaderLabels(SippDrawConf.COLUMN_HEADERS)
        header = self.ui.table_constructor.horizontalHeader()
        header.setSectionResizeMode(SippDrawConf.RECV_CMD_COLUMN, QHeaderView.Stretch)
        header.setSectionResizeMode(SippDrawConf.ACTION_CMD_COLUMN, QHeaderView.Stretch)
        header.setSectionResizeMode(SippDrawConf.SEND_CMD_COLUMN, QHeaderView.Stretch)
        self.ui.table_constructor.cellClicked.connect(slotBlockWasClicked)

    def __initToolBox(self):
        self.ui.toolBox.setCurrentIndex(SippDrawConf.TOOLBOX_COMM_ATTR_PAGE)

    def __initButtons(self):
        self.ui.pushButton_add_recv.clicked.connect(slotAddRecvCommand)
        self.ui.pushButton_add_send.clicked.connect(slotAddSendCommand)
        self.ui.pushButton_add_action.clicked.connect(slotAddActionCommand)

    def __initInputWidgets(self):
        self.ui.attr_com_rtd_spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr_com_chance_doubleSpinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr_retrans_spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr_lost_send_spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)

        self.ui.attr_response_spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr_lost_spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr_timeout_spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)

        self.ui.attr_milliseconds_spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr_variable_spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    getMainWindow().show()
    sys.exit(app.exec_())

