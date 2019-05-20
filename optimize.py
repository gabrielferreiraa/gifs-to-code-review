#!/usr/bin/python

import os

for filename in os.listdir('.'):
    if filename.endswith('.gif'):
       command="convert " + filename + " -fuzz 13% -layers Optimize " + filename
       os.system(command)
