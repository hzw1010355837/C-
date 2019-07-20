#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import clr # pythonnet
import sys
import System
sys.path.append(r'C:\Users\hzw\Desktop\score\Project2.dll')
clr.AddReference("Project2")
from HelloWorldApplication import *

print(scan.Add(2,3))
print(scan.Run())




