import os
import clean
import operator
from datetime import datetime




def num_to_jour(num):
    if num == 1:
        return "Lundi"
    if num == 2:
        return "Mardi"
    if num == 3:
        return "Mercredi"
    if num == 4:
        return "Jeudi"
    if num == 5:
        return "Vendredi"
    if num == 6:
        return "Samedi"
    else:
        return "Dimanche"


def num_to_mois(num):
    if num == 1:
        return "Janvier"
    if num == 2:
        return "Février"
    if num == 3:
        return "Mars"
    if num == 4:
        return "Avril"
    if num == 5:
        return "Mai"
    if num == 6:
        return "Juin"
    if num == 7:
        return "Juillet"
    if num == 8:
        return "Aout"
    if num == 9:
        return "Septembre"
    if num == 10:
        return "Octobre"
    if num == 11:
        return "Novembre"
    else:
        return "Decembre"



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




def nb_mail_mois(corpus):
    tab_mois = [0 for i in range(12)]
    for path, subdirs, files in os.walk('tmp'):
        try:
            doss = path.split(clean.slash())[1]
            for name in files:
                if (corpus == [] or ((os.path.join(doss,name) in corpus))):
                    with open(os.path.join(path, name), "r", encoding="utf-8", errors="surrogateescape") as fd:
                        for ligne in fd:
                            mois = (ligne.split(" ")[1]).split("/")[1]
                            tab_mois[int(mois)-1] += 1
                            break
        except:
            pass
    return tab_mois



def nb_mail_semaine(corpus):
    tab_semaine = [0 for i in range(7)]
    for path, subdirs, files in os.walk('tmp'):
        try:
            doss = path.split(clean.slash())[1]
            for name in files:
                if (corpus == [] or ((os.path.join(doss,name) in corpus))):
                    with open(os.path.join(path, name), "r", encoding="utf-8", errors="surrogateescape") as fd:
                        for ligne in fd:
                            date = (ligne.split(" ")[1]).split("/")
                            jour = datetime.strptime(date[2]+"-"+date[1]+"-"+date[0], "%Y-%m-%d")
                            tab_semaine[jour.weekday()] += 1
                            break
        except:
            pass
    return tab_semaine




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
        f = open("rapport_complet.csv", "w", encoding="utf-8", errors="surrogateescape")
        #rapport pour les années
        f.write("sep=;\nAnnées;Pourcentage\n")
        tab = {}
        for an in ans:
            nb_an = nb_mail_annee(an, [])
            tab[an] = round(100*nb_an/nb_total,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k+ ";" + str(v) + "%\n")
        #rapport pour les adresses  
        f.write("\nAdresses;Pourcentage\n")
        tab = {}
        for addr in addrs:
            nb_adr = nb_mail_adresse(addr, [])
            tab[addr] = round(100*nb_adr/nb_total,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k + ";" + str(v) + "%\n")
        #rapport pour les mois  
        f.write("\nMois;Pourcentage\n")
        tab = {}
        tab_mois = nb_mail_mois([])
        for i in range(len(tab_mois)):
            if tab_mois[i] != 0:
                tab[num_to_mois(i+1)] = round(100*tab_mois[i]/sum(tab_mois),2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k + ";" + str(v) + "%\n")
        #rapport pour les jour de la semaine  
        f.write("\nSemaine;Pourcentage\n")
        tab = {}
        tab_semaine = nb_mail_semaine([])
        for i in range(len(tab_semaine)):
            if tab_semaine[i] != 0:
                tab[num_to_jour(i+1)] = round(100*tab_semaine[i]/sum(tab_semaine),2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k + ";" + str(v) + "%\n")
        #rapport pour les pièces jointes
        nb_pj = nb_mail_pj([])
        f.write("\nPourcentage de pièces jointes\n"+str(round(100*nb_pj/nb_total,2))+"%")
                  
        f.close()

    else: #si on a passé un corpus en paramètres
        IDs = (corpus.replace("-","/")).split(" ")[:-1]
        nb_corpus = len(IDs)
        addrs = all_adr(IDs)
        ans = all_dates(IDs)
        nb_total = total_mail()
        #Création du fichier du rapport
        f = open("rapport_corpus.csv", "w", encoding="utf-8", errors="surrogateescape")
        #rapport pour les années
        f.write("sep=;\nAnnées;Pourcentage\n")
        tab = {}
        for an in ans:
            nb_an = nb_mail_annee(an, corpus)
            tab[an] = round(100*nb_an/nb_corpus,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k+ ";" + str(v) + "%\n")
        #rapport pour les adresses  
        f.write("\nAdresses du corpus;Pourcentage\n")  
        tab = {}
        for addr in addrs:
            nb_adr = nb_mail_adresse(addr, [])
            tab[addr] = round(100*nb_adr/nb_total,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k+ ";" + str(v) + "%\n")
        #rapport pour les adresses 
        f.write("\nAdresses au sein du corpus;Pourcentage\n")
        tab = {}
        for addr in addrs:
            nb_adr = nb_mail_adresse(addr, corpus)
            tab[addr] = round(100*nb_adr/nb_corpus,2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k+ ";" + str(v) + "%\n")
        #rapport pour les mois  
        f.write("\nMois;Pourcentage\n")
        tab = {}
        tab_mois = nb_mail_mois(corpus)
        for i in range(len(tab_mois)):
            if tab_mois[i] != 0:
                tab[num_to_mois(i+1)] = round(100*tab_mois[i]/sum(tab_mois),2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k+ ";" + str(v) + "%\n")
        #rapport pour les jour de la semaine  
        f.write("\nSemaine;Pourcentage\n")
        tab = {}
        tab_semaine = nb_mail_semaine(corpus)
        for i in range(len(tab_semaine)):
            if tab_semaine[i] != 0:
                tab[num_to_jour(i+1)] = round(100*tab_semaine[i]/sum(tab_semaine),2)
        for k, v in sorted(tab.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k+ ";" + str(v) + "%\n")
        #rapport pour les pièces jointes
        nb_pj = nb_mail_pj(corpus)
        f.write("\nPourcentage de pièces jointes\n"+str(round(100*nb_pj/nb_total,2))+"%")
                  
        f.close()




def main(corpus):
    clean.cleanScreen()
    while True:
        print("-----------------------------\nQue voulez-vous faire ?\n-----------------------------\n 1. Statistiques sur le corpus\n 2. Générer un rapport complet\n 3. Quitter\n")
        action = input("Votre choix : ")
        if (action == "1"):
            print("création du rapport sur le corpus...")
            rapport_total(corpus)
            print("rapport_corpus.txt généré")
            break
        elif (action == "2"): #rapport complet
            print("création du rapport complet...")
            rapport_total("")
            print("rapport_complet.txt généré")
            break
        elif (action == "3"): #sortie
            exit(1)
        else: #autre choix
            clean.cleanScreen()
            print("Cette option n'existe pas")
