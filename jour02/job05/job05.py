# À l’aide d’un requête calculer la superficie de l’ensemble des étages et afficher “La
# superficie de La Plateforme est de X m2”, X étant le résultat de la requête.

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

# Exécutez la requête SQL pour calculé la superficie total de la table "etage"
cursor.execute("SELECT SUM(superficie) FROM etage")
result = cursor.fetchone()[0]

print("la superficie de La Plateforme est :", result, "m²")

# Fermez le curseur et la connexion à la base de données
cursor.close()
conn.close()