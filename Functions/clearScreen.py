#!/usr/bin/python

import time
import os

def clear():
  # forw indows
  #if name == 'nt':
  #    _ = system('cls')
  #else:
  #    _ = system('clear')
    _ = os.system('clear')

# Print some text
print('HELLO!!!!\n' * 15)

# Sleep a moment
print("Let's sleep 5 seconds")
time.sleep(5)

clear()

print('HELLO AGAIN!\n' * 10)

time.sleep(5)

clear()
