import os
import time
import codecs
import _StringOp

from datetime import datetime
from threading import Timer

#########################################################
NOTE = '<NOTE>'
TITLETIMECONTENT = '<TITLETIMECONTENT>'

afterPeriod = 0
beforeNoteTime = 0

class Note:
    title=[]
    time=[]
    content=[]

beforeNoteTimeArr=[]

#########################################################

def Check_Note():
    os.chdir('Data/Notes')
    title=[]
    time=[]
    content=[]
    fileName = _StringOp.ReverseDateFormatDash(str(datetime.now().date())) + '.txt'
    with codecs.open(fileName, 'r', 'utf-8') as f:
        tmp = f.read()
    notes = tmp.split(NOTE)
    for i in range(0, len(notes)-1):
        title.append(notes[i].split(TITLETIMECONTENT)[0])
        time.append(notes[i].split(TITLETIMECONTENT)[1])
        content.append(notes[i].split(TITLETIMECONTENT)[2])

    tNow = datetime.now()
    i=0
    while i<=len(time):
        try:
            t = datetime.strptime(time[i], '%H:%M')
        except:
            break
        if (tNow.time()>t.time()):
            title.remove(title[i])
            time.remove(time[i])
            content.remove(content[i])
            continue
        i+=1
    with codecs.open(fileName, 'w', 'utf-8') as f:
        if(len(time)>0):
            for i in range(0, len(time)):
                note = title[i] + TITLETIMECONTENT + time[i] + TITLETIMECONTENT + content[i] + NOTE
                f.write(note)
        else:
            f.write('')
        
    os.chdir('../../')

#########################################################
                                                        #
def Run():                                              #
    Check_Note()
    with open('Data/setting.conf', 'rt' ) as f:         #
        tmp = f.read()                                  #
    data = tmp.split('\n')                              #
    if(data[0]=='2'):                                   #
        Start_Note()                                    #
    if(data[1].split(' ')[0]=='2'):                     #
        global afterPeriod                              #
        afterPeriod = int(data[1].split(' ')[1])*60     #
        Timer(afterPeriod, After_Period).start()        #
    if(data[2].split(' ')[0]=='2'):                     #
        Get_Time()
        global beforeNoteTime                           #
        beforeNoteTime = int(data[2].split(' ')[1])     #
        Before_Note_Time()                              #
                                                        #
#########################################################
        
def Start_Note():
    os.startfile('main.pyw')

#########################################################
    
def After_Period():
    Timer(afterPeriod, After_Period).start()
    Start_Note()

#########################################################
    
def Open_Note(note):
    with codecs.open('Data/note.txt', 'w', 'utf-8') as f:
        f.write(note)
    os.startfile('Note.pyw')

def Call_Before_Note_Time():
    note=Note
    
    currentTime = str(datetime.now().time())
    hh = currentTime.split(':')[0]
    mm = currentTime.split(':')[1]
    timeFormat = hh + ':' + mm
    tNow = datetime.strptime(timeFormat, '%H:%M')
    print(tNow.time())
    try:
        tB = datetime.strptime(beforeNoteTimeArr[0], '%H:%M')
        print(t.time())
    except:
        pass
    
    try:
        t = datetime.strptime(note.time[0], '%H:%M')
        print(t.time())
    except:
        pass

    print(t.time()==tNow.time())

    print(note.title)
    print(note.time)
    print(note.content)
    print()
    print(timeFormat)
    print(beforeNoteTimeArr)
    print(note.time)

    try:
        if(tB.time()==tNow.time()):
            print('t1')
            Open_Note(note.title[0] + TITLETIMECONTENT + note.time[0] + TITLETIMECONTENT + note.content[0])
            beforeNoteTimeArr.remove(beforeNoteTimeArr[0])
    except:
        pass

    try:
        if(t.time()==tNow.time()):
            print('t2')
            Open_Note(note.title[0] + TITLETIMECONTENT + note.time[0] + TITLETIMECONTENT + note.content[0])
            note.title.remove(note.title[0])
            note.time.remove(note.time[0])
            note.content.remove(note.content[0])
            Check_Note()
    except:
        pass
    Timer(45, Call_Before_Note_Time).start()

def Before_Note_Time():
    note=Note
    hh = int(beforeNoteTime/60)
    mm = beforeNoteTime%60
    for Time in note.time:
        noteHH = int(Time.split(':')[0])
        noteMM = int(Time.split(':')[1])
        correctHH = noteHH-hh
        if(correctHH<0):
            correctHH=0
        correctMM = noteMM-mm
        if(correctMM<0):
            correctMM=0
        beforeNoteTimeArr.append(str(correctHH) + ':' + str(correctMM))
    Call_Before_Note_Time()

def Get_Time():
    global fileName
    fileName = _StringOp.ReverseDateFormatDash(str(datetime.now().date())) + '.txt'
    with codecs.open(f'Data/Notes/{fileName}', 'r', 'utf-8') as f:
        tmp=f.read()
    notes = tmp.split(NOTE)
    note = Note
    for i in range(0,len(notes)-1):
        note.title.append(notes[i].split(TITLETIMECONTENT)[0])
        note.time.append(notes[i].split(TITLETIMECONTENT)[1])
        note.content.append(notes[i].split(TITLETIMECONTENT)[2])

#########################################################

if __name__=='__main__':
    Run()
