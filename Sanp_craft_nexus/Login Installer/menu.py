# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res2
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1919, 1082)

        # Existing QLabel with background image
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1040))  # Match the size of the window
        self.label.setStyleSheet("border-image: url(:/images/360_F_195508679_tMnsBg8hznqrvJNFPyZD7qFUyyzdc56M.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(700, 0, 561, 371))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setStyleSheet("image: url(:/images/loho-removebg-preview.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 390, 210, 75))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius: 15px; \n"
"\n"
"background-color: #ffffff;\n"
"text-align: right;\n"
"padding-right: 18px;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/Icons/media-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(95, 48))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 600, 210, 75))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(17)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius: 15px; \n"
"background-color: #ffffff;\n"
"text-align: right;\n"
"padding-right: 5px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/Icons/Productivity-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(89, 42))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 390, 210, 75))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(17)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius: 15px; \n"
"background-color: #ffffff;\n"
"text-align: right;\n"
"padding-right: 18px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/Icons/Graphics-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(85, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1170, 390, 210, 75))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(17)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius: 15px; \n"
"background-color: #ffffff;\n"
"text-align: right;\n"
"padding-right: 15px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/Icons/code_editor-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(90, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(1170, 600, 210, 75))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(17)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-radius: 15px; \n"
"background-color: #ffffff;\n"
"text-align: right;\n"
"padding-right: 15px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/Icons/web_scan-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(70, 35))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.webscan)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(860, 600, 210, 75))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(17)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-radius: 15px; \n"
"background-color: #ffffff;\n"
"text-align: right;\n"
"padding-right: 15px;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/Icons/Utiliti-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(85, 40))
        self.pushButton_6.setObjectName("pushButton_6")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 370, 51, 41))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_6.clicked.connect(self.utility)
        self.pushButton_5.clicked.connect(self.webscan)
        self.pushButton_4.clicked.connect(self.codeeditor)
        self.pushButton_3.clicked.connect(self.tools)
        self.pushButton_2.clicked.connect(self.Productivity)
        self.pushButton.clicked.connect(self.run_multimeda)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", " Multimedia"))
        self.pushButton_2.setText(_translate("Form", "Producitivity "))
        self.pushButton_3.setText(_translate("Form", "       Tools    "))
        self.pushButton_4.setText(_translate("Form", " Code Editor"))
        self.pushButton_5.setText(_translate("Form", "    Web Scan"))
        self.pushButton_6.setText(_translate("Form", "      Utilities "))

    def run_multimeda(self):
        path_to_tools_py = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/Multimedia/multimedia.py"
        command = f"python {path_to_tools_py}"
        print("Executing command:", command)
        os.system(command)
    def Productivity(self):
        path_to_tools_py = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/Productivity/Productivity.py"
        command = f"python {path_to_tools_py}"
        print("Executing command:", command)
        os.system(command)
    def utility(self):
        path_to_tools_py = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/Utility/utility.py"
        command = f"python {path_to_tools_py}"
        print("Executing command:", command)
        os.system(command)
    def webscan(self):
        path_to_tools_py = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/WebScan/WebScan.py"
        command = f"python {path_to_tools_py}"
        print("Executing command:", command)
        os.system(command)
    def tools(self):
        path_to_tools_py = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/Tools/Tools.py"
        command = f"python {path_to_tools_py}"
        print("Executing command:", command)
        os.system(command)
    def codeeditor(self):
        path_to_tools_py = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/codeeditor/Code_editor.py"
        command = f"python {path_to_tools_py}"
        print("Executing command:", command)
        os.system(command)


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
