# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:43:34 2021

@author: alexi
"""

import requests
import bs4
import re
import pandas as pd

url = "https://www.insee.fr/fr/statistiques/4801229"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
#print(soup)

table = soup.find_all("table", {"id": "produit-tableau-figure4_radio1"})
#print(table)

THEADtable = table[0].find_all("thead")
#print(THEADtable)

typeEmploi = []

for th in THEADtable[0].find_all("th") :
    if(th.text == ""):
        del th
    else :
        typeEmploi.append(th.text)

typeEmploi[len(typeEmploi) - 1] = typeEmploi[len(typeEmploi) - 1][:-1]
typeEmploi[len(typeEmploi) - 1] = re.sub(r'\xa0', ' ', typeEmploi[len(typeEmploi) - 1])
print(typeEmploi)
#print(typeEmploi[len(typeEmploi) - 1])


TBODYtable = table[0].find_all("tbody")
#print(TBODYtable)

TR = TBODYtable[0].find_all("tr")
#print(TR[0])


PartEmploiPourcent = []

for td in TR[0].find_all("td"):
    PartEmploiPourcent.append(float(re.sub(r'\,', '.', td.text)))

print(PartEmploiPourcent)

DureeTravailSem2019H = []

for td in TR[2].find_all("td"):
    DureeTravailSem2019H.append(float(re.sub(r'\,', '.', td.text)))

print(DureeTravailSem2019H)


DureeTravailSem2020H = []

for td in TR[3].find_all("td"):
    DureeTravailSem2020H.append(float(re.sub(r'\,', '.', td.text)))

print(DureeTravailSem2020H)


DureeTravailSemEvo19_20Pourcent = []

for td in TR[4].find_all("td"):
    DureeTravailSemEvo19_20Pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(DureeTravailSemEvo19_20Pourcent)

Teletravail19Pourcent = []

for td in TR[6].find_all("td"):
    Teletravail19Pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(Teletravail19Pourcent)

Teletravail20Pourcent = []

for td in TR[7].find_all("td"):
    Teletravail20Pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(Teletravail20Pourcent)

Teletravail19_20Points = []

for td in TR[8].find_all("td"):
    Teletravail19_20Points.append(float(re.sub(r'\,', '.', td.text)))

print(Teletravail19_20Points)

Statut20Inde = []

for td in TR[16].find_all("td"):
    Statut20Inde.append(float(re.sub(r'\,', '.', td.text)))

print(Statut20Inde)

Statut20Prive = []

for td in TR[17].find_all("td"):
    Statut20Prive.append(float(re.sub(r'\,', '.', td.text)))

print(Statut20Prive)

Statut20Etat = []

for td in TR[18].find_all("td"):
    Statut20Etat.append(float(re.sub(r'\,', '.', td.text)))

print(Statut20Etat)

Statut20Terr = []

for td in TR[19].find_all("td"):
    Statut20Terr.append(float(re.sub(r'\,', '.', td.text)))

print(Statut20Terr)

Statut20Hosp = []

for td in TR[20].find_all("td"):
    Statut20Hosp.append(float(re.sub(r'\,', '.', td.text)))

print(Statut20Hosp)


tab = pd.DataFrame()
columntypeEmploi = pd.DataFrame(typeEmploi, columns=["typeEmploi"])
columnPartEmploiPourcent = pd.DataFrame(PartEmploiPourcent, columns=["PartEmploiPourcent"])
columnDureeTravailSem2019H = pd.DataFrame(DureeTravailSem2019H, columns=["DureeTravailSem2019H"])
columnDureeTravailSem2020H= pd.DataFrame(DureeTravailSem2020H, columns=["DureeTravailSem2020H"])
columnDureeTravailSemEvo19_20Pourcent = pd.DataFrame(DureeTravailSemEvo19_20Pourcent, columns=["DureeTravailSemEvo19_20Pourcent"])
columnTeletravail19Pourcent = pd.DataFrame(Teletravail19Pourcent, columns=["Teletravail19Pourcent"])
columnTeletravail20Pourcent = pd.DataFrame(Teletravail20Pourcent, columns=["Teletravail20Pourcent"])
columnTeletravail19_20Points= pd.DataFrame(Teletravail19_20Points, columns=["Teletravail19_20Points"])
columnStatut20Inde = pd.DataFrame(Statut20Inde, columns=["Statut20Inde"])
columnStatut20Prive = pd.DataFrame(Statut20Prive, columns=["Statut20Prive"])
columnStatut20Etat = pd.DataFrame(Statut20Etat, columns=["Statut20Etat"])
columnStatut20Terr = pd.DataFrame(Statut20Terr, columns=["Statut20Terr"])
columnStatut20Hosp = pd.DataFrame(Statut20Hosp, columns=["Statut20Hosp"])
tab = pd.concat([columntypeEmploi, columnPartEmploiPourcent, columnDureeTravailSem2019H, columnDureeTravailSem2020H, columnDureeTravailSemEvo19_20Pourcent, columnTeletravail19Pourcent, columnTeletravail20Pourcent, columnTeletravail19_20Points, columnStatut20Inde, columnStatut20Prive, columnStatut20Etat, columnStatut20Terr, columnStatut20Hosp], axis=1)

tab.to_json("./insee_teletravail_1.json", orient="records")










