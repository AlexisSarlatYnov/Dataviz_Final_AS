# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:31:18 2021

@author: alexi
"""

import requests
import bs4
import re
import pandas as pd

url = "https://www.insee.fr/fr/statistiques/4238573?sommaire=4238635#consulter"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
#print(soup)

table = soup.find_all("table", {"id": "produit-tableau-figure1"})
print(table)

THEADtable = table[0].find_all("thead")
#print(THEADtable)

typeEmploi = []

for th in THEADtable[0].find_all("th") :
    if(th.text == ""):
        del th
    else :
        typeEmploi.append(th.text)

print(typeEmploi)

TBODYtable = table[0].find_all("tbody")
#print(TBODYtable)

TR = TBODYtable[0].find_all("tr")
#print(TR[0])

JourParSem1en2017pourcent = []

for td in TR[1].find_all("td"):
    JourParSem1en2017pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017pourcent)

JourParSem2en2017pourcent = []

for td in TR[2].find_all("td"):
    JourParSem2en2017pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem2en2017pourcent)

JourParSem3etplusen2017pourcent = []

for td in TR[3].find_all("td"):
    JourParSem3etplusen2017pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem3etplusen2017pourcent)

Ensembleen2017pourcent = []

for td in TR[4].find_all("td"):
    Ensembleen2017pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(Ensembleen2017pourcent)

tab = pd.DataFrame()
columntypeEmploi = pd.DataFrame(typeEmploi, columns=["typeEmploi"])
columnJourParSem1en2017pourcent = pd.DataFrame(JourParSem1en2017pourcent, columns=["JourParSem1en2017pourcent"])
columnJourParSem2en2017pourcent= pd.DataFrame(JourParSem2en2017pourcent, columns=["JourParSem2en2017pourcent"])
columnJourParSem3etplusen2017pourcent = pd.DataFrame(JourParSem3etplusen2017pourcent, columns=["JourParSem3etplusen2017pourcent"])
columnEnsembleen2017pourcent = pd.DataFrame(Ensembleen2017pourcent, columns=["Ensembleen2017pourcent"])
tab = pd.concat([columntypeEmploi, columnJourParSem1en2017pourcent, columnJourParSem2en2017pourcent, columnJourParSem3etplusen2017pourcent, columnEnsembleen2017pourcent], axis=1)

tab.to_json("./insee_teletravail_2.json", orient="records")







