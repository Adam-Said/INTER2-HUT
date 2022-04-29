import os
import clean



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




def all_dates():
    return os.listdir('tmp')





def all_adr():
    l = []
    for path, subdirs, files in os.walk('tmp'):
        for name in files:
            with open(os.path.join(path, name), "r", encoding="utf-8", errors="surrogateescape") as fd:
                for ligne in fd:
                    if (ligne.startswith("__From__")):
                        adr = ligne.split(" ")[1][:-1]
                        if not(adr in l):
                            l.append(adr)
                        break
    return l




def nb_mail(clef):
    nb_total = total_mail()
    res = ""
    try:
        int(clef)
        res = nb_mail_annee(clef)
    except:
        res = nb_mail_adresse(clef)
        
    print("Nombre de mails de "+clef+" :",str(round(100*res/nb_total,1))+"%")




def rapport_total():
    addrs = all_adr()
    ans = all_dates()
    nb_total = total_mail()
    #Création du fichier du rapport
    f = open("rapport_complet.txt", "w", encoding="utf-8", errors="surrogateescape")
    #rapport pour les années
    f.write("Années :\n")
    for an in ans:
        nb_an = nb_mail_annee(an, [])
        f.write(an+" : "+str(round(100*nb_an/nb_total,2))+"%\n")
    f.write("Adresses :\n")
    #rapport pour les adresses    
    for addr in addrs:
        nb_adr = nb_mail_adresse(addr, [])
        f.write(addr+" : "+str(round(100*nb_adr/nb_total,2))+"%\n")
    #rapport pour les pièces jointes
    nb_pj = nb_mail_pj([])
    f.write("Pièces jointes : "+str(round(100*nb_pj/nb_total,2))+"%")
              
    f.close()






def main(corpus):
    clean.cleanScreen()
    while True:
        print("-----------------------------\nQue voulez-vous faire ?\n-----------------------------\n 1. Statistiques sur le corpus\n 2. Statistiques sur l'ensemble des mails\n 3. Quitter\n")
        action = input("Votre choix : ")
        if (action == "1"):
            print("-----------------------------\nStatistiques sur le corpus\n-----------------------------\n 1. Chercher une adresse mail\n 2. Chercher une année\n 3. Chercher des pièces jointes\n 4. Quitter\n")
            action2 = input("Votre choix : ")
            if (action2 == "1" or action2 == "2"):
                True
        elif (action == "2"):
            True
        elif (action == "3"):
            exit(1)
        else:
            clean.cleanScreen()
            print("Cette option n'existe pas")
              
        if corpus.strip() != "":
            IDs = corpus.split(" ")
            lenCorpus = len(corpus)
            print("Corpus :",IDs)
            print("nb malo :",nb_mail_pj([]))
      # for elt in liste:
          # fd = open("tmp/" + elt.split("-")[0] + "/" + elt.split("-")[1], "r", encoding="utf-8", errors="surrogateescape")
          
        else:
            pass
      
        return True
  



#corpus = "2015/1 2015/2 2015/3 2015/14"
#main(corpus)

#rapport_total()