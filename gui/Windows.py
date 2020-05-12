from PySide2.QtWidgets import QMainWindow, QHeaderView, QDialog

from SippDrawConf import SippDrawConf
from Slots import slotAddRecvCommand, slotAddSendCommand, slotAddActionCommand, slotBlockWasClicked
from gui.ui_mainwindow import Ui_MainWindow
from gui.ui_add_block_dialog import Ui_Add_Block_Dialog
from models.SIPpCommands import PauseCommand, NopCommand


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


class AddBlockDialog(QDialog):

    action_cmd = None
    action_template = None
    recv_send_template = None
    opened_page = 0

    def __init__(self):
        super(AddBlockDialog, self).__init__()
        self.ui = Ui_Add_Block_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox_action_block.accepted.connect(self.slotActionBlockAccepted)
        self.ui.buttonBox_action_block.rejected.connect(self.slotActionBlockRejected)

        self.ui.buttonBox_recv_send_block.accepted.connect(self.slotRecvSendBlockAccepted)
        self.ui.buttonBox_recv_send_block.rejected.connect(self.slotRecvSendBlockRejected)

    def slotActionBlockAccepted(self):
        print('accept 1 it')
        cmd = self.ui.comboBox_command_action_block.currentText()
        template = self.ui.comboBox_template_action_block.currentText()

        if cmd == 'nop':
            self.action_cmd = NopCommand()
        else:
            self.action_cmd = PauseCommand()

        if template != 'Empty command':
            # initialize cmd object.
            pass
        self.accept()

    def slotRecvSendBlockAccepted(self):
        print('accept 2 it')
        template = self.ui.comboBox_template_recv_send_block.currentText()

        if template != 'Empty command':
            # initialize cmd object.
            pass
        self.accept()

    def slotActionBlockRejected(self):
        print('close it')
        self.reject()

    def slotRecvSendBlockRejected(self):
        print('close it')
        self.reject()

    def setPageToShow(self, pindex):
        if pindex < 0 or pindex > self.ui.stackedw_add_block_dialog.count() - 1:
            raise ValueError('Incorrect ({}) index of stackwidget page!'.format(pindex))
        self.ui.stackedw_add_block_dialog.setCurrentIndex(pindex)
