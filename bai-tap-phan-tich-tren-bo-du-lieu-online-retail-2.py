import pandas as pd
df = pd.read_csv('OnlineRetail.csv',encoding = 'ISO-8859-1')
print(df.info())
df.loc[ : ,'Description','Quantity'].to_csv('demo_OnlineRetail.csv')