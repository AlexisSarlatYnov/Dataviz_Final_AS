# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:06:49 2020

@author: alexi
"""

from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["pornhub"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='FR', gprop='')

dfPorn = pytrends.interest_over_time()

#print(dfPorn)

dfPorn2019_2020 = dfPorn.tail(104)
del dfPorn2019_2020["isPartial"]

#print(dfPorn2019_2020)



dfPorn2019_2020.index = pd.to_datetime(dfPorn2019_2020.index)

dfDate = pd.DataFrame(dfPorn2019_2020.index, index = dfPorn2019_2020.index)

#print(dfDate)

dfValues = pd.DataFrame(dfPorn2019_2020["pornhub"], index = dfPorn2019_2020.index)
dfFinal = pd.DataFrame()

dfFinal = pd.concat([dfDate, dfValues], axis=1)

#print(dfFinal)

dfFinal.to_json("./pornhub_2019_2020.json", orient="records", date_format="iso", date_unit="s")



#"Les résultats reflètent la proportion de recherches portant sur un mot clé donné dans une région et pour
# une période spécifiques, par rapport à la région où le taux d'utilisation de ce mot clé est le plus 
#élevé (valeur de 100). Ainsi, une valeur de 50 signifie que le mot clé a été utilisé moitié moins souvent 
#dans la région concernée, et une valeur de 0 signifie que les données pour ce mot clé sont insuffisantes."