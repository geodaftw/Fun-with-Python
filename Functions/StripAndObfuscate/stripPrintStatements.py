#!/usr/bin/python

#s = open("template.ps1", "r").read() # Open template.ps1


while True:
    s = open("template.ps1", "r").read() # Open Template.ps1
    user_input = str(raw_input("[!] Do you wish to strip print statements from final Agent File?" + '\n' + "[+] Type 'yes' or 'no'" + '\n'))

    print(user_input)

    if user_input.lower() == 'yes':
        print("It's a yes")
        g = open("output.ps1", "w")        
        for line in s.splitlines():
            if not (line.startswith('Write-Output') or line.startswith('    Write-Output') or line.startswith('        Write-Output') or line.startswith('write-host') or line.startswith('    write-host') or line.startswith('        write-host')):
                g.write(line + '\n')
        g.close()
        break
    elif user_input.lower() == 'no':
        print("It's a no")
        break
    else:
        print("[-] Invalid command.. try again")
        continue



