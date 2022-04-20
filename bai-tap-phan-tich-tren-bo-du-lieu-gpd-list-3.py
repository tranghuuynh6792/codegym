import pandas as pd
df=pd.read_csv('GDPlist.csv',encoding = "ISO-8859-1")
df.info()
print(df)
print("Số dòng dữ liệu: ",df.shape[0])
print("Số cột dữ liệu: ",df.shape[1])
print(df.columns)
print(df.dtypes)
df_GDP = df.loc[:,'GDP_(millions_of_US$)']
print("Gia tri nho nhat cua GDP",df_GDP.min())
print("Gia tri lon nhat cua GDP",df_GDP.max())
print(df.describe())
df_Country = df.loc[:,'Country']

print(df_Country,df_Country.count())
