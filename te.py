# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/te.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 580)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(-1, 540, 501, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.start_btn.setEnabled(True)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout.addWidget(self.start_btn)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cap_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.cap_btn.setObjectName("cap_btn")
        self.horizontalLayout.addWidget(self.cap_btn)
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(0, 0, 501, 381))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgLabel.setLineWidth(5)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.TEXT = QtWidgets.QTextBrowser(Dialog)
        self.TEXT.setGeometry(QtCore.QRect(0, 390, 501, 141))
        self.TEXT.setObjectName("TEXT")
        self.action_Exit = QtWidgets.QAction(Dialog)
        self.action_Exit.setObjectName("action_Exit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start_btn.setText(_translate("Dialog", "start?"))
        self.cap_btn.setText(_translate("Dialog", "Capture!"))
        self.TEXT.setPlaceholderText(_translate("Dialog", "press start to connect with camera"))
        self.action_Exit.setText(_translate("Dialog", "exit"))
