import os
from PySide2.QtCore import Slot, Qt, QSize

from PySide2.QtGui import QColor, QIcon
from PySide2.QtWidgets import QMainWindow, QHeaderView, QDialog, QLineEdit, QSpinBox, QCheckBox,\
    QComboBox, QTextEdit, QDoubleSpinBox, QMenu, QFileDialog

from SippDrawConf import SippDrawConf
from gui.ui_add_block_dialog import Ui_Add_Block_Dialog
from gui.ui_mainwindow import Ui_MainWindow
from gui.ui_run_scenario import Ui_Run_Scenario
from models.SIPpCommands import RecvCommand, SendCommand, PauseCommand, NopCommand
from models.TableBlock import TableBlock
from Control import UIModelController, TestScenarioExecutionController
from TestScenario import TestScenario


class RunScenarioDialog(QDialog):

    def __init__(self, main_ui, test_scenario):
        super(RunScenarioDialog, self).__init__()
        self.ui = Ui_Run_Scenario()
        self.main_ui = main_ui
        self.test_scenario = test_scenario
        self.ui.setupUi(self)

        self.ui.run_button.clicked.connect(self.runButtonClicked)
        self.ui.stop_button.clicked.connect(self.stopButtonClicked)
        self.ui.cancel_Button.clicked.connect(self.cancelButtonClicked)

        self.ui.buttons_stackedWidget.setCurrentIndex(0)

        for cl in range(SippDrawConf.COUNT_OF_COLUMN):
            block = self.main_ui.table_constructor.item(0, cl)
            if block is not None:
                if isinstance(block.command, SendCommand):
                    self.ui.input_stackedWidget.setCurrentIndex(0)
                else:
                    self.ui.input_stackedWidget.setCurrentIndex(1)

    @Slot()
    def runButtonClicked(self):
        # this data was got from UI to UAC scenario
        remote_ip_stab = '192.168.243.148'
        remote_service_stab = '123004'

        executor = TestScenarioExecutionController(self.ui,
                                                   self.test_scenario.path_to_file,
                                                   remote_ip = remote_ip_stab,
                                                   service = remote_service_stab)
        executor.run()

    @Slot()
    def stopButtonClicked(self):
        pass

    @Slot()
    def cancelButtonClicked(self):
        self.reject()


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
        print('NEW WINDOW')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.opened_test_scenario = TestScenario()
        self.uimodel_controller = UIModelController(self.ui)
        self.add_block_dialog = AddBlockDialog()

        self.__initChildWidgets()

    def __initChildWidgets(self):
        self.__initConstructorTable()
        self.__initToolBox()
        self.__initButtons()
        self.__initInputWidgets()
        self.ui.statusbar.showMessage('Scenario: {}'.format(self.opened_test_scenario.name))

    def __initConstructorTable(self):
        self.ui.table_constructor.setColumnCount(SippDrawConf.COUNT_OF_COLUMN)
        self.ui.table_constructor.setHorizontalHeaderLabels(SippDrawConf.COLUMN_HEADERS)
        header = self.ui.table_constructor.horizontalHeader()
        header.setSectionResizeMode(SippDrawConf.RECV_CMD_COLUMN, QHeaderView.Stretch)
        header.setSectionResizeMode(SippDrawConf.ACTION_CMD_COLUMN, QHeaderView.Stretch)
        header.setSectionResizeMode(SippDrawConf.SEND_CMD_COLUMN, QHeaderView.Stretch)

        self.ui.table_constructor.cellClicked.connect(self.slotBlockWasClicked)
        self.ui.table_constructor.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.table_constructor.customContextMenuRequested.connect(self.slotContextMenuRequested)

    def __initToolBox(self):
        self.ui.toolBox.setCurrentIndex(SippDrawConf.TOOLBOX_COMM_ATTR_PAGE)

    def __initButtons(self):
        action_run_icon = QIcon()
        action_new_scenario_icon = QIcon()
        action_open_icon = QIcon()
        action_save_icon = QIcon()

        action_run_icon.addFile(u"resources/run_scenario.png", QSize(), QIcon.Normal, QIcon.Off)
        action_new_scenario_icon.addFile(u"resources/new_file.png", QSize(), QIcon.Normal, QIcon.Off)
        action_open_icon.addFile(u"resources/open.png", QSize(), QIcon.Normal, QIcon.Off)
        action_save_icon.addFile(u"resources/save.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.action_run.setIcon(action_run_icon)
        self.ui.action_new_scenario.setIcon(action_new_scenario_icon)
        self.ui.action_open.setIcon(action_open_icon)
        self.ui.action_save.setIcon(action_save_icon)

        self.ui.action_save.triggered.connect(self.slotActionExportClicked)
        self.ui.action_open.triggered.connect(self.slotActionOpenClicked)
        self.ui.action_new_scenario.triggered.connect(self.slotActionNewScenarioClicked)
        self.ui.action_run.triggered.connect(self.slotActionRunScenarioClicked)

        self.ui.pushButton_add_block_to_table.clicked.connect(self.slotAddBlockToTable)

    def __initInputWidgets(self):
        self.ui.attr__rtd__spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr__chance__doubleSpinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr__retrans__spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr__lost_send__spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)

        self.ui.attr__response__spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr__lost__spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr__timeout__spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)

        self.ui.attr__milliseconds__spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)
        self.ui.attr__variable__spinBox.setSpecialValueText(SippDrawConf.SPECIAL_VALUE_SPINBOX)

        # Setup slots for edit signals

        # 1 section: common attrs
        self.ui.attr__start_rtd__LineEdit.editingFinished.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.attr__start_rtd__LineEdit))
        self.ui.attr__rtd__spinBox.valueChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__rtd__spinBox, x))
        self.ui.attr__chance__doubleSpinBox.valueChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__chance__doubleSpinBox, x))
        self.ui.attr__next__LineEdit.editingFinished.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.attr__next__LineEdit))
        self.ui.attr__test__LineEdit.editingFinished.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.attr__test__LineEdit))
        self.ui.attr__condexec__LineEdit.editingFinished.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.attr__condexec__LineEdit))
        self.ui.attr__counter__LineEdit.editingFinished.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.attr__counter__LineEdit))
        self.ui.attr__repeat_rtd__checkBox.stateChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__repeat_rtd__checkBox, x))
        self.ui.attr__crlf__checkBox.stateChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__crlf__checkBox, x))
        self.ui.attr__condexec_inverse__checkBox.stateChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__condexec_inverse__checkBox, x))

        # 2 section: Specific attrs for recv command
        self.ui.attr__response__spinBox.valueChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__response__spinBox, x))
        self.ui.attr__request__comboBox.currentTextChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__request__comboBox, x))
        self.ui.attr__lost__spinBox.valueChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__lost__spinBox, x))
        self.ui.attr__timeout__spinBox.valueChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__timeout__spinBox, x))
        self.ui.attr__ontimeout__LineEdit.editingFinished.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.attr__ontimeout__LineEdit))
        self.ui.attr__response_txn__LineEdit.editingFinished.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.attr__response_txn__LineEdit))
        self.ui.attr__optional__checkBox.stateChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__optional__checkBox, x))
        self.ui.attr__ignoresdp__checkBox.stateChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__ignoresdp__checkBox, x))
        self.ui.attr__rrs__checkBox.stateChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__rrs__checkBox, x))
        self.ui.attr__auth__checkBox.stateChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__auth__checkBox, x))
        self.ui.attr__regexp_match__checkBox.stateChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__regexp_match__checkBox, x))

        # 2 section: Specific attrs for send command
        self.ui.attr__retrans__spinBox.valueChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__retrans__spinBox, x))
        self.ui.attr__lost_send__spinBox.valueChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__lost_send__spinBox, x))
        self.ui.attr__start_txn__LineEdit.editingFinished.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.attr__start_txn__LineEdit))
        self.ui.attr__ack_txn__LineEdit.editingFinished.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.attr__ack_txn__LineEdit))

        # 2 section: Specific attrs for pause command
        self.ui.attr__milliseconds__spinBox.valueChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__milliseconds__spinBox, x))
        self.ui.attr__variable__spinBox.valueChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__variable__spinBox, x))
        self.ui.attr__distribution__comboBox.currentTextChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__distribution__comboBox, x))
        self.ui.attr__sanity_check__checkBox.stateChanged.connect(
            lambda x: self.slotHandleAttrsEdit(self.ui.attr__sanity_check__checkBox, x))

        # 3 section: Specific content for command
        self.ui.texte__content.textChanged.connect(
            lambda: self.slotHandleAttrsEdit(self.ui.texte__content))

    def __clearTable(self):
        """Deletes all existing rows from the constructor table."""
        model = self.ui.table_constructor.model()
        model.removeRows(0, model.rowCount())

    @Slot()
    def slotHandleAttrsEdit(self, widget, *args):
        command = self.ui.table_constructor.currentItem().command
        attr_name = widget.objectName().split('__')[1]

        new_value = None
        if isinstance(widget, QLineEdit):
            new_value = widget.text()
        elif isinstance(widget, (QComboBox, QSpinBox, QDoubleSpinBox)):
            new_value = args[0]
        elif isinstance(widget, QCheckBox):
            new_value = bool(args[0])
        elif isinstance(widget, QTextEdit):
            new_value = widget.toPlainText()

        if not hasattr(command, attr_name):
            raise AttributeError('The {} attribute is not exist in the {}!'.format(attr_name, command))
        elif new_value is None:
            raise ValueError('Value is not got from widget!')

        print('new_value={}; arr_name={}'.format(new_value, attr_name))

        setattr(command, attr_name, new_value)
        self.opened_test_scenario.saved = False

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
        self.opened_test_scenario.saved = False

    @Slot()
    def slotBlockWasClicked(self, row, column):
        print("slotBlockWasClicked(): Row %d and Column %d was clicked" % (row, column))
        block = self.ui.table_constructor.currentItem()
        self.uimodel_controller.displayCommandDataInAttrPages(block.command)

    @Slot()
    def slotContextMenuRequested(self, position):
        def deleteSelectedRows():
            selected_rows = [item.row() for item in self.ui.table_constructor.selectedItems()]
            for row in selected_rows:
                print(row)
                self.ui.table_constructor.removeRow(row)
            self.opened_test_scenario.saved = False

        menu = QMenu()
        menu.addAction("Delete", deleteSelectedRows)
        menu.addSeparator()
        menu.exec_(self.ui.table_constructor.mapToGlobal(position))

    @Slot()
    def slotActionExportClicked(self, _checked):
        if self.opened_test_scenario.saved:
            return

        if self.opened_test_scenario.path_to_file is None:
            # create new file to save.
            save_as = QFileDialog.getSaveFileName(self, '', os.getenv('HOME'))[0]
            self.opened_test_scenario.path_to_file = save_as
            self.opened_test_scenario.name = save_as.split('/')[-1]
            self.ui.statusbar.showMessage('Scenario: {}'.format(self.opened_test_scenario.name))

        self.opened_test_scenario.loadToFile()
        self.opened_test_scenario.saved = True

    @Slot()
    def slotActionOpenClicked(self, _checked):
        if not self.opened_test_scenario.saved:
            print('Old file not save (has changes)')

        path_to_file = QFileDialog.getOpenFileName(self, '', os.getenv('HOME'), "XML files (*.xml)")[0]
        if not path_to_file:
            return

        self.__clearTable()
        self.opened_test_scenario = TestScenario(path_to_file)
        self.ui.statusbar.showMessage('Scenario: {}'.format(self.opened_test_scenario.name))

    @Slot()
    def slotActionNewScenarioClicked(self, _checked):
        if not self.opened_test_scenario.saved:
            print('Old file not save (has changes)')

        self.opened_test_scenario = TestScenario()
        self.__clearTable()
        self.ui.statusbar.showMessage('Scenario: {}'.format(self.opened_test_scenario.name))

    @Slot()
    def slotActionRunScenarioClicked(self, _checked):
        if not self.opened_test_scenario.saved:
            self.ui.action_save.triggered.emit()

        dialog_w = RunScenarioDialog(self.ui, self.opened_test_scenario)
        dialog_w.show()
        dialog_w.exec_()
