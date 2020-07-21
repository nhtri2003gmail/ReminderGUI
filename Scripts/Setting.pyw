import os
import sys

try:
    import PyQt5
except:
    os.system('pip install PyQt5')
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from datetime import datetime

try:
    import winshell
except:
    os.system('pip install winshell')
    os.system('pip install pywin32')
from swinlnk.swinlnk import SWinLnk

######################################################

ui,_ = loadUiType('UI\\setting.ui')

class Setting(QMainWindow,ui):
    def __init__(self, parent=None):
        super(Setting, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Setting')
        self.setGeometry(400,300,765,280)
        self.Button_Handle()

        self.Create_Folder()
        self.Get_Homepath()
        self.Set_Conf()

    def Create_Folder(self):
        if not os.path.isdir('Data'):
            os.mkdir('Data')
        if not os.path.isdir('Data/Notes'):
            os.mkdir('Data/Notes')
        if not os.path.isdir('Data/Weekly'):
            os.mkdir('Data/Weekly')

        if not os.path.isdir('Data/Notes/1'):
            os.mkdir('Data/Notes/1')
        if not os.path.isdir('Data/Notes/2'):
            os.mkdir('Data/Notes/2')
        if not os.path.isdir('Data/Notes/3'):
            os.mkdir('Data/Notes/3')
        if not os.path.isdir('Data/Notes/4'):
            os.mkdir('Data/Notes/4')
        if not os.path.isdir('Data/Notes/5'):
            os.mkdir('Data/Notes/5')
        if not os.path.isdir('Data/Notes/6'):
            os.mkdir('Data/Notes/6')
        if not os.path.isdir('Data/Notes/7'):
            os.mkdir('Data/Notes/7')
        if not os.path.isdir('Data/Notes/8'):
            os.mkdir('Data/Notes/8')
        if not os.path.isdir('Data/Notes/9'):
            os.mkdir('Data/Notes/9')
        if not os.path.isdir('Data/Notes/10'):
            os.mkdir('Data/Notes/10')
        if not os.path.isdir('Data/Notes/11'):
            os.mkdir('Data/Notes/11')
        if not os.path.isdir('Data/Notes/12'):
            os.mkdir('Data/Notes/12')
        
        
    def Get_Homepath(self):
        if not os.path.exists('Data/HOMEPATH.txt'):
            os.system('echo %HOMEPATH% > Data/HOMEPATH.txt')
        with open('Data/HOMEPATH.txt', 'rt') as f:
            tmp = f.read()
        homePath=''
        for i in range(0,len(tmp)-2):
            homePath+=tmp[i]
        return homePath
    
    def Set_Startup(self):
        homePath = self.Get_Homepath()
        startupPath = 'C:' + homePath + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Start_Reminder.lnk'

        currentPath = str(os.getcwd())
        fullPath = currentPath + '\\Start_Reminder.pyw'
        
        with winshell.shortcut(startupPath) as link:
            link.path = fullPath
            link.working_directory = currentPath

    def Set_Conf(self):
        os.chdir('Data')
        if os.path.exists('setting.conf'):
            with open('setting.conf', 'r') as f:
                conf = f.read()
            tmp = conf.split('\n')
            self.startUp.setCheckState(int(tmp[0]))
            self.afterPeriod.setCheckState(int(tmp[1].split(' ')[0]))
            self.beforeNoteTime.setCheckState(int(tmp[2].split(' ')[0]))
            self.afterPeriodSpin.setValue(int(tmp[1].split(' ')[1]))
            self.beforeNoteTimeSpin.setValue(int(tmp[2].split(' ')[1]))
        os.chdir('../')

    def Button_Handle(self):
        self.saveButton.clicked.connect(self.Save_Config)
        self.resetDefaultButton.clicked.connect(self.Set_Default_Config)

    def Save_Config(self):
        self.Set_Startup()
        os.chdir('Data')
        with open('setting.conf', 'w') as f:
            f.write(str(self.startUp.checkState()) + '\n')
            f.write(str(self.afterPeriod.checkState()) + ' ' + str(self.afterPeriodSpin.value()) + '\n')
            f.write(str(self.beforeNoteTime.checkState()) + ' ' + str(self.beforeNoteTimeSpin.value()))
        os.chdir('../')

    def Set_Default_Config(self):
        self.startUp.setCheckState(0)
        self.afterPeriod.setCheckState(0)
        self.beforeNoteTime.setCheckState(0)
        self.afterPeriodSpin.setValue(0)
        self.beforeNoteTimeSpin.setValue(0)
        

def main():
    app=QApplication(sys.argv)
    window = Setting()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()

