#!/usr/bin/python

import os

command = raw_input('What local command do you want to run?\n')

print('Your command was ' + command + '\n')
print('Output is below: \n')
output = os.system(command)
print(output)
