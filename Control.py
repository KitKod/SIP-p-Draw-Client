from SippDrawConf import SippDrawConf
from models.SIPpCommands import RecvCommand, SendCommand, PauseCommand


class UIModelController:
    ui = None

    def __init__(self, ui):
        self.ui = ui

    def displayCommandDataInAttrPages(self, command):
        ui = self.ui
        ui.attr__rtd__spinBox.setValue(command.rtd)
        ui.attr__chance__doubleSpinBox.setValue(command.chance)

        ui.attr__start_rtd__LineEdit.setText(command.start_rtd)
        ui.attr__next__LineEdit.setText(command.next)
        ui.attr__test__LineEdit.setText(command.test)
        ui.attr__condexec__LineEdit.setText(command.condexec)
        ui.attr__counter__LineEdit.setText(command.counter)

        ui.attr__repeat_rtd__checkBox.setChecked(command.repeat_rtd)
        ui.attr__crlf__checkBox.setChecked(command.crlf)
        ui.attr__condexec_inverse__checkBox.setChecked(command.condexec_inverse)

        if isinstance(command, RecvCommand):
            ui.stackedw_spec_attrs.setCurrentIndex(SippDrawConf.STACK_SPEC_ATTR_RECV_PAGE)

            ui.attr__request__comboBox.setCurrentText(command.request)

            ui.attr__response__spinBox.setValue(command.response)
            ui.attr__lost__spinBox.setValue(command.lost)
            ui.attr__timeout__spinBox.setValue(command.timeout)

            ui.attr__ontimeout__LineEdit.setText(command.ontimeout)
            ui.attr__response_txn__LineEdit.setText(command.response_txn)

            ui.attr__optional__checkBox.setChecked(command.optional)
            ui.attr__ignoresdp__checkBox.setChecked(command.ignoresdp)
            ui.attr__rrs__checkBox.setChecked(command.rrs)
            ui.attr__auth__checkBox.setChecked(command.auth)
            ui.attr__regexp_match__checkBox.setChecked(command.regexp_match)

            ui.stackedw_content.setCurrentIndex(SippDrawConf.STACK_CONTENT_PAGE)
            ui.texte__content.setText(command.content)
        elif isinstance(command, SendCommand):
            ui.stackedw_spec_attrs.setCurrentIndex(SippDrawConf.STACK_SPEC_ATTR_SEND_PAGE)

            ui.attr_retrans_spinBox.setValue(command.retrans)
            ui.attr_lost_send_spinBox.setValue(command.send_lost)

            ui.attr_start_txn_LineEdit.setText(command.start_txn)
            ui.attr_ack_txn_LineEdit.setText(command.ack_txn)

            ui.stackedw_content.setCurrentIndex(SippDrawConf.STACK_CONTENT_PAGE)
            ui.texte__content.setText(command.content)

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
            ui.texte__content.setText(command.content)
