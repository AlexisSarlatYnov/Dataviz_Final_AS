# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:37:30 2021

@author: alexi
"""

import requests
import bs4
import re
import pandas as pd

url = "https://www.afjv.com/news/10402_octobre-2020-rapport-sur-les-ventes-de-jeux-video-aux-usa.htm"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
#print(soup)

table = soup.find_all("table", {"class": "table_news"})
#print(table)

# TBODYtable = table[0].find_all("tbody")
#print(TBODYtable)

TR = table[0].find_all("tr")
#print(TR[1])

DiffOct19_20_millionsVentesTotalJV = []

for td in TR[1].find_all("td"):
    if(re.search(r'^\$|^[0-9]', td.text)) :
        DiffOct19_20_millionsVentesTotalJV.append(float(re.sub(r'\$|%|\s', '', td.text)))
    else :
        del td

print(DiffOct19_20_millionsVentesTotalJV)

DiffOct19_20_millionsHardwareJV = []

for td in TR[2].find_all("td"):
    if(re.search(r'^\$|^[0-9]', td.text)) :
        DiffOct19_20_millionsHardwareJV.append(float(re.sub(r'\$|%|\s', '', td.text)))
    else :
        del td

print(DiffOct19_20_millionsHardwareJV)

DiffOct19_20_millionsCompleteDLCJV = []

for td in TR[3].find_all("td"):
    if(re.search(r'^\$|^[0-9]', td.text)) :
        DiffOct19_20_millionsCompleteDLCJV.append(float(re.sub(r'\$|%|\s', '', td.text)))
    else :
        del td

print(DiffOct19_20_millionsCompleteDLCJV)

DiffOct19_20_millionsAccessoiresJV = []

for td in TR[4].find_all("td"):
    if(re.search(r'^\$|^[0-9]', td.text)) :
        DiffOct19_20_millionsAccessoiresJV.append(float(re.sub(r'\$|%|\s', '', td.text)))
    else :
        del td

print(DiffOct19_20_millionsAccessoiresJV)

DiffYEAR19_20_millionVentesTotalJV = []

for td in TR[6].find_all("td"):
    if(re.search(r'^\$|^[0-9]', td.text)) :
        DiffYEAR19_20_millionVentesTotalJV.append(float(re.sub(r'\$|%|\s', '', td.text)))
    else :
        del td

print(DiffYEAR19_20_millionVentesTotalJV)

DiffYEAR19_20_millionHardwareJV = []

for td in TR[7].find_all("td"):
    if(re.search(r'^\$|^[0-9]', td.text)) :
        DiffYEAR19_20_millionHardwareJV.append(float(re.sub(r'\$|%|\s', '', td.text)))
    else :
        del td

print(DiffYEAR19_20_millionHardwareJV)

DiffYEAR19_20_millionCompleteDLCJV = []

for td in TR[8].find_all("td"):
    if(re.search(r'^\$|^[0-9]', td.text)) :
        DiffYEAR19_20_millionCompleteDLCJV.append(float(re.sub(r'\$|%|\s', '', td.text)))
    else :
        del td

print(DiffYEAR19_20_millionCompleteDLCJV)

DiffYEAR19_20_millionAccessoiresJV = []

for td in TR[9].find_all("td"):
    if(re.search(r'^\$|^[0-9]', td.text)) :
        DiffYEAR19_20_millionAccessoiresJV.append(float(re.sub(r'\$|%|\s', '', td.text)))
    else :
        del td

print(DiffYEAR19_20_millionAccessoiresJV)


tab = pd.DataFrame()
columnDiffOct19_20_millionsVentesTotalJV = pd.DataFrame(DiffOct19_20_millionsVentesTotalJV, columns=["DiffOct19_20_millionsVentesTotalJV"])
columnDiffOct19_20_millionsHardwareJV = pd.DataFrame(DiffOct19_20_millionsHardwareJV, columns=["DiffOct19_20_millionsHardwareJV"])
columnDiffOct19_20_millionsCompleteDLCJV = pd.DataFrame(DiffOct19_20_millionsCompleteDLCJV, columns=["DiffOct19_20_millionsCompleteDLCJV"])
columnDiffOct19_20_millionsAccessoiresJV = pd.DataFrame(DiffOct19_20_millionsAccessoiresJV, columns=["DiffOct19_20_millionsAccessoiresJV"])
columnDiffYEAR19_20_millionVentesTotalJV = pd.DataFrame(DiffYEAR19_20_millionVentesTotalJV, columns=["DiffYEAR19_20_millionVentesTotalJV"])
columnDiffYEAR19_20_millionHardwareJV = pd.DataFrame(DiffYEAR19_20_millionHardwareJV, columns=["DiffYEAR19_20_millionHardwareJV"])
columnDiffYEAR19_20_millionCompleteDLCJV = pd.DataFrame(DiffYEAR19_20_millionCompleteDLCJV, columns=["DiffYEAR19_20_millionCompleteDLCJV"])
columnDiffYEAR19_20_millionAccessoiresJV = pd.DataFrame(DiffYEAR19_20_millionAccessoiresJV, columns=["DiffYEAR19_20_millionAccessoiresJV"])
tab = pd.concat([columnDiffOct19_20_millionsVentesTotalJV, columnDiffOct19_20_millionsHardwareJV, columnDiffOct19_20_millionsCompleteDLCJV, columnDiffOct19_20_millionsAccessoiresJV, columnDiffYEAR19_20_millionVentesTotalJV, columnDiffYEAR19_20_millionHardwareJV, columnDiffYEAR19_20_millionCompleteDLCJV, columnDiffYEAR19_20_millionAccessoiresJV], axis=1)

tab.to_json("./JV_USA_19_20.json", orient="records")



