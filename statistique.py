import os
import clean
import operator


def total_mail():
    cpt = 0
    for path, subdirs, files in os.walk('tmp'):
        for name in files:
            cpt += 1
    return cpt




def nb_mail_annee(an, corpus):
    cpt = 0
    for path, subdirs, files in os.walk('tmp'):
        try:
            doss = path.split(clean.slash())[1]
            for name in files:
                if doss == an and (corpus == [] or (os.path.join(doss,name) in corpus)):
                    cpt += 1
        except:
            pass
    return cpt




def nb_mail_adresse(ad, corpus):
    cpt = 0
    for path, subdirs, files in os.walk('tmp'):
        try:
            doss = path.split(clean.slash())[1]
            for name in files:
                if (corpus == [] or ((os.path.join(doss,name) in corpus))):
                    with open(os.path.join(path, name), "r", encoding="utf-8", errors="surrogateescape") as fd:
                        for ligne in fd:
                            if (ligne.startswith("__From__")):
                                if ad in ligne.split(" ")[1]:
                                    cpt += 1
                                break
        except:
            pass
    return cpt




def nb_mail_pj(corpus):
    cpt = 0
    for path, subdirs, files in os.walk('tmp'):
        try:
            doss = path.split(clean.slash())[1]
            for name in files:
                if (corpus == [] or ((os.path.join(doss,name) in corpus))):
                    with open(os.path.join(path, name), "r", encoding="utf-8", errors="surrogateescape") as fd:
                        for ligne in fd:
                            if (ligne.startswith("__PJ__")):
                                try:
                                    ligne.split("-")[1]
                                    cpt += 1
                                except:
                                    pass
                                break
        except:
            pass
    return cpt




def all_dates(corpus):
    if corpus == []:
        return os.listdir('tmp')
    else:
        l = []
        ans = os.listdir('tmp')
        for an in corpus:
            if (an[:4] in ans) and (an[:4] not in l):
                l.append(an[:4])
        return l




def nb_par_mois(corpus):
    tab_mois = [0 for i in range(12)]
    for path, subdirs, files in os.walk('tmp'):
        try:
            doss = path.split(clean.slash())[1]
            for name in files:
                if (corpus == [] or ((os.path.join(doss,name) in corpus))):
                    with open(os.path.join(path, name), "r", encoding="utf-8", errors="surrogateescape") as fd:
                        print(fd[1][12:15])
                        #tab_mois[fd[1][12:15]] += 1
        except:
            pass
    return tab_mois


print(nb_par_mois([]))
input()


def all_adr(corpus):
    l = []
    for path, subdirs, files in os.walk('tmp'):
        for name in files:
            if (corpus == []) or (os.path.join(path[4:], name) in corpus):
                with open(os.path.join(path, name), "r", encoding="utf-8", errors="surrogateescape") as fd:
                    for ligne in fd:
                        if (ligne.startswith("__From__")):
                            adr = ligne.split(" ")[1][:-1]
                            if not(adr in l):
                                l.append(adr)
                            break
    return l

  





def rapport_total(corpus):
    if corpus.strip() == "":
        addrs = all_adr([])
        ans = all_dates([])
        nb_total = total_mail()
        #Création du fichier du rapport
        f = open("rapport_complet.txt", "w", encoding="utf-8", errors="surrogateescape")
        #rapport pour les années
        f.write("\nAnnées :\n")
        tab = {}
        for an in ans:
            nb_an = nb_mail_annee(an, [])
            tab[an] = round(100*nb_an/nb_total,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(str(v) + "% " + k + "\n")
        #rapport pour les adresses  
        f.write("\nAdresses :\n")
        tab = {}
        for addr in addrs:
            nb_adr = nb_mail_adresse(addr, [])
            tab[addr] = round(100*nb_adr/nb_total,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(str(v) + "% " + k + "\n")
        #rapport pour les pièces jointes
        nb_pj = nb_mail_pj([])
        f.write("\n"+str(round(100*nb_pj/nb_total,2))+"% de pièces jointes")
                  
        f.close()

    else: #si on a passé un corpus en paramètres
        IDs = corpus.split(" ")
        nb_corpus = len(IDs)
        addrs = all_adr(IDs)
        ans = all_dates(IDs)
        nb_total = total_mail()
        #Création du fichier du rapport
        f = open("rapport_corpus.txt", "w", encoding="utf-8", errors="surrogateescape")
        #rapport pour les années
        f.write("Années :\n")
        tab = {}
        for an in ans:
            nb_an = nb_mail_annee(an, corpus)
            tab[an] = round(100*nb_an/nb_corpus,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(str(v) + "% " + k + "\n")
        #rapport pour les adresses  
        f.write("\nAdresses du corpus :\n")  
        tab = {}
        for addr in addrs:
            nb_adr = nb_mail_adresse(addr, [])
            tab[addr] = round(100*nb_adr/nb_total,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(str(v) + "% " + k + "\n")
        #rapport pour les adresses 
        f.write("\nAdresses au sein corpus :\n")
        tab = {}
        for addr in addrs:
            nb_adr = nb_mail_adresse(addr, corpus)
            tab[addr] = round(100*nb_adr/nb_corpus,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(str(v) + "% " + k + "\n")
        #rapport pour les pièces jointes
        nb_pj = nb_mail_pj(corpus)
        f.write("\n"+str(round(100*nb_pj/nb_total,2))+"% de pièces jointes")
                  
        f.close()




def main(corpus):
    clean.cleanScreen()
    while True:
        print("-----------------------------\nQue voulez-vous faire ?\n-----------------------------\n 1. Statistiques sur le corpus\n 2. Générer un rapport complet\n 3. Quitter\n")
        action = input("Votre choix : ")
        if (action == "1"):
            rapport_total(corpus)
            print("rapport_corpus.txt généré")
            break
        elif (action == "2"): #rapport complet
            rapport_total("")
            print("rapport_complet.txt généré")
            break
        elif (action == "3"): #sortie
            exit(1)
        else: #autre choix
            clean.cleanScreen()
            print("Cette option n'existe pas")




corpus = "2015/1 2015/2 2015/3 2015/14"
main(corpus)


#rapport_total()