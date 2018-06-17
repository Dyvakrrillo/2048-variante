from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_instructionsWindow import Ui_instructionsWindow


class WindowInstructions(QDialog, Ui_instructionsWindow):
    flagInstructions=False
    def __init__(self, parent=None):
        super(WindowInstructions,self).__init__(parent)
        self.setupUi(self)
        
        #Flag qui indique que la fenetre est ouverte
        self.flagInstructions=True
      
    @pyqtSlot()
    def on_accepterBtn_clicked(self):
        self.flagInstructions=False
        self.close()
