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
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget_2 = QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_2 = QHBoxLayout(self.page_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_change = QPushButton(self.page_3)
        self.pushButton_change.setObjectName(u"pushButton_change")

        self.horizontalLayout_2.addWidget(self.pushButton_change)

        self.pushButton_delete = QPushButton(self.page_3)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.horizontalLayout_2.addWidget(self.pushButton_delete)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget_2.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget_2, 1, 1, 1, 1)

        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.page_common_attr = QWidget()
        self.page_common_attr.setObjectName(u"page_common_attr")
        self.page_common_attr.setEnabled(True)
        self.page_common_attr.setGeometry(QRect(0, 0, 388, 436))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page_common_attr.sizePolicy().hasHeightForWidth())
        self.page_common_attr.setSizePolicy(sizePolicy1)
        self.page_common_attr.setLayoutDirection(Qt.LeftToRight)
        self.page_common_attr.setAutoFillBackground(True)
        self.gridLayout_9 = QGridLayout(self.page_common_attr)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.scrollArea_5 = QScrollArea(self.page_common_attr)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 368, 416))
        self.formLayout_5 = QFormLayout(self.scrollAreaWidgetContents_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_18 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_17 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEdit_17)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.spinBox_8 = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.spinBox_8)

        self.stab1Label_18 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_18.setObjectName(u"stab1Label_18")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.stab1Label_18)

        self.doubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox)

        self.stab1Label_16 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_16.setObjectName(u"stab1Label_16")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.stab1Label_16)

        self.stab1LineEdit_16 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_16.setObjectName(u"stab1LineEdit_16")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.stab1LineEdit_16)

        self.stab1Label_17 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_17.setObjectName(u"stab1Label_17")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.stab1Label_17)

        self.stab1LineEdit_17 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_17.setObjectName(u"stab1LineEdit_17")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.stab1LineEdit_17)

        self.stab1Label_19 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_19.setObjectName(u"stab1Label_19")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.stab1Label_19)

        self.stab1LineEdit_19 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_19.setObjectName(u"stab1LineEdit_19")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.stab1LineEdit_19)

        self.stab1Label_20 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_20.setObjectName(u"stab1Label_20")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.stab1Label_20)

        self.stab1LineEdit_20 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_20.setObjectName(u"stab1LineEdit_20")

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.stab1LineEdit_20)

        self.stab1Label_21 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_21.setObjectName(u"stab1Label_21")

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.stab1Label_21)

        self.stab1LineEdit_21 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_21.setObjectName(u"stab1LineEdit_21")

        self.formLayout_5.setWidget(7, QFormLayout.FieldRole, self.stab1LineEdit_21)

        self.stab1Label_14 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_14.setObjectName(u"stab1Label_14")

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.stab1Label_14)

        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.checkBox_8)

        self.stab1Label_15 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_15.setObjectName(u"stab1Label_15")

        self.formLayout_5.setWidget(9, QFormLayout.LabelRole, self.stab1Label_15)

        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.formLayout_5.setWidget(9, QFormLayout.FieldRole, self.checkBox_7)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_9.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_common_attr, u"Common attributes")
        self.page_spec_attr = QWidget()
        self.page_spec_attr.setObjectName(u"page_spec_attr")
        self.page_spec_attr.setGeometry(QRect(0, 0, 388, 436))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 368, 416))
        self.formLayout_2 = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_response = QLabel(self.scrollAreaWidgetContents)
        self.label_response.setObjectName(u"label_response")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_response)

        self.attr_response_spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.attr_response_spinBox.setObjectName(u"attr_response_spinBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.attr_response_spinBox)

        self.label_request = QLabel(self.scrollAreaWidgetContents)
        self.label_request.setObjectName(u"label_request")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_request)

        self.attr_request_comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.addItem("")
        self.attr_request_comboBox.setObjectName(u"attr_request_comboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.attr_request_comboBox)

        self.label_lost = QLabel(self.scrollAreaWidgetContents)
        self.label_lost.setObjectName(u"label_lost")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_lost)

        self.attr_lost_spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.attr_lost_spinBox.setObjectName(u"attr_lost_spinBox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.attr_lost_spinBox)

        self.label_timeout = QLabel(self.scrollAreaWidgetContents)
        self.label_timeout.setObjectName(u"label_timeout")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_timeout)

        self.attr_timeout_spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.attr_timeout_spinBox.setObjectName(u"attr_timeout_spinBox")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.attr_timeout_spinBox)

        self.label_ontimeout = QLabel(self.scrollAreaWidgetContents)
        self.label_ontimeout.setObjectName(u"label_ontimeout")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_ontimeout)

        self.attr_ontimeout_LineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.attr_ontimeout_LineEdit.setObjectName(u"attr_ontimeout_LineEdit")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.attr_ontimeout_LineEdit)

        self.label_response_txn = QLabel(self.scrollAreaWidgetContents)
        self.label_response_txn.setObjectName(u"label_response_txn")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_response_txn)

        self.attr_response_txn_LineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.attr_response_txn_LineEdit.setObjectName(u"attr_response_txn_LineEdit")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.attr_response_txn_LineEdit)

        self.label_optional = QLabel(self.scrollAreaWidgetContents)
        self.label_optional.setObjectName(u"label_optional")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_optional)

        self.attr_optional_checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr_optional_checkBox.setObjectName(u"attr_optional_checkBox")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.attr_optional_checkBox)

        self.label_ignoresdp = QLabel(self.scrollAreaWidgetContents)
        self.label_ignoresdp.setObjectName(u"label_ignoresdp")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_ignoresdp)

        self.attr_ignoresdp_checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr_ignoresdp_checkBox.setObjectName(u"attr_ignoresdp_checkBox")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.attr_ignoresdp_checkBox)

        self.label_rrs = QLabel(self.scrollAreaWidgetContents)
        self.label_rrs.setObjectName(u"label_rrs")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_rrs)

        self.attr_rrs_checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr_rrs_checkBox.setObjectName(u"attr_rrs_checkBox")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.attr_rrs_checkBox)

        self.label_auth = QLabel(self.scrollAreaWidgetContents)
        self.label_auth.setObjectName(u"label_auth")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_auth)

        self.attr_auth_checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr_auth_checkBox.setObjectName(u"attr_auth_checkBox")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.attr_auth_checkBox)

        self.label_regexp_match = QLabel(self.scrollAreaWidgetContents)
        self.label_regexp_match.setObjectName(u"label_regexp_match")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_regexp_match)

        self.attr_regexp_match_checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.attr_regexp_match_checkBox.setObjectName(u"attr_regexp_match_checkBox")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.attr_regexp_match_checkBox)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 368, 416))
        self.formLayout_3 = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_retrans = QLabel(self.scrollAreaWidgetContents_2)
        self.label_retrans.setObjectName(u"label_retrans")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_retrans)

        self.label_lost_send = QLabel(self.scrollAreaWidgetContents_2)
        self.label_lost_send.setObjectName(u"label_lost_send")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_lost_send)

        self.attr_lost_send_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.attr_lost_send_spinBox.setObjectName(u"attr_lost_send_spinBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.attr_lost_send_spinBox)

        self.label_start_txn = QLabel(self.scrollAreaWidgetContents_2)
        self.label_start_txn.setObjectName(u"label_start_txn")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_start_txn)

        self.attr_start_txn_LineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.attr_start_txn_LineEdit.setObjectName(u"attr_start_txn_LineEdit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.attr_start_txn_LineEdit)

        self.label_ack_txn = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ack_txn.setObjectName(u"label_ack_txn")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_ack_txn)

        self.attr_ack_txn_LineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.attr_ack_txn_LineEdit.setObjectName(u"attr_ack_txn_LineEdit")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.attr_ack_txn_LineEdit)

        self.attr_retrans_spinBox = QSpinBox(self.scrollAreaWidgetContents_2)
        self.attr_retrans_spinBox.setObjectName(u"attr_retrans_spinBox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.attr_retrans_spinBox)

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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 368, 416))
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

        self.attr_milliseconds_spinBox = QSpinBox(self.scrollAreaWidgetContents_3)
        self.attr_milliseconds_spinBox.setObjectName(u"attr_milliseconds_spinBox")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.attr_milliseconds_spinBox)

        self.attr_variable_spinBox = QSpinBox(self.scrollAreaWidgetContents_3)
        self.attr_variable_spinBox.setObjectName(u"attr_variable_spinBox")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.attr_variable_spinBox)

        self.attr_distribution_comboBox = QComboBox(self.scrollAreaWidgetContents_3)
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.addItem("")
        self.attr_distribution_comboBox.setObjectName(u"attr_distribution_comboBox")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.attr_distribution_comboBox)

        self.attr_sanity_check_checkBox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.attr_sanity_check_checkBox.setObjectName(u"attr_sanity_check_checkBox")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.attr_sanity_check_checkBox)

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
        self.page_content.setGeometry(QRect(0, 0, 388, 436))
        self.gridLayout_2 = QGridLayout(self.page_content)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedw_content = QStackedWidget(self.page_content)
        self.stackedw_content.setObjectName(u"stackedw_content")
        self.page_stackw_contentof_send = QWidget()
        self.page_stackw_contentof_send.setObjectName(u"page_stackw_contentof_send")
        self.gridLayout_10 = QGridLayout(self.page_stackw_contentof_send)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.texte_cdata = QTextEdit(self.page_stackw_contentof_send)
        self.texte_cdata.setObjectName(u"texte_cdata")

        self.gridLayout_10.addWidget(self.texte_cdata, 0, 0, 1, 1)

        self.stackedw_content.addWidget(self.page_stackw_contentof_send)
        self.page_stackw_contentof_nop = QWidget()
        self.page_stackw_contentof_nop.setObjectName(u"page_stackw_contentof_nop")
        self.formLayout = QFormLayout(self.page_stackw_contentof_nop)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.page_stackw_contentof_nop)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBox_3 = QComboBox(self.page_stackw_contentof_nop)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_3)

        self.stackedw_content.addWidget(self.page_stackw_contentof_nop)

        self.gridLayout_2.addWidget(self.stackedw_content, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_content, u"Content")

        self.gridLayout.addWidget(self.toolBox, 0, 1, 1, 1)

        self.table_constructor = QTableWidget(self.centralwidget)
        self.table_constructor.setObjectName(u"table_constructor")

        self.gridLayout.addWidget(self.table_constructor, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_add_recv = QPushButton(self.centralwidget)
        self.pushButton_add_recv.setObjectName(u"pushButton_add_recv")

        self.horizontalLayout.addWidget(self.pushButton_add_recv)

        self.pushButton_add_action = QPushButton(self.centralwidget)
        self.pushButton_add_action.setObjectName(u"pushButton_add_action")

        self.horizontalLayout.addWidget(self.pushButton_add_action)

        self.pushButton_add_send = QPushButton(self.centralwidget)
        self.pushButton_add_send.setObjectName(u"pushButton_add_send")

        self.horizontalLayout.addWidget(self.pushButton_add_send)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton_add_send, self.table_constructor)
        QWidget.setTabOrder(self.table_constructor, self.pushButton_add_recv)
        QWidget.setTabOrder(self.pushButton_add_recv, self.pushButton_add_action)

        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.actionnew)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.stackedw_spec_attrs.setCurrentIndex(0)
        self.stackedw_content.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.pushButton_change.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.page_common_attr.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"start_rtd", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"rtd", None))
        self.stab1Label_18.setText(QCoreApplication.translate("MainWindow", u"chance", None))
        self.stab1Label_16.setText(QCoreApplication.translate("MainWindow", u"next", None))
        self.stab1Label_17.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.stab1Label_19.setText(QCoreApplication.translate("MainWindow", u"condexec", None))
        self.stab1Label_20.setText(QCoreApplication.translate("MainWindow", u"condexec_inverse", None))
        self.stab1Label_21.setText(QCoreApplication.translate("MainWindow", u"counter", None))
        self.stab1Label_14.setText(QCoreApplication.translate("MainWindow", u"repeat_rtd", None))
        self.checkBox_8.setText("")
        self.stab1Label_15.setText(QCoreApplication.translate("MainWindow", u"crlf", None))
        self.checkBox_7.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_common_attr), QCoreApplication.translate("MainWindow", u"Common attributes", None))
        self.label_response.setText(QCoreApplication.translate("MainWindow", u"response", None))
        self.label_request.setText(QCoreApplication.translate("MainWindow", u"request", None))
        self.attr_request_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))
        self.attr_request_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"INVITE", None))
        self.attr_request_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"ACK", None))
        self.attr_request_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"BYE", None))
        self.attr_request_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.attr_request_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.attr_request_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"OPTIONS", None))
        self.attr_request_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"PRACK", None))
        self.attr_request_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"SUBSCRIBE", None))
        self.attr_request_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"NOTIFY", None))
        self.attr_request_comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"PUBLISH", None))
        self.attr_request_comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"INFO", None))
        self.attr_request_comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"REFER", None))
        self.attr_request_comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"MESSAGE", None))
        self.attr_request_comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"UPDATE", None))

        self.label_lost.setText(QCoreApplication.translate("MainWindow", u"lost", None))
        self.label_timeout.setText(QCoreApplication.translate("MainWindow", u"timeout", None))
        self.label_ontimeout.setText(QCoreApplication.translate("MainWindow", u"ontimeout", None))
        self.label_response_txn.setText(QCoreApplication.translate("MainWindow", u"response_txn", None))
        self.label_optional.setText(QCoreApplication.translate("MainWindow", u"optional", None))
        self.attr_optional_checkBox.setText("")
        self.label_ignoresdp.setText(QCoreApplication.translate("MainWindow", u"ignoresdp", None))
        self.attr_ignoresdp_checkBox.setText("")
        self.label_rrs.setText(QCoreApplication.translate("MainWindow", u"rrs", None))
        self.attr_rrs_checkBox.setText("")
        self.label_auth.setText(QCoreApplication.translate("MainWindow", u"auth", None))
        self.attr_auth_checkBox.setText("")
        self.label_regexp_match.setText(QCoreApplication.translate("MainWindow", u"regexp_match", None))
        self.attr_regexp_match_checkBox.setText("")
        self.label_retrans.setText(QCoreApplication.translate("MainWindow", u"retrans", None))
        self.label_lost_send.setText(QCoreApplication.translate("MainWindow", u"lost", None))
        self.label_start_txn.setText(QCoreApplication.translate("MainWindow", u"start_txn", None))
        self.label_ack_txn.setText(QCoreApplication.translate("MainWindow", u"ack_txn", None))
        self.label_milliseconds.setText(QCoreApplication.translate("MainWindow", u"milliseconds", None))
        self.label_variable.setText(QCoreApplication.translate("MainWindow", u"variable", None))
        self.label_distribution.setText(QCoreApplication.translate("MainWindow", u"distribution", None))
        self.attr_distribution_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))
        self.attr_distribution_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"fixed", None))
        self.attr_distribution_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"uniform", None))
        self.attr_distribution_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"normal", None))
        self.attr_distribution_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"lognormal", None))
        self.attr_distribution_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"exponential", None))
        self.attr_distribution_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"weibull", None))
        self.attr_distribution_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"pareto", None))
        self.attr_distribution_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"gamma", None))
        self.attr_distribution_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"negbin", None))

        self.attr_sanity_check_checkBox.setText("")
        self.labal_sanity_check.setText(QCoreApplication.translate("MainWindow", u"sanity_check", None))
        self.label_missing_attr.setText(QCoreApplication.translate("MainWindow", u"This command has not specific attributes.", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_spec_attr), QCoreApplication.translate("MainWindow", u"Specific attributes", None))
        self.texte_cdata.setDocumentTitle("")
        self.texte_cdata.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<![CDATA[. . .]]>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"action", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"exec", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_content), QCoreApplication.translate("MainWindow", u"Content", None))
        self.pushButton_add_recv.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_add_action.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_add_send.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
    # retranslateUi

