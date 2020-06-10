import time
import subprocess
from multiprocessing import Value
from threading import Thread

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

            ui.attr__retrans__spinBox.setValue(command.retrans)
            ui.attr__lost_send__spinBox.setValue(command.lost_send)

            ui.attr__start_txn__LineEdit.setText(command.start_txn)
            ui.attr__ack_txn__LineEdit.setText(command.ack_txn)

            ui.stackedw_content.setCurrentIndex(SippDrawConf.STACK_CONTENT_PAGE)
            ui.texte__content.setText(command.content)

        elif isinstance(command, PauseCommand):
            ui.stackedw_spec_attrs.setCurrentIndex(SippDrawConf.STACK_SPEC_ATTR_PAUSE_PAGE)

            ui.attr__milliseconds__spinBox.setValue(command.milliseconds)
            ui.attr__variable__spinBox.setValue(command.variable)

            ui.attr__distribution__comboBox.setCurrentText(command.distribution)

            ui.attr__sanity_check__checkBox.setChecked(command.sanity_check)

            ui.stackedw_content.setCurrentIndex(SippDrawConf.STACK_CONTENT_STAB_PAGE)
        else:
            ui.stackedw_spec_attrs.setCurrentIndex(SippDrawConf.STACK_SPEC_ATTR_NOP_PAGE)
            ui.stackedw_content.setCurrentIndex(SippDrawConf.STACK_CONTENT_PAGE)
            ui.texte__content.setText(command.content)


class MyProcess(Thread):
    def __init__(self, dialog, shared_pid, cmd):
        Thread.__init__(self)
        self.dialog = dialog
        self.shared_pid = shared_pid
        self.cmd = cmd

    def run(self):
        process = subprocess.Popen(self.cmd, stdout = subprocess.PIPE, encoding = 'utf8')
        self.shared_pid.value = process.pid
        result_code = process.wait()
        self.dialog.testScenarioCompleted(result_code)


class TestScenarioExecutionController:
    dialog = None
    path = None
    tests_count = 1
    duration = None
    service = None
    remote_ip = None
    trace_stat = False

    def __init__(self, dialog, path, tests_count = 1, duration = None, service = None, remote_ip = None,
                 trace_stat = False):
        self.dialog = dialog
        self.path = path
        self.tests_count = tests_count
        self.duration = duration
        self.service = service
        self.remote_ip = remote_ip
        self.trace_stat = trace_stat

    def run(self):
        cmd_args = []
        if self.remote_ip is not None:
            cmd_args.append(self.remote_ip)
        if self.service is not None:
            cmd_args.append('-s')
            cmd_args.append(str(self.service))
        if self.duration is not None:
            cmd_args.append('-d')
            cmd_args.append(str(self.duration))
        if self.tests_count:
            cmd_args.append('-m')
            cmd_args.append(str(self.tests_count))
        if self.trace_stat:
            cmd_args.append('-trace_stat')
        cmd_args.append('-sf')
        cmd_args.append(self.path)
        cmd = ["sipp"] + cmd_args

        print('PATH={}'.format(cmd))

        shared_pid = Value('i', -10)
        p = MyProcess(self.dialog, shared_pid, cmd)
        p.start()
        pid = shared_pid.value
        while pid == -10:
            time.sleep(0.3)
            pid = shared_pid.value
        print('return final pid={}'.format(pid))

        return pid

