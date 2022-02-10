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

country = "China"

plot1 = "Cumulative_cases"
plot2 = "New_cases"

ax = countryData(country).plot('Date_reported', 'Cumulative_cases', label = plot1)
countryData(country).plot('Date_reported', 'New_cases', ax = ax, label = plot2)

plt.show()
