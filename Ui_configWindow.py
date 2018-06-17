# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_configWindow(object):
    def setupUi(self, configWindow):
        configWindow.setObjectName("configWindow")
        configWindow.resize(643, 434)
        configWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Img_rc/configIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        configWindow.setWindowIcon(icon)
        configWindow.setStyleSheet("QWidget, #configWindow{\n"
"    border-image: url(./Img_rc/img4.jpg);\n"
"	alternate-background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.0511364 rgba(0, 0, 0, 255), stop:0.142045 rgba(255, 63, 128, 207), stop:0.232955 rgba(0, 0, 0, 255), stop:0.301136 rgba(171, 236, 51, 219), stop:0.369318 rgba(0, 0, 0, 255), stop:0.426136 rgba(255, 183, 0, 227), stop:0.505682 rgba(245, 46, 138, 221), stop:0.607955 rgba(0, 0, 0, 245), stop:0.698864 rgba(182, 248, 0, 210), stop:0.710227 rgba(255, 255, 0, 212), stop:0.795455 rgba(0, 0, 0, 255), stop:0.875 rgba(228, 0, 203, 227), stop:0.909091 rgba(228, 0, 87, 227), stop:0.960227 rgba(0, 0, 0, 227));"
"}\n"
"#musicComboBox,#gameModeComboBox{\n"
"    border-image: none;\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(212, 16, 104, 0.6);\n"
"    font: 15pt;\n"
"    font-family: \'Patrick Hand\', cursive, \"Magneto\";\n"
"    font-weight: bold;\n"
"\n"
"    border-radius: 6px;\n"
"    width: 200px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border-image:none;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 16pt;\n"
"    background: rgba(212, 16, 104, 0.6);\n"
"    border-radius: 6px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    border-image: url(./Img_rc/Down-Arrow-Transparent-Image.png);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border-image: none;\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(212, 16, 104, 0.6);\n"
"    font: 16pt;\n"
"    border-radius: 6px;\n"
"    selection-background-color:rgb(138, 138, 138);\n"
"}\n"
"#soundBtn{\n"
"    border-image: none;\n"
"}\n"
" QCheckBox::indicator {\n"
"     width: 80px;\n"
"     height: 80px;\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    border-image: url(./Img_rc/sound.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"    border-image: url(./Img_rc/soundOFF.png);\n"
"}\n"
"#titleGameMode,#titleMusic{\n"
"    font: 75 22pt;\n"
"    font-family: \'Rock Salt\', cursive, \"Magneto\";\n"
"    font-weight: bold;\n"
"    border-image: none;\n"
"    background-color:none;\n"
"    border-image: none;    \n"
"    color: rgb(193, 82, 149);\n"
"}\n"
"#accepterBtn{\n"
"    border-image: none;\n"
"    font: 75 24pt;\n"
"    font-family: \'Indie Flower\', cursive, \"Bauhaus 93\";\n"
"    font-weight: bold;\n"
"    background: rgba(158, 127, 139, 0.6);\n"
"    color: rgb(255, 255, 255);\n"
"    border-image: none;\n"
"    border-radius: 8px;\n"
"}\n"
"#accepterBtn:hover {\n"
"   background: rgba(232, 12, 122, 0.6);\n"
"    color: rgba(59,3,31);\n"
"}\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"    border-image: none;\n"
"}\n"
"")
        configWindow.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(configWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout1 = QtWidgets.QVBoxLayout()
        self.verticalLayout1.setObjectName("verticalLayout1")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout1.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.titleGameMode = QtWidgets.QLabel(configWindow)
        self.titleGameMode.setObjectName("titleGameMode")
        self.horizontalLayout_2.addWidget(self.titleGameMode)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gameModeComboBox = QtWidgets.QComboBox(configWindow)
        self.gameModeComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gameModeComboBox.setObjectName("gameModeComboBox")
        self.gameModeComboBox.addItem("")
        self.gameModeComboBox.addItem("")
        self.gameModeComboBox.addItem("")
        self.gameModeComboBox.addItem("")
        self.gameModeComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.gameModeComboBox)
        self.labelStr = QtWidgets.QLabel(configWindow)
        self.labelStr.setStyleSheet("")
        self.labelStr.setText("")
        self.labelStr.setObjectName("labelStr")
        self.horizontalLayout_3.addWidget(self.labelStr)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout1.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleMusic = QtWidgets.QLabel(configWindow)
        self.titleMusic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.titleMusic.setObjectName("titleMusic")
        self.horizontalLayout.addWidget(self.titleMusic)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.musicComboBox = QtWidgets.QComboBox(configWindow)
        self.musicComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.musicComboBox.setObjectName("musicComboBox")
        self.musicComboBox.addItem("")
        self.musicComboBox.addItem("")
        self.musicComboBox.addItem("")
        self.musicComboBox.addItem("")
        self.musicComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.musicComboBox)
        self.soundBtn = QtWidgets.QCheckBox(configWindow)
        self.soundBtn.setEnabled(True)
        self.soundBtn.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.soundBtn.setText("")
        self.soundBtn.setChecked(True)
        self.soundBtn.setTristate(False)
        self.soundBtn.setObjectName("soundBtn")
        self.horizontalLayout_4.addWidget(self.soundBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout1.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout1.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.accepterBtn = QtWidgets.QPushButton(configWindow)
        self.accepterBtn.setEnabled(True)
        self.accepterBtn.setObjectName("accepterBtn")
        self.horizontalLayout_5.addWidget(self.accepterBtn)
        self.verticalLayout1.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout1)

        self.retranslateUi(configWindow)
        QtCore.QMetaObject.connectSlotsByName(configWindow)

    def retranslateUi(self, configWindow):
        _translate = QtCore.QCoreApplication.translate
        configWindow.setWindowTitle(_translate("configWindow", "Réglages"))
        self.titleGameMode.setText(_translate("configWindow", "Jouer en mode... "))
        self.gameModeComboBox.setItemText(0, _translate("configWindow", "Ça passe"))
        self.gameModeComboBox.setItemText(1, _translate("configWindow", "Ouh la..."))
        self.gameModeComboBox.setItemText(2, _translate("configWindow", "Ça devient serieux"))
        self.gameModeComboBox.setItemText(3, _translate("configWindow", "7x7=49"))
        self.gameModeComboBox.setItemText(4, _translate("configWindow", "Cauchemard"))
        self.titleMusic.setText(_translate("configWindow", "Musique du jeu :"))
        self.musicComboBox.setItemText(0, _translate("configWindow", "Seven Twenty"))
        self.musicComboBox.setItemText(1, _translate("configWindow", "Church of 8 Wheels"))
        self.musicComboBox.setItemText(2, _translate("configWindow", "Firefly"))
        self.musicComboBox.setItemText(3, _translate("configWindow", "Hi Q"))
        self.musicComboBox.setItemText(4, _translate("configWindow", "Renegade Jubilee"))
        self.accepterBtn.setText(_translate("configWindow", "  Accepter  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    configWindow = QtWidgets.QWidget()
    ui = Ui_configWindow()
    ui.setupUi(configWindow)
    configWindow.show()
    sys.exit(app.exec_())

