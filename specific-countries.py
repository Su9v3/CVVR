import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cbook as cbook
from sqlalchemy import true

covidData = pd.read_csv('who-global-data.csv')

#covidData.plot('Date_reported', 'Cumulative_cases')
countries = covidData.loc[:, 'Country']
countries = countries.drop_duplicates()
countries = countries.reset_index(drop=true)
print(countries)

def countryData(country):
    parse = covidData[covidData['Country'].str.match(country)]
    return parse

country1 = "China"
country2 = "United States of America"

ax = countryData(country1).plot('Date_reported', 'New_cases', label = country1)
countryData(country2).plot('Date_reported', 'New_cases', ax = ax, label = country2)

plt.show()
