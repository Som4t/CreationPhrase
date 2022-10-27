import random
import pymysql
import time

connection = pymysql.connect(host="localhost",user="root",passwd="root",database="bddphrase" )
cursor = connection.cursor()

sujet = "Select * from terme where idTypeTerme = 1"
verbe = "Select * from terme where idTypeTerme = 2"
complement = "Select * from terme where idTypeTerme = 3"

# Sujets
cursor.execute(sujet)
sujets = cursor.fetchall()

# Verbes
cursor.execute(verbe)
verbes = cursor.fetchall()

# Compléments
cursor.execute(complement)
complements = cursor.fetchall()

cursor.execute("select count(idPhrase) from phrase")
ai= cursor.fetchone()
result= int(ai[0])+1

fichier = open("chronogenerateur.txt", "a")
compteur=0

start = time.time()
for x in sujets:
	for y in verbes:
		for z in complements:
			cursor.execute("INSERT INTO `phrase`(`idPhrase`, `idLangue`) VALUES (%s,1)", (str(result)))
			# connection.commit()
			cursor.execute("INSERT INTO `asso_2`(`idTerme`, `idPhrase`) VALUES (%s,%s)", (x[0], str(result)))
			cursor.execute("INSERT INTO `asso_2`(`idTerme`, `idPhrase`) VALUES (%s,%s)", (y[0], str(result)))
			cursor.execute("INSERT INTO `asso_2`(`idTerme`, `idPhrase`) VALUES (%s,%s)", (z[0], str(result)))
			result+=1
			print(str(result))
			if result%200000==0:
				connection.commit()

stop = time.time()
fichier2 = open("generateurtotal.txt", "a")
fichier2.write("\nGénérateur phrase, temps: "+str(stop-start)+" secondes")
fichier2.close()
fichier.close()



connection.commit()
connection.close()