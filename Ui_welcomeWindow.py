# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Img_rc/2048.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{\n"
"    border-image: url(./Img_rc/img1.jpg);\n"
"}\n"
"QVBoxLayout{\n"
"    border-image: none;\n"
"}\n"
"#playGameBtn,#configBtn,#instructionsBtn,#aboutBtn,QAbstractButton{\n"
"    border-image: none;\n"
"    font: 75 23pt;\n"
"    font-family: \'Indie Flower\', cursive, \"Bauhaus 93\";\n"
"    font-weight: bold;\n"
"    background: rgba(158, 127, 139, 0.6);\n"
"    color: rgb(255, 255, 255);\n"
"    border-image: none;\n"
"    border-radius: 8px;\n"
"    height: 35px;\n"
"}\n"
"#playGameBtn:hover ,#configBtn:hover ,#instructionsBtn:hover ,#aboutBtn:hover,QAbstractButton:hover {\n"
"   background: rgba(232, 12, 122, 0.6);\n"
"    color: rgba(59,3,31);\n"
"}\n"
"#title2048{    \n"
"    font: 72pt \"Bauhaus 93\";\n"
"    border-image: none;\n"
"    background-color:none;\n"
"    border-image: none;\n"
"    color: rgb(227, 227, 76);\n"
"}\n"
"QMessageBox{\n"
"    font: 16pt;\n"
"    font-family: \'Indie Flower\', cursive, \"Bauhaus 93\";\n"
"    border-image:url(./Img_rc/img5.jpg);\n"
"}\n"
"QMessageBox QLabel {\n"
"    border-image: none;\n"
"    color:white;\n"
"    font-weight: bold;\n"
"}\n"
"#quitBtn{\n"
"    border-image: url(./Img_rc/quit.png);\n"
"    background:none;\n"
"    width:50px;\n"
"    height: 50px;\n"
"}\n"
"#quitBtn:hover{\n"
"    border-image: url(./Img_rc/quitHover.png);\n"
"    background:none;\n"
"}")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.welcomeLayoutV = QtWidgets.QVBoxLayout()
        self.welcomeLayoutV.setObjectName("welcomeLayoutV")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.quitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.quitBtn.setEnabled(True)
        self.quitBtn.setText("")
        self.quitBtn.setObjectName("quitBtn")
        self.horizontalLayout_3.addWidget(self.quitBtn)
        self.welcomeLayoutV.addLayout(self.horizontalLayout_3)
        self.layoutUp = QtWidgets.QVBoxLayout()
        self.layoutUp.setObjectName("layoutUp")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutUp.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.title2048 = QtWidgets.QLabel(self.centralwidget)
        self.title2048.setObjectName("title2048")
        self.horizontalLayout.addWidget(self.title2048)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.layoutUp.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutUp.addItem(spacerItem4)
        self.welcomeLayoutV.addLayout(self.layoutUp)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.playGameBtn = QtWidgets.QPushButton(self.centralwidget)
        self.playGameBtn.setObjectName("playGameBtn")
        self.verticalLayout.addWidget(self.playGameBtn)
        self.instructionsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.instructionsBtn.setObjectName("instructionsBtn")
        self.verticalLayout.addWidget(self.instructionsBtn)
        self.configBtn = QtWidgets.QPushButton(self.centralwidget)
        self.configBtn.setObjectName("configBtn")
        self.verticalLayout.addWidget(self.configBtn)
        self.aboutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.aboutBtn.setObjectName("aboutBtn")
        self.verticalLayout.addWidget(self.aboutBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.welcomeLayoutV.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.welcomeLayoutV.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.welcomeLayoutV)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2048"))
        self.title2048.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">2048</p></body></html>"))
        self.playGameBtn.setText(_translate("MainWindow", "  Jouer  "))
        self.instructionsBtn.setText(_translate("MainWindow", "  Instructions  "))
        self.configBtn.setText(_translate("MainWindow", "  Réglages  "))
        self.aboutBtn.setText(_translate("MainWindow", "  À propos de  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

