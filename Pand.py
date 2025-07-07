import pandas as pd

data = {
    'Name' : ['Saad' , 'abdo' , 'omar'],
    'Age' : [24 , 34 , 20],
    'Ville': ['Casablanca' , 'Casablanca' , 'Casablanca'],
}

df = pd.DataFrame(data)
ll = df.head(1)
ll2 = df.tail(1)
pp = df.info()
# print(df)
# print(ll)
# print(ll2)
print(pp)

