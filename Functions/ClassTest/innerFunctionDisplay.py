#!/usr/bin/python

####
# Using a class with functions
####

import os
import time
import socket
import sys

# Define Global Variables
lastCommand = ''

# Outter Functions
def loop(userCommand):
    # Valid Commands
    commandList = ['1', '2', '3', '4', '5', 'shell', 'panic', 'q', 'Q']
    
    # Command Function
    def command():
        if userCommand == '1':
            print('its an command')
        else:
            pass

    # Download Function
    def download():
        if userCommand == '2':
            print('its a download')
        else:
            pass

    def upload():
        if userCommand == '3':
            print('its a upload')
        else:
            pass

    def screenCap():
        if userCommand == '4':
            print('its a screen cap')
        else:
            pass

    def shell():
        if userCommand == 'shell':
            print('its a shell')
        else:
            pass

    def panic():
        if userCommand == 'panic':
            print('its a panic')
        else:
            pass

    def runScripts():
        if userCommand == '5':
            print('run scripts')
        else:
            pass

    def quit():
        if userCommand == 'q':
            print('we quit')
            sys.exit()
        else:
            pass

    def Quit():
        if userCommand == 'Q':
            print('we QUIT')
            sys.exit()
        else:
            pass
    
    # This doesn't work below
    def nothing():
        if any(item.lower() == userCommand.lower() for item in commandList): 
            pass
        else:
            print("Invalid command.. let's start over")


    # Run all inner functions
    command()
    download()
    upload()
    screenCap()
    shell()
    panic()
    runScripts()
    quit()
    Quit()
    nothing()

# While Loop with "loop Function"
while True:
    # Print Last Command
    print("Last Command was: " + lastCommand)
    
    # Print Current Server Port is
    print("Current Server Port is: ")

    # Check if Port is open
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ("127.0.0.1", 22)
    result_of_check = a_socket.connect_ex(location)
    if result_of_check == 0:
        print("Port is Open")
    else:
        print("Port is CLosed")
    a_socket.close()
    
    # Blank Space
    print('')

    # User Input
    userCommand = raw_input('Give a number\n')
    # Add user input to "loop" function
    loop(userCommand)
    # Sleep 5 seconds and clear screen
    lastCommand = userCommand
    time.sleep(5)
    _ = os.system('clear')



