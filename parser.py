import os
import shutil
from difflib import SequenceMatcher

# Dictionnaire des caractères UTF-8 pour le réencodage
utf_code = [ligne.split(":") for ligne in open("dico_utf8.txt", encoding="utf-8")]
utf8Dico = {utf[0]:utf[1].strip('\n') for utf in utf_code}

def dateTranslation(date_input) : # Traduction des mois en lettres en chiffres
    date_tmp = date_input.split(" ")
    for element in date_tmp:
        if(element == "" or element == " "):
            date_tmp.remove("")
    jour = date_tmp[1]
    mois = date_tmp[2]
    annee = date_tmp[3]
    horraire = date_tmp[4].split(":")
    heure = horraire[0]
    minute = horraire[1]
    seconde = horraire[2]

    if (mois == "Jan"):
        mois = "01"
    elif (mois == "Fev" or mois == "Feb"):
        mois = "02"
    elif (mois == "Mar"):
        mois = "03"
    elif (mois == "Avr" or mois == "Apr"):
        mois = "04"
    elif (mois == "Mai" or mois == "May"):
        mois = "05"
    elif (mois == "Jui" or mois == "Jun"):
        mois = "06"
    elif (mois == "Jul"):
        mois = "07"
    elif (mois == "Aou" or mois == "Aug"):
        mois = "08"
    elif (mois == "Sep"):
        mois = "09"
    elif (mois == "Oct"):
        mois = "10"
    elif (mois == "Nov"):
        mois = "11"
    elif (mois == "Dec"):
        mois = "12"
    else :
        mois = "Unknown"

    return jour+"/"+mois+"/"+annee+" "+heure+":"+minute+":"+seconde

def cutter() :
    for bigFile in os.listdir("__MAIL_DEPOT__"):
        try:
            os.mkdir("tmp/" + str(bigFile))
        except:
            shutil.rmtree("tmp/" + str(bigFile))
            os.mkdir("tmp/" + str(bigFile))
            True
        with open("__MAIL_DEPOT__/" + bigFile, encoding="utf-8", errors="surrogateescape") as currentBigFile:
            mailCount = 0
            writingState = 0
            for line in currentBigFile:
                if(line.startswith("From - ") and writingState == 0):
                    try:
                        mailFile.close() # Warning normal : faux positif
                    except:
                        True
                    mailCount += 1
                    mailFile = open("tmp/" + str(bigFile) + "/" + str(mailCount), "w",encoding="utf-8", errors="surrogateescape")
                    writingState = 1

                elif(line.startswith("From - ") and writingState == 1):
                    mailFile.close()
                    mailCount += 1
                    mailFile = open("tmp/" + str(bigFile) + "/" + str(mailCount), "w", encoding="utf-8", errors="surrogateescape")
                    writingState = 0

                mailFile.write(line)
            mailFile.close()
        currentBigFile.close()


