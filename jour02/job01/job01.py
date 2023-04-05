# Récupérer votre base de données “LaPlateforme” créée hier. À l’aide du module
# “mysql-python-connector”, connectez-vous à votre base de données “LaPlateforme”.
# Récupérer l’ensemble des étudiants et afficher le résultat de la requête en console.

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

# Exécutez la requête SQL pour récupérer tous les étudiants
cursor.execute("SELECT * FROM etudiants")
result = cursor.fetchall()

print(result)

# Fermez le curseur et la connexion à la base de données
cursor.close()
conn.close()