# Kjelde (og diskusjon): https://stackoverflow.com/questions/20302331/typing-effect-in-python
# Her kan du altså bytte ut print() med din eigen effekt

import sys
from time import sleep

words = "This is just a test :P"

def skrivUt(ord):
    for char in ord:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
        

skrivUt(words)