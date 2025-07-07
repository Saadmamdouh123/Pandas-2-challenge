import pandas as pd
import numpy as np
data = {
    'Name' : ['Saad' , 'abdo' , 'omar'],
    'Age' : [24 , 34 , 20],
    'Ville': ['casablanca' , 'kkkkkkk' , np.nan]
}

df = pd.DataFrame(data)
# print(df.head())
# print(df.tail(2))
# print(df.info())
# print (df.describe(include='all'))
# print(df['Ville'])
# print(df[df['Age'] > 10])
print(df.loc[df['Ville'] == 'casablanca'])

