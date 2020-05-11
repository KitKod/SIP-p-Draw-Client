from PySide2.QtCore import Slot
from PySide2.QtGui import QColor

from SippDrawConf import getUI
from gui.TableBlock import TableBlock
from models.SIPpCommands import RecvCommand


@Slot()
def slotAddRecvCommand():
    print('called - slotAddRecvCommand()')
    ui = getUI()

    position_new_row = ui.table_constructor.rowCount()
    ui.table_constructor.insertRow(position_new_row)

    block = TableBlock('NotConfigured', RecvCommand())

    block.command.crlf = True
    block.command.test = 'It is so cool :) I love QT!'

    block.setBackgroundColor(QColor('red'))
    ui.table_constructor.setItem(position_new_row, 0, block)

    ui.table_constructor.setCurrentCell(position_new_row, 0)
    ui.table_constructor.cellClicked.emit(position_new_row, 0)


@Slot()
def slotBlockWasClicked(row, column):
    print("slotBlockWasClicked(): Row %d and Column %d was clicked" % (row, column))

    ui = getUI()
    block = ui.table_constructor.currentItem()
    command = block.command

    attr_com_start_rtd = '' if command.start_rtd is None else command.start_rtd
    attr_com_rtd = '-' if command.rtd is None else command.rtd
    attr_com_chance = '-' if command.chance is None else command.chance
    attr_com_next = '' if command.next is None else command.next
    attr_com_test = '' if command.test is None else command.test
    attr_com_condexec = '' if command.condexec is None else command.condexec
    attr_com_counter = '' if command.counter is None else command.counter
    attr_com_repeat_rtd = command.repeat_rtd
    attr_com_crlf = command.crlf
    attr_com_condexec_inverse = command.condexec_inverse

    print('rtd={}, chng={}'.format(attr_com_rtd, attr_com_chance))
    # if isinstance(attr_com_rtd, str):
    #     print('seted')
    #     ui.attr_com_rtd_spinBox.setSpecialValueText(attr_com_rtd)
    # else:
    #     ui.attr_com_rtd_spinBox.setValue(attr_com_rtd)
    #
    # if isinstance(attr_com_chance, str):
    #     ui.attr_com_chance_doubleSpinBox.setSpecialValueText(attr_com_chance)
    # else:
    #     ui.attr_com_chance_doubleSpinBox.setValue(attr_com_chance)

    ui.attr_com_rtd_spinBox.setValue(-1)
    ui.attr_com_chance_doubleSpinBox.setValue(-1)

    ui.attr_com_start_rtd_LineEdit.setText(attr_com_start_rtd)
    ui.attr_com_next_LineEdit.setText(attr_com_next)
    ui.attr_com_test_LineEdit.setText(attr_com_test)
    ui.attr_com_condexec_LineEdit.setText(attr_com_condexec)
    ui.attr_com_counter_LineEdit.setText(attr_com_counter)

    ui.attr_com_repeat_rtd_checkBox.setChecked(attr_com_repeat_rtd)
    ui.attr_com_crlf_checkBox.setChecked(attr_com_crlf)
    ui.attr_com_condexec_inverse_checkBox.setChecked(attr_com_condexec_inverse)

    if isinstance(command, RecvCommand):
        pass





