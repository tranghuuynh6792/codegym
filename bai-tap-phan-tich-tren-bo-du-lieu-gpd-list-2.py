import pandas as pd
df = pd.read_csv('GDPlist.csv',encoding = 'ISO-8859-1')
print(df.info())
df.rename(columns={'Country':'Nuoc','Continent':'Chau_Luc','GDP_(millions_of_US$)':'GDP_trieu'},inplace=True)
df['Thanh_pho'] = df.loc[:,'Nuoc']
df.replace(df.loc[df.Thanh_pho == 'Vietnam'].index,'HaNoi',inplace = True)
print(df)
df.drop(df.loc[df.Chau_Luc == 'Asia'].index, inplace=True)
print(df)
df.drop(df.loc[df.GDP_trieu < 3000000].index, inplace=True)
print(df)
