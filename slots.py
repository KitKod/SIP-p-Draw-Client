from PySide2.QtCore import Slot
from PySide2.QtGui import QColor

from SippDrawConf import getUI
from gui.TableBlock import TableBlock
from models.SIPpCommands import RecvCommand, SendCommand, NopCommand, PauseCommand


@Slot()
def slotAddRecvCommand():
    print('called - slotAddRecvCommand()')
    ui = getUI()

    position_new_row = ui.table_constructor.rowCount()
    ui.table_constructor.insertRow(position_new_row)

    block = TableBlock('NotConfigured', RecvCommand())

    block.command.crlf = True
    block.command.test = 'It is so cool :) I love QT!'
    block.command.request = 'OPTIONS'

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

    ui.attr_com_rtd_spinBox.setValue(command.rtd)
    ui.attr_com_chance_doubleSpinBox.setValue(command.chance)

    ui.attr_com_start_rtd_LineEdit.setText(command.start_rtd)
    ui.attr_com_next_LineEdit.setText(command.next)
    ui.attr_com_test_LineEdit.setText(command.test)
    ui.attr_com_condexec_LineEdit.setText(command.condexec)
    ui.attr_com_counter_LineEdit.setText(command.counter)

    ui.attr_com_repeat_rtd_checkBox.setChecked(command.repeat_rtd)
    ui.attr_com_crlf_checkBox.setChecked(command.crlf)
    ui.attr_com_condexec_inverse_checkBox.setChecked(command.condexec_inverse)

    if isinstance(command, RecvCommand):
        ui.stackedw_spec_attrs.setCurrentIndex(0)

        ui.attr_request_comboBox.setCurrentText(command.request)

        ui.attr_response_spinBox.setValue(command.response)
        ui.attr_lost_spinBox.setValue(command.lost)
        ui.attr_timeout_spinBox.setValue(command.timeout)

        ui.attr_ontimeout_LineEdit.setText(command.ontimeout)
        ui.attr_response_txn_LineEdit.setText(command.response_txn)

        ui.attr_optional_checkBox.setChecked(command.optional)
        ui.attr_ignoresdp_checkBox.setChecked(command.ignoresdp)
        ui.attr_rrs_checkBox.setChecked(command.rrs)
        ui.attr_auth_checkBox.setChecked(command.auth)
        ui.attr_regexp_match_checkBox.setChecked(command.regexp_match)
    elif isinstance(command, SendCommand):
        ui.stackedw_spec_attrs.setCurrentIndex(1)

        ui.attr_retrans_spinBox.setValue(command.retrans)
        ui.attr_lost_send_spinBox.setValue(command.lost)

        ui.attr_start_txn_LineEdit.setText(command.start_txn)
        ui.attr_ack_txn_LineEdit.setText(command.ack_txn)
    elif isinstance(command, PauseCommand):
        ui.stackedw_spec_attrs.setCurrentIndex(2)

        ui.attr_milliseconds_spinBox.setValue(command.milliseconds)
        ui.attr_variable_spinBox.setValue(command.variable)

        ui.attr_distribution_comboBox.setCurrentText(command.distribution)

        ui.attr_sanity_check_checkBox.setChecked(command.sanity_check)
    else:
        ui.stackedw_spec_attrs.setCurrentIndex(3)





