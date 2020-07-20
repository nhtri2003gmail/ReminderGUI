import sys
import os
import codecs

try:
    import PyQt5
except:
    os.system('pip install PyQt5')
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from datetime import datetime

##################### Variables ####################
TITLETIMECONTENT = '<TITLETIMECONTENT>'
NOTE = '<NOTE>'
## title_1
## time_1
## plainTextEdit_1
####################################################
ui,_ = loadUiType('UI\\note.ui')

class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Note")
        self.setGeometry(250,125,551,390)
        self.tableLine = 0
        self.pageDisplay = 0
        self.pageSetup = 0

        self.Set_Display()
#################################################################################   
    def Set_Display(self):
        with codecs.open('Data/note.txt', 'r', 'utf-8') as f:
            data=f.read()
        self.title_1.setText(data.split(TITLETIMECONTENT)[0])
        self.time_1.setText(data.split(TITLETIMECONTENT)[1])
        self.plainTextEdit_1.setPlainText(data.split(TITLETIMECONTENT)[2])

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()
