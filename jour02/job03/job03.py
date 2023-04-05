# Ajouter les données suivantes a la table “etage” :
# - RDC, 0, 500
# - R+1, 1, 500

# Ajouter les données suivantes a la table “salles” :
# - Lounge, 1, 100
# - Studio Son, 1, 5
# - Broadcasting, 2, 50
# - Bocal Peda, 2, 4
# - Coworking, 2, 80
# - Studio Video, 2, 5




#  insert into etage (nom, numero, superficie)
#     -> values
#     -> ('RDC', 0, 500),
#     -> ('R+1', 1, 500);

# insert into salles (nom, id_etage, capacite)
#     -> values
#     -> ('lounge', 1, 100),
#     -> ('studio son', 1, 5),
#     -> ('broadcasting', 2, 50),
#     -> ('bocal peda', 2, 4),
#     -> ('coworking', 2, 80),
#     -> ('studio video', 2, 5);



# Exporter votre base de données.

# mysqldump -u root -p laplateforme > laplateforme_V2.sql
