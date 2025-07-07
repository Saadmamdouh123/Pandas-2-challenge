import pandas as pd
import numpy as np
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

# df['Salary'] = df['Salary'].fillna(df.groupby('Department')['Salary'].transform('mean'))
# print(df)

# df['Remote'].replace({'Yes':'Oui','No' :'Non'},inplace=True)
# # print(df)

# df['Ancienneté_Catégorie'] = df['Years_Experience'].apply(
#     lambda x: 'junior' if x < 3 else ('intermédiaire' if x < 6 else ('senior' if x < 15 else 'expert')))
# print(df)

############################################
#3

# salaire_moyen_global = df['Salary'].mean()
# print(salaire_moyen_global)

# idx_salaire_max = df['Salary'].idxmax()
# employe_salaire_max = df.loc[idx_salaire_max]
# print(employe_salaire_max)

# idp = df['Salary'].mean()
# print(idp)

# cc = df.groupby('Department')['Salary'].median()
# print(cc)

# moyenne =df.groupby('Ancienneté_Catégorie')['Salary'].mean()
# print(moyenne)
# mediane=df.groupby('Ancienneté_Catégorie')['Salary'].median()
# print(df)
# m = df[df['Remote'] == 'Yes'].groupby('Department').size()
# print(m)

#4
# table1=pd.pivot_table(df, 
#                values='Salary', 
#                index='Department', 
#                columns='Remote', 
#                aggfunc='mean')
# print(table1)

# table2=pd.pivot_table(df, 
#                values='Years_Experience', 
#                index='Department', 
#                columns='Age', 
#                aggfunc='mean')
# print(table2)


# #partie 5

# df['Performance'] = np.where(
#     df['Salary'] < 60000, 'Bon',
#     np.where(df['Salary'] < 80000, 'Moyen', 'Haut')
# )
# print(df)



# Conditions
# conditions = [
#     (df['Age'] < 40) & (df['Years_Experience'] < 10),   
#     (df['Age'] < 40) & (df['Years_Experience'] >= 10),  
#     (df['Age'] >= 40) & (df['Years_Experience'] < 10),  
#     (df['Age'] >= 40) & (df['Years_Experience'] >= 10) 
# ]

# Les valeurs correspondantes
# choices = [
#     'Jeune & Nouveau',
#     'Jeune & Expérimenté',
#     'Senior & Nouveau',
#     'Senior & Expérimenté'
# ]

# Créer la nouvelle colonne
# df['Profil'] = np.select(conditions, choices, default='Inconnu')
# print(df)

moyenne_salaire_dept = df.groupby('Department')['Salary'].transform('mean')

df['Diff_Salaire_Moyenne'] = df['Salary'] - moyenne_salaire_dept

print(df)

