# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/camera_widget.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CameraWidget(object):
    def setupUi(self, CameraWidget):
        CameraWidget.setObjectName("CameraWidget")
        CameraWidget.resize(386, 311)
        CameraWidget.setStyleSheet("#canvas {\n"
"    background: rgb(0, 0, 0)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(CameraWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.focal_len = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.focal_len.setMinimum(0.1)
        self.focal_len.setSingleStep(0.1)
        self.focal_len.setProperty("value", 1.0)
        self.focal_len.setObjectName("focal_len")
        self.gridLayout_2.addWidget(self.focal_len, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 1, 1, 5)
        self.pos_0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pos_0.setMinimum(-99.99)
        self.pos_0.setSingleStep(0.1)
        self.pos_0.setObjectName("pos_0")
        self.gridLayout_2.addWidget(self.pos_0, 0, 3, 1, 1)
        self.rot_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rot_2.setMinimum(-99.99)
        self.rot_2.setSingleStep(0.1)
        self.rot_2.setObjectName("rot_2")
        self.gridLayout_2.addWidget(self.rot_2, 2, 5, 1, 1)
        self.rot_1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rot_1.setMinimum(-99.99)
        self.rot_1.setSingleStep(0.1)
        self.rot_1.setObjectName("rot_1")
        self.gridLayout_2.addWidget(self.rot_1, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 5)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 2)
        self.rot_0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.rot_0.sizePolicy().hasHeightForWidth())
        self.rot_0.setSizePolicy(sizePolicy)
        self.rot_0.setMinimum(-99.99)
        self.rot_0.setSingleStep(0.1)
        self.rot_0.setObjectName("rot_0")
        self.gridLayout_2.addWidget(self.rot_0, 2, 3, 1, 1)
        self.pos_1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pos_1.setMinimum(-99.99)
        self.pos_1.setSingleStep(0.1)
        self.pos_1.setObjectName("pos_1")
        self.gridLayout_2.addWidget(self.pos_1, 0, 4, 1, 1)
        self.dist_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dist_4.setMinimum(-99.99)
        self.dist_4.setSingleStep(0.1)
        self.dist_4.setObjectName("dist_4")
        self.gridLayout_2.addWidget(self.dist_4, 9, 4, 1, 1)
        self.dist_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dist_3.setMinimum(-99.99)
        self.dist_3.setSingleStep(0.1)
        self.dist_3.setObjectName("dist_3")
        self.gridLayout_2.addWidget(self.dist_3, 9, 3, 1, 1)
        self.dist_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dist_2.setMinimum(-99.99)
        self.dist_2.setSingleStep(0.1)
        self.dist_2.setObjectName("dist_2")
        self.gridLayout_2.addWidget(self.dist_2, 8, 3, 1, 1)
        self.dist_0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dist_0.setMinimum(-99.99)
        self.dist_0.setSingleStep(0.1)
        self.dist_0.setObjectName("dist_0")
        self.gridLayout_2.addWidget(self.dist_0, 8, 5, 1, 1)
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setStyleSheet("font: 11pt;")
        self.reset.setObjectName("reset")
        self.gridLayout_2.addWidget(self.reset, 11, 4, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 10, 1, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 1, 1, 5)
        self.dist_1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dist_1.setMinimum(-99.99)
        self.dist_1.setSingleStep(0.1)
        self.dist_1.setObjectName("dist_1")
        self.gridLayout_2.addWidget(self.dist_1, 8, 4, 1, 1)
        self.pos_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pos_2.setMinimum(-99.99)
        self.pos_2.setSingleStep(0.1)
        self.pos_2.setProperty("value", 3.0)
        self.pos_2.setObjectName("pos_2")
        self.gridLayout_2.addWidget(self.pos_2, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 5, 1, 1, 5)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 2)
        self.center_0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.center_0.setMinimum(0.1)
        self.center_0.setMaximum(0.9)
        self.center_0.setSingleStep(0.01)
        self.center_0.setProperty("value", 0.5)
        self.center_0.setObjectName("center_0")
        self.gridLayout_2.addWidget(self.center_0, 6, 3, 1, 1)
        self.center_1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.center_1.setMinimum(0.1)
        self.center_1.setMaximum(0.9)
        self.center_1.setSingleStep(0.01)
        self.center_1.setProperty("value", 0.5)
        self.center_1.setObjectName("center_1")
        self.gridLayout_2.addWidget(self.center_1, 6, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        CameraWidget.setCentralWidget(self.centralwidget)
        self.actionSave = QtWidgets.QAction(CameraWidget)
        self.actionSave.setObjectName("actionSave")

        self.retranslateUi(CameraWidget)
        QtCore.QMetaObject.connectSlotsByName(CameraWidget)
        CameraWidget.setTabOrder(self.pos_0, self.pos_1)
        CameraWidget.setTabOrder(self.pos_1, self.pos_2)
        CameraWidget.setTabOrder(self.pos_2, self.rot_0)
        CameraWidget.setTabOrder(self.rot_0, self.rot_1)
        CameraWidget.setTabOrder(self.rot_1, self.rot_2)
        CameraWidget.setTabOrder(self.rot_2, self.focal_len)
        CameraWidget.setTabOrder(self.focal_len, self.dist_2)
        CameraWidget.setTabOrder(self.dist_2, self.dist_1)
        CameraWidget.setTabOrder(self.dist_1, self.dist_0)
        CameraWidget.setTabOrder(self.dist_0, self.dist_3)
        CameraWidget.setTabOrder(self.dist_3, self.dist_4)

    def retranslateUi(self, CameraWidget):
        _translate = QtCore.QCoreApplication.translate
        CameraWidget.setWindowTitle(_translate("CameraWidget", "Camera Settings"))
        self.label_3.setText(_translate("CameraWidget", "Focal length"))
        self.label_4.setText(_translate("CameraWidget", "Distortion"))
        self.label_2.setText(_translate("CameraWidget", "Rotation"))
        self.reset.setText(_translate("CameraWidget", "Reset Camera"))
        self.label.setText(_translate("CameraWidget", "Position"))
        self.label_5.setText(_translate("CameraWidget", "Center"))
        self.actionSave.setText(_translate("CameraWidget", "Save"))

