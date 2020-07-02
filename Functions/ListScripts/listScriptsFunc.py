#!/usr/bin/python

import os
import shutil

# TODO: Right now it's an if/else with a Static list of scripts. This is good, but what if I add a script.. I don't want to have to update this function. It should be more dynamic based off the number of scripts found in the directory

# TODO: Maybe do a for loop?

while True:
    user_input = str(raw_input("[!] Type '5' or 'q'\n"))
    if user_input is '5':
        while True:
            print("You chose 5")
        
            scripts = os.listdir('./Scripts/')
            countScripts = len(scripts)

            print("All items are: " + str(scripts))
            print("The first script is: " + str(scripts[1]))
            print("Below are the items")
            for list in scripts:
                #print("Item is: " + list)
                #print("List Number is: " + str(scripts.index(list)))
                #print("Item Number is: " + str(scripts.index(list) +1))
                print("Choose: " + str(scripts.index(list)+1) + " for " + list)

            user_input = str(raw_input("[!] Choose the Item number\n"))

            new = (int(user_input) -1)
            choice = str(scripts[new])
            print("You chose script: " + choice)
            
            print("Let's move that to the current directory")

            shutil.copy('./Scripts/' + choice, '.')

            print("File is now in cwd")



            break # Needed for "While True"
    elif user_input is 'q':
        print("You chose quit")
        break
    else:
        print("[!] Not a valid answer")


