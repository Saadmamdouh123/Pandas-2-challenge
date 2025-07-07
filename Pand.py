import pandas as pd
import numpy as np
data = {
    'Name' : ['Saad' , 'abdo' , 'omar'],
    'Age' : [24 , 34  , None],
    'Ville': ['casablanca' , 'kkkkkkk' , np.nan]
}

df = pd.DataFrame(data)
# print(df.head())
# print(df.tail(2))
# print(df.info())
# print (df.describe(include='all'))
# print(df['Ville'])
# print(df[df['Age'] > 10])
# print(df.loc[df['Ville'] == 'casablanca'])
# data = ['jjjj', 'llll', 'oooo']
# df['State'] = data
# kk = df['Name'] = df['Name'].str.upper()
# print(kk)
# df.rename(columns={'Name': 'Full_Name', 'Ville': 'Location'}, inplace=True)# print(df)
# print(df.isnull())
# print(df.fillna())
# #print(df.isnull())
# replace = df.fillna(df["Age"].mean())
# print(replace)

