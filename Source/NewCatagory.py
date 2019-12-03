from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from SqlCmd import DatabaseManagement
from os import chdir, mkdir, path, getcwd
class Ui_CreateNewCatagory():
    def __init__(self):
        if path.isdir("DATA"):
            try:
                chdir("DATA")
                print("current dir changed to data folder.")
            except:
                print("unable to get into DATA dir (chdir error )")
                pass
        else:
            if "DATA" in getcwd():
                print('ALREADY IN DATA')
                pass
            else:
                mkdir("DATA")
        pass
    def setupUi(self, CreateNewCatagory):
        CreateNewCatagory.setObjectName("CreateNewCatagory")
        CreateNewCatagory.resize(640, 517)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(7)
        CreateNewCatagory.setFont(font)
        self.CreateNewCatagory = CreateNewCatagory
        self.newcatagory_banner = QtWidgets.QLabel(CreateNewCatagory)
        self.newcatagory_banner.setGeometry(QtCore.QRect(170, 20, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Nokia Standard Light")
        font.setPointSize(30)
        self.newcatagory_banner.setFont(font)
        self.newcatagory_banner.setObjectName("newcatagory_banner")
        self.line = QtWidgets.QFrame(CreateNewCatagory)
        self.line.setGeometry(QtCore.QRect(20, 130, 621, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(CreateNewCatagory)
        self.label.setGeometry(QtCore.QRect(20, 110, 601, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(CreateNewCatagory)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 190, 571, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.newcatagory_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.newcatagory_name.setObjectName("newcatagory_name")
        self.gridLayout.addWidget(self.newcatagory_name, 0, 1, 1, 1)
        self.newcatagory_disc = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.newcatagory_disc.setObjectName("newcatagory_disc")
        self.gridLayout.addWidget(self.newcatagory_disc, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(CreateNewCatagory)
        self.label_4.setGeometry(QtCore.QRect(50, 350, 521, 21))
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(CreateNewCatagory)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 400, 271, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newcatagory_create = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.newcatagory_create.setObjectName("newcatagory_create")
        self.horizontalLayout.addWidget(self.newcatagory_create)
        self.cancel_newcatagory = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_newcatagory.setObjectName("cancel_newcatagory")
        self.horizontalLayout.addWidget(self.cancel_newcatagory)

        self.retranslateUi(CreateNewCatagory)
        QtCore.QMetaObject.connectSlotsByName(CreateNewCatagory)
    def CreateCatagoryHandler(self):
        self.CatagoryName = self.newcatagory_name.text()
        self.CatagoryDisc = self.newcatagory_disc.text()
        if len(self.CatagoryName) == 0 or len(self.CatagoryDisc) == 0:
            self.error_msgBox = QMessageBox()
            self.error_msgBox.setIcon(QMessageBox.Critical)
            self.error_msgBox.setText("Please Enter Reliable Information To Create Catagory.")
            self.error_msgBox.setWindowTitle("Incorrect Information Provided")
            self.error_msgBox.setStandardButtons(QMessageBox.Ok)
            self.error_msgBox.show()
        else:
            self.DBName = self.CatagoryName + ".db"
            self.DbObj = DatabaseManagement(self.DBName)
            self.DbObj.CreateTable()
            self.DbObj.CloseConnections()
            try:
                self.details = self.CatagoryName + ":" + self.CatagoryDisc
                with open("catadetails","a+") as fp:
                    fp.write(self.details)
                    fp.write("\n")
            except:
                pass
        self.CreateNewCatagory.close()

    def retranslateUi(self, CreateNewCatagory):
        _translate = QtCore.QCoreApplication.translate
        CreateNewCatagory.setWindowTitle(_translate("CreateNewCatagory", "Create New Catagory Wizard"))
        self.newcatagory_banner.setText(_translate("CreateNewCatagory", "Vocabuilder"))
        self.label.setText(_translate("CreateNewCatagory", " - Create New Catagory For Holding Words Of Same Nature To Remember Where You\'ve Saved Them Later."))
        self.label_2.setText(_translate("CreateNewCatagory", "New Catagory Name : "))
        self.label_3.setText(_translate("CreateNewCatagory", "Discription Of Catagory : "))
        self.label_4.setText(_translate("CreateNewCatagory", "Eg. Catagory Name \'Nature \' And Discription \'All Words Of Nature Here\' "))
        self.newcatagory_create.setText(_translate("CreateNewCatagory", "Create"))
        self.cancel_newcatagory.setText(_translate("CreateNewCatagory", "Cancel"))
        self.cancel_newcatagory.clicked.connect(CreateNewCatagory.close)
        self.newcatagory_create.clicked.connect(self.CreateCatagoryHandler)

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateNewCatagory = QtWidgets.QDialog()
    CreateNewCatagoryUI = Ui_CreateNewCatagory()
    CreateNewCatagoryUI.setupUi(CreateNewCatagory)
    CreateNewCatagory.show()
    sys.exit(app.exec_())



"""