# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multimedia.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res_mul
from pythonProject.projectmain.sliderpage.slider import SecondWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1242, 860)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 1251, 841))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("border: none;")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setGeometry(QtCore.QRect(200, 20, 791, 121))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setGeometry(QtCore.QRect(320, 20, 371, 81))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_7 = QtWidgets.QFrame(self.frame_8)
        self.frame_7.setGeometry(QtCore.QRect(210, 10, 101, 101))
        self.frame_7.setStyleSheet("image: url(:/mul_photos/multimedia_logo.png);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(110, 160, 1081, 91))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        self.label_13.setGeometry(QtCore.QRect(110, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.frame_14 = QtWidgets.QFrame(self.frame_9)
        self.frame_14.setGeometry(QtCore.QRect(240, 0, 841, 91))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_23 = QtWidgets.QLabel(self.frame_14)
        self.label_23.setGeometry(QtCore.QRect(30, 10, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_14)
        self.label_24.setGeometry(QtCore.QRect(30, 40, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.push_multi_1 = QtWidgets.QPushButton(self.frame_9)
        self.push_multi_1.setGeometry(QtCore.QRect(10, 10, 91, 75))
        self.push_multi_1.setStyleSheet("\n"
"border: none")
        self.push_multi_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mul_photos/vlc_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_multi_1.setIcon(icon)
        self.push_multi_1.setIconSize(QtCore.QSize(120, 120))
        self.push_multi_1.setObjectName("push_multi_1")
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setGeometry(QtCore.QRect(110, 280, 1081, 91))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_14 = QtWidgets.QLabel(self.frame_10)
        self.label_14.setGeometry(QtCore.QRect(110, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.frame_15 = QtWidgets.QFrame(self.frame_10)
        self.frame_15.setGeometry(QtCore.QRect(240, 0, 841, 91))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_25 = QtWidgets.QLabel(self.frame_15)
        self.label_25.setGeometry(QtCore.QRect(30, 10, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_15)
        self.label_26.setGeometry(QtCore.QRect(30, 40, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.push_multi_2 = QtWidgets.QPushButton(self.frame_10)
        self.push_multi_2.setGeometry(QtCore.QRect(10, 10, 91, 71))
        self.push_multi_2.setStyleSheet("\n"
"border: none")
        self.push_multi_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mul_photos/gimp_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_multi_2.setIcon(icon1)
        self.push_multi_2.setIconSize(QtCore.QSize(100, 100))
        self.push_multi_2.setObjectName("push_multi_2")
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setGeometry(QtCore.QRect(110, 400, 1081, 91))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_16 = QtWidgets.QLabel(self.frame_12)
        self.label_16.setGeometry(QtCore.QRect(110, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.frame_17 = QtWidgets.QFrame(self.frame_12)
        self.frame_17.setGeometry(QtCore.QRect(240, 0, 841, 91))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_29 = QtWidgets.QLabel(self.frame_17)
        self.label_29.setGeometry(QtCore.QRect(30, 10, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_17)
        self.label_30.setGeometry(QtCore.QRect(30, 40, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.push_multi_3 = QtWidgets.QPushButton(self.frame_12)
        self.push_multi_3.setGeometry(QtCore.QRect(0, 10, 91, 71))
        self.push_multi_3.setStyleSheet("\n"
"border: none")
        self.push_multi_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mul_photos/chesse_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_multi_3.setIcon(icon2)
        self.push_multi_3.setIconSize(QtCore.QSize(100, 80))
        self.push_multi_3.setObjectName("push_multi_3")
        self.frame_13 = QtWidgets.QFrame(self.frame)
        self.frame_13.setGeometry(QtCore.QRect(110, 520, 1081, 91))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_17 = QtWidgets.QLabel(self.frame_13)
        self.label_17.setGeometry(QtCore.QRect(110, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.frame_18 = QtWidgets.QFrame(self.frame_13)
        self.frame_18.setGeometry(QtCore.QRect(240, 0, 841, 91))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_31 = QtWidgets.QLabel(self.frame_18)
        self.label_31.setGeometry(QtCore.QRect(30, 10, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame_18)
        self.label_32.setGeometry(QtCore.QRect(30, 40, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.push_multi_4 = QtWidgets.QPushButton(self.frame_13)
        self.push_multi_4.setGeometry(QtCore.QRect(10, 10, 81, 71))
        self.push_multi_4.setStyleSheet("\n"
"border: none")
        self.push_multi_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mul_photos/um_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_multi_4.setIcon(icon3)
        self.push_multi_4.setIconSize(QtCore.QSize(80, 69))
        self.push_multi_4.setObjectName("push_multi_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1242, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MULTIMEDIA"))
        self.label_13.setText(_translate("MainWindow", "VLC"))
        self.label_23.setText(_translate("MainWindow", "A versatile, open-source multimedia player supporting various audio and video formats, with customizable "))
        self.label_24.setText(_translate("MainWindow", "features and robust playback capabilities."))
        self.label_14.setText(_translate("MainWindow", "GIMP"))
        self.label_25.setText(_translate("MainWindow", "A free and powerful image editing software offering versatile tools for graphic design, photo manipulation, "))
        self.label_26.setText(_translate("MainWindow", "and digital art creation."))
        self.label_16.setText(_translate("MainWindow", "Chesse"))
        self.label_29.setText(_translate("MainWindow", "An intuitive, user-friendly software for capturing photos and videos through webcam, with basic editing "))
        self.label_30.setText(_translate("MainWindow", "and sharing functionalities."))
        self.label_17.setText(_translate("MainWindow", "UM Player"))
        self.label_31.setText(_translate("MainWindow", "Lightweight, feature-rich media player with support for numerous formats, customizable interface, and "))
        self.label_32.setText(_translate("MainWindow", "seamless playback experience for users."))

        self.push_multi_1.clicked.connect(self.VLC)
        self.push_multi_2.clicked.connect(self.GIMP)
        self.push_multi_3.clicked.connect(self.cheese)
        self.push_multi_4.clicked.connect(self.UM_Player)
    def VLC(self):
        label_text = "VLC"
        label_disc = "A versatile, open-source multimedia player supporting various audio and video formats, with customizable features and robust playback capabilities."
        label_image = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/Multimedia/vlc_logo.png"
        soft_weight = 10
        self.open_slider(label_text, label_disc, label_image,soft_weight)

    def GIMP(self):
        label_text = "GIMP"
        label_disc = "A free and powerful image editing software offering versatile tools for graphic design, photo manipulation,and digital art creation."
        label_image = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/Multimedia/gimp_logo.png"
        soft_weight = 11
        self.open_slider(label_text, label_disc, label_image,soft_weight)

    def cheese(self):
        label_text = "Cheese"
        label_disc = "An intuitive, user-friendly software for capturing photos and videos through webcam, with basic editing and sharing functionalities."
        label_image = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/Multimedia/chesse_logo.png"
        soft_weight = 12
        self.open_slider(label_text, label_disc, label_image,soft_weight)

    def UM_Player(self):
        label_text = "UM Player"
        label_disc = "Lightweight, feature-rich media player with support for numerous formats, customizable interface, and seamless playback experience for users."
        label_image = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/Multimedia/um_logo.png"
        soft_weight = 13
        self.open_slider(label_text, label_disc, label_image,soft_weight)

    def open_slider(self, label_text, label_disc, label_image,soft_weight ):
        self.second_window = SecondWindow(parent=self.centralwidget, label_text=label_text, label_disc=label_disc,
                                          label_image=label_image,soft_weight=soft_weight)
        self.second_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.second_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
