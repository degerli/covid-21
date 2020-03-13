import numpy as np
import pandas as pd

class load_data:
  def __init__(self, fname):
    # read continent and population info
    self.df_countries = pd.read_csv('../input/countries.csv')
    self.df_countries['Region'] = self.df_countries['Region'].replace('ASIA', 'Asia')
    self.df_countries['Region'] = self.df_countries['Region'].replace('AFRICA', 'Africa')
    self.df_countries['Region'] = self.df_countries['Region'].replace('EUROPE', 'Europe')
    self.df_countries['Region'] = self.df_countries['Region'].replace('LATIN', 'Latin')
    self.df_countries['Region'] = self.df_countries['Region'].replace('NEAR_EAST', 'Near_East')
    self.df_countries['Region'] = self.df_countries['Region'].replace('NORTHERN_AMERICA', 'Northern_America')
    self.df_countries['Region'] = self.df_countries['Region'].replace('OCEANIA', 'Oceania')

    # read covid-19 data, and clean up country names
    self.df_table = pd.read_csv('../input/covid_19_clean_complete.csv', parse_dates=['Date'])
    self.df_table.drop(self.df_table[((self.df_table['Date'].dt.month == 3)&(self.df_table['Date'].dt.day > 11))].index, inplace=True)
    self.df_table['Active'] = self.df_table['Confirmed']-self.df_table['Deaths']-self.df_table['Recovered']
    self.df_table['Closed'] = self.df_table['Confirmed']-self.df_table['Active']
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Mainland China', 'China')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('US', 'United States')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('UK', 'United Kingdom')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('North Macedonia', 'Macedonia')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Bosnia and Herzegovina', 'Bosnia & Herzegovina')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('South Africa', 'SouthAfrica')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Others', 'Ship')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Cruise Ship', 'Ship')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Iran (Islamic Republic of)', 'Iran')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Republic of Korea', 'South Korea')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Korea, South', 'South Korea')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Hong Kong SAR', 'Hong Kong')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Viet Nam', 'Vietnam')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Macao SAR', 'Macau')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Russian Federation', 'Russia')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Republic of Moldova', 'Moldova')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Saint Martin', 'St. Martin')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Taipei and environs', 'Taiwan')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Taiwan*', 'Taiwan')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Congo (Kinshasa)', 'Congo')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('occupied Palestinian territory', 'Palestine')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Holy See', 'Vatican City')
    self.df_table['Country/Region'] = self.df_table['Country/Region'].replace('Czechia', 'Czech Republic')
    self.df_table['Province/State'] = self.df_table['Province/State'].fillna('NA')

    # US States counted twice

    self.df_table.drop(self.df_table[(self.df_table['Province/State'].str.contains(','))& 
                          ((self.df_table['Date'].dt.month == 3)&(self.df_table['Date'].dt.day > 9))].index, inplace=True)

    # create dictionary of continent names
    self.continent_dict = {}
    for c in np.unique(self.df_countries['Country']):
      self.continent_dict[c] = self.df_countries[self.df_countries['Country']==c]['Region'].values[0]
    self.continent_dict['Ship'] = 'None'
    self.continent_dict['Saint Barthelemy'] = 'Latin'
    self.continent_dict['St. Martin'] = 'Latin'
    self.continent_dict['Palestine'] = 'Near_East'
    self.continent_dict['Vatican City'] = 'Europe'
    self.continent_dict['Channel Islands'] = 'North_America'
    self.continent_dict["Cote d'Ivoire"] = 'Africac'
    self.df_table['Continent'] = self.df_table['Country/Region'].apply(lambda x: self.continent_dict[x])

