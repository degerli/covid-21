import numpy as np
import pandas as pd
import urllib.request
from datetime import date, timedelta
import glob

# download all jhu data
sdate = date(2020, 1, 22)   # start date
edate = date.today()   # end date
delta = edate - sdate
df_arr = []
for i in range(delta.days + 1):
  day = sdate + timedelta(days=i)
  day = day.strftime('%m-%d-%Y')
  url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/' + \
      'csse_covid_19_daily_reports/{:s}.csv'.format(day)
  fname = '../input/jhu/covid-19_daily_{:s}.csv'.format(day)
  try:
    urllib.request.urlretrieve(url, fname)
    df = pd.read_csv(fname, index_col=None, parse_dates=['Last Update'])
    df['Date'] = day
    df_arr.append(df)
    #print(day)
  except:
    continue;
df_table = pd.concat(df_arr, axis=0, ignore_index=True)
#df_table['Date'] = pd.DatetimeIndex(df_table['Date']).normalize()

df_table['Active'] = df_table['Confirmed']-df_table['Deaths']-df_table['Recovered']
df_table['Closed'] = df_table['Confirmed']-df_table['Active']
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

df_table.to_csv('../input/covid_19_master.csv')
