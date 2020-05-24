# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SIP-p-Draw.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 640)
        self.action_import = QAction(MainWindow)
        self.action_import.setObjectName(u"action_import")
        icon = QIcon()
        icon.addFile(u"../resources/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_import.setIcon(icon)
        self.action_export = QAction(MainWindow)
        self.action_export.setObjectName(u"action_export")
        icon1 = QIcon()
        icon1.addFile(u"../resources/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_export.setIcon(icon1)
        self.action_run = QAction(MainWindow)
        self.action_run.setObjectName(u"action_run")
        icon2 = QIcon()
        icon2.addFile(u"../resources/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_run.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.page_common_attr = QWidget()
        self.page_common_attr.setObjectName(u"page_common_attr")
        self.page_common_attr.setEnabled(True)
        self.page_common_attr.setGeometry(QRect(0, 0, 388, 413))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_common_attr.sizePolicy().hasHeightForWidth())
        self.page_common_attr.setSizePolicy(sizePolicy)
        self.page_common_attr.setLayoutDirection(Qt.LeftToRight)
        self.page_common_attr.setAutoFillBackground(True)
        self.gridLayout_9 = QGridLayout(self.page_common_attr)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.scrollArea_5 = QScrollArea(self.page_common_attr)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 368, 393))
        self.formLayout_5 = QFormLayout(self.scrollAreaWidgetContents_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_18 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.attr__start_rtd__LineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.attr__start_rtd__LineEdit.setObjectName(u"attr__start_rtd__LineEdit")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.attr__start_rtd__LineEdit)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.attr__rtd__spinBox = QSpinBox(self.scrollAreaWidgetContents_5)
        self.attr__rtd__spinBox.setObjectName(u"attr__rtd__spinBox")
        self.attr__rtd__spinBox.setMinimum(-1)
        self.attr__rtd__spinBox.setValue(-1)
        self.attr__rtd__spinBox.setDisplayIntegerBase(10)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.attr__rtd__spinBox)

        self.stab1Label_18 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_18.setObjectName(u"stab1Label_18")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.stab1Label_18)

        self.attr__chance__doubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.attr__chance__doubleSpinBox.setObjectName(u"attr__chance__doubleSpinBox")
        self.attr__chance__doubleSpinBox.setMinimum(-1.000000000000000)
        self.attr__chance__doubleSpinBox.setValue(-1.000000000000000)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.attr__chance__doubleSpinBox)

        self.stab1Label_16 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_16.setObjectName(u"stab1Label_16")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.stab1Label_16)

        self.attr__next__LineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.attr__next__LineEdit.setObjectName(u"attr__next__LineEdit")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.attr__next__LineEdit)

        self.stab1Label_17 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_17.setObjectName(u"stab1Label_17")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.stab1Label_17)

        self.attr__test__LineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.attr__test__LineEdit.setObjectName(u"attr__test__LineEdit")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.attr__test__LineEdit)

        self.stab1Label_19 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_19.setObjectName(u"stab1Label_19")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.stab1Label_19)

        self.attr__condexec__LineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.attr__condexec__LineEdit.setObjectName(u"attr__condexec__LineEdit")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.attr__condexec__LineEdit)

        self.stab1Label_14 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_14.setObjectName(u"stab1Label_14")

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.stab1Label_14)

        self.attr__repeat_rtd__checkBox = QCheckBox(self.scrollAreaWidgetContents_5)
        self.attr__repeat_rtd__checkBox.setObjectName(u"attr__repeat_rtd__checkBox")

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.attr__repeat_rtd__checkBox)

        self.stab1Label_15 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_15.setObjectName(u"stab1Label_15")

        self.formLayout_5.setWidget(9, QFormLayout.LabelRole, self.stab1Label_15)

        self.attr__crlf__checkBox = QCheckBox(self.scrollAreaWidgetContents_5)
        self.attr__crlf__checkBox.setObjectName(u"attr__crlf__checkBox")

        self.formLayout_5.setWidget(9, QFormLayout.FieldRole, self.attr__crlf__checkBox)

        self.stab1Label_20 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_20.setObjectName(u"stab1Label_20")

        self.formLayout_5.setWidget(10, QFormLayout.LabelRole, self.stab1Label_20)

        self.attr__condexec_inverse__checkBox = QCheckBox(self.scrollAreaWidgetContents_5)
        self.attr__condexec_inverse__checkBox.setObjectName(u"attr__condexec_inverse__checkBox")

        self.formLayout_5.setWidget(10, QFormLayout.FieldRole, self.attr__condexec_inverse__checkBox)

        self.stab1Label_21 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_21.setObjectName(u"stab1Label_21")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.stab1Label_21)

        self.attr__counter__LineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.attr__counter__LineEdit.setObjectName(u"attr__counter__LineEdit")

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.attr__counter__LineEdit)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_9.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_common_attr, u"Common attributes")
        self.page_spec_attr = QWidget()
        self.page_spec_attr.setObjectName(u"page_spec_attr")
        self.page_spec_attr.setGeometry(QRect(0, 0, 388, 397))
        self.gridLayout_3 = QGridLayout(self.page_spec_attr)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedw_spec_attrs = QStackedWidget(self.page_spec_attr)
        self.stackedw_spec_attrs.setObjectName(u"stackedw_spec_attrs")
        self.page_stackw_recv_cmd = QWidget()
        self.page_stackw_recv_cmd.setObjectName(u"page_stackw_recv_cmd")
        self.gridLayout_4 = QGridLayout(self.page_stackw_recv_cmd)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_stackw_recv_cmd)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 368, 377))
        self.formLayout_2 = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_response = QLabel(self.scrollAreaWidgetContents)
        self.label_response.setObjectName(u"label_response")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_response)

        self.attr__response__spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.attr__response__spinBox.setObjectName(u"attr__response__spinBox")
        self.attr__response__spinBox.setMinimum(-1)
        self.attr__response__spinBox.setValue(-1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.attr__response__spinBox)

        self.label_request = QLabel(self.scrollAreaWidgetContents)
        self.label_request.setObjectName(u"label_request")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_request)

        self.attr__request__comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.addItem("")
        self.attr__request__comboBox.setObjectName(u"attr__request__comboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.attr__request__comboBox)

        self.label_lost = QLabel(self.scrollAreaWidgetContents)
        self.label_lost.setObjectName(u"label_lost")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_lost)

        self.attr__lost__spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.attr__lost__spinBox.setObjectName(u"attr__lost__spinBox")
        self.attr__lost__spinBox.setMinimum(-1)
        self.attr__lost__spinBox.setValue(-1)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.attr__lost__spinBox)

        self.label_timeout = QLabel(self.scrollAreaWidgetContents)
        self.label_timeout.setObjectName(u"label_timeout")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_timeout)

        self.attr__timeout__spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.attr__timeout__spinBox.setObjectName(u"attr__timeout__spinBox")
        self.attr__timeout__spinBox.setMinimum(-1)
        self.attr__timeout__spinBox.setValue(-1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.attr__timeout__spinBox)

        self.label_ontimeout = QLabel(self.scrollAreaWidgetContents)
        self.label_ontimeout.setObjectName(u"label_ontimeout")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_ontimeout)

        self.attr__ontimeout__LineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.attr__ontimeout__LineEdit.setObjectName(u"attr__ontimeout__LineEdit")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.attr__ontimeout__LineEdit)

        self.label_response_txn = QLabel(self.scrollAreaWidgetContents)
        self.label_response_txn.setObjectName(u"label_response_txn")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_response_txn)

        self.attr__response_txn__LineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.attr__response_txn__LineEdit.setObjectName(u"attr__response_txn__LineEdit")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.attr__response_txn__LineEdit)

        self.label_optional = QLabel(self.scrollAreaWidgetContents)
        self.label_optional.setObjectName(u"label_optional")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_optional)

        self.attr__optional__checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr__optional__checkBox.setObjectName(u"attr__optional__checkBox")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.attr__optional__checkBox)

        self.label_ignoresdp = QLabel(self.scrollAreaWidgetContents)
        self.label_ignoresdp.setObjectName(u"label_ignoresdp")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_ignoresdp)

        self.attr__ignoresdp__checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr__ignoresdp__checkBox.setObjectName(u"attr__ignoresdp__checkBox")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.attr__ignoresdp__checkBox)

        self.label_rrs = QLabel(self.scrollAreaWidgetContents)
        self.label_rrs.setObjectName(u"label_rrs")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_rrs)

        self.attr__rrs__checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr__rrs__checkBox.setObjectName(u"attr__rrs__checkBox")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.attr__rrs__checkBox)

        self.label_auth = QLabel(self.scrollAreaWidgetContents)
        self.label_auth.setObjectName(u"label_auth")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_auth)

        self.attr__auth__checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr__auth__checkBox.setObjectName(u"attr__auth__checkBox")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.attr__auth__checkBox)

        self.label_regexp_match = QLabel(self.scrollAreaWidgetContents)
        self.label_regexp_match.setObjectName(u"label_regexp_match")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_regexp_match)

        self.attr__regexp_match__checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr__regexp_match__checkBox.setObjectName(u"attr__regexp_match__checkBox")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.attr__regexp_match__checkBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedw_spec_attrs.addWidget(self.page_stackw_recv_cmd)
        self.page_stackw_send_cmd = QWidget()
        self.page_stackw_send_cmd.setObjectName(u"page_stackw_send_cmd")
        self.gridLayout_5 = QGridLayout(self.page_stackw_send_cmd)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.page_stackw_send_cmd)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 368, 377))
        self.formLayout_3 = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_retrans = QLabel(self.scrollAreaWidgetContents_2)
        self.label_retrans.setObjectName(u"label_retrans")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_retrans)

        self.label_lost_send = QLabel(self.scrollAreaWidgetContents_2)
        self.label_lost_send.setObjectName(u"label_lost_send")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_lost_send)

        self.attr__lost_send__spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.attr__lost_send__spinBox.setObjectName(u"attr__lost_send__spinBox")
        self.attr__lost_send__spinBox.setMinimum(-1)
        self.attr__lost_send__spinBox.setValue(-1)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.attr__lost_send__spinBox)

        self.label_start_txn = QLabel(self.scrollAreaWidgetContents_2)
        self.label_start_txn.setObjectName(u"label_start_txn")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_start_txn)

        self.attr__start_txn__LineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.attr__start_txn__LineEdit.setObjectName(u"attr__start_txn__LineEdit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.attr__start_txn__LineEdit)

        self.label_ack_txn = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ack_txn.setObjectName(u"label_ack_txn")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_ack_txn)

        self.attr__ack_txn__LineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.attr__ack_txn__LineEdit.setObjectName(u"attr__ack_txn__LineEdit")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.attr__ack_txn__LineEdit)

        self.attr__retrans__spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.attr__retrans__spinBox.setObjectName(u"attr__retrans__spinBox")
        self.attr__retrans__spinBox.setMinimum(-1)
        self.attr__retrans__spinBox.setValue(-1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.attr__retrans__spinBox)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_5.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedw_spec_attrs.addWidget(self.page_stackw_send_cmd)
        self.page_stackw_pause_cmd = QWidget()
        self.page_stackw_pause_cmd.setObjectName(u"page_stackw_pause_cmd")
        self.gridLayout_6 = QGridLayout(self.page_stackw_pause_cmd)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.page_stackw_pause_cmd)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 223, 130))
        self.formLayout_4 = QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_milliseconds = QLabel(self.scrollAreaWidgetContents_3)
        self.label_milliseconds.setObjectName(u"label_milliseconds")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_milliseconds)

        self.label_variable = QLabel(self.scrollAreaWidgetContents_3)
        self.label_variable.setObjectName(u"label_variable")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_variable)

        self.label_distribution = QLabel(self.scrollAreaWidgetContents_3)
        self.label_distribution.setObjectName(u"label_distribution")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_distribution)

        self.attr__milliseconds__spinBox = QSpinBox(self.scrollAreaWidgetContents_3)
        self.attr__milliseconds__spinBox.setObjectName(u"attr__milliseconds__spinBox")
        self.attr__milliseconds__spinBox.setMinimum(-1)
        self.attr__milliseconds__spinBox.setValue(-1)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.attr__milliseconds__spinBox)

        self.attr__variable__spinBox = QSpinBox(self.scrollAreaWidgetContents_3)
        self.attr__variable__spinBox.setObjectName(u"attr__variable__spinBox")
        self.attr__variable__spinBox.setMinimum(-1)
        self.attr__variable__spinBox.setValue(-1)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.attr__variable__spinBox)

        self.attr__distribution__comboBox = QComboBox(self.scrollAreaWidgetContents_3)
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.addItem("")
        self.attr__distribution__comboBox.setObjectName(u"attr__distribution__comboBox")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.attr__distribution__comboBox)

        self.attr__sanity_check__checkBox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.attr__sanity_check__checkBox.setObjectName(u"attr__sanity_check__checkBox")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.attr__sanity_check__checkBox)

        self.labal_sanity_check = QLabel(self.scrollAreaWidgetContents_3)
        self.labal_sanity_check.setObjectName(u"labal_sanity_check")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.labal_sanity_check)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_6.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.stackedw_spec_attrs.addWidget(self.page_stackw_pause_cmd)
        self.page_stackw_nop_cmd = QWidget()
        self.page_stackw_nop_cmd.setObjectName(u"page_stackw_nop_cmd")
        self.gridLayout_7 = QGridLayout(self.page_stackw_nop_cmd)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.page_stackw_nop_cmd)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 299, 35))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_missing_attr = QLabel(self.scrollAreaWidgetContents_4)
        self.label_missing_attr.setObjectName(u"label_missing_attr")
        self.label_missing_attr.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_missing_attr, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_7.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.stackedw_spec_attrs.addWidget(self.page_stackw_nop_cmd)

        self.gridLayout_3.addWidget(self.stackedw_spec_attrs, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_spec_attr, u"Specific attributes")
        self.page_content = QWidget()
        self.page_content.setObjectName(u"page_content")
        self.page_content.setGeometry(QRect(0, 0, 388, 397))
        self.gridLayout_2 = QGridLayout(self.page_content)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedw_content = QStackedWidget(self.page_content)
        self.stackedw_content.setObjectName(u"stackedw_content")
        self.page_stackw_content = QWidget()
        self.page_stackw_content.setObjectName(u"page_stackw_content")
        self.gridLayout_10 = QGridLayout(self.page_stackw_content)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.texte__content = QTextEdit(self.page_stackw_content)
        self.texte__content.setObjectName(u"texte__content")

        self.gridLayout_10.addWidget(self.texte__content, 0, 0, 1, 1)

        self.stackedw_content.addWidget(self.page_stackw_content)
        self.page_stackw_content_stab = QWidget()
        self.page_stackw_content_stab.setObjectName(u"page_stackw_content_stab")
        self.gridLayout_11 = QGridLayout(self.page_stackw_content_stab)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_missing_content = QLabel(self.page_stackw_content_stab)
        self.label_missing_content.setObjectName(u"label_missing_content")
        self.label_missing_content.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_missing_content, 0, 0, 1, 1)

        self.stackedw_content.addWidget(self.page_stackw_content_stab)

        self.gridLayout_2.addWidget(self.stackedw_content, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_content, u"Content")

        self.gridLayout.addWidget(self.toolBox, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_add_block_to_table = QPushButton(self.centralwidget)
        self.pushButton_add_block_to_table.setObjectName(u"pushButton_add_block_to_table")

        self.horizontalLayout.addWidget(self.pushButton_add_block_to_table)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.table_constructor = QTableWidget(self.centralwidget)
        self.table_constructor.setObjectName(u"table_constructor")

        self.gridLayout.addWidget(self.table_constructor, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setAutoFillBackground(False)
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        QWidget.setTabOrder(self.table_constructor, self.pushButton_add_block_to_table)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menufile.addAction(self.action_import)
        self.menufile.addAction(self.action_export)
        self.menuRun.addAction(self.action_run)
        self.toolBar.addAction(self.action_import)
        self.toolBar.addAction(self.action_export)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_run)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.stackedw_spec_attrs.setCurrentIndex(1)
        self.stackedw_content.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_import.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.action_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.action_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(tooltip)
        self.page_common_attr.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"start_rtd", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"rtd", None))
        self.stab1Label_18.setText(QCoreApplication.translate("MainWindow", u"chance", None))
        self.stab1Label_16.setText(QCoreApplication.translate("MainWindow", u"next", None))
        self.stab1Label_17.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.stab1Label_19.setText(QCoreApplication.translate("MainWindow", u"condexec", None))
        self.stab1Label_14.setText(QCoreApplication.translate("MainWindow", u"repeat_rtd", None))
        self.attr__repeat_rtd__checkBox.setText("")
        self.stab1Label_15.setText(QCoreApplication.translate("MainWindow", u"crlf", None))
        self.attr__crlf__checkBox.setText("")
        self.stab1Label_20.setText(QCoreApplication.translate("MainWindow", u"condexec_inverse", None))
        self.attr__condexec_inverse__checkBox.setText("")
        self.stab1Label_21.setText(QCoreApplication.translate("MainWindow", u"counter", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_common_attr), QCoreApplication.translate("MainWindow", u"Common attributes", None))
        self.label_response.setText(QCoreApplication.translate("MainWindow", u"response", None))
        self.label_request.setText(QCoreApplication.translate("MainWindow", u"request", None))
        self.attr__request__comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))
        self.attr__request__comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"INVITE", None))
        self.attr__request__comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"ACK", None))
        self.attr__request__comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"BYE", None))
        self.attr__request__comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.attr__request__comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.attr__request__comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"OPTIONS", None))
        self.attr__request__comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"PRACK", None))
        self.attr__request__comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"SUBSCRIBE", None))
        self.attr__request__comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"NOTIFY", None))
        self.attr__request__comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"PUBLISH", None))
        self.attr__request__comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"INFO", None))
        self.attr__request__comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"REFER", None))
        self.attr__request__comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"MESSAGE", None))
        self.attr__request__comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"UPDATE", None))

        self.label_lost.setText(QCoreApplication.translate("MainWindow", u"lost", None))
        self.label_timeout.setText(QCoreApplication.translate("MainWindow", u"timeout", None))
        self.label_ontimeout.setText(QCoreApplication.translate("MainWindow", u"ontimeout", None))
        self.label_response_txn.setText(QCoreApplication.translate("MainWindow", u"response_txn", None))
        self.label_optional.setText(QCoreApplication.translate("MainWindow", u"optional", None))
        self.attr__optional__checkBox.setText("")
        self.label_ignoresdp.setText(QCoreApplication.translate("MainWindow", u"ignoresdp", None))
        self.attr__ignoresdp__checkBox.setText("")
        self.label_rrs.setText(QCoreApplication.translate("MainWindow", u"rrs", None))
        self.attr__rrs__checkBox.setText("")
        self.label_auth.setText(QCoreApplication.translate("MainWindow", u"auth", None))
        self.attr__auth__checkBox.setText("")
        self.label_regexp_match.setText(QCoreApplication.translate("MainWindow", u"regexp_match", None))
        self.attr__regexp_match__checkBox.setText("")
        self.label_retrans.setText(QCoreApplication.translate("MainWindow", u"retrans", None))
        self.label_lost_send.setText(QCoreApplication.translate("MainWindow", u"lost", None))
        self.label_start_txn.setText(QCoreApplication.translate("MainWindow", u"start_txn", None))
        self.label_ack_txn.setText(QCoreApplication.translate("MainWindow", u"ack_txn", None))
        self.label_milliseconds.setText(QCoreApplication.translate("MainWindow", u"milliseconds", None))
        self.label_variable.setText(QCoreApplication.translate("MainWindow", u"variable", None))
        self.label_distribution.setText(QCoreApplication.translate("MainWindow", u"distribution", None))
        self.attr__distribution__comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))
        self.attr__distribution__comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"fixed", None))
        self.attr__distribution__comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"uniform", None))
        self.attr__distribution__comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"normal", None))
        self.attr__distribution__comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"lognormal", None))
        self.attr__distribution__comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"exponential", None))
        self.attr__distribution__comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"weibull", None))
        self.attr__distribution__comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"pareto", None))
        self.attr__distribution__comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"gamma", None))
        self.attr__distribution__comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"negbin", None))

        self.attr__sanity_check__checkBox.setText("")
        self.labal_sanity_check.setText(QCoreApplication.translate("MainWindow", u"sanity_check", None))
        self.label_missing_attr.setText(QCoreApplication.translate("MainWindow", u"This command has not specific attributes.", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_spec_attr), QCoreApplication.translate("MainWindow", u"Specific attributes", None))
        self.texte__content.setDocumentTitle("")
        self.texte__content.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<![CDATA[. . .]]>", None))
        self.label_missing_content.setText(QCoreApplication.translate("MainWindow", u"This command has not content.", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_content), QCoreApplication.translate("MainWindow", u"Content", None))
        self.pushButton_add_block_to_table.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Test", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

