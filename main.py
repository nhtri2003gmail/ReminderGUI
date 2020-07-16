import sys
import os
import os.path
import codecs

import _GetPath
import _StringOp

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
ROWCOLUMNITEM = '<ROWCOLUMNITEM>'
TITLETIMECONTENT = '<TITLETIMECONTENT>'

currentDate = str(datetime.now().date())

class Note:
    title = []
    time = []
    content = []
####################################################
ui,_ = loadUiType('main.ui')

class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Reminder GUI")
        self.setGeometry(250,125,120000,700)
        self.tableLine = 0
        self.pageDisplay = 0
        self.pageSetup = 0
        self.calendarWidgetSetupCreate.setSelectedDate(QDate(int(currentDate.split('-')[0]), int(currentDate.split('-')[1]), int(currentDate.split('-')[2])))
        self.calendarWidgetSetupEdit.setSelectedDate(QDate(int(currentDate.split('-')[0]), int(currentDate.split('-')[1]), int(currentDate.split('-')[2])))
        self.calendarWidgetDisplay.setSelectedDate(QDate(int(currentDate.split('-')[0]), int(currentDate.split('-')[1]), int(currentDate.split('-')[2])))

        self.Button_Handler()
        try:
            self.Set_Table()
        except:
            pass
        
    def Set_Table(self):
        os.chdir(_GetPath.Weekly_Path())
        with codecs.open('WeeklySave.txt', 'r', 'utf-8') as f:
            data = f.read()
        cells = data.split('\n')
        self.tableWidgetSetup.setRowCount(int(cells[0]))    ## Set Row Table
        self.tableWidgetDisplay.setRowCount(int(cells[0]))  ## Set Row Table
        self.tableLine = int(cells[0])
        
        for i in range(1,len(cells)-1):
            tmp = cells[i].split(ROWCOLUMNITEM)
            self.tableWidgetSetup.setItem(int(tmp[0]), int(tmp[1]), QTableWidgetItem(tmp[2]))
            self.tableWidgetDisplay.setItem(int(tmp[0]), int(tmp[1]), QTableWidgetItem(tmp[2]))        

    def Button_Handler(self):
        self.seeNote.clicked.connect(self.See_Note)
        self.weeklySave.clicked.connect(self.Weekly_Save)
        self.addLine.clicked.connect(self.Add_Line)
        self.removeLine.clicked.connect(self.Remove_Line)
##        self.pushButton.clicked.connect(self.Notes_Save)
        self.prevPageDisplay.clicked.connect(self.Prev_Page_Display)
        self.nextPageDisplay.clicked.connect(self.Next_Page_Display)
        self.prevPageSetup.clicked.connect(self.Prev_Page_Setup)
        self.nextPageSetup.clicked.connect(self.Next_Page_Setup)
        self.setupCreateButton.clicked.connect(self.Create_Note)

    def Add_Line(self):
        self.tableLine += 1
        self.tableWidgetSetup.setRowCount(self.tableLine)

    def Remove_Line(self):
        self.tableLine -= 1
        self.tableWidgetSetup.setRowCount(self.tableLine)

    def Weekly_Save(self):
        weeklyPath = _GetPath.Weekly_Path()
        os.chdir(weeklyPath)
        row = self.tableWidgetSetup.rowCount()
        column = self.tableWidgetSetup.columnCount()
        
        with codecs.open('WeeklySave.txt', 'w', 'utf-8') as f:
            f.write(str(self.tableLine) + '\n')
            for i in range(0,row):
                for j in range(0,column):
                    try:
                        item = str(self.tableWidgetSetup.item(i,j).text())
                        cell = str(i) + ROWCOLUMNITEM + str(j) + ROWCOLUMNITEM + item + '\n'
                        f.write(cell)
                    except:
                        pass      
        self.tableWidgetDisplay.setRowCount(0)  ## Set Row Table
        self.Set_Table()

    def See_Note(self):
        selectedDate = self.calendarWidgetDisplay.selectedDate().getDate()
        dateFormat = _StringOp.DateFormatDash(str(selectedDate)) + '.txt'
        print(dateFormat)
        os.chdir(_GetPath.Note_Path())
        if os.path.exists(dateFormat):
            print('exist')
        else:
            print('non-exist')



    def Prev_Page_Display(self):
        if self.pageDisplay>0:
            self.pageDisplay -= 1
        self.stackedWidgetDisplay.setCurrentIndex(self.pageDisplay)

    def Next_Page_Display(self):
        if self.pageDisplay<9:
            self.pageDisplay += 1
        self.stackedWidgetDisplay.setCurrentIndex(self.pageDisplay)

    def Prev_Page_Setup(self):
        if self.pageSetup>0:
            self.pageSetup -= 1
        self.stackedWidgetSetup.setCurrentIndex(self.pageSetup)

    def Next_Page_Setup(self):
        if self.pageSetup<9:
            self.pageSetup += 1
        self.stackedWidgetSetup.setCurrentIndex(self.pageSetup)

    def Create_Note(self):
        selectedDate = self.calendarWidgetSetupCreate.selectedDate().getDate()
        title = self.titleSetup.text()
        h = str(self.timeSetup.time().hour())       ## Convert int to string
        m = str(self.timeSetup.time().minute())     ## Convert int to string
        time = h + ':' + m
        content = self.plainTextEditSetup.toPlainText()
        note = title + TITLETIMECONTENT + time + TITLETIMECONTENT + content + '\n'
        
        dateFormat = _StringOp.DateFormatDash(str(selectedDate)) + '.txt'
        os.chdir(_GetPath.Note_Path())
        if os.path.exists(dateFormat):
            with codecs.open(dateFormat, 'a', 'utf-8') as f:
                f.write(note)
        else:
            with codecs.open(dateFormat, 'w', 'utf-8') as f:
                f.write(note)

        self.titleSetup.clear()
        content = self.plainTextEditSetup.clear()

    

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()
