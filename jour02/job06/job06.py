# À l’aide d’une requête, calculer la somme des capacités des salles et afficher le résultat
# en console.

import mysql.connector 

# Connexion à la BDD
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)

# Créez un curseur pour exécuter les requêtes SQL
cursor = conn.cursor()

# Exécutez la requête SQL pour calculé la capacité de toute les salle de la table "salles"
cursor.execute("SELECT SUM(capacite) FROM salles")
result = cursor.fetchone()[0]

print("la capacité totale des salles est :", result, "places")

# Fermez le curseur et la connexion à la base de données
cursor.close()
conn.close()