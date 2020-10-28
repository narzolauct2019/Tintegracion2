import csv;import requests;import pandas as pd;import sys;import os;import datetime;import time as ti

#Borrado de carpeta
from os import listdir
test=os.listdir("C:/Users/icorr/Desktop/TALLER IV") #cambiar por ruta local
for item in test:
    if item.endswith(".csv"):
        os.remove(item)

#descarga csv
a = 0
dias = 0
for a in range(5):
    fecha = datetime.date.today()
    n = fecha - datetime.timedelta(days=dias)
    dias = dias + 1
    F_string = n.strftime('%y%y-%m-%d')

    Url='https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/'+F_string+'-CasosConfirmados-totalRegional.csv'
    req = requests.get(Url)
    url_content = req.content
    csv_file = open(F_string+'.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()
    a = a + 1

