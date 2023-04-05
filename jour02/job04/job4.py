# Écrire un programme qui récupère tous les noms et les capacités de la table “salles” et
# afficher le résultat en console.

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

# Exécutez la requête SQL pour récupérer le nom et la capacité des salles de la table "salles"
cursor.execute("SELECT nom, capacite FROM salles;")
result = cursor.fetchall()

print(result)

# Fermez le curseur et la connexion à la base de données
cursor.close()
conn.close()