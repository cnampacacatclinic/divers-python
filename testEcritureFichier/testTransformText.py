import csv

#Pour modifier le texte suivant dans un fichier 
#nom,metier,couleur_preferee
#Jacob Smith,Ingénieur en informatique,Violet
#Nora Scheffer,Stratégiste numérique,Bleu
#Emily Adams,Responsable Marketing,Orange "
#

#Et pour obtenir qq ch comme 
#['nom', 'metier', 'couleur_preferee']
#['Jacob Smith', 'Ingénieur en informatique', 'Violet']
#['Nora Scheffer', 'Stratégiste numérique', 'Bleu']
#
#VOICI UN PREMIER EXEMPLA SANS LE PACKAGE CSV


# Lire le contenu du fichier d'origine et le transformer
with open("file.txt", "r") as fichier:
    lignes = fichier.readlines()

# Créer une liste de listes à partir des lignes lues
tableau = [ligne.strip().split(',') for ligne in lignes]

# Écrire la nouvelle structure formatée dans un nouveau fichier
with open("output.txt", "w") as fichier:
    for ligne in tableau:
        fichier.write(f"{ligne}\n")

#SECOND EXEMPLE AVEC LE PACKAGE CSV

# Lire le contenu du fichier d'origine et le transformer
with open("file.txt", "r") as fichier:
    reader = csv.reader(fichier)
    tableau = [row for row in reader]

# Écrire la nouvelle structure formatée dans un nouveau fichier
with open("couleurs_preferees.csv", "w") as fichier:
    for row in tableau:
        fichier.write(f"{row}\n")

#DictReader() est une méthode de csv qui sait que la première ligne est l'en-tête des colones
with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])
