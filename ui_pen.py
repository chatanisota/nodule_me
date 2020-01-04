# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PenDialog(object):
    def setupUi(self, PenDialog):
        PenDialog.setObjectName("PenDialog")
        PenDialog.resize(203, 65)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PenDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(PenDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(PenDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.labelPenDialog = QtWidgets.QLabel(PenDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPenDialog.sizePolicy().hasHeightForWidth())
        self.labelPenDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPenDialog.setFont(font)
        self.labelPenDialog.setObjectName("labelPenDialog")
        self.horizontalLayout.addWidget(self.labelPenDialog)
        self.label_2 = QtWidgets.QLabel(PenDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(PenDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(PenDialog)
        QtCore.QMetaObject.connectSlotsByName(PenDialog)

    def retranslateUi(self, PenDialog):
        _translate = QtCore.QCoreApplication.translate
        PenDialog.setWindowTitle(_translate("PenDialog", "Pen (step 1/2)"))
        self.label_3.setText(_translate("PenDialog", "You are labeling"))
        self.labelPenDialog.setText(_translate("PenDialog", "TextLabel"))
        self.label_2.setText(_translate("PenDialog", "labeling."))
        self.label.setText(_translate("PenDialog", "If you finish labeling for one nodule,\n"
"please RIGHT click."))

