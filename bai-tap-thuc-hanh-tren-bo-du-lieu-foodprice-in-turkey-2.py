import pandas as pd
data = pd.read_csv('FoodPrice_in_Turkey.csv',encoding= 'ISO-8859-1')
print(data.info())
print(data.groupby('ProductName')['Price'].mean())