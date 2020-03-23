# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xio_figureplot.ui'
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
        Form.resize(1440, 900)
        self.graphicsView_MT = QtGui.QGraphicsView(Form)
        self.graphicsView_MT.setGeometry(QtCore.QRect(210, 40, 500, 360))
        self.graphicsView_MT.setObjectName(_fromUtf8("graphicsView_MT"))
        self.graphicsView_OEE = QtGui.QGraphicsView(Form)
        self.graphicsView_OEE.setGeometry(QtCore.QRect(740, 40, 500, 360))
        self.graphicsView_OEE.setObjectName(_fromUtf8("graphicsView_OEE"))
        self.graphicsView_Loss = QtGui.QGraphicsView(Form)
        self.graphicsView_Loss.setGeometry(QtCore.QRect(210, 450, 500, 360))
        self.graphicsView_Loss.setObjectName(_fromUtf8("graphicsView_Loss"))
        self.graphicsView_Pie = QtGui.QGraphicsView(Form)
        self.graphicsView_Pie.setGeometry(QtCore.QRect(740, 450, 500, 360))
        self.graphicsView_Pie.setObjectName(_fromUtf8("graphicsView_Pie"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

