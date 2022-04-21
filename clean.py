import os


import os

def cleanScreen():
    OS = os.name
    if (OS == "nt"):
        os.system('cls')
    elif (OS == "posix"):
        os.system("clear")


def slash():
    OS = os.name
    if (OS == "nt"):
        return "\\"
    elif (OS == "posix"):
        return "/"
