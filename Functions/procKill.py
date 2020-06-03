import psutil

#SERVER1 = "eguiHTTPS.py"
#SERVER2 = "server.py"

processes = {'eguiHTTPS.py', 'server.py'}
for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() in processes:
        proc.kill()
