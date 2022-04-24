import pandas as pd
import numpy as np
df=pd.read_csv('OnlineRetail.csv', encoding = "ISO-8859-1")
# hiển thị 5 dòng dữ liệu đầu tiên
df.head()
print (df.info())
df['InvoiceDate1']=df['InvoiceDate'].str.split(' ').str[0]
df['Month']=pd.to_datetime(df['InvoiceDate1'],format='%m/%d/%Y').dt.month
conditions = [(df['Month'] <= 3),
 (df['Month'] > 3) & (df['Month'] <= 6),(df['Month'] > 6) & (df['Month'] <= 9),(df['Month'] <= 12)]
choices = [1,2,3,4]
df['PreviousQuater'] = np.select(conditions, choices)
df['Amount'] = df['Quantity'] * df['UnitPrice']
conditions = [(df['PreviousQuater'] == 4) & (df['Country'] == 'United Kingdom'),(df['Country'] == 'France')]
choices = [0.1*df['Amount'],0.05*df['Amount']]
df['Discount'] = np.select(conditions, choices,default = 0)
df['Total'] = df['Amount'] - df['Discount']
print(df)