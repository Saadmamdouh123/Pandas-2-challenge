import pandas as pd
# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('C:/Users/Saad/Desktop/Pandas 1/employees2 (1).csv')

# Afficher les premières lignes pour vérifier le contenu
# print(df.head())
ll = df.iloc[0]
# print(ll)  
# pp = df.dtypes
# print(pp)
# oo = df.isna()
# print(oo)
print("####################################")
# replace = df.fillna(df["Age"].mean())
# print(replace)

df['Salary'] = df['Salary'].fillna(df.groupby('Department')['Salary'].transform('mean'))
print(df)

