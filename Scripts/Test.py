##import winshell # pip install winshell && pip install pywin32
##import os
##import win32con
##
##link_filepath = "C:\\Users\\JohnathanHuuTri\\Desktop\\Test.lnk"
##with winshell.shortcut(link_filepath) as link:
##    link.path = "D:\\Application\\Python\\ReminderGUI\\Start_Reminder.pyw"
##    link.working_directory = 'D:\\Application\\Python\\ReminderGUI'

########################################################################

##import win32con
##
##from swinlnk.swinlnk import SWinLnk
##
##swl = SWinLnk()
##
##swl.create_lnk('D:\\Application\\Python\\ReminderGUI\\Setting.pyw', 'C:\\Users\\JohnathanHuuTri\\Desktop\\Setting.lnk')

########################################################################

from threading import Semaphore, Timer

def test():
    print('try')
    Timer(1, test).start()


test()
