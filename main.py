import shutil
from clean import cleanScreen
import parser
import filter
import responseTime
import statistique
import os

# ---------- Définition des fonctions ----------
def affichageMail():
    nb_mail = 1
    print("Liste complète des mails :\n")
    for dossier in os.listdir("tmp") :
        for file in os.listdir("tmp/" +  dossier):
            current_file = open("tmp/" + dossier +"/"+ file, encoding="utf-8", errors="surrogateescape").readlines()
            obj = current_file[3][11:]
            exped = current_file[1][9:]
            print(str(nb_mail)+". Objet : "+obj+" De : "+exped)
            nb_mail +=1

def affichageMailCorpus(corpus):
  nb_mail = 1
  print("Liste complète des mails :\n")
  for i in range(len(corpus.split(" "))-1):
        dossier = (corpus.split(" ")[i]).split("-")[0]
        file = (corpus.split(" ")[i]).split("-")[1]
        current_file = open("tmp/" + dossier +"/"+ file, encoding="utf-8", errors="surrogateescape").readlines()
        obj = current_file[3][11:]
        exped = current_file[1][9:]
        print(str(nb_mail)+". Objet : "+obj+" De : "+exped)
        nb_mail +=1

def menuPrincipal():
    cleanScreen()
    print("-----------------------------\n Que voulez-vous faire ?\n -----------------------------\n 1. Afficher les mails\n 2. Filtrer les mails\n 3. Utiliser les fils de discussion (threads)\n 4. Générer un rapport complet\n 5. Quitter\n")
    choice = str(input("Votre choix : "))
    corpus = ""
    if (choice == "1"):
        affichageMail()
        foo = input("\nAppuyer sur Entrée pour continuer... ")
    elif (choice == "2") :
        affichageMail()
        corpus = filter.main()
        print("Affichage du corpus de mails sélectionné :\n")
        affichageMailCorpus(corpus)
    elif (choice == "3"):
        try: # Création des threads
            os.mkdir("threads")
            print("Création des threads, merci de patienter...\n Cette opération peut prendre du temps !")
            parser.threader()
            print("Création des threads terminée")
        except:
            pass
        nb_fil = 0
        print("Choisissez le minimum de mails voulu par fil (0 sinon)\n")
        min = input("Votre choix... ")
        print("Choisissez le maximum de mails voulu par fil (0 sinon)\n")
        max = input("Votre choix... ")
        print("Affichage des corpus de mails :\n")
        for dossier in os.listdir("threads") :
            nb_fil +=1
            if(int(max) == 0 and int(len(os.listdir("threads/"+dossier))) >= int(min)):
                print(str(nb_fil) + ". Objet: "+dossier)
            elif(int(len(os.listdir("threads/"+dossier))) >= int(min) and int(len(os.listdir("threads/"+dossier))) < int(max)):
                print(str(nb_fil) + ". Objet: "+dossier)
        fils = os.listdir("threads")
        num_fil = int(input("Choisisez un fil... "))
        corpus = fils[num_fil-1]
        print("Affichage du fil sélectionné : \n")
        nb_mail = 0
        for file in os.listdir("threads/" + corpus) :
            nb_mail +=1
            current_file = open("threads/" + corpus +"/"+ file, encoding="utf-8", errors="surrogateescape").readlines()
            obj = current_file[3][11:]
            exped = current_file[1][9:]
            date = current_file[0][9:]
            print(str(nb_mail)+". Objet : "+obj+" De : "+exped + " Date : "+date)
    elif (choice == "4") :
        print("Etes-vous sûr de vouloir générer un rapport complet ? Cette action peut être très longue")
        valider = input("[o/n] : ")
        if valider in ["y","Y","O","o"]:
            print("création du rapport complet en cours...")
            statistique.rapport_total("")
            print("rapport_complet.csv généré")
    else:
        try:
            print("Suppression de tmp")
            shutil.rmtree("tmp")
            print("Suppression de threads")
            shutil.rmtree("threads")
        except:
            True
        print("\n------- Fin -------")
        exit(1)
      
    if(corpus == ""):
        menuPrincipal()
    else:
        return corpus



def menuAction(corpus):
    while True:
        print("-----------------------------\nQue voulez-vous faire ?\n-----------------------------\n 1. Calcul du temps de réponse\n 2. Statistiques sur les mails\n 3. Quitter\n")
        action = input("Votre choix : ")
        if (action == "1"):
            if(set('abcdefghijklmnopqrstuvwxyz').intersection(corpus)):
                print("Temps de réponse\n")
                responseTime.main(corpus)
            else:
                print("Le calcul du temps de réponse est calculable uniquement sur les fils de discussions.\n")
        elif (action == "2"):
            print("Statistiques sur les mails\n")
            statistique.main(corpus)
        elif (action == "3"):
            print("------ Fin ------")
            break
        else:
            cleanScreen()
            print("Cette option n'existe pas")
            
      
def main() :
    cleanScreen()
    print("------- Scripts HUT V3.0.5 -------")

    # Création dossiers de dépôt et de destination
    try:
        os.mkdir("__MAIL_DEPOT__")
    except:
        pass
    
    try:
        os.mkdir("tmp")
    except:
        shutil.rmtree("tmp")
        os.mkdir("tmp")
    
    try:
        shutil.rmtree("threads")
    except:
        pass
    # Attente du dépôt des fichiers
    check = "" #ok pour debug_mode
    while check != "ok" or len(os.listdir('__MAIL_DEPOT__')) == 0:
        check = input("Pour commencer, ajoutez vos fichiers à traiter dans le dossier __MAIL_DEPOT__ puis écrivez \"ok\" \n")
    
    # Découpage des mails
    print("Découpage des mails, merci de patienter...\n Cette opération peut prendre du temps !")
    parser.cutter()
    print("Découpage des mails terminé")

    # Nettoyage des mails
    print("Nettoyage des mails, merci de patienter...\n Cette opération peut prendre du temps !")
    parser.cleaner()
    print("Nettoyage des mails terminé")

    while(True):
        # Affichage du menu et choix du corpus
        corpus = menuPrincipal()

        # Affichage des actions
        menuAction(corpus)

main()