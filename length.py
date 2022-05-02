import os
import clean


def main(corpus):
    print(corpus)
    input()
    tabAdresses = {}
    if(set('abcdefghijklmnopqrstuvwxyz').intersection(corpus)): # True = corpus de threads
        for mail in os.listdir("threads"+clean.slash()+ corpus):
            file = open("threads"+clean.slash()+corpus+clean.slash()+ mail, encoding="utf-8", errors="surrogateescape").readlines()
            adresse = file[1][9:]
            length = len(file) - 6
            arrayValue = []
            if adresse in tabAdresses.items():
                cpt = tabAdresses.get(adresse)[0]
                arrayValue.append(cpt+1)
                arrayValue.append((tabAdresses.get(adresse)[1] + length)/ (cpt+1))
                tabAdresses[adresse] = arrayValue
            else:
                arrayValue.append(0)
                arrayValue.append(length)
                tabAdresses[adresse] = arrayValue
              
    else: # corpus de mails différents
        corpus = corpus.split(" ")
        corpus = list(filter(None, corpus))
        for doss in corpus:
            mail = doss.split("-")
            file = open("tmp"+clean.slash() + mail[0] +clean.slash()+ mail[1], encoding="utf-8", errors="surrogateescape").readlines()
            adresse = file[1][9:]
            length = len(file) - 6
            arrayValue = []
            if adresse in tabAdresses.items():
                cpt = tabAdresses.get(adresse)[0]
                print(cpt)
                arrayValue.append(cpt+1)
                print(tabAdresses.get(adresse)[1])
                arrayValue.append((tabAdresses.get(adresse)[1] + length)/ (cpt+1))
                tabAdresses[adresse] = arrayValue
            else:
                arrayValue.append(0)
                arrayValue.append(length)
                tabAdresses[adresse] = arrayValue

    fd = open("rapport_longueur.txt", "w", encoding="utf-8", errors="surrogateescape")
    for adresse in tabAdresses:
        print(adresse + " a écrit en moyenne " + str(tabAdresses[adresse][1]) + " lignes en " + str(tabAdresses[adresse][0]) + " mails\n")
        fd.write(adresse + " : " + str(tabAdresses[adresse][1]) + " - " + str(tabAdresses[adresse][0] - 1))
    fd.close()
    print("Rapport de longueur généré, appuyez sur entrer pour continuer.")
    input()

'''
corpus = "2015-1 2015-2 2015-3 2015-14"
main(corpus)
'''