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
        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.page_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

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

        self.lineEdit_18 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEdit_18)

        self.stab1Label_14 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_14.setObjectName(u"stab1Label_14")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.stab1Label_14)

        self.stab1LineEdit_14 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_14.setObjectName(u"stab1LineEdit_14")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.stab1LineEdit_14)

        self.stab1Label_15 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_15.setObjectName(u"stab1Label_15")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.stab1Label_15)

        self.stab1LineEdit_15 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_15.setObjectName(u"stab1LineEdit_15")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.stab1LineEdit_15)

        self.stab1LineEdit_16 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_16.setObjectName(u"stab1LineEdit_16")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.stab1LineEdit_16)

        self.stab1LineEdit_17 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_17.setObjectName(u"stab1LineEdit_17")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.stab1LineEdit_17)

        self.stab1LineEdit_18 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_18.setObjectName(u"stab1LineEdit_18")

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.stab1LineEdit_18)

        self.stab1LineEdit_19 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_19.setObjectName(u"stab1LineEdit_19")

        self.formLayout_5.setWidget(7, QFormLayout.FieldRole, self.stab1LineEdit_19)

        self.stab1LineEdit_20 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_20.setObjectName(u"stab1LineEdit_20")

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.stab1LineEdit_20)

        self.stab1LineEdit_21 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_21.setObjectName(u"stab1LineEdit_21")

        self.formLayout_5.setWidget(9, QFormLayout.FieldRole, self.stab1LineEdit_21)

        self.stab1LineEdit_22 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.stab1LineEdit_22.setObjectName(u"stab1LineEdit_22")

        self.formLayout_5.setWidget(10, QFormLayout.FieldRole, self.stab1LineEdit_22)

        self.stab1Label_16 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_16.setObjectName(u"stab1Label_16")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.stab1Label_16)

        self.stab1Label_17 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_17.setObjectName(u"stab1Label_17")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.stab1Label_17)

        self.stab1Label_18 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_18.setObjectName(u"stab1Label_18")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.stab1Label_18)

        self.stab1Label_19 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_19.setObjectName(u"stab1Label_19")

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.stab1Label_19)

        self.stab1Label_20 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_20.setObjectName(u"stab1Label_20")

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.stab1Label_20)

        self.stab1Label_21 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_21.setObjectName(u"stab1Label_21")

        self.formLayout_5.setWidget(9, QFormLayout.LabelRole, self.stab1Label_21)

        self.stab1Label_22 = QLabel(self.scrollAreaWidgetContents_5)
        self.stab1Label_22.setObjectName(u"stab1Label_22")

        self.formLayout_5.setWidget(10, QFormLayout.LabelRole, self.stab1Label_22)

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
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName(u"spinBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinBox)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox)

        self.stab1Label_5 = QLabel(self.scrollAreaWidgetContents)
        self.stab1Label_5.setObjectName(u"stab1Label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.stab1Label_5)

        self.spinBox_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.spinBox_2)

        self.stab1Label_6 = QLabel(self.scrollAreaWidgetContents)
        self.stab1Label_6.setObjectName(u"stab1Label_6")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.stab1Label_6)

        self.spinBox_3 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.spinBox_3)

        self.stab1Label_7 = QLabel(self.scrollAreaWidgetContents)
        self.stab1Label_7.setObjectName(u"stab1Label_7")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.stab1Label_7)

        self.stab1LineEdit_7 = QLineEdit(self.scrollAreaWidgetContents)
        self.stab1LineEdit_7.setObjectName(u"stab1LineEdit_7")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.stab1LineEdit_7)

        self.stab1Label_9 = QLabel(self.scrollAreaWidgetContents)
        self.stab1Label_9.setObjectName(u"stab1Label_9")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.stab1Label_9)

        self.stab1LineEdit_9 = QLineEdit(self.scrollAreaWidgetContents)
        self.stab1LineEdit_9.setObjectName(u"stab1LineEdit_9")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.stab1LineEdit_9)

        self.stab1Label = QLabel(self.scrollAreaWidgetContents)
        self.stab1Label.setObjectName(u"stab1Label")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.stab1Label)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.checkBox)

        self.stab1Label_2 = QLabel(self.scrollAreaWidgetContents)
        self.stab1Label_2.setObjectName(u"stab1Label_2")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.stab1Label_2)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.checkBox_2)

        self.stab1Label_3 = QLabel(self.scrollAreaWidgetContents)
        self.stab1Label_3.setObjectName(u"stab1Label_3")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.stab1Label_3)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.checkBox_3)

        self.stab1Label_4 = QLabel(self.scrollAreaWidgetContents)
        self.stab1Label_4.setObjectName(u"stab1Label_4")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.stab1Label_4)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.checkBox_4)

        self.stab1Label_8 = QLabel(self.scrollAreaWidgetContents)
        self.stab1Label_8.setObjectName(u"stab1Label_8")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.stab1Label_8)

        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.checkBox_5)

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
        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_13)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_14 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_14)

        self.stab1Label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.stab1Label_10.setObjectName(u"stab1Label_10")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.stab1Label_10)

        self.stab1LineEdit_10 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.stab1LineEdit_10.setObjectName(u"stab1LineEdit_10")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.stab1LineEdit_10)

        self.stab1Label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.stab1Label_11.setObjectName(u"stab1Label_11")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.stab1Label_11)

        self.stab1LineEdit_11 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.stab1LineEdit_11.setObjectName(u"stab1LineEdit_11")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.stab1LineEdit_11)

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
        self.label_15 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.lineEdit_15 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_15)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_16 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_16)

        self.stab1Label_12 = QLabel(self.scrollAreaWidgetContents_3)
        self.stab1Label_12.setObjectName(u"stab1Label_12")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.stab1Label_12)

        self.stab1LineEdit_12 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.stab1LineEdit_12.setObjectName(u"stab1LineEdit_12")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.stab1LineEdit_12)

        self.stab1Label_13 = QLabel(self.scrollAreaWidgetContents_3)
        self.stab1Label_13.setObjectName(u"stab1Label_13")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.stab1Label_13)

        self.stab1LineEdit_13 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.stab1LineEdit_13.setObjectName(u"stab1LineEdit_13")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.stab1LineEdit_13)

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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 368, 416))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_17 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_17, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_7.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.stackedw_spec_attrs.addWidget(self.page_stackw_nop_cmd)

        self.gridLayout_3.addWidget(self.stackedw_spec_attrs, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_spec_attr, u"Specific attributes")
        self.page_content = QWidget()
        self.page_content.setObjectName(u"page_content")
        self.gridLayout_2 = QGridLayout(self.page_content)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.page_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.lineEdit_22 = QLineEdit(self.page)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(100, 130, 113, 25))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_content, u"Content")

        self.gridLayout.addWidget(self.toolBox, 0, 1, 1, 1)

        self.table_constructor = QTableWidget(self.centralwidget)
        self.table_constructor.setObjectName(u"table_constructor")

        self.gridLayout.addWidget(self.table_constructor, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")

        self.horizontalLayout.addWidget(self.button_1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


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
        QWidget.setTabOrder(self.pushButton_3, self.table_constructor)
        QWidget.setTabOrder(self.table_constructor, self.button_1)
        QWidget.setTabOrder(self.button_1, self.pushButton)

        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.actionnew)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        self.stackedw_spec_attrs.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.page_common_attr.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Common Attrr", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stab1Label_14.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_15.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_16.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_17.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_18.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_19.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_20.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_21.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_22.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_common_attr), QCoreApplication.translate("MainWindow", u"Common attributes", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"response", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"request", None))
        self.stab1Label_5.setText(QCoreApplication.translate("MainWindow", u"lost", None))
        self.stab1Label_6.setText(QCoreApplication.translate("MainWindow", u"timeout", None))
        self.stab1Label_7.setText(QCoreApplication.translate("MainWindow", u"ontimeout", None))
        self.stab1Label_9.setText(QCoreApplication.translate("MainWindow", u"response_txn", None))
        self.stab1Label.setText(QCoreApplication.translate("MainWindow", u"optional", None))
        self.checkBox.setText("")
        self.stab1Label_2.setText(QCoreApplication.translate("MainWindow", u"ignoresdp", None))
        self.checkBox_2.setText("")
        self.stab1Label_3.setText(QCoreApplication.translate("MainWindow", u"rrs", None))
        self.checkBox_3.setText("")
        self.stab1Label_4.setText(QCoreApplication.translate("MainWindow", u"auth", None))
        self.checkBox_4.setText("")
        self.stab1Label_8.setText(QCoreApplication.translate("MainWindow", u"regexp_match", None))
        self.checkBox_5.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stab1Label_10.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_11.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stab1Label_12.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.stab1Label_13.setText(QCoreApplication.translate("MainWindow", u"stab1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"This command has not specific attributes.", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_spec_attr), QCoreApplication.translate("MainWindow", u"Specific attributes", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_content), QCoreApplication.translate("MainWindow", u"Content", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
    # retranslateUi

