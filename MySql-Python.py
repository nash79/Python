import random
import mysql.connector

from datetime import date

lstnames = ['tata','toto', 'ritchi', 'paul', 'apple', 'nano']
lstprenom = ['gg','fifi','low','flo','tyty','riri']
lstville = ['paris','montpellier','bordeaux','nimes','marseille','nice']
lstcodepostal =['75000','34000','33000','30000','13000','06000']


cnx = mysql.connector.connect(user='root', database='db_cours')
cursor = cnx.cursor()

cursor.execute("truncate utilisateur")

for index in range(0,5000):

    nom = random.choice(lstnames)
    prenom = random.choice(lstprenom)
    email = nom +  '.' + prenom + '@laposte.fr'
    datenaissance = date(random.randint(1970,1999),random.randint(1,12), random.randint(1,28))
    pays = 'france'

    indexville = int(random.randint(0,5))

    ville = lstville[indexville]
    codepostal = lstcodepostal[indexville]

    user = (index,nom,prenom,email,datenaissance,pays,ville,codepostal)


    cursor.execute("""insert into utilisateur (id,nom, prenom,email,date_naissance,pays, ville, code_postal) values (%s,%s,%s,%s,%s,%s,%s,%s)""", user)

cursor.close()

cnx.commit()

cnx.close()
