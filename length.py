import os
import clean


def main(corpus):
    
    tabAdresses = {}
    if(set('abcdefghijklmnopqrstuvwxyz').intersection(corpus)): # True = corpus de threads
        for mail in os.listdir("threads/"+ corpus):
            file = open("threads/" + corpus +"/"+ mail, encoding="utf-8", errors="surrogateescape").readlines()
            adresse = file[1][9:]
            length = len(file) - 6
            arrayValue = []
            if adresse in tabAdresses.items():
                cpt = tabAdresses.get(adresse)[0]
                arrayValue.append(cpt+1, (tabAdresses.get(adresse)[1] + length)/ (cpt+1))
                tabAdresses[adresse] = arrayValue
            else:
                arrayValue.append(0, length)
                tabAdresses.add(adresse, length)
              
    else: # corpus de mails différents
        corpus = corpus.split(" ")
        for doss in corpus:
            mail = doss.split("/")
            file = open("tmp/" + mail[0] +"/"+ mail[1], encoding="utf-8", errors="surrogateescape").readlines()
            adresse = file[1][9:]
            length = len(file) - 6
            arrayValue = []
            if adresse in tabAdresses.items():
                cpt = tabAdresses.get(adresse)[0]
                arrayValue.append(cpt+1, (tabAdresses.get(adresse)[1] + length)/ (cpt+1))
                tabAdresses[adresse] = arrayValue
            else:
                arrayValue.append(0, length)
                tabAdresses.add(adresse, length)

    