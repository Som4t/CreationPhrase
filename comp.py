import random
import pymysql
import time


connection = pymysql.connect(host="localhost",user="root",passwd="root",database="bddphrase" )
cursor = connection.cursor()

nombre_sujet=0
total=0
cursor.execute("select count(idTerme) from terme")
ai= cursor.fetchone()


caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789"
longueur = 10
mdp = ""
compteur = 0
result= int(ai[0])+1

fichier = open("chrono.txt", "a")
fichier.write("\nCompléments")

start = time.time()
while total != 100000:
    tic=time.time()
    while nombre_sujet != 10000:
        while compteur < longueur:
            lettre = caracteres[random.randint(0, len(caracteres)-1)] 
            mdp += lettre
            compteur += 1 
        result+=1
        print(result)
        cursor.execute("INSERT INTO `terme`(`idTerme`, `libelle`, `idLangue`, `idTypeTerme`) values(%s,%s,1,3)", (str(result), mdp))
        nombre_sujet+=1
        connection.commit()
    total+=nombre_sujet
    nombre_sujet=0
    tac=time.time()
    fichier.write("\nNombre sujet:"+str(total)+" Temps: "+ str(tac-tic) +"secondes")
    
stop = time.time()
fichier2 = open("tempstotal.txt", "a")
fichier2.write("\nCompléments, temps: "+str(stop-start)+" secondes")
fichier2.close()

fichier.close()

connection.close()