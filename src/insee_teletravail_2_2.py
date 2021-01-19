# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:44:11 2021

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

table = soup.find_all("table", {"id": "produit-tableau-figure2"})
#print(table)

THEADtable = table[0].find_all("thead")
#print(THEADtable)

THEADtable2 = THEADtable[0].find_all("tr")

typeEmploi = []

for th in THEADtable2[0].find_all("th") :
    if(th.text == ""):
        del th
    else :
        if(th.text == "Cadres ") :
            cadres = th.text
        else :
            typeEmploi.append(th.text)

for th in THEADtable2[1].find_all("th") :
    if(th.text == ""):
        del th
    else :
        typeEmploi.append(cadres + th.text)

print(typeEmploi)


TBODYtable = table[0].find_all("tbody")
#print(TBODYtable)

TR = TBODYtable[0].find_all("tr")
#print(TR[0])

JourParSem1en2017_FEMMES_pourcent = []

for td in TR[1].find_all("td"):
    JourParSem1en2017_FEMMES_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_FEMMES_pourcent)

JourParSem1en2017_HOMMES_pourcent = []

for td in TR[2].find_all("td"):
    JourParSem1en2017_HOMMES_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_HOMMES_pourcent)

JourParSem1en2017_A15_29_pourcent = []

for td in TR[4].find_all("td"):
    JourParSem1en2017_A15_29_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_A15_29_pourcent)

JourParSem1en2017_A29_39_pourcent = []

for td in TR[5].find_all("td"):
    JourParSem1en2017_A29_39_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_A29_39_pourcent)

JourParSem1en2017_A39_49_pourcent = []

for td in TR[6].find_all("td"):
    JourParSem1en2017_A39_49_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_A39_49_pourcent)

JourParSem1en2017_A49_59_pourcent = []

for td in TR[7].find_all("td"):
    JourParSem1en2017_A49_59_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_A49_59_pourcent)

JourParSem1en2017_A60plus_pourcent = []

for td in TR[8].find_all("td"):
    JourParSem1en2017_A60plus_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_A60plus_pourcent)

JourParSem1en2017_SectPRIVE_pourcent = []

for td in TR[18].find_all("td"):
    JourParSem1en2017_SectPRIVE_pourcent.append(float(re.sub(r'\,', '.', td.text)))
    
for td in TR[18].find_all("td", {"colspan": "2"}):
    JourParSem1en2017_SectPRIVE_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_SectPRIVE_pourcent)

JourParSem1en2017_SectPUBLETAT_pourcent = []

for td in TR[20].find_all("td"):
    if(td.text == "///"):
        JourParSem1en2017_SectPUBLETAT_pourcent.append(None)
    else :
        JourParSem1en2017_SectPUBLETAT_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_SectPUBLETAT_pourcent)

JourParSem1en2017_SectPUBLTERR_pourcent = []

for td in TR[21].find_all("td"):
    if(td.text == "///"):
        JourParSem1en2017_SectPUBLTERR_pourcent.append(None)
    else :
        JourParSem1en2017_SectPUBLTERR_pourcent.append(float(re.sub(r'\,', '.', td.text)))
print(JourParSem1en2017_SectPUBLTERR_pourcent)

JourParSem1en2017_SectPUBLHOSP_pourcent = []

for td in TR[22].find_all("td"):
    if(td.text == "///"):
        JourParSem1en2017_SectPUBLHOSP_pourcent.append(None)
    else :
        JourParSem1en2017_SectPUBLHOSP_pourcent.append(float(re.sub(r'\,', '.', td.text)))

print(JourParSem1en2017_SectPUBLHOSP_pourcent)


tab = pd.DataFrame()
columntypeEmploi = pd.DataFrame(typeEmploi, columns=["typeEmploi"])
columnJourParSem1en2017_FEMMES_pourcent = pd.DataFrame(JourParSem1en2017_FEMMES_pourcent, columns=["JourParSem1en2017_FEMMES_pourcent"])
columnJourParSem1en2017_HOMMES_pourcent = pd.DataFrame(JourParSem1en2017_HOMMES_pourcent, columns=["JourParSem1en2017_HOMMES_pourcent"])
columnJourParSem1en2017_A15_29_pourcent = pd.DataFrame(JourParSem1en2017_A15_29_pourcent, columns=["JourParSem1en2017_A15_29_pourcent"])
columnJourParSem1en2017_A29_39_pourcent = pd.DataFrame(JourParSem1en2017_A29_39_pourcent, columns=["JourParSem1en2017_A29_39_pourcent"])
columnJourParSem1en2017_A39_49_pourcent = pd.DataFrame(JourParSem1en2017_A39_49_pourcent, columns=["JourParSem1en2017_A39_49_pourcent"])
columnJourParSem1en2017_A49_59_pourcent = pd.DataFrame(JourParSem1en2017_A49_59_pourcent, columns=["JourParSem1en2017_A49_59_pourcent"])
columnJourParSem1en2017_A60plus_pourcent = pd.DataFrame(JourParSem1en2017_A60plus_pourcent, columns=["JourParSem1en2017_A60plus_pourcent"])
columnJourParSem1en2017_SectPRIVE_pourcent = pd.DataFrame(JourParSem1en2017_SectPRIVE_pourcent, columns=["Ensembleen2017pourcent"])
columnJourParSem1en2017_SectPUBLETAT_pourcent = pd.DataFrame(JourParSem1en2017_SectPUBLETAT_pourcent, columns=["JourParSem1en2017_SectPUBLETAT_pourcent"])
columnJourParSem1en2017_SectPUBLTERR_pourcent = pd.DataFrame(JourParSem1en2017_SectPUBLTERR_pourcent, columns=["JourParSem1en2017_SectPUBLTERR_pourcent"])
columnJourParSem1en2017_SectPUBLHOSP_pourcent = pd.DataFrame(JourParSem1en2017_SectPUBLHOSP_pourcent, columns=["JourParSem1en2017_SectPUBLHOSP_pourcent"])
tab = pd.concat([columntypeEmploi, columnJourParSem1en2017_FEMMES_pourcent, columnJourParSem1en2017_HOMMES_pourcent, columnJourParSem1en2017_A15_29_pourcent, columnJourParSem1en2017_A29_39_pourcent, columnJourParSem1en2017_A39_49_pourcent, columnJourParSem1en2017_A49_59_pourcent, columnJourParSem1en2017_A60plus_pourcent, columnJourParSem1en2017_SectPRIVE_pourcent, columnJourParSem1en2017_SectPUBLETAT_pourcent, columnJourParSem1en2017_SectPUBLTERR_pourcent, columnJourParSem1en2017_SectPUBLHOSP_pourcent], axis=1)

tab.to_json("./insee_teletravail_2_2.json", orient="records")








