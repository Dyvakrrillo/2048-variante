# -*- coding: utf-8 -*-
# start_app.py
# utilisation de Qt designer

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from welcomeWindow import MainWindowGame

app = QApplication(sys.argv)
QFontDatabase.addApplicationFont("./fonts/IndieFlower.ttf")
QFontDatabase.addApplicationFont("./fonts/PatrickHand-Regular.ttf" )
QFontDatabase.addApplicationFont("./fonts/RockSalt-Regular.ttf" )

translator = QTranslator()
translator.load("gameapp_en")
app.installTranslator(translator)

mainWindowGame = MainWindowGame()
mainWindowGame.show()

rc = app.exec_()
sys.exit(rc)


