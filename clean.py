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
            



def thread_to_corpus(corpus):
    if(set('abcdefghijklmnopqrstuvwxyz').intersection(corpus)): # True = corpus de threads
        corpus2 = ""
        for mail in os.listdir("threads"+slash()+corpus):
            corpus2 += (mail.split(",")[1] + " ")
        return corpus2
    else:
        return corpus