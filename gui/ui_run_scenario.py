# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Run-Scenario.ui'
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


class Ui_Run_Scenario(object):
    def setupUi(self, Run_Scenario):
        if Run_Scenario.objectName():
            Run_Scenario.setObjectName(u"Run_Scenario")
        Run_Scenario.resize(404, 158)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Run_Scenario.sizePolicy().hasHeightForWidth())
        Run_Scenario.setSizePolicy(sizePolicy)
        Run_Scenario.setMinimumSize(QSize(0, 0))
        Run_Scenario.setSizeGripEnabled(False)
        Run_Scenario.setModal(True)
        self.verticalLayout = QVBoxLayout(Run_Scenario)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.input_stackedWidget = QStackedWidget(Run_Scenario)
        self.input_stackedWidget.setObjectName(u"input_stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.service_lineEdit = QLineEdit(self.page)
        self.service_lineEdit.setObjectName(u"service_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.service_lineEdit.sizePolicy().hasHeightForWidth())
        self.service_lineEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.service_lineEdit)

        self.remoteip_LineEdit = QLineEdit(self.page)
        self.remoteip_LineEdit.setObjectName(u"remoteip_LineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.remoteip_LineEdit.sizePolicy().hasHeightForWidth())
        self.remoteip_LineEdit.setSizePolicy(sizePolicy2)
        self.remoteip_LineEdit.setMaxLength(15)

        self.verticalLayout_3.addWidget(self.remoteip_LineEdit)

        self.collect_stat_checkBox = QCheckBox(self.page)
        self.collect_stat_checkBox.setObjectName(u"collect_stat_checkBox")

        self.verticalLayout_3.addWidget(self.collect_stat_checkBox)

        self.input_stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.input_stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.input_stackedWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.buttons_stackedWidget = QStackedWidget(Run_Scenario)
        self.buttons_stackedWidget.setObjectName(u"buttons_stackedWidget")
        sizePolicy.setHeightForWidth(self.buttons_stackedWidget.sizePolicy().hasHeightForWidth())
        self.buttons_stackedWidget.setSizePolicy(sizePolicy)
        self.buttons_stackedWidget.setAutoFillBackground(False)
        self.buttons_stackedWidget.setFrameShape(QFrame.NoFrame)
        self.buttons_stackedWidget.setFrameShadow(QFrame.Plain)
        self.buttons_stackedWidget.setLineWidth(1)
        self.buttons_stackedWidget.setMidLineWidth(0)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        sizePolicy.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(6, 0, 0, 0)
        self.run_button = QPushButton(self.page_3)
        self.run_button.setObjectName(u"run_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy3)
        self.run_button.setLayoutDirection(Qt.LeftToRight)
        self.run_button.setAutoFillBackground(False)
        self.run_button.setStyleSheet(u"background-color: rgb(46, 204, 113);")
        self.run_button.setFlat(False)

        self.verticalLayout_4.addWidget(self.run_button, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.cancel_Button = QPushButton(self.page_3)
        self.cancel_Button.setObjectName(u"cancel_Button")
        sizePolicy3.setHeightForWidth(self.cancel_Button.sizePolicy().hasHeightForWidth())
        self.cancel_Button.setSizePolicy(sizePolicy3)
        self.cancel_Button.setAutoFillBackground(False)
        self.cancel_Button.setStyleSheet(u"background-color: rgb(239, 41, 41);")
        self.cancel_Button.setFlat(False)

        self.verticalLayout_4.addWidget(self.cancel_Button, 0, Qt.AlignRight)

        self.buttons_stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 0, 0, 0)
        self.stop_button = QPushButton(self.page_4)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setStyleSheet(u"background-color: rgb(231, 76, 60);")

        self.verticalLayout_5.addWidget(self.stop_button, 0, Qt.AlignRight|Qt.AlignTop)

        self.buttons_stackedWidget.addWidget(self.page_4)

        self.verticalLayout_2.addWidget(self.buttons_stackedWidget, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.load_label = QLabel(Run_Scenario)
        self.load_label.setObjectName(u"load_label")
        self.load_label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.load_label.sizePolicy().hasHeightForWidth())
        self.load_label.setSizePolicy(sizePolicy)
        self.load_label.setLineWidth(1)
        self.load_label.setMidLineWidth(0)
        self.load_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.load_label)

        self.load_status_label = QLabel(Run_Scenario)
        self.load_status_label.setObjectName(u"load_status_label")

        self.verticalLayout.addWidget(self.load_status_label)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.retranslateUi(Run_Scenario)

        self.input_stackedWidget.setCurrentIndex(0)
        self.buttons_stackedWidget.setCurrentIndex(1)
        self.run_button.setDefault(False)


        QMetaObject.connectSlotsByName(Run_Scenario)
    # setupUi

    def retranslateUi(self, Run_Scenario):
        Run_Scenario.setWindowTitle(QCoreApplication.translate("Run_Scenario", u"Run Scenario", None))
        self.service_lineEdit.setPlaceholderText(QCoreApplication.translate("Run_Scenario", u"service", None))
        self.remoteip_LineEdit.setInputMask("")
        self.remoteip_LineEdit.setText("")
        self.remoteip_LineEdit.setPlaceholderText(QCoreApplication.translate("Run_Scenario", u"remote IP", None))
        self.collect_stat_checkBox.setText(QCoreApplication.translate("Run_Scenario", u"Collect statistic", None))
        self.run_button.setText(QCoreApplication.translate("Run_Scenario", u"Run", None))
        self.cancel_Button.setText(QCoreApplication.translate("Run_Scenario", u"Cancel", None))
        self.stop_button.setText(QCoreApplication.translate("Run_Scenario", u"Stop", None))
        self.load_label.setText(QCoreApplication.translate("Run_Scenario", u"LoadIcon", None))
        self.load_status_label.setText(QCoreApplication.translate("Run_Scenario", u"LoadStatus", None))
    # retranslateUi

