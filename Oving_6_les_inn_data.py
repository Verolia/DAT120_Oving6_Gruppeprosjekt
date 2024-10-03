# -*- coding: utf-8 -*-

import csv
from datetime import datetime
import matplotlib.pyplot as plt

def les_data(filnavn):

    lokal_tidspunkt = []
    lokal_temperatur = []
    lokal_trykk = []
    bar_trykk = []
    bar_trykk_tidspunkt = []
    
    
    with open(filnavn, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for rad in reader:
            if len(rad) == 5: 
                dato_tid = rad[0]
                absolutt_trykk = rad[3].replace(",", ".")
                temperatur = rad[4].replace(",", ".")
                if rad[2] != " ":
                    trykk_barometer = rad[2].replace(",", ".")
                    bar_tidspunkt = rad[0]
                
                try: 
                    dato_tid_objekt = datetime.strptime(dato_tid,'%m.%d.%Y %H:%M')
                    lokal_tidspunkt.append(dato_tid_objekt)
                    lokal_trykk.append(float(absolutt_trykk))
                    lokal_temperatur.append(float(temperatur))
                    bar_trykk.append(float(trykk_barometer))
                    bar_dato_objekt = datetime.strptime(bar_tidspunkt,'%m.%d.%Y %H:%M')
                    bar_trykk_tidspunkt.append(bar_dato_objekt)
                except ValueError:
                    continue
  
    return lokal_tidspunkt, lokal_trykk, lokal_temperatur, bar_trykk, bar_trykk_tidspunkt
        
filnavn = "trykk_og_temperaturlogg_rune_time.csv.txt"
lokal_tidspunkt, lokal_trykk, lokal_temperatur, bar_trykk, bar_trykk_tidspunkt = les_data(filnavn)

def gjennomsnitt(tallene):
    return sum(tallene)/len(tallene)
n = 60

gjennomsnitt_t = []
for i in range(0,len(lokal_temperatur),n):
    split_list = lokal_temperatur[i:n+i]
    gjennomsnitt_t.append(gjennomsnitt(split_list))
#print(gjennomsnitt_t)

gjennomsnitt_dato =[]
gjennomsnitt_dato = lokal_tidspunkt[0::n]


plt.subplot(2, 1, 1)
plt.plot(lokal_tidspunkt, lokal_temperatur, color="blue", label="Temperatur (Celcius)")
plt.plot(gjennomsnitt_dato, gjennomsnitt_t, color="orange")
plt.legend(['Gjennomsnitt temperatur'])
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(lokal_tidspunkt, lokal_trykk, color ="blue", label="Trykk")
plt.plot(bar_trykk_tidspunkt, bar_trykk, color="orange")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

