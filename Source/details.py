from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Details(object):
    def __init__(self,CatagoryName,CatagoryDesc):
        self.CatagoryName = CatagoryName
        self.CatagoryDesc = CatagoryDesc
        if len(self.CatagoryName) == 0:
            self.CatagoryName = "Unknown"
        elif len(self.CatagoryDesc) == 0:
            self.CatagoryDesc = "Unknown"
    def setupUi(self, Details):
        self.Details = Details
        self.Details.setObjectName("Details")
        self.Details.resize(622, 354)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        self.Details.setFont(font)
        self.details_label = QtWidgets.QLabel(self.Details)
        self.details_label.setGeometry(QtCore.QRect(150, 10, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Nokia Standard Light")
        font.setPointSize(30)
        self.details_label.setFont(font)
        self.details_label.setObjectName("details_label")
        self.gridLayoutWidget = QtWidgets.QWidget(Details)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 150, 301, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.details_cataname = QtWidgets.QLabel(self.gridLayoutWidget)
        self.details_cataname.setStyleSheet("color:green\n"
"")
        self.details_cataname.setText("")
        self.details_cataname.setObjectName("details_cataname")
        self.gridLayout.addWidget(self.details_cataname, 0, 1, 1, 1)
        self.details_catadesc = QtWidgets.QLabel(self.gridLayoutWidget)
        self.details_catadesc.setStyleSheet("color:green\n"
"")
        self.details_catadesc.setText("")
        self.details_catadesc.setObjectName("details_catadesc")
        self.gridLayout.addWidget(self.details_catadesc, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.details_ok = QtWidgets.QPushButton(Details)
        self.details_ok.setGeometry(QtCore.QRect(250, 300, 93, 41))
        self.details_ok.setObjectName("details_ok")
        self.label_5 = QtWidgets.QLabel(self.Details)
        self.label_5.setGeometry(QtCore.QRect(80, 90, 491, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.Details)
        self.line.setGeometry(QtCore.QRect(40, 120, 541, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(self.Details)
        QtCore.QMetaObject.connectSlotsByName(self.Details)
    def CloseDetailWindow(self):
        self.Details.close()
    def retranslateUi(self, Details):
        _translate = QtCore.QCoreApplication.translate
        self.Details.setWindowTitle(_translate("Details", "Current Catagory Details"))
        self.details_label.setText(_translate("Details", "Vocabuilder"))
        self.label.setText(_translate("Details", "Catagory Name : "))
        self.label_2.setText(_translate("Details", "Catagory Description : "))
        self.details_ok.setText(_translate("Details", "OK"))
        self.label_5.setText(_translate("Details", " - This Window Shows You The Current Catagory And It\'s Desciption."))
        self.details_cataname.setText(self.CatagoryName)
        self.details_catadesc.setText(self.CatagoryDesc)
        self.details_ok.clicked.connect(self.CloseDetailWindow)