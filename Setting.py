import sys
import os
import os.path

import GetPath

def Set_Table():
    print(weeklyPath)
    try:
        os.mkdir(weeklyPath)
        print('Created')
    except:
        pass
    
