from datetime import datetime
import os
from clean import cleanScreen

def main():
    corpus = ""
    corpusTmp = []
    nb_mail = 0
    print("---- Recherche ----\nRechercher par :\n\t1. Adresse\n\t2. Date\n\t3. Présence de Pièces jointe\n\t4. Mot clé dans l'objet\n\t5. Mot clé dans le contenu\n")

    choice = int(input("Votre choix : "))

    if(choice == 1): # Recherche par Adresse
        exp = input("Adresse(s) séparées par des espaces (format exemple@exemple.com) : ")
        adressesList = exp.split(" ")
        for dossier in os.listdir("tmp") :
            for file in os.listdir("tmp/" + dossier):
                current_file = open("tmp/" + dossier +"/"+ file, encoding="utf-8").readlines()
                for adresse in adressesList :
                    if(adresse in current_file[1] or adresse in current_file[2]) :
                        nb_mail +=1
                        date = current_file[0][9:]
                        exped = current_file[1][9:]
                        ID = dossier+"-"+file
                        corpusTmp.append(str(nb_mail) + ". ID: "+ ID + " Date: " + date + " | "+ exped)

    elif(choice == 2): # Recherche par Date
        print("1. Date exacte\n2. Avant la date\n3. Après la date\n4. Encadrement de dates")
        choice2 = int(input())
        exp = str(input("Date (format jj/mm/aaaa) : "))

        if (len(exp) == 10) : # Conversion de la date
            exp = datetime.strptime((exp.split(" ")[0]), '%d/%m/%Y')
        else :
            print("Format incorrect\n")
            exit(1)
        cleanScreen()
        print("Date : "+str(exp)+"\n")
        if(choice2 == 1) : # Recherche date exacte
            for dossier in os.listdir("tmp") :
                for file in os.listdir("tmp/" + dossier):
                    current_file = open("tmp/" + dossier +"/"+ file, encoding="utf-8").readlines()
                    date_gen = current_file[0].split(" ") #ligne avec la date
                    date_mail = datetime.strptime((date_gen[1]), "%d/%m/%Y") #Date du mail
                    if(exp == date_mail) :
                        nb_mail +=1
                        date = current_file[0][9:]
                        exped = current_file[1][9:]
                        ID = dossier+"-"+file
                        corpusTmp.append(str(nb_mail) + ". ID: "+ID+ " Date: " + date + " | "+ exped)

        elif(choice2 == 2) : # Recherche date exacte et avant
            for dossier in os.listdir("tmp") :
                for file in os.listdir("tmp/" + dossier):
                    current_file = open("tmp/" + dossier +"/"+ file, encoding="utf-8").readlines()
                    date_gen = current_file[0].split(" ") #ligne avec la date
                    date_mail = datetime.strptime((date_gen[1]), '%d/%m/%Y') #Date du mail
                    if(date_mail <= exp) :
                        nb_mail +=1
                        date = current_file[0][9:]
                        exped = current_file[1][9:]
                        ID = dossier+"-"+file
                        corpusTmp.append(str(nb_mail) + ". ID: "+ID+ " Date: " + date + " | "+ exped)

        elif(choice2 == 3) : # Recherche date exacte et après
            for dossier in os.listdir("tmp") :
                for file in os.listdir("tmp/" + dossier):
                    current_file = open("tmp/" + dossier +"/"+ file, encoding="utf-8").readlines()
                    date_gen = current_file[0].split(" ") #ligne avec la date
                    date_mail = datetime.strptime((date_gen[1]), '%d/%m/%Y') #Date et horraire du mail
                    if(date_mail >= exp) :
                        nb_mail +=1
                        date = current_file[0][9:]
                        exped = current_file[1][9:]
                        ID = dossier+"-"+file
                        corpusTmp.append(str(nb_mail) + ". ID: "+ID+ " Date: " + date + " | "+ exped)

        else : # Recherche entre 2 dates
            exp2 = str(input("Seconde date (format jj/mm/aaaa) : "))

            if (len(exp2) == 10) : # Conversion de la date
                exp2 = datetime.strptime((exp2.split(" ")[0]), '%d/%m/%Y')
            else :
                print("Format incorrect\n")
                exit(1)
            for dossier in os.listdir("tmp") :
                for file in os.listdir("tmp/" + dossier):
                    current_file = open("tmp/" + dossier +"/"+ file, encoding="utf-8").readlines()
                    date_gen = current_file[0].split(" ") #ligne avec la date
                    date_mail = datetime.strptime((date_gen[1]), '%d/%m/%Y') #Date et horraire du mail
                    if(exp <= date_mail <= exp2) :
                        nb_mail +=1
                        date = current_file[0][9:]
                        exped = current_file[1][9:]
                        ID = dossier+"-"+file
                        corpusTmp.append(str(nb_mail) + ". ID: "+ID+ " Date: " + date + " | "+ exped)

    elif(choice == 3): # Recherche par présence de pièces jointes
        exp = input("Contient une/des pièces [o/n]\nVotre choix : ")
        flag = (exp.lower() == "o")
        for dossier in os.listdir("tmp") :
            for file in os.listdir("tmp" + "/" + dossier):
                current_file = open("tmp" + "/" + dossier +"/"+ file, encoding="utf-8").readlines()
                if(("." in current_file[4]) == flag) :
                    nb_mail +=1
                    date = current_file[0][9:]
                    exped = current_file[1][9:]
                    ID = dossier+"-"+file
                    corpusTmp.append(str(nb_mail) + ". ID: "+ID+ " Date: " + date + " | "+ exped)

    elif(choice == 4): # Recherche par objet
        exp = str(input("Mot-clé à rechercher :"))
        for dossier in os.listdir("tmp") :
            for file in os.listdir("tmp" + "/" + dossier):
                current_file = open("tmp" + "/" + dossier +"/"+ file, encoding="utf-8").readlines()
                if((exp in current_file[3])) :
                    nb_mail +=1
                    date = current_file[0][9:]
                    exped = current_file[1][9:]
                    ID = dossier+"-"+file
                    corpusTmp.append(str(nb_mail) + ". ID: "+ID+ " Date: " + date + " | "+ exped)

    else: # Recherche par contenu
        exp = str(input("Mot-clé à rechercher :"))
        for dossier in os.listdir("tmp") :
            for file in os.listdir("tmp" + "/" + dossier):
                current_file = open("tmp" + "/" + dossier +"/"+ file, encoding="utf-8").readlines()
                i = 5
                while(i < len(current_file)):
                    if((exp in current_file[i])) :
                        nb_mail +=1
                        date = current_file[0][9:]
                        exped = current_file[1][9:]
                        ID = dossier+"-"+file
                        corpusTmp.append(str(nb_mail) + ". ID: "+ID+ " Date: " + date + " | "+ exped)
                        break
                    i+=1

    print("Nombre de mails trouvés : "+str(nb_mail)+"\n")
  
    if(nb_mail == 0) :
        print("Aucun résultat suivant vos critères\n")
        exit(1)
    for i in range (len(corpusTmp)):
        print(corpusTmp[i])

    choice = input("Combien de mails voulez-vous sélectionner ?\n Tout : \"tout\"\n Un ou certains : numéro des mails séparés par un espace\n Votre choix : ")
    if(choice == "tout") :
        for i in range (len(corpusTmp)):
            print(corpusTmp[i].split(" ")[2])
            corpus += corpusTmp[i].split(" ")[2] + " "
    else:
        choice = choice.split(" ")
        for i in range (len(choice)):
            print(corpusTmp[int(choice[i])-1].split(" ")[2])
            corpus +=corpusTmp[int(choice[i])-1].split(" ")[2] + " "
    return corpus