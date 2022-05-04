# Projet INTER2-HUT ✉

## Projet d'analyseur de mails dans le cadre d'un sous-projet pour l'HUman at home projecT 🏠

### 🖐Contributeurs : Adam S, Arnaud C, Gatien H, Maxime B

### 👩‍🏫Encadré par : Anne Laurent

Ce projet consiste en un analyseur permettant de déteminer des données telles que les nombre d'adresses différentes, la proportion de pièces jointes, la longueur moyenne de mails, le temps de réponse dans un fil de discussion et bien d'autres. Tout cela à partir de mails.

Pour ce faire le programme utilise des mails exportés depuis Thunderbird qu'il va analyser, découper et nettoyer pour ensuite pouvoir appliquer des filtres et des calculs dessus afin de déterminer les informations demandées.

## Comment l'utiliser ❔

❗ Il vous faut avoir Python3 🐍 d'installé sur votre machine ❗

1. Tout d'abord téléchargez le package sur notre Github.
2. Depuis Thunderbird exportez vos mails dans des fichiers.
   - Pour ce faire, sélectionnez les dossiers dans l'arborescence à gauche (ou Boîte de réception).
   - Clique droit, Enregistrez-sous, Format texte brut.
   - Attention, plus il y'a de mails dans un fichier plus il sera long à analyser. Nous vous conseillons d'exporter chaque années séparement voire chaque mois en créant de nouveaux dossiers.
3. Si vous êtes sur ```Windows``` vous pouvez lancer le fichier "launcher.bat" puis suivre les insctructions.
4. Si vous êtes sur ```MacOS ou Linux``` vous pouvez dans l'invité de commande (terminal) entrer la commande :
  ```python3 main.py``` depuis le répertoire du programme
5. Comme indiqué par le programme, glissez les mails dans le dossier ```__MAIL_DEPOT__``` et tapez "ok".
6. Laissez le programme analyser vos mails puis suivez les instructions à l'écran.

## Les Possibilités 🔧

> Pour chaque fonction il est possible d'au préalable filtrer les mails par adresse, date (précise, avant, après, entre), mot contenu, présence de pièces jointes ou bien d'utiliser les mails regroupés par fils de discussion

Sur un corpus de mails vous pouvez :

- Calculer le temps de réponse
- Calculer la longueur de moyenne des mails par adresses
- Générer des rapports précisant la part d'adresses par corpus, le nombre de mails par mois ou jour de la semaine et le pourcentage de pièces jointes
- Exporter vos données précédemment calculées