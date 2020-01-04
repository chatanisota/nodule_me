# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pen_regist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PenRegistDialog(object):
    def setupUi(self, PenRegistDialog):
        PenRegistDialog.setObjectName("PenRegistDialog")
        PenRegistDialog.resize(241, 111)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PenRegistDialog.setWindowIcon(icon)
        self.buttonRegistPenRegist = QtWidgets.QPushButton(PenRegistDialog)
        self.buttonRegistPenRegist.setGeometry(QtCore.QRect(10, 60, 111, 41))
        self.buttonRegistPenRegist.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.buttonRegistPenRegist.setObjectName("buttonRegistPenRegist")
        self.buttonCancelPenRegist = QtWidgets.QPushButton(PenRegistDialog)
        self.buttonCancelPenRegist.setGeometry(QtCore.QRect(130, 60, 101, 41))
        self.buttonCancelPenRegist.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.buttonCancelPenRegist.setObjectName("buttonCancelPenRegist")
        self.label = QtWidgets.QLabel(PenRegistDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 41))
        self.label.setObjectName("label")

        self.retranslateUi(PenRegistDialog)
        QtCore.QMetaObject.connectSlotsByName(PenRegistDialog)

    def retranslateUi(self, PenRegistDialog):
        _translate = QtCore.QCoreApplication.translate
        PenRegistDialog.setWindowTitle(_translate("PenRegistDialog", "Pen (step 2/2)"))
        self.buttonRegistPenRegist.setText(_translate("PenRegistDialog", "Complete label"))
        self.buttonCancelPenRegist.setText(_translate("PenRegistDialog", "Delete label"))
        self.label.setText(_translate("PenRegistDialog", "Press the [Complete label] button\n"
" to complete and end labeling."))

