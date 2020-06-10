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
        Run_Scenario.resize(404, 300)
        Run_Scenario.setModal(True)
        self.verticalLayout = QVBoxLayout(Run_Scenario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_stackedWidget = QStackedWidget(Run_Scenario)
        self.input_stackedWidget.setObjectName(u"input_stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.remoteip_LineEdit = QLineEdit(self.page)
        self.remoteip_LineEdit.setObjectName(u"remoteip_LineEdit")

        self.verticalLayout_3.addWidget(self.remoteip_LineEdit)

        self.service_lineEdit = QLineEdit(self.page)
        self.service_lineEdit.setObjectName(u"service_lineEdit")

        self.verticalLayout_3.addWidget(self.service_lineEdit)

        self.collect_stat_checkBox = QCheckBox(self.page)
        self.collect_stat_checkBox.setObjectName(u"collect_stat_checkBox")

        self.verticalLayout_3.addWidget(self.collect_stat_checkBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.input_stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.input_stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.input_stackedWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.buttons_stackedWidget = QStackedWidget(Run_Scenario)
        self.buttons_stackedWidget.setObjectName(u"buttons_stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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

        self.verticalLayout_4.addWidget(self.run_button)

        self.cancel_Button = QPushButton(self.page_3)
        self.cancel_Button.setObjectName(u"cancel_Button")

        self.verticalLayout_4.addWidget(self.cancel_Button)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.buttons_stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.stop_button = QPushButton(self.page_4)
        self.stop_button.setObjectName(u"stop_button")

        self.verticalLayout_5.addWidget(self.stop_button)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.buttons_stackedWidget.addWidget(self.page_4)

        self.verticalLayout_2.addWidget(self.buttons_stackedWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.status_stackedWidget = QStackedWidget(Run_Scenario)
        self.status_stackedWidget.setObjectName(u"status_stackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout = QGridLayout(self.page_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.load_label = QLabel(self.page_5)
        self.load_label.setObjectName(u"load_label")
        sizePolicy.setHeightForWidth(self.load_label.sizePolicy().hasHeightForWidth())
        self.load_label.setSizePolicy(sizePolicy)
        self.load_label.setLineWidth(1)
        self.load_label.setMidLineWidth(0)
        self.load_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.load_label, 0, 0, 1, 1)

        self.status_stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.pushButton = QPushButton(self.page_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 10, 89, 25))
        self.status_stackedWidget.addWidget(self.page_6)

        self.verticalLayout.addWidget(self.status_stackedWidget)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.retranslateUi(Run_Scenario)

        self.input_stackedWidget.setCurrentIndex(0)
        self.buttons_stackedWidget.setCurrentIndex(0)
        self.status_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Run_Scenario)
    # setupUi

    def retranslateUi(self, Run_Scenario):
        Run_Scenario.setWindowTitle(QCoreApplication.translate("Run_Scenario", u"Dialog", None))
        self.collect_stat_checkBox.setText(QCoreApplication.translate("Run_Scenario", u"Collect statistic", None))
        self.run_button.setText(QCoreApplication.translate("Run_Scenario", u"Run", None))
        self.cancel_Button.setText(QCoreApplication.translate("Run_Scenario", u"Cancel", None))
        self.stop_button.setText(QCoreApplication.translate("Run_Scenario", u"Stop", None))
        self.load_label.setText(QCoreApplication.translate("Run_Scenario", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Run_Scenario", u"PushButton", None))
    # retranslateUi

