#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################################
# comArduino.py
#
# Communication serial entre Arduino et Raspberry
# Protocol :
#  - Emettre "M" pour demander les mesures
#  - Recevoir un entier entre 0 et 1023 suivit de \r\n
#  - 9600bps, 8, 1, n, n
######################################################

import serial

import time    # pour le délai d'attente entre les messages

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1)   #on attend un peu, pour que l'Arduino soit pret.

ser.write('M')
recu = ser.readline() #on affiche la reponse
print(recu)

ser.close()
