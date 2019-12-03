# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opencata.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from openedcata import Ui_SpecificCatagory_Manager
from SqlCmd import DatabaseManagement
from os import chdir, path

class OpenCata_(object):
    def __init__(self):
        if path.isdir("DATA"):
            try:
                chdir("DATA")
            except:
                pass
        else:
            pass
    def RetriveCatagories(self):
        self.CCT = []
        try:
            with open("catadetails","r") as fp:
                self.catacontents = fp.readlines()
                if len(self.catacontents) != 0:
                    #we have some contents.
                    pass
                else:
                    self.CCT = []
            for eachcatagory in self.catacontents:
                print("%s added to catagory"%eachcatagory)
                self.eachcatagory = eachcatagory.replace("\n","")
                self.eachcatagory = self.eachcatagory.split(":")[0]
                self.CCT.append(self.eachcatagory)
        except FileNotFoundError:
            #!no catagory file found.
            self.CCT = []
            try:
                print("catagory file not found earlier hence created newly.")
                with open("catadetails","w") as fp:
                    pass
            except:
                pass

        if len(self.CCT) == 0:
            self.error_msgBox = QMessageBox()
            self.error_msgBox.setIcon(QMessageBox.Critical)
            self.error_msgBox.setText("No Catagory Found , Please Select New Catagory To  Create One.")
            self.error_msgBox.setWindowTitle("No Catagory Exists.")
            self.error_msgBox.setStandardButtons(QMessageBox.Ok)
            self.error_msgBox.show()


    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(619, 313)
        self.gridLayoutWidget = QtWidgets.QWidget(self.Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 140, 461, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.selectcata_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.selectcata_comboBox.setObjectName("selectcata_comboBox")
        self.gridLayout.addWidget(self.selectcata_comboBox, 0, 1, 1, 1)
        self.opencata_selectcat_banner = QtWidgets.QLabel(self.gridLayoutWidget)
        self.opencata_selectcat_banner.setObjectName("opencata_selectcat_banner")
        self.gridLayout.addWidget(self.opencata_selectcat_banner, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.opencata_banner = QtWidgets.QLabel(self.Dialog)
        self.opencata_banner.setGeometry(QtCore.QRect(170, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Nokia Standard Light")
        font.setPointSize(30)
        self.opencata_banner.setFont(font)
        self.opencata_banner.setObjectName("opencata_banner")
        self.opencata_punchline = QtWidgets.QLabel(self.Dialog)
        self.opencata_punchline.setGeometry(QtCore.QRect(100, 80, 521, 20))
        self.opencata_punchline.setObjectName("opencata_punchline")
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setGeometry(QtCore.QRect(10, 110, 581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(175, 249, 241, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectcata_opencatagory_ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.selectcata_opencatagory_ok.setObjectName("selectcata_opencatagory_ok")
        self.horizontalLayout.addWidget(self.selectcata_opencatagory_ok)
        self.opencata_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.opencata_cancel.setObjectName("opencata_cancel")
        self.horizontalLayout.addWidget(self.opencata_cancel)
        self.RetriveCatagories() 
        self.selectcata_comboBox.clear()
        for eachCata in self.CCT:
            self.selectcata_comboBox.addItem(eachCata)#! to update combobox contents automatically.
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def OpenCataManager(self,catagory_name):
        if path.isfile(catagory_name):
            self.Dialog.close()
            self.SpecificCatagory_Manager = QtWidgets.QMainWindow()
            self.SpecificCatagory_ManagerUI = Ui_SpecificCatagory_Manager(catagory_name)
            self.SpecificCatagory_ManagerUI.setupUi(self.SpecificCatagory_Manager)
            self.SpecificCatagory_Manager.show()
        else:
            #!Catagory Entry Found In Configuration File But No Database Found Of Such Catagory.
            DbObj = DatabaseManagement(catagory_name)
            DbObj.CreateTable()
            DbObj.CloseConnections()
            self.error_msgBox = QMessageBox()
            self.error_msgBox.setIcon(QMessageBox.Information)
            self.error_msgBox.setText("No Database Entry Found Of Catagory, Blank Database Created.")
            self.error_msgBox.setWindowTitle("No Catagory Exists.")
            DbObj.CloseConnections()
            self.error_msgBox.setStandardButtons(QMessageBox.Ok)
            self.error_msgBox.show()

    def CheckAvaiCatagory(self):
        self.selected_catagory = self.selectcata_comboBox.currentText()
        self.selected_catagory = self.selected_catagory + ".db"
        if len(self.CCT) != 0:
            self.OpenCataManager(self.selected_catagory)
        else:
            self.error_msgBox = QMessageBox()
            self.error_msgBox.setIcon(QMessageBox.Critical)
            self.error_msgBox.setText("No Catagory Found\nPlease Select New Catagory To  Create One.")
            self.error_msgBox.setWindowTitle("New Database Created.")
            self.error_msgBox.setStandardButtons(QMessageBox.Ok)
            self.error_msgBox.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open Catagory Wizard"))
        self.opencata_selectcat_banner.setText(_translate("Dialog", "Select Catagory : "))
        self.opencata_banner.setText(_translate("Dialog", "Vocabuilder"))
        self.opencata_punchline.setText(_translate("Dialog", " - Select Any Catagory To Retrived Associated Words Saved In That Catagory."))
        self.selectcata_opencatagory_ok.setText(_translate("Dialog", "Open Catagory"))
        self.opencata_cancel.setText(_translate("Dialog", "Cancel"))
        self.opencata_cancel.clicked.connect(Dialog.close)
        self.selectcata_opencatagory_ok.clicked.connect(self.CheckAvaiCatagory)

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenCata = QtWidgets.QDialog()
    OpenCataUI = OpenCata_()
    OpenCataUI.setupUi(OpenCata)
    OpenCata.show()
    sys.exit(app.exec_())
"""