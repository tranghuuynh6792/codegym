import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.preprocessing import MinMaxScaler

# tạo các cột theo các phần phối khác nhau

df = pd.DataFrame({ 

    'beta': np.random.beta(5, 1, 1000) * 60,        # beta

    'exponential': np.random.exponential(10, 1000), # exponential

    'normal_p': np.random.normal(10, 2, 1000),      # normal platykurtic

    'normal_l': np.random.normal(10, 10, 1000),     # normal leptokurtic

})

# thêm dữ liệu được tạo theo phân phối nhị thức

first_half = np.random.normal(20, 3, 500) 

second_half = np.random.normal(-20, 3, 500) 

bimodal = np.concatenate([first_half, second_half])


df['bimodal'] = bimodal
print(df.head())
sns.kdeplot(data=df)
plt.show()
df.describe()
normal_big = np.random.normal(1000000, 10000, (1000,1))  # normal distribution of large values
df['normal_big'] = normal_big
sns.kdeplot(data=df)
plt.show()
print(df.describe())
normal_big = np.random.normal(1000000, 10000, (1000,1))  # normal distribution of large values
df['normal_big'] = normal_big
sns.kdeplot(data=df)
plt.show()
df.boxplot()
plt.show()
scaler = MinMaxScaler()
df_s = scaler.fit_transform(df)
col_names = list(df.columns)
df_s = pd.DataFrame(df_s, columns=col_names)
df_s.head()
sns.kdeplot(data=df_s)
plt.show()
df_s.boxplot()
plt.show()
print(df_s.describe())
df_s['beta'].min()
df_s['beta'].max()
mins = [df[col].min() for col in df.columns]
print(mins)
mins = [df_s[col].min() for col in df_s.columns]
print(mins)
maxs = [df[col].max() for col in df.columns]
print(maxs)
maxs = [df_s[col].max() for col in df_s.columns]
print(maxs)