# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        aboutWindow.setObjectName("aboutWindow")
        aboutWindow.resize(680, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Img_rc/aboutIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutWindow.setWindowIcon(icon)
        aboutWindow.setStyleSheet("#aboutWindow{\n"
"    border-image: url(./Img_rc/img2.jpg);\n"
"}\n"
"QPushButton{\n"
"    border-image: none;\n"
"    font: 75 16pt;\n"
"    font-family: \'Indie Flower\', cursive, \"Bauhaus 93\";\n"
"    font-weight: bold;\n"
"    background: rgba(158, 127, 139, 0.6);\n"
"    color: rgb(255, 255, 255);\n"
"    border-image: none;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"   background: rgba(232, 12, 122, 0.6);\n"
"    color: rgba(59,3,31);\n"
"}\n"
"#retourBtn{\n"
"    width:10px;\n"
"}")
        aboutWindow.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.gridLayout_2 = QtWidgets.QGridLayout(aboutWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(aboutWindow)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(aboutWindow)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(aboutWindow)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(aboutWindow)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(aboutWindow)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(aboutWindow)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(aboutWindow)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(aboutWindow)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cindyBtn = QtWidgets.QPushButton(aboutWindow)
        self.cindyBtn.setObjectName("cindyBtn")
        self.verticalLayout.addWidget(self.cindyBtn)
        self.stephBtn = QtWidgets.QPushButton(aboutWindow)
        self.stephBtn.setObjectName("stephBtn")
        self.verticalLayout.addWidget(self.stephBtn)
        self.cyrilBtn = QtWidgets.QPushButton(aboutWindow)
        self.cyrilBtn.setObjectName("cyrilBtn")
        self.verticalLayout.addWidget(self.cyrilBtn)
        self.loickBtn = QtWidgets.QPushButton(aboutWindow)
        self.loickBtn.setObjectName("loickBtn")
        self.verticalLayout.addWidget(self.loickBtn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.retourBtn = QtWidgets.QPushButton(aboutWindow)
        self.retourBtn.setObjectName("retourBtn")
        self.horizontalLayout.addWidget(self.retourBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        _translate = QtCore.QCoreApplication.translate
        aboutWindow.setWindowTitle(_translate("aboutWindow", "A propos de"))
        self.cindyBtn.setText(_translate("aboutWindow", "Cindy Carrillo"))
        self.stephBtn.setText(_translate("aboutWindow", "Stephane Bernard"))
        self.cyrilBtn.setText(_translate("aboutWindow", "Cyril Delpierre"))
        self.loickBtn.setText(_translate("aboutWindow", "Loick Appere"))
        self.retourBtn.setText(_translate("aboutWindow", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutWindow = QtWidgets.QDialog()
    ui = Ui_aboutWindow()
    ui.setupUi(aboutWindow)
    aboutWindow.show()
    sys.exit(app.exec_())

