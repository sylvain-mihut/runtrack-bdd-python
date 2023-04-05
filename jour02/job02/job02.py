# À l'aide de votre terminal SQL, créez les tables suivantes :
# - “etage” ayant comme champs :

# ● id, int, clé primaire et Auto Incrément
# ● nom, varchar de taille 255
# ● numero, int
# ● superficie, int
# - “salles” ayant comme champs :

# ● id, int, clé primaire et Auto Incrément
# ● nom, varchar de taille 255
# ● id_etage, int
# ● capacite, int


#  create table etage (

#     -> id int primary key auto_increment,
#     -> nom varchar(255) not null,
#     -> numero int not null,
#     -> superficie int not null
#     -> );


#  create table salles (
#     -> id int primary key auto_increment,
#     -> nom varchar(255)
#     -> not null,
#     -> id_etage int not null,
#     -> capacite int not null
#     -> );