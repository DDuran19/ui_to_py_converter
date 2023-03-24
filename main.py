# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(304, 266)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.compilerdirectory = QLineEdit(self.centralwidget)
        self.compilerdirectory.setObjectName(u"compilerdirectory")
        self.compilerdirectory.setGeometry(QRect(10, 30, 201, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 16))
        self.compilerbrowse = QPushButton(self.centralwidget)
        self.compilerbrowse.setObjectName(u"compilerbrowse")
        self.compilerbrowse.setGeometry(QRect(220, 30, 71, 23))
        self.inputbrowse = QPushButton(self.centralwidget)
        self.inputbrowse.setObjectName(u"inputbrowse")
        self.inputbrowse.setGeometry(QRect(220, 80, 71, 23))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 201, 16))
        self.inputdirectory = QLineEdit(self.centralwidget)
        self.inputdirectory.setObjectName(u"inputdirectory")
        self.inputdirectory.setGeometry(QRect(10, 80, 201, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 201, 16))
        self.outputdirectory = QLineEdit(self.centralwidget)
        self.outputdirectory.setObjectName(u"outputdirectory")
        self.outputdirectory.setGeometry(QRect(10, 130, 201, 20))
        self.outputbrowse = QPushButton(self.centralwidget)
        self.outputbrowse.setObjectName(u"outputbrowse")
        self.outputbrowse.setGeometry(QRect(220, 130, 71, 23))
        self.convertbutton = QPushButton(self.centralwidget)
        self.convertbutton.setObjectName(u"convertbutton")
        self.convertbutton.setGeometry(QRect(10, 160, 101, 23))
        self.gotogithub = QPushButton(self.centralwidget)
        self.gotogithub.setObjectName(u"gotogithub")
        self.gotogithub.setGeometry(QRect(140, 160, 151, 23))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 180, 281, 51))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 304, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ui to Py converter by DDuran19", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"UI compiler directory:", None))
        self.compilerbrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.inputbrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input directory", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Output directory", None))
        self.outputbrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.convertbutton.setText(QCoreApplication.translate("MainWindow", u"Convert Files", None))
        self.gotogithub.setText(QCoreApplication.translate("MainWindow", u"Go to GITHUB open source", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"An open source small project to conveniently use Pyside2/PYQT to convert ui files to python files. Developed by Denver James Duran", None))
    # retranslateUi

