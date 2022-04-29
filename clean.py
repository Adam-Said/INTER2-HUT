import os

def cleanScreen():
    if (os.name == "nt"):
        os.system('cls')
    elif (os.name == "posix"):
        os.system("clear")


def slash():
    if (os.name == "nt"):
        return "\\"
    elif (os.name == "posix"):
        return "/"


def progress(nb, max, message):
    if max > 0:
        progress = (nb/max)
        if int(progress*100) - progress*100 <= progress - 1:
            cleanScreen()
            print(message, str(int(progress*100)) + "%")