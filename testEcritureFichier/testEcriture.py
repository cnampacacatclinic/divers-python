#On va ecrire dans le fichier
#puis dans le terminal on lance avec la commande :  python testEcriture.py
fichier = open("hello.txt", "w")
fichier.write("Hello, world!")
fichier.close()

#autre version avec with
# Ouverture du fichier en mode écriture avec 'with', ce qui garantit que le fichier sera fermé automatiquement
with open("hello.txt", "w") as fichier:
    # Écriture dans le fichier
    fichier.write("Hello, world!")
