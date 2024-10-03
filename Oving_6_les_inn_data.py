# -*- coding: utf-8 -*-

import csv
from datetime import datetime
import matplotlib.pyplot as plt

def les_data(filnavn):

    lokal_tidspunkt = []
    lokal_temperatur = []
    lokal_trykk = []
    
    
    with open(filnavn, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for rad in reader:
            if len(rad) == 5: 
                dato_tid = rad[0]
                absolutt_trykk = rad[3].replace(",", ".")
                temperatur = rad[4].replace(",", ".")
                
                try: 
                    dato_tid_objekt = datetime.strptime(dato_tid,'%m.%d.%Y %H:%M')
                    lokal_tidspunkt.append(dato_tid_objekt)
                    lokal_trykk.append(float(absolutt_trykk))
                    lokal_temperatur.append(float(temperatur))
                except ValueError:
                    continue
  
    return lokal_tidspunkt, lokal_trykk, lokal_temperatur
        
filnavn = "trykk_og_temperaturlogg_rune_time.csv.txt"
lokal_tidspunkt, lokal_trykk, lokal_temperatur = les_data(filnavn)

plt.subplot(2, 1, 1)
plt.plot(lokal_tidspunkt, lokal_temperatur, marker ="o", color="blue", label="Temperatur (Celcius)")
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(lokal_tidspunkt, lokal_trykk, marker ="o", color ="red", label="Trykk")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

def gjennomsnitt(tallene):
    return sum(tallene)/len(tallene)
n = 60

gjennomsnitt_t = []
for i in range(0,len(lokal_temperatur),n):
    split_list = lokal_temperatur[i:n+i]
    gjennomsnitt_t.append(gjennomsnitt(split_list))
#print(gjennomsnitt_t)

gjennomsnitt_dato =[]
gjennomsnitt_dato = lokal_tidspunkt[0::60]
plt.plot(gjennomsnitt_dato, gjennomsnitt_t)
plt.legend(['Gjennomsnitt temperatur'])
plt.savefig("figuren.pdf")
