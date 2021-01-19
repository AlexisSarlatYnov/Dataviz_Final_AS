# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 09:22:36 2021

@author: alexi
"""

import requests
import bs4
import re
import pandas as pd

url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid-19-pandemic-data"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
#print(soup)

table = soup.find_all("table", {"id": "thetable"})
#print(table)

TRworld = table[0].find_all("tr", {"class": "sorttop"})
#print(TRworld)

ROWworld = TRworld[0].find_all("th", {"scope": "row"})
#print(ROWworld)

NAMEworld = re.sub( r'\n|(\[.+\])?', '', ROWworld[1].text)
#print(NAMEworld)

STYLEworld = TRworld[0].find_all("th", {"style": "text-align:right; font-weight: normal; padding: 0 2px;"})
#print(STYLEworld)

CASESworld = int(re.sub( r'\n|\,', '', STYLEworld[0].text))
#print(CASESworld)

DEATHSworld = int(re.sub( r'\n|\,', '', STYLEworld[1].text))
#print(DEATHSworld)

RECOVSworld = int(re.sub( r'\n|\,', '', STYLEworld[2].text))
#print(RECOVSworld)

Location = []
Cases = []
Deaths = []
Recoveries = []

Location.append(NAMEworld)
Cases.append(CASESworld)
Deaths.append(DEATHSworld)
Recoveries.append(RECOVSworld)

TBODYorld = table[0].find_all("tbody")
#print(TBODYorld)

for tr in TBODYorld[0].find_all("tr") :
    if(re.search(r'\[.+\]|\^|UTC',tr.find_all("a")[0].text)):
        del tr
    elif (tr.find_all("a")[0].text == ""):
        print("Hungary")
        Location.append("Hungary")
        if(len(tr.find_all("td", {"data-sort-value": "-1"}))>=1):
            print("Nb Cases : " + str(re.sub( r'\,', '', tr.find_all("td")[0].text)))
            print("Nb Deaths : " + str(re.sub( r'\,', '', tr.find_all("td")[1].text)))
            print("Nb Recoveries : null")
            Cases.append(int(re.sub( r'\,', '', tr.find_all("td")[0].text)))
            Deaths.append(int(re.sub( r'\,', '', tr.find_all("td")[1].text)))
            Recoveries.append(None)
        else :
            print("Nb Cases : " + str(re.sub( r'\,', '', tr.find_all("td")[0].text)))
            print("Nb Deaths : " + str(re.sub( r'\,', '', tr.find_all("td")[1].text)))
            print("Nb Recoveries : " + str(re.sub( r'\,', '', tr.find_all("td")[2].text)))
            Cases.append(int(re.sub( r'\,', '', tr.find_all("td")[0].text)))
            Deaths.append(int(re.sub( r'\,', '', tr.find_all("td")[1].text)))
            Recoveries.append(int(re.sub( r'\,', '', tr.find_all("td")[2].text)))
    else : 
        print(tr.find_all("a")[0].text)
        Location.append(tr.find_all("a")[0].text)
        if(len(tr.find_all("td", {"data-sort-value": "-1"}))>=1):
            if(tr.find_all("a")[0].text == "Tanzania"):
                print("Nb Cases : null")
                print("Nb Deaths : null")
                print("Nb Recoveries : null")
                Cases.append(None)
                Deaths.append(None)
                Recoveries.append(None)
            else:
                print("Nb Cases : " + str(re.sub( r'\,', '', tr.find_all("td")[0].text)))
                print("Nb Deaths : " + str(re.sub( r'\,', '', tr.find_all("td")[1].text)))
                print("Nb Recoveries : null")
                Cases.append(int(re.sub( r'\,', '', tr.find_all("td")[0].text)))
                Deaths.append(int(re.sub( r'\,', '', tr.find_all("td")[1].text)))
                Recoveries.append(None)
        else :
            print("Nb Cases : " + str(re.sub( r'\,', '', tr.find_all("td")[0].text)))
            print("Nb Deaths : " + str(re.sub( r'\,', '', tr.find_all("td")[1].text)))
            print("Nb Recoveries : " + str(re.sub( r'\,', '', tr.find_all("td")[2].text)))
            Cases.append(int(re.sub( r'\,', '', tr.find_all("td")[0].text)))
            Deaths.append(int(re.sub( r'\,', '', tr.find_all("td")[1].text)))
            Recoveries.append(int(re.sub( r'\,', '', tr.find_all("td")[2].text)))


tab = pd.DataFrame()
columnLocation = pd.DataFrame(Location, columns=["Location"])
columnCases = pd.DataFrame(Cases, columns=["Cases"])
columnDeaths= pd.DataFrame(Deaths, columns=["Deaths"])
columnRecoveries = pd.DataFrame(Recoveries, columns=["Recoveries"])
tab = pd.concat([columnLocation, columnCases, columnDeaths, columnRecoveries], axis=1)

tab.to_json("./covid_data.json", orient="records")



