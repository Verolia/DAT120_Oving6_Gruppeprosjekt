# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:05:07 2024

@author: veron
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt


def les_inn_data_2(filnavn): 
    fil2_tidspunkt = []
    fil2_temperatur = []
    fil2_trykk = []
   
    with open(filnavn, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for rad in reader:
            if len(rad) == 5: 
                dato_tid = rad[2]
                absolutt_trykk = rad[4].replace(",", ".")
                temperatur = rad[3].replace(",", ".")
                try:
                    dato_tid_objekt = datetime.strptime(dato_tid, '%d.%m.%Y %H:%M')
                    datetime.strftime(dato_tid_objekt, '%m.%d.%y %H:%M')
                    fil2_tidspunkt.append(dato_tid_objekt)
                    fil2_trykk.append(float(absolutt_trykk))
                    fil2_temperatur.append(float(temperatur))
                except ValueError:
                    continue
                

  
    return fil2_tidspunkt, fil2_trykk, fil2_temperatur
    
fil2_tidspunkt, fil2_trykk, fil2_temperatur = les_inn_data_2("temperatur_trykk_met_samme_rune_time_datasett.csv.txt")


plt.subplot(2, 1, 1)
plt.plot(fil2_tidspunkt, fil2_temperatur, color="blue", label="Temperatur (Celcius)")
plt.legend(['Gjennomsnitt temperatur'])
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(fil2_tidspunkt, fil2_trykk, color ="blue", label="Trykk")
plt.grid()
plt.legend()