# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addword.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from SqlCmd import DatabaseManagement
from os import chdir, path, getcwd

class Ui_AddWord_(object):
    def __init__(self,databasename):
        self.databasename=databasename
    def setupUi(self, AddWord_):
        self.AddWord_ = AddWord_
        self.AddWord_.setObjectName("AddWord_")
        self.AddWord_.resize(640, 483)
        self.addword_label = QtWidgets.QLabel(AddWord_)
        self.addword_label.setGeometry(QtCore.QRect(130, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Nokia Standard Light")
        font.setPointSize(30)
        self.addword_label.setFont(font)
        self.addword_label.setObjectName("addword_label")
        self.addword_punchline = QtWidgets.QLabel(self.AddWord_)
        self.addword_punchline.setGeometry(QtCore.QRect(160, 60, 651, 91))
        self.addword_punchline.setObjectName("addword_punchline")
        self.line = QtWidgets.QFrame(AddWord_)
        self.line.setGeometry(QtCore.QRect(30, 130, 561, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget = QtWidgets.QWidget(self.AddWord_)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 190, 521, 211))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.additem_meaning = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.additem_meaning.setFont(font)
        self.additem_meaning.setObjectName("additem_meaning")
        self.gridLayout.addWidget(self.additem_meaning, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.addword_inputsynonym = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.addword_inputsynonym.setFont(font)
        self.addword_inputsynonym.setObjectName("addword_inputsynonym")
        self.gridLayout.addWidget(self.addword_inputsynonym, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.addword_inputneword = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.addword_inputneword.setFont(font)
        self.addword_inputneword.setStyleSheet("color:green;")
        self.addword_inputneword.setObjectName("addword_inputneword")
        self.gridLayout.addWidget(self.addword_inputneword, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addword_ok = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addword_ok.setObjectName("addword_ok")
        self.horizontalLayout.addWidget(self.addword_ok)
        self.addword_cancel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addword_cancel.setObjectName("addword_cancel")
        self.horizontalLayout.addWidget(self.addword_cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.retranslateUi(AddWord_)
        QtCore.QMetaObject.connectSlotsByName(self.AddWord_)
    def AddWordEntryToDatabase(self):
        defaultpointervalue = int(0)
        if path.isdir("DATA"):
            try:
                chdir("DATA")
            except:
                pass
        if not path.isfile("position"):
            with open("position","w") as ap:
                ap.write("%d"%defaultpointervalue)
        self.DbObj = DatabaseManagement(self.databasename)
        self.DbObj.CreateTable()
        with open("position","r") as gp:
            self.databaseposition = int(gp.read())
        self.databasePosition = self.databaseposition + 1
        #self.databasePosition = len(self.DbObj.FetchData()) + 1
        self.newword = self.addword_inputneword.text()
        self.newword_syn = self.addword_inputsynonym.text()
        self.newword_mean = self.additem_meaning.text()
        if len(self.newword) == 0 or len(self.newword_mean) == 0:
            #!it should raise error as requisite information is not given.
            self.error_msgBox = QMessageBox()
            self.error_msgBox.setIcon(QMessageBox.Critical)
            self.error_msgBox.setText("Please Input Required information To Save New Word.")
            self.error_msgBox.setWindowTitle("Complete Details Not Provided")
            self.error_msgBox.setStandardButtons(QMessageBox.Ok)
            self.error_msgBox.show()
            pass
        else:
            with open("position","w") as lp:
                lp.write("%d"%self.databasePosition)
            self.DbObj.InsertNewDetails(self.databasePosition,self.newword,self.newword_syn,self.newword_mean)
            self.AddWord_.close()
        

    def CloseAddWord(self):
        self.AddWord_.close()
    def retranslateUi(self, AddWord_):
        _translate = QtCore.QCoreApplication.translate
        AddWord_.setWindowTitle(_translate("AddWord_", "Add Word Wizard (Vocabuilder)"))
        self.addword_label.setText(_translate("AddWord_", "Vocabuilder"))
        self.addword_punchline.setText(_translate("AddWord_", " - Add Your Vocabulary Findings Here To Remember Them Forever."))
        self.label_3.setText(_translate("AddWord_", "Synonym (If Any ) : "))
        self.label_4.setText(_translate("AddWord_", "Actual Meaning : "))
        self.label_5.setText(_translate("AddWord_", "New Word : "))
        self.addword_ok.setText(_translate("AddWord_", "Add"))
        self.addword_cancel.setText(_translate("AddWord_", "Cancel"))
        self.addword_cancel.clicked.connect(self.CloseAddWord)
        self.addword_ok.clicked.connect(self.AddWordEntryToDatabase)

