# À l’aide d’une requête, calculer la somme des capacités des salles et afficher le résultat
# en console.

#  create table employes (
#     -> id int primary key auto_increment,
#     -> nom varchar(255) not null,
#     -> prenom varchar(255) not null,
#     -> salaire decimal(10,2) not null,
#     -> id_service int not null
#     -> );

# Insérer des employées dans la table “employes”.

#  insert into employes (nom, prenom, salaire, id_service)
#     -> values
#     -> ('Jean', 'delacours', 3556.27, 3),
#     -> ('John', 'doe', 8410.84, 1),
#     -> ('Jeanne', 'binkie', 1594.40, 2),
#     -> ('Clara', 'binkie', 3684.61, 3),
#     -> ('Josette', 'delacours', 3984.61, 1);


# Écrire une requête SQL pour récupérer tout les employées dont le salaire est supérieur à
# 3 000 €. Exécuter la requête et afficher le résultat.

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

# Exécutez la requête SQL pour recuperer tous les employé avec un salaire supérieur a 3000€
cursor.execute("SELECT * FROM employes WHERE salaire > 3000")
result = cursor.fetchall()

for resultat in result:
    print(resultat)

# Fermez le curseur 
cursor.close()


# Ajouter la table “services” contenant les champs suivants :
# - id, int, primary key, auto-incrémente
# - nom, varchar

# create table service (
#         id int primary key auto_increment
#         nom varcchar(255)not null


# Insérer des services dans votre table.

#  insert into service (nom)
#     -> values
#     -> ('Administration'),
#     -> ('Comptabilité'),
#     -> ('R&D'),
#     -> ('Ressource humaine');


# Récupérer tous les employés et leur service respectif. Afficher le résultat en console.

cursor = conn.cursor()

cursor.execute("SELECT employes.nom, employes.prenom, service.nom AS service FROM employes INNER JOIN service ON employes.id_service = service.id")
result2 = cursor.fetchall()

for res in result2:
    print(res)

cursor.close()
conn.close()
