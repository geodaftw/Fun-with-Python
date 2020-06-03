#!/usr/bin/python 

import psutil

PROCNAME = "eguiHTTPS.py"

for proc in psutil.process_iter():
    if any(procstr in proc.name() for procstr in\
            [PROCNAME]):
        print('Killing: ' + proc.name())
        proc.kill()
