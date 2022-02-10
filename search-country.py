import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cbook as cbook
from sqlalchemy import true

covidData = pd.read_csv('who-global-data.csv')

countries = covidData.loc[:, 'Country']
countries = countries.drop_duplicates()
countries = countries.reset_index(drop=true)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
	print(countries)

parse = countries.str.contains('China')
print(parse)
