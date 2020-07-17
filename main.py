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
NOTE = '<NOTE>'

currentDate = str(datetime.now().date())

class Note:
    title = []
    date = ''
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
        
    def Button_Handler(self):
        pageDisplay = [self.prevPageDisplay,
                        self.nextPageDisplay]
        pageSetup = [self.prevPageSetup,
                        self.nextPageSetup]
        
        self.seeNoteDisplay.clicked.connect(self.See_Notes_Display)
        self.weeklySave.clicked.connect(self.Weekly_Save)
        self.addLine.clicked.connect(self.Add_Line)
        self.removeLine.clicked.connect(self.Remove_Line)
        pageDisplay[0].clicked.connect(self.Prev_Page_Display)
        pageDisplay[1].clicked.connect(self.Next_Page_Display)
        pageSetup[0].clicked.connect(self.Prev_Page_Setup)
        pageSetup[1].clicked.connect(self.Next_Page_Setup)
        
        self.setupCreateButton.clicked.connect(self.Create_Note)
        self.seeNoteEdit.clicked.connect(self.See_Notes_Edit)
        self.editNoteSet.clicked.connect(self.Edit_Note)
        self.editNoteDelete.clicked.connect(self.Del_Note)

##        self.pushButton.clicked.connect(self.test)

##    def test(self):
##        print(self.label_84.setText('hello'))

    def Add_Line(self):
        self.tableLine += 1
        self.tableWidgetSetup.setRowCount(self.tableLine)

    def Remove_Line(self):
        self.tableLine -= 1
        self.tableWidgetSetup.setRowCount(self.tableLine)

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

#################################################################################

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

#################################################################################

    def Object_Name_List_Display(self):
        titleObjectName = [self.title_1,
                       self.title_2,
                       self.title_3,
                       self.title_4,
                       self.title_5,
                       self.title_6,
                       self.title_7,
                       self.title_8,
                       self.title_9,
                       self.title_10]
        timeObjectName = [self.time_1,
                          self.time_2,
                          self.time_3,
                          self.time_4,
                          self.time_5,
                          self.time_6,
                          self.time_7,
                          self.time_8,
                          self.time_9,
                          self.time_10]
        contentObjectName = [self.plainTextEdit_1,
                             self.plainTextEdit_2,
                             self.plainTextEdit_3,
                             self.plainTextEdit_4,
                             self.plainTextEdit_5,
                             self.plainTextEdit_6,
                             self.plainTextEdit_7,
                             self.plainTextEdit_8,
                             self.plainTextEdit_9,
                             self.plainTextEdit_10]
        return titleObjectName, timeObjectName, contentObjectName

    def Clean_Notes_Display(self):
        titleObjectName, timeObjectName, contentObjectName = self.Object_Name_List_Display()
        for i in range(0,10):
                titleObjectName[i].setText('')
                timeObjectName[i].setText('')
                contentObjectName[i].setPlainText('')

    def See_Notes_Display(self):
        titleObjectName, timeObjectName, contentObjectName = self.Object_Name_List_Display()
        selectedDate = self.calendarWidgetDisplay.selectedDate().getDate()
        dateFormat = _StringOp.DateFormatDash(str(selectedDate)) + '.txt'
        os.chdir(_GetPath.Note_Path())
        self.Clean_Notes_Display()
        if os.path.exists(dateFormat):
            with codecs.open(dateFormat, 'r', 'utf-8') as f:
                notes = f.read()
            tmp = notes.split(NOTE)
            for i in range(0,len(tmp)-1):
                title = str(tmp[i].split(TITLETIMECONTENT)[0])
                time = str(tmp[i].split(TITLETIMECONTENT)[1])
                content = str(tmp[i].split(TITLETIMECONTENT)[2])
                titleObjectName[i].setText(title)
                timeObjectName[i].setText(time)
                contentObjectName[i].setPlainText(content)
                print(title, time, content)
                print('------------------')

#################################################################################

    def Set_Notes_Number(self, dateFormat):
        os.chdir(_GetPath.Note_Path())
        if os.path.exists(dateFormat):
            with codecs.open(dateFormat, 'r', 'utf-8') as f:
                tmp = f.read()
        self.label_86.setText(str(len(tmp.split(NOTE))-1))
        self.label_84.setText(str(len(tmp.split(NOTE))-1))        

    def Check_Notes_Number(self, dateFormat):
        if os.path.exists(dateFormat):
            with codecs.open(dateFormat, 'r', 'utf-8') as f:
                notes = f.read()
            tmp = notes.split(NOTE)
            if(len(tmp)-1<10):
                return True
            else:
                return False
        else:
            return True
    
    def Create_Note(self):
        selectedDate = self.calendarWidgetSetupCreate.selectedDate().getDate()
        title = self.titleSetup.text()
        h = str(self.timeSetup.time().hour())       ## Convert int to string
        m = str(self.timeSetup.time().minute())     ## Convert int to string
        time = h + ':' + m
        content = self.plainTextEditSetup.toPlainText()
        note = title + TITLETIMECONTENT + time + TITLETIMECONTENT + content + NOTE
        
        dateFormat = _StringOp.DateFormatDash(str(selectedDate)) + '.txt'

        os.chdir(_GetPath.Note_Path())
        if self.Check_Notes_Number(dateFormat):
            if os.path.exists(dateFormat):
                with codecs.open(dateFormat, 'a', 'utf-8') as f:
                    f.write(note)
            else:
                with codecs.open(dateFormat, 'w', 'utf-8') as f:
                    f.write(note)
            self.titleSetup.clear()
            self.plainTextEditSetup.clear()
            self.Set_Notes_Number(dateFormat)

