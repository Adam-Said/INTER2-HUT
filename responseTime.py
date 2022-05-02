from datetime import datetime
from operator import itemgetter
import os


#Renvoie le tableau de tableaux [@,time] pour chaque mail de 'folder'
def getTimesFolder(folder) :
    resTab = []
    for mail in os.listdir(folder):
        tempTab = []
        currentFile = open(folder + str(mail), encoding="utf-8", errors="surrogateescape").readlines()
        sSender = currentFile[1][9:-1]
        sDate = currentFile[0][9:-1]
        dtDate = datetime.strptime(sDate, "%d/%m/%Y %H:%M:%S")
        tempTab.append(sSender)
        tempTab.append(dtDate)
        resTab.append(tempTab)
    return sorted(resTab, key=itemgetter(1))

def graphTimes(arrayTimes) :
    indent = ""
    for i in range (len(arrayTimes)) :
        if (i == 0) :
            displayString = arrayTimes[0][0] + " a écrit le " + toStringDT(str(arrayTimes[0][1]))
            indent += "    "
        else :
            displayString = indent + "|  " + arrayTimes[i][0] + " a répondu " + toStringDTdiff(str(arrayTimes[i][1] - arrayTimes[i-1][1])) + " plus tard"
            indent += "    "
        print(displayString)

def toStringDT(Sdatetime) :
    months = [" Janvier"," Février","Mars"," Avril"," Mai"," Juin"," Juillet"," Août"," Septembre"," Octobre"," Novembre"," Décembre"]
    resString = Sdatetime[8:10] + months[int(Sdatetime[5:7])-1] + " " + Sdatetime[0:4] + " à " + Sdatetime[11:13] + "h" + Sdatetime[14:16] + "m" + Sdatetime[17:19] + "s"
    return resString
  
def toStringDTdiff(Sdatetime) :
    if ("days" in Sdatetime) :
        resString = Sdatetime[0:2].replace(" ","") + " jours "
        Sdatetime = Sdatetime[8:]
        dt = Sdatetime.split(":")
        return resString + dt[0] + " heures " + dt[1] + " minutes " + dt[2] + " secondes"
    else :
        if ("day" in Sdatetime) :
            resString = Sdatetime[0:1] + " jour "
            Sdatetime = Sdatetime[7:]
            dt = Sdatetime.split(":")
            return resString + dt[0] + " heures " + dt[1] + " minutes " + dt[2] + " secondes"
        else :
            dt = Sdatetime.split(":")
            return dt[0] + " heures " + dt[1] + " minutes " + dt[2] + " secondes"


def main(corpus):
    current_folder = "threads/" + str(corpus) + "/"
    arrayTimes = getTimesFolder(current_folder)
    graphTimes(arrayTimes)
    print("\nExporter ces résultats dans un fichier ? (o/n) ")
    choix = input()
    if (choix in ["y","Y","O","o","1"]) :
        resString = "sep=;\nadresse;date;heure\n"
        for temps in arrayTimes :
            resString += temps[0] + ";" + (str(temps[1])).split(" ")[0] + ";" + (str(temps[1])).split(" ")[1] + "\n"
        text_file = open("rapport_"+corpus+".csv", "w", encoding="utf-8", errors="surrogateescape")
        text_file.write(resString)
        text_file.close()
        print("Données exportées avec succès")