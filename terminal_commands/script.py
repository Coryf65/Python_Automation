# Automate Terminal Commands / Shell
import subprocess

# runs that file 5 times
for i in range(0, 5):
    subprocess.check_call(['python3', 'example.py'])
