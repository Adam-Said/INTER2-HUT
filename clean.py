import os


import os

def cleanScreen():
    OS = os.name
    if (OS == "nt"):
        os.system('cls')
    elif (OS == "posix"):
        os.system("clear")
