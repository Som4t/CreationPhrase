import random
import pymysql
import time
from connectionbdd import connectionbdd

connect = connectionbdd()

sujet = "Select * from terme where idTypeTerme = 1"
verbe = "Select * from terme where idTypeTerme = 2"
complement = "Select * from terme where idTypeTerme = 3"

# Sujets
connect[0].execute(sujet)
sujets = connect[0].fetchall()

# Verbes
connect[0].execute(verbe)
verbes = connect[0].fetchall()

# Compléments
connect[0].execute(complement)
complements = connect[0].fetchall()

connect[0].execute("select count(idPhrase) from phrase")
ai= connect[0].fetchone()
result= int(ai[0])+1

fichier = open("chronogenerateur.txt", "a")
compteur=0

start = time.time()
for x in sujets:
	for y in verbes:
		for z in complements:
			connect[0].execute("INSERT INTO `phrase`(`idPhrase`, `idLangue`) VALUES (%s,1)", (str(result)))
			connect[0].execute("INSERT INTO `asso_2`(`idTerme`, `idPhrase`) VALUES (%s,%s)", (x[0], str(result)))
			connect[0].execute("INSERT INTO `asso_2`(`idTerme`, `idPhrase`) VALUES (%s,%s)", (y[0], str(result)))
			connect[0].execute("INSERT INTO `asso_2`(`idTerme`, `idPhrase`) VALUES (%s,%s)", (z[0], str(result)))
			result+=1
			print(str(result))
			if result%200000==0:
				connect[1].commit()

stop = time.time()
fichier2 = open("generateurtotal.txt", "a")
fichier2.write("\nGénérateur phrase, temps: "+str(stop-start)+" secondes")
fichier2.close()
fichier.close()



connect[1].commit()
connect[1].close()