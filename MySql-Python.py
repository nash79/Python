import random
import mysql.connector
from datetime import date

def existegroup(idu, idg):
    param = (idu, idg)
    cursor.execute("""Select count(*) FROM utilisateur_group where idutilisateur=%s and idgroup=%s""", param)
    return cursor.fetchone()[0]

lstnames = ['tata','toto', 'ritchi', 'paul', 'apple', 'nano']
lstprenom = ['gg','fifi','low','flo','tyty','riri']
lstville = ['paris','montpellier','bordeaux','nimes','marseille','nice']
lstcodepostal =['75000','34000','33000','30000','13000','06000']
lstgroupe = ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9']

cnx = mysql.connector.connect(user='root', database='db_cours')
cursor = cnx.cursor()

cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
cursor.execute("truncate utilisateur_group;")

cursor.execute("truncate utilisateur;")

cursor.execute("truncate groupe;")

cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

for indexGroups in range(0, 9):
    cursor.execute("""insert into groupe (nom) values (%s)""", (lstgroupe[indexGroups],))
    cnx.commit()

for indexutilisateur in range(0, 50):

    nom = random.choice(lstnames)
    prenom = random.choice(lstprenom)
    email = nom + '.' + prenom + '@laposte.fr'
    datenaissance = date(random.randint(1970, 1999), random.randint(1, 12), random.randint(1, 28))
    pays = 'france'

    indexville = int(random.randint(0,5))

    ville = lstville[indexville]
    codepostal = lstcodepostal[indexville]

    user = (indexutilisateur, nom, prenom, email, datenaissance, pays, ville, codepostal)
    cursor.execute("""insert into utilisateur (id,nom, prenom,email,date_naissance,pays, ville, code_postal) values (%s,%s,%s,%s,%s,%s,%s,%s);""", user)
    cnx.commit()

    for indexgroup in range(0,5):
        iu = int(indexutilisateur)
        ig = int(random.randint(1, 10))
        if existegroup(iu, ig) == 0:
            v = (iu, ig)
            cursor.execute("""insert into utilisateur_group (idutilisateur,idgroup) values (%s,%s);""", v)


cursor.close()
cnx.commit()
cnx.close()
