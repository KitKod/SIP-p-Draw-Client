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

        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.page_common_attr = QWidget()
        self.page_common_attr.setObjectName(u"page_common_attr")
        self.page_common_attr.setEnabled(True)
        self.page_common_attr.setGeometry(QRect(0, 0, 388, 452))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_common_attr.sizePolicy().hasHeightForWidth())
        self.page_common_attr.setSizePolicy(sizePolicy)
        self.page_common_attr.setLayoutDirection(Qt.LeftToRight)
        self.page_common_attr.setAutoFillBackground(True)
        self.formLayoutWidget = QWidget(self.page_common_attr)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 271, 306))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_10 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit_10)

        self.toolBox.addItem(self.page_common_attr, u"Common attributes")
        self.page_spec_attr = QWidget()
        self.page_spec_attr.setObjectName(u"page_spec_attr")
        self.page_spec_attr.setGeometry(QRect(0, 0, 388, 452))
        self.formLayout_3 = QFormLayout(self.page_spec_attr)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_11 = QLabel(self.page_spec_attr)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_11 = QLineEdit(self.page_spec_attr)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_21 = QLabel(self.page_spec_attr)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_21)

        self.lineEdit_12 = QLineEdit(self.page_spec_attr)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_12)

        self.label_14 = QLabel(self.page_spec_attr)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_21 = QLineEdit(self.page_spec_attr)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_21)

        self.label_13 = QLabel(self.page_spec_attr)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_20 = QLineEdit(self.page_spec_attr)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_20)

        self.label_15 = QLabel(self.page_spec_attr)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_15)

        self.lineEdit_19 = QLineEdit(self.page_spec_attr)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_19)

        self.lineEdit_18 = QLineEdit(self.page_spec_attr)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lineEdit_18)

        self.label_12 = QLabel(self.page_spec_attr)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_17 = QLineEdit(self.page_spec_attr)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.lineEdit_17)

        self.label_16 = QLabel(self.page_spec_attr)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_16 = QLineEdit(self.page_spec_attr)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.lineEdit_16)

        self.label_17 = QLabel(self.page_spec_attr)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_17)

        self.lineEdit_15 = QLineEdit(self.page_spec_attr)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.lineEdit_15)

        self.label_18 = QLabel(self.page_spec_attr)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.page_spec_attr)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.label_19)

        self.lineEdit_14 = QLineEdit(self.page_spec_attr)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.lineEdit_14)

        self.label_20 = QLabel(self.page_spec_attr)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.label_20)

        self.lineEdit_13 = QLineEdit(self.page_spec_attr)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.lineEdit_13)

        self.hghjjLabel = QLabel(self.page_spec_attr)
        self.hghjjLabel.setObjectName(u"hghjjLabel")

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.hghjjLabel)

        self.hghjjLineEdit = QLineEdit(self.page_spec_attr)
        self.hghjjLineEdit.setObjectName(u"hghjjLineEdit")

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.hghjjLineEdit)

        self.cfsdf = QLabel(self.page_spec_attr)
        self.cfsdf.setObjectName(u"cfsdf")

        self.formLayout_3.setWidget(14, QFormLayout.LabelRole, self.cfsdf)

        self.hjh = QComboBox(self.page_spec_attr)
        self.hjh.setObjectName(u"hjh")

        self.formLayout_3.setWidget(14, QFormLayout.FieldRole, self.hjh)

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
        self.label_22 = QLabel(self.page_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(160, 120, 67, 17))
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_content, u"Content")

        self.gridLayout.addWidget(self.toolBox, 0, 1, 1, 1)

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

        self.toolBox.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(tooltip)
        self.page_common_attr.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"start_rtd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"rtd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"repeat_rtd", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"crlf", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"next", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"chance", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"condexec", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"condexec_inverse", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"counter", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_common_attr), QCoreApplication.translate("MainWindow", u"Common attributes", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"response", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"response_txn", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ignoresdp", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"optional", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"rrs", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"request", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"auth", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"lost", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"timeout", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"ontimeout", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"regexp_match", None))
        self.hghjjLabel.setText(QCoreApplication.translate("MainWindow", u"hghjj", None))
        self.cfsdf.setText(QCoreApplication.translate("MainWindow", u"fsdf", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_spec_attr), QCoreApplication.translate("MainWindow", u"Specific attributes", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_content), QCoreApplication.translate("MainWindow", u"Content", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
    # retranslateUi

