import os
import time
import codecs
import _StringOp

from datetime import datetime
from threading import Timer

#######################################################
NOTE = '<NOTE>'
TITLETIMECONTENT = '<TITLETIMECONTENT>'

afterPeriod = 0
beforeNoteTime = 0

time=[]

#######################################################
    
def Run():
    with open('Data/setting.conf', 'rt' ) as f:
        tmp = f.read()
    data = tmp.split('\n')
    if(data[0]=='2'):
        os.Start_Note()
    if(data[1].split(' ')[0]=='2'):
        global afterPeriod
        afterPeriod = int(data[1].split(' ')[1])*60
        Timer(afterPeriod, After_Period).start()

def Start_Note():
    os.startfile('main.pyw')

def After_Period():
    Timer(afterPeriod, After_Period).start()
    Start_Note()

def Before_Note_Time():
    print(time[3]<=time[2])

def Get_Time():
    fileName = _StringOp.ReverseDateFormatDash(str(datetime.now().date())) + '.txt'
    with codecs.open(f'Data/Notes/{fileName}', 'r', 'utf-8') as f:
        tmp=f.read()
    notes = tmp.split(NOTE)
    for i in range(0,len(notes)-1):
        time.append(notes[i].split(TITLETIMECONTENT)[1])
    
if __name__=='__main__':
    Get_Time()
    print(time)
    Before_Note_Time()
##    Run()
