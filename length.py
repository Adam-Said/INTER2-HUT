import os
import clean


def main(corpus):
    moyenne = 0.0
    
    tabAdresses = {}
    if(set('abcdefghijklmnopqrstuvwxyz').intersection(corpus)): # True = corpus de threads
        for mail in os.listdir("threads/"+ corpus):
            file = open("threads/" + corpus +"/"+ mail, encoding="utf-8", errors="surrogateescape").readlines()
            adresse = file[1][9:]
            length = len(file - 6)
            if adresse in tabAdresses.items():
                tabAdresses[adresse] += length
            else:
                tabAdresses.add(adresse, length)
    else: # corpus de mails différents
        corpus = corpus.split(" ")
        for mail in os.listdir("tmp/"+ corpus):
            file = open("threads/" + corpus +"/"+ mail, encoding="utf-8", errors="surrogateescape").readlines()
            adresse = file[1][9:]
            length = len(file - 6)
            if adresse in tabAdresses.items():
                tabAdresses[adresse] += length
            else:
                tabAdresses.add(adresse, length)