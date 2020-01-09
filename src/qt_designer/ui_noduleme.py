# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_noduleme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1014, 693)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonOpen = QtWidgets.QPushButton(MainWidget)
        self.buttonOpen.setObjectName("buttonOpen")
        self.horizontalLayout_2.addWidget(self.buttonOpen)
        self.buttonSave = QtWidgets.QPushButton(MainWidget)
        self.buttonSave.setObjectName("buttonSave")
        self.horizontalLayout_2.addWidget(self.buttonSave)
        self.buttonSaveAsNew = QtWidgets.QPushButton(MainWidget)
        self.buttonSaveAsNew.setObjectName("buttonSaveAsNew")
        self.horizontalLayout_2.addWidget(self.buttonSaveAsNew)
        spacerItem = QtWidgets.QSpacerItem(10000, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.comboBoxUser = QtWidgets.QComboBox(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxUser.sizePolicy().hasHeightForWidth())
        self.comboBoxUser.setSizePolicy(sizePolicy)
        self.comboBoxUser.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxUser.setObjectName("comboBoxUser")
        self.comboBoxUser.addItem("")
        self.comboBoxUser.addItem("")
        self.comboBoxUser.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxUser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(MainWidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.buttonPinset = QtWidgets.QToolButton(MainWidget)
        self.buttonPinset.setMinimumSize(QtCore.QSize(30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/pinset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPinset.setIcon(icon)
        self.buttonPinset.setObjectName("buttonPinset")
        self.gridLayout.addWidget(self.buttonPinset, 1, 0, 1, 1)
        self.buttonPen = QtWidgets.QToolButton(MainWidget)
        self.buttonPen.setMinimumSize(QtCore.QSize(30, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPen.setIcon(icon1)
        self.buttonPen.setObjectName("buttonPen")
        self.gridLayout.addWidget(self.buttonPen, 0, 0, 1, 1)
        self.buttonEracer = QtWidgets.QPushButton(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEracer.sizePolicy().hasHeightForWidth())
        self.buttonEracer.setSizePolicy(sizePolicy)
        self.buttonEracer.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonEracer.setMaximumSize(QtCore.QSize(30, 30))
        self.buttonEracer.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonEracer.setIcon(icon2)
        self.buttonEracer.setObjectName("buttonEracer")
        self.gridLayout.addWidget(self.buttonEracer, 2, 0, 1, 1)
        self.buttonTube = QtWidgets.QPushButton(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonTube.sizePolicy().hasHeightForWidth())
        self.buttonTube.setSizePolicy(sizePolicy)
        self.buttonTube.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonTube.setMaximumSize(QtCore.QSize(30, 30))
        self.buttonTube.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/tube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonTube.setIcon(icon3)
        self.buttonTube.setObjectName("buttonTube")
        self.gridLayout.addWidget(self.buttonTube, 3, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(MainWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelImage = CanvasView(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelImage.sizePolicy().hasHeightForWidth())
        self.labelImage.setSizePolicy(sizePolicy)
        self.labelImage.setMinimumSize(QtCore.QSize(500, 500))
        self.labelImage.setMaximumSize(QtCore.QSize(2000, 2000))
        self.labelImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelImage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelImage.setObjectName("labelImage")
        self.horizontalLayout_10.addWidget(self.labelImage)
        self.scrollBarY = QtWidgets.QScrollBar(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollBarY.sizePolicy().hasHeightForWidth())
        self.scrollBarY.setSizePolicy(sizePolicy)
        self.scrollBarY.setOrientation(QtCore.Qt.Vertical)
        self.scrollBarY.setObjectName("scrollBarY")
        self.horizontalLayout_10.addWidget(self.scrollBarY)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.scrollBarX = QtWidgets.QScrollBar(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollBarX.sizePolicy().hasHeightForWidth())
        self.scrollBarX.setSizePolicy(sizePolicy)
        self.scrollBarX.setOrientation(QtCore.Qt.Horizontal)
        self.scrollBarX.setObjectName("scrollBarX")
        self.verticalLayout_3.addWidget(self.scrollBarX)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sliderIndex = QtWidgets.QSlider(MainWidget)
        self.sliderIndex.setOrientation(QtCore.Qt.Horizontal)
        self.sliderIndex.setObjectName("sliderIndex")
        self.horizontalLayout_4.addWidget(self.sliderIndex)
        self.spinIndex = QtWidgets.QSpinBox(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinIndex.sizePolicy().hasHeightForWidth())
        self.spinIndex.setSizePolicy(sizePolicy)
        self.spinIndex.setMinimumSize(QtCore.QSize(61, 0))
        self.spinIndex.setObjectName("spinIndex")
        self.horizontalLayout_4.addWidget(self.spinIndex)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.line_3 = QtWidgets.QFrame(MainWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.buttonZoomUp = QtWidgets.QToolButton(MainWidget)
        self.buttonZoomUp.setMinimumSize(QtCore.QSize(30, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/zoom_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonZoomUp.setIcon(icon4)
        self.buttonZoomUp.setObjectName("buttonZoomUp")
        self.horizontalLayout_5.addWidget(self.buttonZoomUp)
        self.buttonZoomDown = QtWidgets.QToolButton(MainWidget)
        self.buttonZoomDown.setMinimumSize(QtCore.QSize(30, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui/zoom_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonZoomDown.setIcon(icon5)
        self.buttonZoomDown.setObjectName("buttonZoomDown")
        self.horizontalLayout_5.addWidget(self.buttonZoomDown)
        self.buttonZoomDefault = QtWidgets.QPushButton(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonZoomDefault.sizePolicy().hasHeightForWidth())
        self.buttonZoomDefault.setSizePolicy(sizePolicy)
        self.buttonZoomDefault.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonZoomDefault.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui/zoom_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonZoomDefault.setIcon(icon6)
        self.buttonZoomDefault.setObjectName("buttonZoomDefault")
        self.horizontalLayout_5.addWidget(self.buttonZoomDefault)
        spacerItem3 = QtWidgets.QSpacerItem(1000, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.labelMap = ZoomView(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMap.sizePolicy().hasHeightForWidth())
        self.labelMap.setSizePolicy(sizePolicy)
        self.labelMap.setMinimumSize(QtCore.QSize(200, 200))
        self.labelMap.setMaximumSize(QtCore.QSize(200, 200))
        self.labelMap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelMap.setObjectName("labelMap")
        self.verticalLayout_4.addWidget(self.labelMap)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.line_4 = QtWidgets.QFrame(MainWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelHistogram = QtWidgets.QLabel(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHistogram.sizePolicy().hasHeightForWidth())
        self.labelHistogram.setSizePolicy(sizePolicy)
        self.labelHistogram.setMinimumSize(QtCore.QSize(300, 150))
        self.labelHistogram.setMaximumSize(QtCore.QSize(300, 150))
        self.labelHistogram.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelHistogram.setObjectName("labelHistogram")
        self.verticalLayout_5.addWidget(self.labelHistogram)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sliderMaxHistogram = QtWidgets.QSlider(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderMaxHistogram.sizePolicy().hasHeightForWidth())
        self.sliderMaxHistogram.setSizePolicy(sizePolicy)
        self.sliderMaxHistogram.setMinimumSize(QtCore.QSize(300, 0))
        self.sliderMaxHistogram.setMaximumSize(QtCore.QSize(300, 16777215))
        self.sliderMaxHistogram.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sliderMaxHistogram.setOrientation(QtCore.Qt.Horizontal)
        self.sliderMaxHistogram.setObjectName("sliderMaxHistogram")
        self.horizontalLayout_7.addWidget(self.sliderMaxHistogram)
        self.label_3 = QtWidgets.QLabel(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(25, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.spinMaxHistogram = QtWidgets.QSpinBox(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinMaxHistogram.sizePolicy().hasHeightForWidth())
        self.spinMaxHistogram.setSizePolicy(sizePolicy)
        self.spinMaxHistogram.setMinimumSize(QtCore.QSize(80, 20))
        self.spinMaxHistogram.setMaximumSize(QtCore.QSize(100, 30))
        self.spinMaxHistogram.setObjectName("spinMaxHistogram")
        self.horizontalLayout_7.addWidget(self.spinMaxHistogram)
        spacerItem4 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sliderMinHistogram = QtWidgets.QSlider(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderMinHistogram.sizePolicy().hasHeightForWidth())
        self.sliderMinHistogram.setSizePolicy(sizePolicy)
        self.sliderMinHistogram.setMinimumSize(QtCore.QSize(300, 0))
        self.sliderMinHistogram.setMaximumSize(QtCore.QSize(300, 16777215))
        self.sliderMinHistogram.setOrientation(QtCore.Qt.Horizontal)
        self.sliderMinHistogram.setObjectName("sliderMinHistogram")
        self.horizontalLayout_6.addWidget(self.sliderMinHistogram)
        self.label_4 = QtWidgets.QLabel(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(25, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.spinMinHistogram = QtWidgets.QSpinBox(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinMinHistogram.sizePolicy().hasHeightForWidth())
        self.spinMinHistogram.setSizePolicy(sizePolicy)
        self.spinMinHistogram.setMinimumSize(QtCore.QSize(80, 20))
        self.spinMinHistogram.setMaximumSize(QtCore.QSize(100, 30))
        self.spinMinHistogram.setObjectName("spinMinHistogram")
        self.horizontalLayout_6.addWidget(self.spinMinHistogram)
        spacerItem5 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.line_5 = QtWidgets.QFrame(MainWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.buttonSwitchSoloAll = QtWidgets.QPushButton(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSwitchSoloAll.sizePolicy().hasHeightForWidth())
        self.buttonSwitchSoloAll.setSizePolicy(sizePolicy)
        self.buttonSwitchSoloAll.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonSwitchSoloAll.setText("")
        self.buttonSwitchSoloAll.setObjectName("buttonSwitchSoloAll")
        self.horizontalLayout_8.addWidget(self.buttonSwitchSoloAll)
        self.buttonSwitchMyEveryone = QtWidgets.QPushButton(MainWidget)
        self.buttonSwitchMyEveryone.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonSwitchMyEveryone.setText("")
        self.buttonSwitchMyEveryone.setObjectName("buttonSwitchMyEveryone")
        self.horizontalLayout_8.addWidget(self.buttonSwitchMyEveryone)
        spacerItem6 = QtWidgets.QSpacerItem(1000, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.buttonDeleteLabel = QtWidgets.QPushButton(MainWidget)
        self.buttonDeleteLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDeleteLabel.sizePolicy().hasHeightForWidth())
        self.buttonDeleteLabel.setSizePolicy(sizePolicy)
        self.buttonDeleteLabel.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonDeleteLabel.setStyleSheet("background-color: rgb(255, 107, 142);")
        self.buttonDeleteLabel.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDeleteLabel.setIcon(icon7)
        self.buttonDeleteLabel.setFlat(False)
        self.buttonDeleteLabel.setObjectName("buttonDeleteLabel")
        self.horizontalLayout_8.addWidget(self.buttonDeleteLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.tableWidgetLabels = QtWidgets.QTableWidget(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetLabels.sizePolicy().hasHeightForWidth())
        self.tableWidgetLabels.setSizePolicy(sizePolicy)
        self.tableWidgetLabels.setMinimumSize(QtCore.QSize(20, 0))
        self.tableWidgetLabels.setMaximumSize(QtCore.QSize(450, 16777215))
        self.tableWidgetLabels.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidgetLabels.setObjectName("tableWidgetLabels")
        self.tableWidgetLabels.setColumnCount(5)
        self.tableWidgetLabels.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLabels.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLabels.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLabels.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLabels.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLabels.setHorizontalHeaderItem(4, item)
        self.verticalLayout_6.addWidget(self.tableWidgetLabels)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.labelInfo = QtWidgets.QLabel(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelInfo.sizePolicy().hasHeightForWidth())
        self.labelInfo.setSizePolicy(sizePolicy)
        self.labelInfo.setObjectName("labelInfo")
        self.horizontalLayout_13.addWidget(self.labelInfo)
        spacerItem7 = QtWidgets.QSpacerItem(10000, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.verticalLayout.addLayout(self.verticalLayout_9)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Nodule me"))
        self.buttonOpen.setText(_translate("MainWidget", "Open"))
        self.buttonSave.setText(_translate("MainWidget", "Save"))
        self.buttonSaveAsNew.setText(_translate("MainWidget", "Save as ..."))
        self.comboBoxUser.setCurrentText(_translate("MainWidget", "user1"))
        self.comboBoxUser.setItemText(0, _translate("MainWidget", "user1"))
        self.comboBoxUser.setItemText(1, _translate("MainWidget", "user2"))
        self.comboBoxUser.setItemText(2, _translate("MainWidget", "user3"))
        self.buttonPinset.setText(_translate("MainWidget", "Ed"))
        self.buttonPen.setText(_translate("MainWidget", "+"))
        self.labelImage.setText(_translate("MainWidget", "Here is CT image"))
        self.buttonZoomUp.setText(_translate("MainWidget", "+"))
        self.buttonZoomDown.setText(_translate("MainWidget", "-"))
        self.labelMap.setText(_translate("MainWidget", "Here is Map"))
        self.labelHistogram.setText(_translate("MainWidget", "Here is Histogram"))
        self.label_3.setText(_translate("MainWidget", "MAX"))
        self.label_4.setText(_translate("MainWidget", "MIN"))
        item = self.tableWidgetLabels.horizontalHeaderItem(0)
        item.setText(_translate("MainWidget", "ID"))
        item = self.tableWidgetLabels.horizontalHeaderItem(1)
        item.setText(_translate("MainWidget", "Index"))
        item = self.tableWidgetLabels.horizontalHeaderItem(2)
        item.setText(_translate("MainWidget", "M level"))
        item = self.tableWidgetLabels.horizontalHeaderItem(3)
        item.setText(_translate("MainWidget", "User"))
        item = self.tableWidgetLabels.horizontalHeaderItem(4)
        item.setText(_translate("MainWidget", "Comments"))
        self.labelInfo.setText(_translate("MainWidget", "TextLabel"))

from view.canvas_view import CanvasView
from view.zoom_view import ZoomView