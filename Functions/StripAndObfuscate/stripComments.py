#!/usr/bin/python

import os
#s = open("template.ps1", "r").read() # Open template.ps1


while True:
    s = open("template.ps1", "r").read() # Open Template.ps1
    user_input = str(raw_input("[!] Do you wish to strip comments from final Agent File?" + '\n' + "[+] Type 'yes' or 'no'" + '\n'))

    print(user_input)

    if user_input.lower() == 'yes':
        print("It's a yes")
        g = open("output.ps1", "w")        
        for line in s.splitlines():
            if not (line.startswith('#') or line.startswith('    #') or line.startswith('        #')):
                g.write(line + '\n')
        g.close()
        break
    elif user_input.lower() == 'no':
        print("It's a no")
        break
    else:
        print("[-] Invalid command.. try again")
        continue

#### Replace "END COMMENTS" with the #>
with open('output.ps1', 'r') as f:
    for line in f:
        line = line.replace('END COMMENTS', '#>')
        i = open('newOutput.ps1', 'a')
        i.write(line)
        i.close

os.rename('newOutput.ps1', 'output.ps1')