#################################################################################

    def Object_Name_List_Setup(self):
        titleObjectName = [self.title_11,
                       self.title_12,
                       self.title_13,
                       self.title_14,
                       self.title_15,
                       self.title_16,
                       self.title_17,
                       self.title_18,
                       self.title_19,
                       self.title_20]
        timeObjectName = [self.time_11,
                          self.time_12,
                          self.time_13,
                          self.time_14,
                          self.time_15,
                          self.time_16,
                          self.time_17,
                          self.time_18,
                          self.time_19,
                          self.time_20]
        contentObjectName = [self.plainTextEdit_11,
                             self.plainTextEdit_12,
                             self.plainTextEdit_13,
                             self.plainTextEdit_14,
                             self.plainTextEdit_15,
                             self.plainTextEdit_16,
                             self.plainTextEdit_17,
                             self.plainTextEdit_18,
                             self.plainTextEdit_19,
                             self.plainTextEdit_20]
        return titleObjectName, timeObjectName, contentObjectName

    def Clean_Notes_Setup(self):
        titleObjectName, timeObjectName, contentObjectName = self.Object_Name_List_Setup()
        for i in range(0,10):
                titleObjectName[i].setText('')
                timeObjectName[i].setText('')
                contentObjectName[i].setPlainText('')

    def Clear_Note_Data(self):
        noteData = Note
        while len(noteData.title)!=0:
            for i in noteData.title:
                noteData.title.remove(i)

    def See_Notes_Edit(self):
        titleObjectName, timeObjectName, contentObjectName = self.Object_Name_List_Setup()
        selectedDate = self.calendarWidgetSetupEdit.selectedDate().getDate()
        dateFormat = _StringOp.DateFormatDash(str(selectedDate)) + '.txt'

        self.Set_Notes_Number(dateFormat)
        self.Clear_Note_Data()
        self.Clean_Notes_Setup()

        noteData = Note
        noteData.date = dateFormat
        print(dateFormat)
        
        os.chdir(_GetPath.Note_Path())
        if os.path.exists(dateFormat):
            with codecs.open(dateFormat, 'r', 'utf-8') as f:
                notes = f.read()
            tmp = notes.split(NOTE)
            
            for i in range(0,len(tmp)-1):
                title = str(tmp[i].split(TITLETIMECONTENT)[0])
                time = str(tmp[i].split(TITLETIMECONTENT)[1])
                content = str(tmp[i].split(TITLETIMECONTENT)[2])
                
                noteData.title.append(title)
                noteData.time.append(time)
                noteData.content.append(content)
                
                titleObjectName[i].setText(title)                
                timeObjectName[i].setText(time)
                contentObjectName[i].setPlainText(content)
                
                print(title, time, content)
                print('------------------')
            for i in range(0,len(noteData.title)):
                print(noteData.title[i])
                print(noteData.time[i])
                print(noteData.content[i])
                print('------------------')

    def Edit_Note(self):
        noteData = Note
        dateFormat = noteData.date

        if(noteData.title!=0):
            titleObjectName, timeObjectName, contentObjectName = self.Object_Name_List_Setup()

            currentIndex = self.stackedWidgetSetup.currentIndex()
            print(currentIndex)
            print(len(noteData.title)-1)
            print(dateFormat)
            
            title = titleObjectName[currentIndex].text()
            time = timeObjectName[currentIndex].text()
            content = contentObjectName[currentIndex].toPlainText()
            
            if(currentIndex<=len(noteData.title)-1):
                noteData.title[currentIndex] = title
                noteData.time[currentIndex] = time
                noteData.content[currentIndex] = content
                
                os.chdir(_GetPath.Note_Path())
                with codecs.open(dateFormat, 'w', 'utf-8') as f:
                    for i in range(0,len(noteData.title)):
                        note = noteData.title[i] + TITLETIMECONTENT + noteData.time[i] + TITLETIMECONTENT + noteData.content[i] + NOTE
                        f.write(note)

    def Del_Note(self):
        noteData = Note
        dateFormat = noteData.date
        currentIndex = self.stackedWidgetSetup.currentIndex()
        if(currentIndex<=len(noteData.title)-1):
            noteData.title.remove(noteData.title[currentIndex])
            noteData.time.remove(noteData.time[currentIndex])
            noteData.content.remove(noteData.content[currentIndex])

            os.chdir(_GetPath.Note_Path())
            with codecs.open(dateFormat, 'w', 'utf-8') as f:
                for i in range(0,len(noteData.title)):
                    note = noteData.title[i] + TITLETIMECONTENT + noteData.time[i] + TITLETIMECONTENT + noteData.content[i] + NOTE
                    f.write(note)
            
            self.See_Notes_Edit()

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()
