import mysql.connector
from mysql.connector import Error

#On teste la connexion
try:
    # Connexion à la base de données
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='pwd',
        database='bddname'
    )

    if conn.is_connected():
        print('Connexion réussie à MariaDB')

    # Création d'un curseur
    cursor = conn.cursor()

    # Exécution d'une requête SQL
    query = "SELECT * FROM section_bddcursus"
    cursor.execute(query)

    # Utilisation de fetchall() pour récupérer toutes les lignes
    rows = cursor.fetchall()

    # Traitement des résultats
    for row in rows:
        print(row)
#Si on obtient une erreur, on l'affiche
except Error as e:
    print(f"Erreur : {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print('Connexion à MariaDB fermée')
