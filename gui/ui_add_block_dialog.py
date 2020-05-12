# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add-Block-Dialog.ui'
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


class Ui_Add_Block_Dialog(object):
    def setupUi(self, Add_Block_Dialog):
        if not Add_Block_Dialog.objectName():
            Add_Block_Dialog.setObjectName(u"Add_Block_Dialog")
        Add_Block_Dialog.resize(400, 123)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Add_Block_Dialog.sizePolicy().hasHeightForWidth())
        Add_Block_Dialog.setSizePolicy(sizePolicy)
        Add_Block_Dialog.setMinimumSize(QSize(400, 0))
        Add_Block_Dialog.setMaximumSize(QSize(16777215, 16777215))
        Add_Block_Dialog.setSizeGripEnabled(False)
        Add_Block_Dialog.setModal(False)
        self.gridLayout = QGridLayout(Add_Block_Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.stackedw_add_block_dialog = QStackedWidget(Add_Block_Dialog)
        self.stackedw_add_block_dialog.setObjectName(u"stackedw_add_block_dialog")
        self.page_add_recv_send_block = QWidget()
        self.page_add_recv_send_block.setObjectName(u"page_add_recv_send_block")
        self.formLayout = QFormLayout(self.page_add_recv_send_block)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.page_add_recv_send_block)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBox_template_recv_send_block = QComboBox(self.page_add_recv_send_block)
        self.comboBox_template_recv_send_block.addItem("")
        self.comboBox_template_recv_send_block.setObjectName(u"comboBox_template_recv_send_block")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_template_recv_send_block)

        self.buttonBox_recv_send_block = QDialogButtonBox(self.page_add_recv_send_block)
        self.buttonBox_recv_send_block.setObjectName(u"buttonBox_recv_send_block")
        self.buttonBox_recv_send_block.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.buttonBox_recv_send_block)

        self.stackedw_add_block_dialog.addWidget(self.page_add_recv_send_block)
        self.page_add_action_block = QWidget()
        self.page_add_action_block.setObjectName(u"page_add_action_block")
        self.formLayout_2 = QFormLayout(self.page_add_action_block)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.page_add_action_block)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBox_command_action_block = QComboBox(self.page_add_action_block)
        self.comboBox_command_action_block.addItem("")
        self.comboBox_command_action_block.addItem("")
        self.comboBox_command_action_block.setObjectName(u"comboBox_command_action_block")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_command_action_block)

        self.label_3 = QLabel(self.page_add_action_block)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.comboBox_template_action_block = QComboBox(self.page_add_action_block)
        self.comboBox_template_action_block.addItem("")
        self.comboBox_template_action_block.setObjectName(u"comboBox_template_action_block")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox_template_action_block)

        self.buttonBox_action_block = QDialogButtonBox(self.page_add_action_block)
        self.buttonBox_action_block.setObjectName(u"buttonBox_action_block")
        self.buttonBox_action_block.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.buttonBox_action_block)

        self.stackedw_add_block_dialog.addWidget(self.page_add_action_block)

        self.gridLayout.addWidget(self.stackedw_add_block_dialog, 0, 0, 1, 1)


        self.retranslateUi(Add_Block_Dialog)

        self.stackedw_add_block_dialog.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Add_Block_Dialog)
    # setupUi

    def retranslateUi(self, Add_Block_Dialog):
        Add_Block_Dialog.setWindowTitle(QCoreApplication.translate("Add_Block_Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Add_Block_Dialog", u"Template", None))
        self.comboBox_template_recv_send_block.setItemText(0, QCoreApplication.translate("Add_Block_Dialog", u"Empty command", None))

        self.label_2.setText(QCoreApplication.translate("Add_Block_Dialog", u"Command", None))
        self.comboBox_command_action_block.setItemText(0, QCoreApplication.translate("Add_Block_Dialog", u"nop", None))
        self.comboBox_command_action_block.setItemText(1, QCoreApplication.translate("Add_Block_Dialog", u"pause", None))

        self.label_3.setText(QCoreApplication.translate("Add_Block_Dialog", u"Template", None))
        self.comboBox_template_action_block.setItemText(0, QCoreApplication.translate("Add_Block_Dialog", u"Empty command", None))

    # retranslateUi

