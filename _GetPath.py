import sys
import os
import os.path

def Home_Path():
    homePath = ''
    os.system('echo %HOMEPATH% > HOMEPATH.txt')
    with open('HOMEPATH.txt','rt') as f:
        tmp = f.read()
    os.system('del HOMEPATH.txt')
    # Get HOMPATH without \n
    for i in range(0,len(tmp)-2):
        homePath+=tmp[i]
    # Return HOMEPATH value
    return homePath

def Document_Reminder_Path():
    documentReminder = 'C:' + Home_Path() + '\\Documents' + '\\ReminderGUI'
    return documentReminder

def Weekly_Path():
    weeklyPath = Document_Reminder_Path() + '\\Weekly'
    return weeklyPath

def Note_Path():
    notePath = Document_Reminder_Path() + '\\Note'
    return notePath
    
