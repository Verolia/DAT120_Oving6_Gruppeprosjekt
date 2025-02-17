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
    
    # deloppgave h: temperaturfall
    start_tidspunkt = datetime(2021, 6, 11, 17, 31, 00)
    slutt_tidspunkt = datetime(2021, 6, 12, 3, 5, 00)
    tempfall_temperatur = []
    tempfall_tidspunkt = []

    
    
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
                    lokal_trykk.append(float(absolutt_trykk)*10)
                    lokal_temperatur.append(float(temperatur))
                    bar_trykk.append(float(trykk_barometer)*10)
                    bar_dato_objekt = datetime.strptime(bar_tidspunkt,'%m.%d.%Y %H:%M')
                    bar_trykk_tidspunkt.append(bar_dato_objekt)
                except ValueError:
                    continue
                
                if start_tidspunkt == dato_tid_objekt or dato_tid_objekt == slutt_tidspunkt:
                    tempfall_tidspunkt.append(dato_tid_objekt)
                    tempfall_temperatur.append(float(temperatur))
                        
  
    return lokal_tidspunkt, lokal_trykk, lokal_temperatur, bar_trykk, bar_trykk_tidspunkt, tempfall_tidspunkt, tempfall_temperatur
        
lokal_tidspunkt, lokal_trykk, lokal_temperatur, bar_trykk, bar_trykk_tidspunkt, tempfall_tidspunkt, tempfall_temperatur = les_data("trykk_og_temperaturlogg_rune_time.csv.txt")


from fil2_funksjon import les_inn_data_2 


fil2_tidspunkt, fil2_trykk, fil2_temperatur = les_inn_data_2("temperatur_trykk_met_samme_rune_time_datasett.csv.txt")


# def gjennomsnitt(tallene):
#     return sum(tallene)/len(tallene)
n = 30

gjennomsnitt_t = []
resultat = []

for i in range(0, len(lokal_temperatur)):
    if i > n and i < len(lokal_temperatur)-n:
        gjennomsnitt = sum(lokal_temperatur[i-n:i+n+1])/(n+n+1)
        resultat.append(gjennomsnitt)
    else: 
        resultat.append(lokal_temperatur[i])
    
        
        # split_list = lokal_temperatur[i:n+i]
        # gjennomsnitt_t.append(gjennomsnitt(split_list))
#print(gjennomsnitt_t)

gjennomsnitt_dato =[]
gjennomsnitt_dato = lokal_tidspunkt[0::n]


plt.subplot(2, 1, 1)
plt.plot(lokal_tidspunkt, lokal_temperatur, color="blue", label="Temperatur ")
plt.plot(fil2_tidspunkt, fil2_temperatur, color="green", label="Temperatur MET")
plt.plot(tempfall_tidspunkt, tempfall_temperatur, color="purple", label="Temperatur maks til min")
plt.plot(lokal_tidspunkt, resultat, color="orange", label= "Gjennomsnittstemperatur")
plt.legend(fontsize="15")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(lokal_tidspunkt, lokal_trykk, color ="blue", label="Absolutt trykk")
plt.plot(bar_trykk_tidspunkt, bar_trykk, color="orange", label="Barometrisk trykk")
plt.plot(fil2_tidspunkt, fil2_trykk, color ="green", label="Absolut trykk MET")
plt.legend(fontsize="15")
plt.grid()
plt.tight_layout()
plt.show()

