# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:35:46 2024

@author: henga
"""
from datetime import datetime

def omgjoring_av_dato_format():
    
    with open ("temperatur_trykk_met_samme_rune_time_datasett.csv.txt" , "r") as fila:
        fila.readline()
        for linje in fila:
            item = linje.strip().split(";")
            datoer = item[2]
            dato = datetime.strptime(datoer, '%d.%m.%Y %H:%M').strftime('%m.%d.%y %H:%M')
    return dato


