true = True
false = False
import os
import clean

def total_mail():
    cpt = 0;
    for path, subdirs, files in os.walk('tmp'):
        for name in files:
            cpt += 1
    return cpt


def nb_mail_annee(an):
    cpt = 0;
    for path, subdirs, files in os.walk('tmp'):
        for name in files:
            if path.split(clean.slash())[1] == an:
                cpt += 1
    return cpt


def nb_mail_adresse(ad):
    cpt = 0;
    for path, subdirs, files in os.walk('tmp'):
        for name in files:
            with open(os.path.join(path, name), "r", encoding="utf-8") as fd:
                for ligne in fd:
                    if (ligne.startswith("__From__")):
                        if ligne.split(" ")[1][:-1] == ad:
                            cpt += 1
                        break
    return cpt


def all_dates():
    return os.listdir('tmp')


def all_adr():
    l = []
    for path, subdirs, files in os.walk('tmp'):
        for name in files:
            with open(os.path.join(path, name), "r", encoding="utf-8") as fd:
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
    f = open("rapport complet", "w", encoding="utf-8") 
    
    for an in ans:
        nb_an = nb_mail_annee(an)
        f.write(an+" : "+str(round(100*nb_an/nb_total,1))+"%\n")
        
    for addr in addrs:
        nb_adr = nb_mail_adresse(addr)
        f.write(addr+" : "+str(round(100*nb_adr/nb_total,1))+"%\n")
            
    f.close()

