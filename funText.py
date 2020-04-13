import time
import sys
from time import sleep
import random
import string

####
# Fun loops for playing with text emulation
# Written by Eric Guillen
####

CURSOR_UP_ONE = "\033[A"
ERASE_LINE = '\x1b[2K'
# Delay Print.. like a typewriter
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

# Delete the Last Line
def delete_last_line():
    #Use this function to delete the last line in the STDOUT"
    #cursor up one line
    sys.stdout.write('\x1b[1A')
    #delete last line
    sys.stdout.write('\x1b[2K')

# Generate a random String
def randomString(stringLength=10):
    # Generate a random string of fixed length 
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Search Hacker Name, Find it and Print it
def hackerName():
    name = "GEODA"
    for x in range (0,6):
        for y in range (0,15):
            b = "[+] Searching for Hacker: " + name[:x] + randomString(5-x)
            print (b, end ="\r")
            time.sleep(.1)
    time.sleep(.5)
    print('')
    delete_last_line()
    for x in range (0,5):
        b = "[!] Hacker Found"
        print(b)
        time.sleep(.5)
        delete_last_line()
        print('')
        time.sleep(.5)
        delete_last_line()
    print("[*] HAKCER = GEODA")
    time.sleep(2)

# Loading Screen
def loading():
    for x in range (0,10):
        b = "Loading" + "." * x
        print (b, end ="\r")
        time.sleep(.25)

if __name__ == "__main__": 
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print ('    Fun with Text and Python               ')
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print ('')
    loading()
    print ('')
    delete_last_line()
    delay_print("[*] BEGIN TRANSMISSION")
    print ('')

    hackerName()
    
    print ('')
    # Should print stuff then clear
    print('This should clear')
    time.sleep(2)
    delete_last_line()

    # Cycle through random strings
    for x in range (0,20):
        b = "Random String " + randomString(10)
        print (b, end ="\r")
        time.sleep(.25)

    print('')

    # Let's get to some fun stuff
    # Preparing hacks... then delete it
    for x in range (0,10):
        b = "[+] Preparing hacks" + "." * x
        print (b, end="\r")
        time.sleep(.25)
    print ('')
    delete_last_line()

    
    # Begin Secret plan with "..."
    for x in range (0,5):
        b = "[+] Begin Secret Plan" + "." * x
        print (b, end ="\r")
        time.sleep(.5)
    time.sleep(2)
    print ('')
    delete_last_line()
    time.sleep(2)
    print('[!] Secret Plan Complete')
    time.sleep(2)
    # Random Hex cycle
    for x in range (0,50):
        random_number = random.randint(0,16777215000000000000)
        hex_number = str(hex(random_number))
        b = "[*] Begin Random Hex: " + hex_number
        print(b, end ="\r")
        time.sleep(.1)

    print ('')

