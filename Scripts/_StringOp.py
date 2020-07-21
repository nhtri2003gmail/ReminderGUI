import sys
import os
import os.path

def DateFormatDash(date):           ## (dd, mm, yyyy) --> dd-mm-yyyy
    tmp = ''
    for i in range(1,len(date)-1):
        tmp += date[i]
    yyyy = tmp.split(', ')[0]
    mm = tmp.split(', ')[1]
    dd = tmp.split(', ')[2]
    dateFormat = dd + '-' + mm + '-' + yyyy
    return dateFormat

def ReverseDateFormatDash(date):    ## yyyy-mm-dd --> dd-mm-yyyy 
    yyyy = str(int(date.split('-')[0]))
    mm = str(int(date.split('-')[1]))
    dd = str(int(date.split('-')[2]))
    dateFormat = dd + '-' + mm + '-' + yyyy
    return dateFormat

def DateFormatSlash(date):          ## dd-mm-yy --> dd/mm/yyyy
    yyyy = date.split('-')[2]
    mm = date.split('-')[1]
    dd = date.split('-')[0]
    dateFormat = dd + '/' + mm + '/' + yyyy
    return dateFormat

def Get_Month(date):                ## dd-mm-yyyy --> mm
    mm = date.split('-')[1]
    return mm
