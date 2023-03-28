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
        MainWindow.resize(413, 382)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(304, 293))
        MainWindow.setMaximumSize(QSize(3040, 2930))
        icon = QIcon()
        icon.addFile(u"converter.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u".QPushButton:hover, .QCheckBox:hover{\n"
"color: green;\n"
"}\n"
"\n"
"\n"
"QCheckBox:checked {\n"
"color:red;\n"
"}")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainoptions = QFrame(self.centralwidget)
        self.mainoptions.setObjectName(u"mainoptions")
        sizePolicy1.setHeightForWidth(self.mainoptions.sizePolicy().hasHeightForWidth())
        self.mainoptions.setSizePolicy(sizePolicy1)
        self.mainoptions.setFrameShape(QFrame.StyledPanel)
        self.mainoptions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainoptions)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 0, 0, 0)
        self.label = QLabel(self.mainoptions)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.frame_9 = QFrame(self.mainoptions)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.compilerdirectory = QLineEdit(self.frame_9)
        self.compilerdirectory.setObjectName(u"compilerdirectory")

        self.horizontalLayout_5.addWidget(self.compilerdirectory)

        self.compilerbrowse = QPushButton(self.frame_9)
        self.compilerbrowse.setObjectName(u"compilerbrowse")

        self.horizontalLayout_5.addWidget(self.compilerbrowse)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.label_2 = QLabel(self.mainoptions)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_8 = QFrame(self.mainoptions)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.inputdirectory = QLineEdit(self.frame_8)
        self.inputdirectory.setObjectName(u"inputdirectory")

        self.horizontalLayout_4.addWidget(self.inputdirectory)

        self.inputbrowse = QPushButton(self.frame_8)
        self.inputbrowse.setObjectName(u"inputbrowse")

        self.horizontalLayout_4.addWidget(self.inputbrowse)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.label_3 = QLabel(self.mainoptions)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame_7 = QFrame(self.mainoptions)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.outputdirectory = QLineEdit(self.frame_7)
        self.outputdirectory.setObjectName(u"outputdirectory")

        self.horizontalLayout_3.addWidget(self.outputdirectory)

        self.outputbrowse = QPushButton(self.frame_7)
        self.outputbrowse.setObjectName(u"outputbrowse")

        self.horizontalLayout_3.addWidget(self.outputbrowse)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.mainoptions)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.option_overwritepython = QCheckBox(self.frame)
        self.option_overwritepython.setObjectName(u"option_overwritepython")
        self.option_overwritepython.setChecked(True)

        self.verticalLayout.addWidget(self.option_overwritepython)

        self.option_guipython = QCheckBox(self.frame)
        self.option_guipython.setObjectName(u"option_guipython")
        self.option_guipython.setChecked(True)

        self.verticalLayout.addWidget(self.option_guipython)

        self.option_txt = QCheckBox(self.frame)
        self.option_txt.setObjectName(u"option_txt")
        self.option_txt.setChecked(True)

        self.verticalLayout.addWidget(self.option_txt)


        self.horizontalLayout_7.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.constructor_pushbutton = QCheckBox(self.frame_2)
        self.constructor_pushbutton.setObjectName(u"constructor_pushbutton")
        self.constructor_pushbutton.setChecked(True)

        self.gridLayout.addWidget(self.constructor_pushbutton, 1, 0, 1, 1)

        self.constructor_label = QCheckBox(self.frame_2)
        self.constructor_label.setObjectName(u"constructor_label")

        self.gridLayout.addWidget(self.constructor_label, 1, 1, 1, 1)

        self.constructor_lineedit = QCheckBox(self.frame_2)
        self.constructor_lineedit.setObjectName(u"constructor_lineedit")

        self.gridLayout.addWidget(self.constructor_lineedit, 2, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.mainoptions)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.convertbutton = QPushButton(self.frame_4)
        self.convertbutton.setObjectName(u"convertbutton")

        self.horizontalLayout_2.addWidget(self.convertbutton)

        self.gotogithub = QPushButton(self.frame_4)
        self.gotogithub.setObjectName(u"gotogithub")

        self.horizontalLayout_2.addWidget(self.gotogithub)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.mainoptions)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 391, 141))
        self.label_4.setLineWidth(1)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.mainoptions)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.option_guipython.toggled.connect(self.frame_2.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UI Compiling Assistant - DDuran19", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"UI compiler directory:", None))
#if QT_CONFIG(tooltip)
        self.compilerdirectory.setToolTip(QCoreApplication.translate("MainWindow", u"will use PySide2-uic as default", None))
#endif // QT_CONFIG(tooltip)
        self.compilerbrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input directory", None))
        self.inputbrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Output directory", None))
        self.outputbrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.option_overwritepython.setText(QCoreApplication.translate("MainWindow", u"Overwrite existing python file", None))
        self.option_guipython.setText(QCoreApplication.translate("MainWindow", u"Create _gui.file (will append existing file)", None))
        self.option_txt.setText(QCoreApplication.translate("MainWindow", u"Create .txt file (will overwrite existing file)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Constructor", None))
        self.constructor_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Push Buttons", None))
        self.constructor_label.setText(QCoreApplication.translate("MainWindow", u"Labels", None))
        self.constructor_lineedit.setText(QCoreApplication.translate("MainWindow", u"Line Edits", None))
        self.convertbutton.setText(QCoreApplication.translate("MainWindow", u"Convert Files", None))
        self.gotogithub.setText(QCoreApplication.translate("MainWindow", u"Go to GITHUB open source", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An open source small project to assist users on compiling ui files</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     - use PySide/PyQT to compile ui files</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     - create a .txt with object names</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     - create a _gu"
                        "i.py files with constructor</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Developed by Denver James Duran</p></body></html>", None))
    # retranslateUi

