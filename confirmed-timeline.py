import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cbook as cbook
from sqlalchemy import true

#pd.plotting.register_matplotlib_converters()

#covidData = pd.read_csv('who-global-data.csv', parse_dates=['Date_reported'])

covidData = pd.read_csv('who-global-data.csv')

#covidData.plot('Date_reported', 'Cumulative_cases')
#sns.lineplot(x='Date_reported', y='Cumulative_cases', data=covidData)

countries = covidData.loc[:, 'Country']
countries = countries.drop_duplicates()
countries = countries.reset_index(drop=true)
print(countries)

def countryData(country):
    parse = covidData[covidData['Country'].str.match(country)]
    return parse

#print(countryData(countries[0]))

i = 0
ax = countryData(countries[i]).plot('Date_reported', 'New_cases', label = countries[i])

while i != 7:
    countryData(countries[i+1]).plot('Date_reported', 'New_cases', ax = ax, label = countries[i+1])
    i += 1

'''
ax = countryData(countries[1]).plot('Date_reported', 'Cumulative_cases')
countryData(countries[2]).plot('Date_reported', 'Cumulative_cases', ax=ax)
'''

plt.show()
