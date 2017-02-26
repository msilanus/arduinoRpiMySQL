#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################################
# surveillanceRiviere.py
#
# Communication serial entre Arduino et Raspberry
# Module : serial
# Protocol :
#  - Emettre "M" pour demander les mesures
#  - Recevoir une chaine "temp;ph;dist\r\n"
#  - 9600bps, 8, 1, n, n
# 
# Connexion au serveur MySQL et insertion de donnée 
# Module : MySQLdb
# Données :
#  - Date : date et heure de la mesure
#  - Temperature : DFRobot LM35 Linear Temperature Sensor
#  - Ph : Kit pH-mètre Analogique DFRobot Gravity
#  - Distance : Parallax Ping Ultrasonic Distance Sensor  
######################################################
import MySQLdb as mysql
import serial
import time
    
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1)   #on attend un peu, pour que l'Arduino soit prêt.

ser.write('M')
recu = ser.readline() #on affiche la reponse
print(recu)
# Test
# recu = "14.1;7.1;239;\r\n"
mesure=recu.split(";")
print(recu)
print(mesure[0])
print(mesure[1])
print(mesure[2]) 
ser.close()

db = mysql.connect("localhost" , "root" , "MySQL" , "myBDD") 
cursor = db.cursor() 
req="INSERT INTO Mesures (Date, Temperature, Ph, Distance) VALUES (NOW(),%s, %s, %s);" % (mesure[0], mesure[1], mesure[2])
cursor.execute(req) 
db.commit()
