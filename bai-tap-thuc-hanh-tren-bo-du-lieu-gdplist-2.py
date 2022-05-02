import pandas as pd
data=pd.read_csv('GDPlist.csv', encoding = "ISO-8859-1")
print(data.head())
print(data.info())