def cleaner() :
    for dossier in os.listdir("tmp"):
        mailCount = 0
        for file in os.listdir("tmp/" + dossier):
            mailCount += 1
            dateEnvoi = "__Date__ "
            expediteur = "__From__ "
            destinataire = "__To__ "
            objet = "__Object__ "
            pieceJ = "__PJ__ "
            content = "__CONTENT__ "
            currentFile = open("tmp/" + dossier +"/"+ file, encoding="utf-8", errors="surrogateescape").readlines()
            for i in range(len(currentFile)):
                ligne = currentFile[i]
                for key, value in utf8Dico.items():
                    if key in ligne:
                        ligne = ligne.replace(key, value)
                # Récupération de la date du mail
                if (ligne.startswith('Date:')) and (dateEnvoi == "__Date__ "):
                    dateEnvoi += dateTranslation(ligne[6:])
                # Récupération du sujet
                if (ligne.startswith('Subject:')) and (objet == "__Object__ "):
                    objTMP = ligne[9:]
                    if(objTMP.find('/') or objTMP.find('\\') or objTMP.find(':') or objTMP.find('?') or objTMP.find('"') or objTMP.find('<') or objTMP.find('>') or objTMP.find('|')):
                        objTMP = objTMP.replace("/",'-')
                        objTMP = objTMP.replace("\\",'-')
                        objTMP = objTMP.replace(":",'-')
                        objTMP = objTMP.replace("?",'-')
                        objTMP = objTMP.replace("\"",'-')
                        objTMP = objTMP.replace("<",'-')
                        objTMP = objTMP.replace(">",'-')
                        objTMP = objTMP.replace("|",'-')
                    if(objTMP.find('.')):
                        objTMP = objTMP.replace('.',"")
                    if(objTMP.startswith("Re - ")) :
                        objTMP = objTMP[5:]
                    if(objTMP.startswith("Re- ")):
                        objTMP = objTMP[4:]
                    if(objTMP.startswith("=-")) :
                        objTMP = objTMP[objTMP.find("Q-")+2:]
                    if(objTMP.find("-Q-")) :
                        objTMP = objTMP[objTMP.find("Q-")+1:]
                    if(objTMP.find("-=")) :
                        objTMP = objTMP.replace("-=","")
                    if("Re_" in objTMP) :
                        objTMP = objTMP[3:]
                    if(objTMP.startswith(" ")) :
                        objTMP = objTMP[1:]
                    if(objTMP.endswith(" ") or objTMP.endswith(" \n")) :
                        objTMP = objTMP[:-2]
                    if(objTMP == "" or objTMP == " " or objTMP == "\n" or objTMP == " \n"):
                        objTMP = "empty"
                    objet += objTMP.split("\n")[0]
                    if(objet == "__Object__ " or objet == "__Object__ \n"):
                        objet += "empty"
                # Récupération de l'expéditeur
                if (ligne.startswith('From:')) and (expediteur == "__From__ "):
                    expediteur = expediteur + ligne[ligne.find("<") + 1:ligne.find(">")]
                # Récupération du/des destinataire(s)
                if (ligne.startswith("To:")):
                    desti = []
                    desti.append(ligne[4:])
                    cpt = 1
                    while ((i + cpt) < len(currentFile)) and ((currentFile[i + cpt]).find("\t") == 0):
                        desti.append(currentFile[i + cpt][4:])
                        cpt += 1
                    for ligne_desti in desti:
                        tab_desti = ligne_desti.split(" ")
                        for addr in tab_desti:
                            if addr.count("@"):
                                if addr.count(";"):
                                    addr = addr[:-1]
                                if addr.count("<"):
                                    addr = addr[1:-2]
                                if addr.count("\""):
                                    addr = addr[1:-2]
                                for i in range(len(addr.split("\n"))):
                                  destinataire += addr.split("\n")[i]
                                
                # Récupération des pièces jointes
                if (("name=\"") in ligne):
                    pieceJ = pieceJ + ligne.split('=')[1].strip("\n") + " - "
        
                # Récupération du contenu
                if ligne.startswith("Content-Type: text/plain;"):
                    j = i + 1
                    while (j < len(currentFile)) and (not("Content-Type:" in currentFile[j])):
                        # Suppression de certaines lignes de métadonnées innutiles et des blocs clés
                        if(currentFile[j].startswith("Content-") or (("charset=") in currentFile[j]) or currentFile[j].startswith("--Apple-Mail") or ("*****************" in currentFile[j]) or currentFile[j].startswith("------=_") or (currentFile[j].find(" ") > 60) or ((len(currentFile[j]) > 1) and (currentFile[j].count(" ") == 0))):
                            j += 1
                        # Suppression des signatures
                        elif (("PENSEZ A L'ENVIRONNEMENT AVANT D'IMPRIMER CE MESSAGE !" in currentFile[j])):
                            j += 21
                        elif (currentFile[j].startswith("### NOTICE LEGALE ###")):
                            j += 11
                        else:
                            if not(currentFile[j].endswith("=")):
                                content += currentFile[j]
                                content += "\n"
                            else:
                                content += currentFile[j][:-1]
                            j += 1 

            os.remove("tmp/" + dossier +"/"+ file)
            content = content.split("\n")
            newContent = ""
            for i in range(len(content)):
                ligne = content[i].strip()
                if(ligne == "\n" or ligne == "" or ligne.startswith(">")):
                    continue
                for key, value in utf8Dico.items():
                    if key in ligne:
                        ligne = ligne.replace(key, value)
                newContent += ligne + "\n"
            mailArray = []
            mailArray.append(dateEnvoi + "\n")
            mailArray.append(expediteur + "\n")
            mailArray.append(destinataire + "\n")
            mailArray.append(objet + "\n")
            mailArray.append(pieceJ + "\n")
            mailArray.append(newContent)
            newMail = open("tmp/" + dossier +"/"+ file, "w", encoding="utf-8", errors="surrogateescape")
            for line in mailArray:
                newMail.write(line)
            newMail.close()



def threader():
    for dossier in os.listdir("tmp"):
        for file in os.listdir("tmp/" + dossier):
            currentFile = open("tmp/" + dossier +"/"+ file, "r", encoding="utf-8", errors="surrogateescape").readlines()
            objet = currentFile[3][11:]
            try:
                if(os.name == "posix"):
                    os.mkdir("threads/" + str(objet.replace("\n","")))
                else:
                    os.mkdir("threads\\" + str(objet.replace("\n","")))
            except:
                True
            fullDateTime = currentFile[0][9:].split(" ")
            date = fullDateTime[0].split("/")
            time = fullDateTime[1].split(":")
            dateTime = str(date[2] + "_" + date[1] + "_" + date[0] + "-" + time[0] + "_" + time[1] + "_" + time[2])
            newFile = open("threads/" + str(objet.replace("\n","")) + "/" + str(dateTime.replace("\n","")), "w", encoding="utf-8", errors="surrogateescape")
            for line in currentFile:
                newFile.write(line)
            newFile.close()
    for dossier in os.listdir("threads"):
        for dossier2 in os.listdir("threads"):
            if(dossier != dossier2):
                s = SequenceMatcher(None, dossier, dossier2)
                if(s.ratio() > 0.75):
                    for mail in os.listdir("threads/"+dossier):
                        fd = open("threads/" + dossier + "/" + mail, "r", encoding="utf-8", errors="surrogateescape").readlines()
                        newFile = open("threads/" + dossier2 + "/" + mail, "w", encoding="utf-8", errors="surrogateescape")
                        for line in fd:
                            newFile.write(line)
                        newFile.close()
                        os.remove("threads/" + dossier + "/" + mail)
                    os.rmdir("threads/" + dossier)

