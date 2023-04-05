import mysql.connector

class EmployesCRUD:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    
    def create(self, nom, prenom, salaire, id_service):
        cursor = self.db.cursor()
        sql = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        val = (nom, prenom, salaire, id_service)
        cursor.execute(sql, val)
        self.db.commit()
        return cursor.lastrowid
    
    def read(self, id):
        cursor = self.db.cursor()
        sql = "SELECT * FROM employes WHERE id=%s"
        val = (id,)
        cursor.execute(sql, val)
        return cursor.fetchone()
    
    def update(self, id, nom, prenom, salaire, id_service):
        cursor = self.db.cursor()
        sql = "UPDATE employes SET nom=%s, prenom=%s, salaire=%s, id_service=%s WHERE id=%s"
        val = (nom, prenom, salaire, id_service, id)
        cursor.execute(sql, val)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "DELETE FROM employes WHERE id=%s"
        val = (id,)
        cursor.execute(sql, val)
        self.db.commit()
    
    def list_all(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM employes"
        cursor.execute(sql)
        return cursor.fetchall()


crud = EmployesCRUD("localhost", "root", "", "laplateforme")


# Créer un nouvel employé
id = crud.create("Dupont", "Jean", 2500, 2)

# Lire les informations d'un employé
employe = crud.read(id)
print(employe) # (id, nom, prenom, salaire, id_service)

# Mettre à jour les informations d'un employé
crud.update(id, "Dupont", "Jeanne", 3000, 2)

# Supprimer un employé
crud.delete(id)

# Lister tous les employés
employes = crud.list_all()
for employe in employes:
    print(employe) # (id, nom, prenom, salaire, id_service)
