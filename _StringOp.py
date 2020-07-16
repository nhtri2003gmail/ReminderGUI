import sys
import os
import os.path

def DateFormatDash(date):
    tmp = ''
    for i in range(1,len(date)-1):
        tmp += date[i]
    yyyy = tmp.split(', ')[0]
    mm = tmp.split(', ')[1]
    dd = tmp.split(', ')[2]
    dateFormat = dd + '-' + mm + '-' + yyyy
    return dateFormat

def DateFormatSlash(date):
    yyyy = date.split('-')[2]
    mm = date.split('-')[1]
    dd = date.split('-')[0]
    dateFormat = dd + '/' + mm + '/' + yyyy
    return dateFormat
