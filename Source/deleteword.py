# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteword.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SqlCmd import DatabaseManagement

class Ui_DeleteWord(object):
    def __init__(self,databasename):
        self.databasename = databasename
    def setupUi(self, DeleteWord):
        self.DeleteWord = DeleteWord
        self.DeleteWord.setObjectName("DeleteWord")
        self.DeleteWord.resize(622, 268)
        self.deleteword_label = QtWidgets.QLabel(self.DeleteWord)
        self.deleteword_label.setGeometry(QtCore.QRect(130, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Nokia Standard Light")
        font.setPointSize(30)
        self.deleteword_label.setFont(font)
        self.deleteword_label.setObjectName("deleteword_label")
        self.deleteword_punchline = QtWidgets.QLabel(self.DeleteWord)
        self.deleteword_punchline.setGeometry(QtCore.QRect(160, 60, 651, 91))
        self.deleteword_punchline.setObjectName("deleteword_punchline")
        self.line = QtWidgets.QFrame(self.DeleteWord)
        self.line.setGeometry(QtCore.QRect(30, 130, 561, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.DeleteWord)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 150, 211, 89))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.deleteword_id = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.deleteword_id.setObjectName("deleteword_id")
        self.horizontalLayout.addWidget(self.deleteword_id)
        self.verticalLayoutWidget = QtWidgets.QWidget(DeleteWord)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 150, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.deleteword_ok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteword_ok.setObjectName("deleteword_ok")
        self.verticalLayout.addWidget(self.deleteword_ok)
        self.deleteword_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteword_cancel.setObjectName("deleteword_cancel")
        self.verticalLayout.addWidget(self.deleteword_cancel)

        self.retranslateUi(self.DeleteWord)
        QtCore.QMetaObject.connectSlotsByName(self.DeleteWord)
    def CloseDeleteWizard(self):
        self.DeleteWord.close()
    def DeleteFinal(self):
        self.targetdeleteID = self.deleteword_id.text()
        self.DbObj = DatabaseManagement(self.databasename)
        self.DbObj.DeleteWholeRow(self.targetdeleteID)
        self.DeleteWord.close()
    def retranslateUi(self, DeleteWord):
        _translate = QtCore.QCoreApplication.translate
        DeleteWord.setWindowTitle(_translate("DeleteWord", "Delete Word Wizard (Vocabuilder)"))
        self.deleteword_label.setText(_translate("DeleteWord", "Vocabuilder"))
        self.deleteword_punchline.setText(_translate("DeleteWord", " - Use Unique ID Of Target Word To Remove It."))
        self.label.setText(_translate("DeleteWord", "Word ID : "))
        self.deleteword_ok.setText(_translate("DeleteWord", "Delete Word"))
        self.deleteword_cancel.setText(_translate("DeleteWord", "Cancel"))
        self.deleteword_cancel.clicked.connect(self.CloseDeleteWizard)
        self.deleteword_ok.clicked.connect(self.DeleteFinal)