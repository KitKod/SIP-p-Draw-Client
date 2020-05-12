from PySide2.QtCore import Slot
from PySide2.QtGui import QColor

from SippDrawConf import getUI, SippDrawConf
from gui.TableBlock import TableBlock
from models.SIPpCommands import RecvCommand, SendCommand, NopCommand, PauseCommand


@Slot()
def slotAddRecvCommand():
    print('called - slotAddRecvCommand()')
    ui = getUI()

    position_new_row = ui.table_constructor.rowCount()
    ui.table_constructor.insertRow(position_new_row)

    block = TableBlock('NotConfigured', RecvCommand())

    # ----------------------------------------------------------------------------------------------
    block.command.crlf = True
    block.command.test = 'It is so cool :) I love QT!'
    block.command.request = 'OPTIONS'
    block.command.content = '''
    <action>
        <ereg regexp="([0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]*"
            search_in="msg"
            check_it="true"
            assign_to="1,2"/>
    </action>
    '''
    # ----------------------------------------------------------------------------------------------

    block.setBackgroundColor(QColor('red'))
    ui.table_constructor.setItem(position_new_row, SippDrawConf.RECV_CMD_COLUMN, block)

    ui.table_constructor.setCurrentCell(position_new_row, SippDrawConf.RECV_CMD_COLUMN)
    ui.table_constructor.cellClicked.emit(position_new_row, SippDrawConf.RECV_CMD_COLUMN)


@Slot()
def slotAddSendCommand():
    print('called - slotAddSendCommand()')
    ui = getUI()

    position_new_row = ui.table_constructor.rowCount()
    ui.table_constructor.insertRow(position_new_row)

    block = TableBlock('NotConfigured', SendCommand())

    # ----------------------------------------------------------------------------------------------
    block.command.crlf = True
    block.command.test = 'Send : It is so cool :) I love QT!'
    block.command.retrans = 2
    block.command.content = '''<![CDATA[
    
      INVITE sip:[service]@[remote_ip]:[remote_port] SIP/2.0
      Via: SIP/2.0/[transport] [local_ip]:[local_port]
      From: sipp <sip:sipp@[local_ip]:[local_port]>;tag=[call_number]
      To: sut <sip:[service]@[remote_ip]:[remote_port]>
      Call-ID: [call_id]
      Cseq: 1 INVITE
      Contact: sip:sipp@[local_ip]:[local_port]
      Max-Forwards: 70
      Subject: Performance Test
      Content-Type: application/sdp
      Content-Length: [len]

      v=0
      o=user1 53655765 2353687637 IN IP[local_ip_type] [local_ip]
      s=-
      t=0 0
      c=IN IP[media_ip_type] [media_ip]
      m=audio [media_port] RTP/AVP 0
      a=rtpmap:0 PCMU/8000

    ]]>
    '''
    # ----------------------------------------------------------------------------------------------

    block.setBackgroundColor(QColor('green'))
    ui.table_constructor.setItem(position_new_row, SippDrawConf.SEND_CMD_COLUMN, block)

    ui.table_constructor.setCurrentCell(position_new_row, SippDrawConf.SEND_CMD_COLUMN)
    ui.table_constructor.cellClicked.emit(position_new_row, SippDrawConf.SEND_CMD_COLUMN)


@Slot()
def slotAddActionCommand():
    print('called - slotAddActionCommand()')
    ui = getUI()

    position_new_row = ui.table_constructor.rowCount()
    ui.table_constructor.insertRow(position_new_row)

    block = TableBlock('NotConfigured', PauseCommand())

    # ----------------------------------------------------------------------------------------------
    block.command.distribution = 'weibull'
    # ----------------------------------------------------------------------------------------------

    block.setBackgroundColor(QColor('white'))
    ui.table_constructor.setItem(position_new_row, SippDrawConf.ACTION_CMD_COLUMN, block)

    ui.table_constructor.setCurrentCell(position_new_row, SippDrawConf.ACTION_CMD_COLUMN)
    ui.table_constructor.cellClicked.emit(position_new_row, SippDrawConf.ACTION_CMD_COLUMN)


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
        ui.stackedw_spec_attrs.setCurrentIndex(SippDrawConf.STACK_SPEC_ATTR_RECV_PAGE)

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

        ui.stackedw_content.setCurrentIndex(SippDrawConf.STACK_CONTENT_PAGE)
        ui.texte_content.setText(command.content)
    elif isinstance(command, SendCommand):
        ui.stackedw_spec_attrs.setCurrentIndex(SippDrawConf.STACK_SPEC_ATTR_SEND_PAGE)

        ui.attr_retrans_spinBox.setValue(command.retrans)
        ui.attr_lost_send_spinBox.setValue(command.lost)

        ui.attr_start_txn_LineEdit.setText(command.start_txn)
        ui.attr_ack_txn_LineEdit.setText(command.ack_txn)

        ui.stackedw_content.setCurrentIndex(SippDrawConf.STACK_CONTENT_PAGE)
        ui.texte_content.setText(command.content)

    elif isinstance(command, PauseCommand):
        ui.stackedw_spec_attrs.setCurrentIndex(SippDrawConf.STACK_SPEC_ATTR_PAUSE_PAGE)

        ui.attr_milliseconds_spinBox.setValue(command.milliseconds)
        ui.attr_variable_spinBox.setValue(command.variable)

        ui.attr_distribution_comboBox.setCurrentText(command.distribution)

        ui.attr_sanity_check_checkBox.setChecked(command.sanity_check)

        ui.stackedw_content.setCurrentIndex(SippDrawConf.STACK_CONTENT_STAB_PAGE)
    else:
        ui.stackedw_spec_attrs.setCurrentIndex(SippDrawConf.STACK_SPEC_ATTR_NOP_PAGE)
        ui.stackedw_content.setCurrentIndex(SippDrawConf.STACK_CONTENT_PAGE)
        ui.texte_content.setText(command.content)


