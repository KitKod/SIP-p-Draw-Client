from PySide2.QtCore import Slot
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QMainWindow, QHeaderView, QDialog

from SippDrawConf import SippDrawConf
from gui.ui_add_block_dialog import Ui_Add_Block_Dialog
from gui.ui_mainwindow import Ui_MainWindow
from models.SIPpCommands import RecvCommand, SendCommand, PauseCommand, NopCommand
from models.TableBlock import TableBlock
from Control import UIModelController


class AddBlockDialog(QDialog):
    block = None
    insert_to_column = None

    def __init__(self):
        super(AddBlockDialog, self).__init__()
        self.ui = Ui_Add_Block_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox_add_block.accepted.connect(self.slotAccepted)
        self.ui.buttonBox_add_block.rejected.connect(self.slotRejected)

    @Slot()
    def slotAccepted(self):
        print('accept ActionBlock')
        cmd_name = self.ui.comboBox_command.currentText()
        cmd_display_name = self.ui.comboBox_cmd_template.currentText()

        color = 'white'
        if cmd_name == 'send':
            cmd = SendCommand()
            color = 'green'
            self.insert_to_column = SippDrawConf.SEND_CMD_COLUMN
        elif cmd_name == 'recv':
            cmd = RecvCommand()
            color = 'red'
            self.insert_to_column = SippDrawConf.RECV_CMD_COLUMN
        elif cmd_name == 'nop':
            cmd = NopCommand()
            self.insert_to_column = SippDrawConf.ACTION_CMD_COLUMN
        else:
            cmd = PauseCommand()
            self.insert_to_column = SippDrawConf.ACTION_CMD_COLUMN

        if cmd_display_name != 'Empty command':
            # initialize cmd object.
            pass

        self.block = TableBlock(cmd_display_name, cmd)
        self.block.setBackgroundColor(QColor(color))
        self.accept()

    @Slot()
    def slotRejected(self):
        print('accept slotRejected')
        self.block = None
        self.insert_to_column = None
        self.reject()


class MainWindow(QMainWindow):
    ui = None
    uimodel_controller = None
    add_block_dialog = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.uimodel_controller = UIModelController(self.ui)
        self.add_block_dialog = AddBlockDialog()

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
        self.ui.table_constructor.cellClicked.connect(self.slotBlockWasClicked)

    def __initToolBox(self):
        self.ui.toolBox.setCurrentIndex(SippDrawConf.TOOLBOX_COMM_ATTR_PAGE)

    def __initButtons(self):
        self.ui.pushButton_add_block_to_table.clicked.connect(self.slotAddBlockToTable)

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

        # --- Test signals to make edit in blocks (shall be deleted)--------------------------------
        # def test(*args):
        #     print('was printed {}'.format(args))
            # doc = self.ui.texte_content.document()
            # print('is mode ?=', doc.isModified())
            #
            # block = self.ui.table_constructor.currentItem()
            # command = block.command
            #
            # print('cmd={}, trext={}'.format(command, self.ui.texte_content.toPlainText()))
            # command.content = self.ui.texte_content.toPlainText()

        # self.ui.attr_com_start_rtd_LineEdit.editingFinished.connect(test)
        # self.ui.texte_content.textChanged.connect(test)
        # self.ui.attr_com_rtd_spinBox.valueChanged.connect(test)
        # self.ui.attr_com_repeat_rtd_checkBox.stateChanged.connect(test)

        # ------------------------------------------------------------------------------------------

    @Slot()
    def slotAddBlockToTable(self):
        ui = self.ui

        self.add_block_dialog.show()
        self.add_block_dialog.exec_()

        if self.add_block_dialog.result() == self.add_block_dialog.Rejected:
            return

        position_new_row = ui.table_constructor.rowCount()
        ui.table_constructor.insertRow(position_new_row)

        ui.table_constructor.setItem(position_new_row,
                                     self.add_block_dialog.insert_to_column,
                                     self.add_block_dialog.block)

        ui.table_constructor.setCurrentCell(position_new_row,
                                            self.add_block_dialog.insert_to_column)
        ui.table_constructor.cellClicked.emit(position_new_row,
                                              self.add_block_dialog.insert_to_column)

    @Slot()
    def slotBlockWasClicked(self, row, column):
        print("slotBlockWasClicked(): Row %d and Column %d was clicked" % (row, column))
        block = self.ui.table_constructor.currentItem()
        self.uimodel_controller.displayCommandDataInAttrPages(block.command)
