#!/usr/bin/python

#####
# Function to get directory listing of directory
# Then ask when file from that directory you want
# It'll then copy that file to another directory
# Written By: Eric Guillen
#####


# Might have to pip install shutil
import os
import shutil

scripts = os.listdir('./Scripts/')
totalScripts = (len(scripts))


print("All items are: " + str(scripts))

print("Below are the items")
for list in scripts:
    #print("Item is: " + list)
    #print("List Number is: " + str(scripts.index(list)))
    #print("Item Number is: " + str(scripts.index(list) +1))
    print("Choose: " + str(scripts.index(list)+1) + " for " + list)

print("There are a total of " + str(totalScripts))


while True:
    try:
        user_input = int(raw_input("[!] Choose the Item number or '0' to quit\n"))
    except ValueError:
        print("That's not a number!")
    else:
        if 1 <= user_input <= int(totalScripts):
            
            second_input = str(raw_input("Are you sure?? 'yes' or 'no'\n"))
            if second_input == 'no':
                print("Good catch, leaving..")
                break
            elif second_input == 'yes':
                print("Good job!")
                new = ((user_input) -1)
                choice = str(scripts[new])
                print("You chose script: " + choice)

                print("Let's move that to the current directory")

                shutil.copy('./Scripts/' + choice, '.')

                print("File is now in cwd")
                break
            else:
                print("Choose 'yes' or 'no'")
                continue
        elif user_input == 0:
            print("Okay we leave, goodbye")
            break
        else:
            print("Out of Range, try again!")
            continue




'''
## THE BELOW WORKS BUT NOT WELL
# List scripts
print("All Items are: " + str(scripts))
print("Choose '1' for: " + str(scripts[0]))
print("Choose '2' for: " + str(scripts[1]))
print("Choose '3' for: " + str(scripts[2]))
print("There are a total of: " + str(countScripts) + " scripts")

script_input = str(raw_input("[!] What script do you want to run?\n"))

print(script_input)
inputList = (int(script_input) - 1)
print("You chose Script: " + str(inputList))
print("That means you chose: " + str(scripts[inputList]))
'''

