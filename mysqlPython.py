#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################################
# mysqlPython.py
#
# Connexion au serveur MySQL et insertion de donnée
# Module : MySQLd
#
######################################################

import MySQLdb as mysql

db = mysql.connect("localhost" , "root" , "MySQL" , "myBDD")
cursor = db.cursor()

req="INSERT INTO Mesures (Date, Temperature, Ph, Distance) VALUES (NOW(), '25.7', '8.3', '124');" 

cursor.execute(req)

db.commit()



