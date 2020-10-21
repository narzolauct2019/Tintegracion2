import csv;import requests;import pandas as pd;import sys;import os;import datetime;import time as ti;


#Borrado de carpeta
from os import listdir
test=os.listdir("C:/Users/icorr/Downloads/TALLER_IV/TALLER IV") #cambiar por ruta local
for item in test:
    if item.endswith(".csv"):
        os.remove(item)

#descarga csv
Url='https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/2020-10-19-CasosConfirmados-totalRegional.csv'

req = requests.get(Url)

url_content = req.content
csv_file = open('downloaded.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

