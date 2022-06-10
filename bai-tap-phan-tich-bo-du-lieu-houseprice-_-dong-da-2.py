import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
df = pd.read_excel("house_price_dống-da.xlsx")
print(df.info())
print(df.describe())
testisna = df.isna()
print(testisna.info())
df1 = df.dropna(subset = ['price'])
print(df1)
df1 = df1.fillna(value = {"land_certificate":"land_certificate","house_direction":(df1["house_direction"].mode()),"balcony_direction":(df1["balcony_direction"].mode()),"toilet":(df1["toilet"].mode()),"bedroom":(df1["bedroom"].mode()),"floor":(df1["floor"].mode())})
print(df1)
df1["giá/m2"] = df1["price"]/df1["area"]
print(df1)
Q1 = df1["giá/m2"].quantile(0.25)
Q3 = df1["giá/m2"].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
print((df1["giá/m2"] < (Q1 - 1.5 * IQR)) | (df1["giá/m2"] > (Q3 + 1.5 * IQR)))
df2 = df1[~((df1["giá/m2"] < (Q1 - 1.5 * IQR)) | (df1["giá/m2"] > (Q3 + 1.5 * IQR)))]
print(df2)
scaler = MinMaxScaler()
df3 = scaler.fit_transform(df2["giá/m2"])
col_names = list(df2["giá/m2"])
df3 = pd.DataFrame(df3, columns=col_names)
print(df3.head())
sns.kdeplot(data=df3)
plt.show()