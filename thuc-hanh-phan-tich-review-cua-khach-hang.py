import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
df = pd.read_csv("Credit_Scoring.csv")
print(df.head())
df.info()
print(df.describe())
df.isna()
df1 = df.dropna()
100 * df1.shape[0]/df.shape[0]
sns.kdeplot(data=df1["MonthlyIncome"])
plt.show()
df2 = df.interpolate(axis=1)
df2.isna()
df2.boxplot()
plt.show()
sns.boxplot(df2["MonthlyIncome"])
plt.show()
Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)
IQR = Q3-Q1
df3 = df2[~((df2 < (Q1 - 1.5 * IQR)) | (df2 > (Q3 + 1.5 * IQR))).any(axis=1)]
df3.boxplot()
plt.show()
print(df3.describe())
sns.kdeplot(data = df3['MonthlyIncome'])
plt.show()
scaler = MinMaxScaler()
mms = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
sns.kdeplot(data = mms)
plt.show()
scaler = RobustScaler()
rbs = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
sns.kdeplot(data = rbs)
plt.show()
scaler = StandardScaler()
sc = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
sns.kdeplot(data = sc)
plt.show()