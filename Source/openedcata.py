from PyQt5 import QtCore, QtGui, QtWidgets
from SqlCmd import DatabaseManagement
from addword import Ui_AddWord_
from deleteword import Ui_DeleteWord
from details import Ui_Details
import threading
from time import sleep

class Ui_SpecificCatagory_Manager(threading.Thread):
    default_state = 0
    DatabaseDeleted = False
    def __init__(self,database_name):
        self.database_name = database_name
        self.catagory_desc = ""
        self.catagory_name = self.database_name.split(".db")[0]
        try:
        	print("in try ")
        	with open("catadetails","r") as fp:
        		self.catadetail = fp.readlines()
        	for eachline in self.catadetail:
        		print("in for loop")
        		eachline = eachline.replace('\n','')
        		print("checking %s in %s"%(self.catagory_name,eachline))
        		if self.catagory_name in eachline:
        			self.catagory_desc = eachline.split(":")[1]
        		else:
        			pass
        except:
        	pass
        threading.Thread.__init__(self)
        print("dbname : ",self.database_name)
        refreshthread = threading.Thread(target = self.RefreshContents, daemon=True)
        refreshthread.start()
    def RefreshContents(self):
    	self.DbObj = DatabaseManagement(self.database_name)
    	self.DbObj.CreateTable()
    	while True:
    		if Ui_SpecificCatagory_Manager.DatabaseDeleted:
    			self.DbObj.DeleteDatabase()
    			Ui_SpecificCatagory_Manager.DatabaseDeleted = False
    		else:
    			sleep(0.5)
    			self.DatabaseDetails = self.DbObj.FetchData()
    			self.opened_cata_tableWidget.clearContents()
    			if len(self.DatabaseDetails) != 0:
    				for rowno,rowdata in enumerate(self.DatabaseDetails):
    					for colno, coldata in enumerate(rowdata):
    						self.opened_cata_tableWidget.setItem(rowno, colno, QtWidgets.QTableWidgetItem(str(coldata)))
    def AddWordWizard(self):
    	self.AddWord_ = QtWidgets.QDialog()
    	self.AddWordUI = Ui_AddWord_(self.database_name)
    	self.AddWordUI.setupUi(self.AddWord_)
    	self.AddWord_.show()
    def setupUi(self, SpecificCatagory_Manager):
        self.SpecificCatagory_Manager = SpecificCatagory_Manager
        self.SpecificCatagory_Manager.setObjectName("SpecificCatagory_Manager")
        self.SpecificCatagory_Manager.resize(1119, 713)
        self.SpecificCatagory_Manager.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(self.SpecificCatagory_Manager)
        self.centralwidget.setObjectName("centralwidget")
        self.opened_cata_banner = QtWidgets.QLabel(self.centralwidget)
        self.opened_cata_banner.setGeometry(QtCore.QRect(380, 10, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Nokia Standard Light")
        font.setPointSize(30)
        self.opened_cata_banner.setFont(font)
        self.opened_cata_banner.setObjectName("opened_cata_banner")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 110, 1061, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.opened_cata_punchline = QtWidgets.QLabel(self.centralwidget)
        self.opened_cata_punchline.setGeometry(QtCore.QRect(220, 80, 601, 20))
        self.opened_cata_punchline.setObjectName("opened_cata_punchline")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(873, 150, 20, 481))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(910, 170, 160, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.opened_cata_details = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.opened_cata_details.setObjectName("opened_cata_details")
        self.verticalLayout.addWidget(self.opened_cata_details)
        self.opened_cata_addword = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.opened_cata_addword.setObjectName("opened_cata_addword")
        self.verticalLayout.addWidget(self.opened_cata_addword)
        self.opened_cata_removeword = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.opened_cata_removeword.setObjectName("opened_cata_removeword")
        self.verticalLayout.addWidget(self.opened_cata_removeword)
        self.opened_cata_deletecatagory = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.opened_cata_deletecatagory.setObjectName("opened_cata_deletecatagory")
        self.verticalLayout.addWidget(self.opened_cata_deletecatagory)
        self.opened_cata_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.opened_cata_tableWidget.setGeometry(QtCore.QRect(100, 170, 761, 471))
        self.opened_cata_tableWidget.setRowCount(1000)
        self.opened_cata_tableWidget.setColumnCount(4)
        self.opened_cata_tableWidget.setObjectName("opened_cata_tableWidget")
        self.opened_cata_tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.opened_cata_tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.opened_cata_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.opened_cata_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.opened_cata_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.opened_cata_tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.opened_cata_tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.SpecificCatagory_Manager.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.SpecificCatagory_Manager)
        self.statusbar.setObjectName("statusbar")
        self.SpecificCatagory_Manager.setStatusBar(self.statusbar)

        self.retranslateUi(self.SpecificCatagory_Manager)
        QtCore.QMetaObject.connectSlotsByName(self.SpecificCatagory_Manager)
    def RemoveParticularWord(self):
    	self.DeleteWord = QtWidgets.QDialog()
    	self.DeleteUI = Ui_DeleteWord(self.database_name)
    	self.DeleteUI.setupUi(self.DeleteWord)
    	self.DeleteWord.show()
    def RemoveCatagory(self):
    	Ui_SpecificCatagory_Manager.DatabaseDeleted = True
    	self.SpecificCatagory_Manager.close()
    def ShowDetails(self):
    	self.Details = QtWidgets.QDialog()
    	self.DetailsUI = Ui_Details(self.catagory_name,self.catagory_desc)
    	self.DetailsUI.setupUi(self.Details)
    	self.Details.show()
    	
    def retranslateUi(self, SpecificCatagory_Manager):
        _translate = QtCore.QCoreApplication.translate
        SpecificCatagory_Manager.setWindowTitle(_translate("SpecificCatagory_Manager", "Vocabuilder"))
        self.opened_cata_banner.setText(_translate("SpecificCatagory_Manager", "Vocabuilder"))
        self.opened_cata_punchline.setText(_translate("SpecificCatagory_Manager", " - Here you will be able to keep track of learned words and also to manage the catagory you\'ve selected."))
        self.opened_cata_details.setText(_translate("SpecificCatagory_Manager", "Details"))
        self.opened_cata_addword.setText(_translate("SpecificCatagory_Manager", "Add Word"))
        self.opened_cata_removeword.setText(_translate("SpecificCatagory_Manager", "Remove Word"))
        self.opened_cata_deletecatagory.setText(_translate("SpecificCatagory_Manager", "Delete Catagory"))
        self.opened_cata_deletecatagory.clicked.connect(self.RemoveCatagory)
        self.opened_cata_addword.clicked.connect(self.AddWordWizard)
        self.opened_cata_removeword.clicked.connect(self.RemoveParticularWord)
        self.opened_cata_details.clicked.connect(self.ShowDetails)

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpecificCatagory_Manager = QtWidgets.QMainWindow()
    SpecificCatagory_ManagerUI = Ui_SpecificCatagory_Manager()
    SpecificCatagory_ManagerUI.setupUi(SpecificCatagory_Manager)
    SpecificCatagory_Manager.show()
    sys.exit(app.exec_())
"""