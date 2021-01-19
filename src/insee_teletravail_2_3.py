# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:50:43 2021

@author: alexi
"""

import requests
import bs4
import re
import pandas as pd

url = "https://www.insee.fr/fr/statistiques/4238573?sommaire=4238635#tableau-figure3"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
#print(soup)

table = soup.find_all("table", {"id": "produit-tableau-figure3"})
#print(table)

TBODYtable = table[0].find_all("tbody")
#print(TBODYtable)

TR = TBODYtable[0].find_all("tr")
#print(TR[0])

Teletravail2017REGUL_Ensemble_pourcent = []

for td in TR[0].find_all("td"):
    Teletravail2017REGUL_Ensemble_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(Teletravail2017REGUL_Ensemble_pourcent)

Teletravail2017REGUL_Moins5km_pourcent = []

for td in TR[1].find_all("td"):
    Teletravail2017REGUL_Moins5km_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(Teletravail2017REGUL_Moins5km_pourcent)

Teletravail2017REGUL_5_10km_pourcent = []

for td in TR[2].find_all("td"):
    Teletravail2017REGUL_5_10km_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(Teletravail2017REGUL_5_10km_pourcent)

Teletravail2017REGUL_10_50km_pourcent = []

for td in TR[3].find_all("td"):
    Teletravail2017REGUL_10_50km_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(Teletravail2017REGUL_10_50km_pourcent)

Teletravail2017REGUL_50plus_pourcent = []

for td in TR[4].find_all("td"):
    Teletravail2017REGUL_50plus_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(Teletravail2017REGUL_50plus_pourcent)


tab = pd.DataFrame()
columnTeletravail2017REGUL_Ensemble_pourcent = pd.DataFrame(Teletravail2017REGUL_Ensemble_pourcent, columns=["Teletravail2017REGUL_Ensemble_pourcent"])
columnTeletravail2017REGUL_Moins5km_pourcent = pd.DataFrame(Teletravail2017REGUL_Moins5km_pourcent, columns=["Teletravail2017REGUL_Moins5km_pourcent"])
columnTeletravail2017REGUL_5_10km_pourcent = pd.DataFrame(Teletravail2017REGUL_5_10km_pourcent, columns=["Teletravail2017REGUL_5_10km_pourcent"])
columnTeletravail2017REGUL_10_50km_pourcent = pd.DataFrame(Teletravail2017REGUL_10_50km_pourcent, columns=["Teletravail2017REGUL_10_50km_pourcent"])
columnTeletravail2017REGUL_50plus_pourcent = pd.DataFrame(Teletravail2017REGUL_50plus_pourcent, columns=["Teletravail2017REGUL_50plus_pourcent"])
tab = pd.concat([columnTeletravail2017REGUL_Ensemble_pourcent, columnTeletravail2017REGUL_Moins5km_pourcent, columnTeletravail2017REGUL_5_10km_pourcent, columnTeletravail2017REGUL_10_50km_pourcent, columnTeletravail2017REGUL_50plus_pourcent], axis=1)

tab.to_json("./insee_teletravail_2_3.json", orient="records")





