import numpy as np
import pandas as pd

df_countries = pd.read_csv('../input/countries.csv')
df_countries['Region'] = df_countries['Region'].replace('ASIA', 'Asia')
df_countries['Region'] = df_countries['Region'].replace('AFRICA', 'Africa')
df_countries['Region'] = df_countries['Region'].replace('EUROPE', 'Europe')
df_countries['Region'] = df_countries['Region'].replace('LATIN', 'Latin')
df_countries['Region'] = df_countries['Region'].replace('NEAR_EAST', 'Near_East')
df_countries['Region'] = df_countries['Region'].replace('NORTHERN_AMERICA', 'Northern_America')
df_countries['Region'] = df_countries['Region'].replace('OCEANIA', 'Oceania')
df_table = pd.read_csv('../input/covid_19_clean_complete.csv', parse_dates=['Date'])
df_table['Active'] = df_table['Confirmed']-df_table['Deaths']-df_table['Recovered']
df_table['Country/Region'] = df_table['Country/Region'].replace('Mainland China', 'China')
df_table['Country/Region'] = df_table['Country/Region'].replace('US', 'United States')
df_table['Country/Region'] = df_table['Country/Region'].replace('UK', 'United Kingdom')
df_table['Country/Region'] = df_table['Country/Region'].replace('North Macedonia', 'Macedonia')
df_table['Country/Region'] = df_table['Country/Region'].replace('Bosnia and Herzegovina', 'Bosnia & Herzegovina')
df_table['Country/Region'] = df_table['Country/Region'].replace('South Africa', 'SouthAfrica')
df_table['Country/Region'] = df_table['Country/Region'].replace('Others', 'Ship')
df_table['Country/Region'] = df_table['Country/Region'].replace('Cruise Ship', 'Ship')
df_table['Country/Region'] = df_table['Country/Region'].replace('Iran (Islamic Republic of)', 'Iran')
df_table['Country/Region'] = df_table['Country/Region'].replace('Republic of Korea', 'South Korea')
df_table['Country/Region'] = df_table['Country/Region'].replace('Korea, South', 'South Korea')
df_table['Country/Region'] = df_table['Country/Region'].replace('Hong Kong SAR', 'Hong Kong')
df_table['Country/Region'] = df_table['Country/Region'].replace('Viet Nam', 'Vietnam')
df_table['Country/Region'] = df_table['Country/Region'].replace('Macao SAR', 'Macau')
df_table['Country/Region'] = df_table['Country/Region'].replace('Russian Federation', 'Russia')
df_table['Country/Region'] = df_table['Country/Region'].replace('Republic of Moldova', 'Moldova')
df_table['Country/Region'] = df_table['Country/Region'].replace('Saint Martin', 'St. Martin')
df_table['Country/Region'] = df_table['Country/Region'].replace('Taipei and environs', 'Taiwan')
df_table['Country/Region'] = df_table['Country/Region'].replace('Taiwan*', 'Taiwan')
df_table['Country/Region'] = df_table['Country/Region'].replace('Congo (Kinshasa)', 'Congo')
df_table['Country/Region'] = df_table['Country/Region'].replace('occupied Palestinian territory', 'Palestine')
df_table['Country/Region'] = df_table['Country/Region'].replace('Holy See', 'Vatican City')
df_table['Country/Region'] = df_table['Country/Region'].replace('Czechia', 'Czech Republic')
df_table['Province/State'] = df_table['Province/State'].fillna('NA')

continent_dict = {}
for c in np.unique(df_countries['Country']):
  continent_dict[c] = df_countries[df_countries['Country']==c]['Region'].values[0]
continent_dict['Ship'] = 'None'
continent_dict['Saint Barthelemy'] = 'Latin'
continent_dict['St. Martin'] = 'Latin'
continent_dict['Palestine'] = 'Near_East'
continent_dict['Vatican City'] = 'Europe'
continent_dict['Channel Islands'] = 'North_America'
continent_dict["Cote d'Ivoire"] = 'Africac'
df_table['Continent'] = df_table['Country/Region'].apply(lambda x: continent_dict[x])

