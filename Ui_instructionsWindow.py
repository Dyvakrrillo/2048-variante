# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instructionsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_instructionsWindow(object):
    def setupUi(self, instructionsWindow):
        instructionsWindow.setObjectName("instructionsWindow")
        instructionsWindow.resize(800, 650)
        instructionsWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Img_rc/manualIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        instructionsWindow.setWindowIcon(icon)
        instructionsWindow.setStyleSheet("QDialog{\n"
"    border-image: url(./Img_rc/img4.jpg);\n"
"}\n"
"QLabel{\n"
"    font: 20pt;\n"
"    font-family: \'Patrick Hand\', cursive, \"Georgia\";\n"
"    font-weight: bold;\n"
"    background: rgba(232, 12, 122, 0.0);\n"
"    color: rgb(237, 223, 238);\n"
"}\n"
"QPushButton{\n"
"    border-image: none;\n"
"    font: 75 24pt;\n"
"    font-family: \'Indie Flower\', cursive, \"Georgia\";\n"
"    font-weight: bold;\n"
"    background: rgba(158, 127, 139, 0.4);\n"
"    color:white;\n"
"    border-image: none;\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"   background: rgba(232, 12, 122, 0.6);\n"
"    color: rgba(59,3,31);\n"
"}")
        instructionsWindow.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(instructionsWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(instructionsWindow)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.accepterBtn = QtWidgets.QPushButton(instructionsWindow)
        self.accepterBtn.setObjectName("accepterBtn")
        self.horizontalLayout_2.addWidget(self.accepterBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(instructionsWindow)
        QtCore.QMetaObject.connectSlotsByName(instructionsWindow)

    def retranslateUi(self, instructionsWindow):
        _translate = QtCore.QCoreApplication.translate
        instructionsWindow.setWindowTitle(_translate("instructionsWindow", "Instructions"))
        self.label.setText(_translate("instructionsWindow", "<html><head/><body><p align=\"justify\">Le gameplay du jeu repose sur l\'utilisation des touches fléchées du clavier<br/>ou des touches ( Z - Q - S - D ) pour déplacer les tuiles vers la gauche, la <br/>droite, le haut ou le bas. </p><p align=\"justify\">Lors d\'un mouvement, l\'ensemble des tuiles du plateau sont déplacés <br/>dans la même direction jusqu\'à rencontrer les bords du plateau ou une <br/>autre tuile sur leur chemin. </p><p align=\"justify\">Si deux tuiles, ayant le même nombre, entrent en collision durant le <br/>mouvement, elles fusionnent en une nouvelle tuile de valeur double <br/>(par ex. : deux tuiles de valeur « 2 » donnent une tuile de valeur « 4 »). </p><p align=\"justify\">À chaque mouvement, une tuile portant un 2 ou un 4 apparaît dans une <br/>case vide de manière aléatoire.</p></body></html>"))
        self.accepterBtn.setText(_translate("instructionsWindow", "  Accepter  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    instructionsWindow = QtWidgets.QDialog()
    ui = Ui_instructionsWindow()
    ui.setupUi(instructionsWindow)
    instructionsWindow.show()
    sys.exit(app.exec_())

