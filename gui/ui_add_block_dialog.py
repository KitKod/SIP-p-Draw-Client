# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add-Block-Dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Add_Block_Dialog(object):
    def setupUi(self, Add_Block_Dialog):
        if Add_Block_Dialog.objectName():
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
        Add_Block_Dialog.setModal(True)
        self.formLayout = QFormLayout(Add_Block_Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Add_Block_Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBox_command = QComboBox(Add_Block_Dialog)
        self.comboBox_command.addItem("")
        self.comboBox_command.addItem("")
        self.comboBox_command.addItem("")
        self.comboBox_command.addItem("")
        self.comboBox_command.setObjectName(u"comboBox_command")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_command)

        self.label_3 = QLabel(Add_Block_Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.buttonBox_add_block = QDialogButtonBox(Add_Block_Dialog)
        self.buttonBox_add_block.setObjectName(u"buttonBox_add_block")
        self.buttonBox_add_block.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.buttonBox_add_block)

        self.comboBox_cmd_template = QComboBox(Add_Block_Dialog)
        self.comboBox_cmd_template.addItem("")
        self.comboBox_cmd_template.setObjectName(u"comboBox_cmd_template")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_cmd_template)


        self.retranslateUi(Add_Block_Dialog)

        QMetaObject.connectSlotsByName(Add_Block_Dialog)
    # setupUi

    def retranslateUi(self, Add_Block_Dialog):
        Add_Block_Dialog.setWindowTitle(QCoreApplication.translate("Add_Block_Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Add_Block_Dialog", u"Command", None))
        self.comboBox_command.setItemText(0, QCoreApplication.translate("Add_Block_Dialog", u"send", None))
        self.comboBox_command.setItemText(1, QCoreApplication.translate("Add_Block_Dialog", u"recv", None))
        self.comboBox_command.setItemText(2, QCoreApplication.translate("Add_Block_Dialog", u"nop", None))
        self.comboBox_command.setItemText(3, QCoreApplication.translate("Add_Block_Dialog", u"pause", None))

        self.label_3.setText(QCoreApplication.translate("Add_Block_Dialog", u"Template", None))
        self.comboBox_cmd_template.setItemText(0, QCoreApplication.translate("Add_Block_Dialog", u"Empty command", None))

    # retranslateUi

