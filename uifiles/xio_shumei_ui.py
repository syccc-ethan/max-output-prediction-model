# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pi_UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1124, 723)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(49,49,49);"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.caution_browser = QtGui.QTextBrowser(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.caution_browser.sizePolicy().hasHeightForWidth())
        self.caution_browser.setSizePolicy(sizePolicy)
        self.caution_browser.setMinimumSize(QtCore.QSize(0, 250))
        self.caution_browser.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-top-color: rgb(49, 49, 49);\n"
"font: 75 80pt \"宋体\";\n"
"border-color: rgb(49, 49, 49);"))
        self.caution_browser.setObjectName(_fromUtf8("caution_browser"))
        self.horizontalLayout_2.addWidget(self.caution_browser)
        self.sign_Browser = QtGui.QTextBrowser(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sign_Browser.sizePolicy().hasHeightForWidth())
        self.sign_Browser.setSizePolicy(sizePolicy)
        self.sign_Browser.setMinimumSize(QtCore.QSize(350, 250))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sign_Browser.setFont(font)
        self.sign_Browser.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-color: rgb(49, 49, 49);"))
        self.sign_Browser.setObjectName(_fromUtf8("sign_Browser"))
        self.horizontalLayout_2.addWidget(self.sign_Browser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.start_label = QtGui.QTextBrowser(Form)
        self.start_label.setMaximumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.start_label.setFont(font)
        self.start_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 11pt \"微软雅黑\";\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 7px;\n"
"border-color: white;\n"
"padding: 5px;"))
        self.start_label.setObjectName(_fromUtf8("start_label"))
        self.gridLayout.addWidget(self.start_label, 1, 1, 1, 1)
        self.end_label = QtGui.QTextBrowser(Form)
        self.end_label.setMaximumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.end_label.setFont(font)
        self.end_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 11pt \"微软雅黑\";\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 7px;\n"
"border-color: white;\n"
"padding: 5px;"))
        self.end_label.setObjectName(_fromUtf8("end_label"))
        self.gridLayout.addWidget(self.end_label, 2, 1, 1, 1)
        self.thing_label = QtGui.QTextBrowser(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thing_label.sizePolicy().hasHeightForWidth())
        self.thing_label.setSizePolicy(sizePolicy)
        self.thing_label.setMaximumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.thing_label.setFont(font)
        self.thing_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 11pt \"微软雅黑\";\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 7px;\n"
"border-color: white;\n"
"padding: 5px;"))
        self.thing_label.setObjectName(_fromUtf8("thing_label"))
        self.gridLayout.addWidget(self.thing_label, 0, 1, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"微软雅黑\";\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 7px;\n"
"border-color: white;\n"
"padding: 5px;"))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout.addWidget(self.pushButton_12, 1, 0, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"微软雅黑\";\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 7px;\n"
"border-color: white;\n"
"padding: 5px;"))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout.addWidget(self.pushButton_13, 2, 0, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"微软雅黑\";\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 7px;\n"
"border-color: white;\n"
"padding: 5px;"))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout.addWidget(self.pushButton_14, 3, 0, 1, 1)
        self.time_label = QtGui.QTextBrowser(Form)
        self.time_label.setMaximumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 11pt \"微软雅黑\";\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 7px;\n"
"border-color: white;\n"
"padding: 5px;"))
        self.time_label.setObjectName(_fromUtf8("time_label"))
        self.gridLayout.addWidget(self.time_label, 3, 1, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QtCore.QSize(96, 0))
        self.pushButton_11.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"微软雅黑\";\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 7px;\n"
"border-color: white;\n"
"padding: 5px;"))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout.addWidget(self.pushButton_11, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.things_browser = QtGui.QTextBrowser(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.things_browser.setFont(font)
        self.things_browser.setStyleSheet(_fromUtf8("font: 75 12pt \"Aharoni\";\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"宋体\";\n"
"border-color: rgb(49, 49, 49);"))
        self.things_browser.setObjectName(_fromUtf8("things_browser"))
        self.horizontalLayout.addWidget(self.things_browser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_12.setText(_translate("Form", "开始时间", None))
        self.pushButton_13.setText(_translate("Form", "结束时间", None))
        self.pushButton_14.setText(_translate("Form", "持续时间", None))
        self.pushButton_11.setText(_translate("Form", "事件", None))

