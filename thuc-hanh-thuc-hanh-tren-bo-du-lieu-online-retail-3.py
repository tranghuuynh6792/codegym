import pandas as pd


import matplotlib.pyplot as plt
import numpy as np


import seaborn as sns


from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler


from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder


# đọc dữ liệu


df = pd.read_csv("OnlineRetail.csv", encoding = "ISO-8859-1")
print(df)


# in ra kich thuoc du lieu
print(df.shape)


# kiểm tra dữ liệu bị khuyết
print(df.isna())


# kiểm tra dữ liệu không bị khuyết


print(df['CustomerID'].notna())


# in những dòng ngoại lai Quantity < 0


print(df[df['Quantity'] < 0])


#Xóa bỏ dòng ngoại lai của Quantity


df = df[df['Quantity'] >= 0]


# xóa những dòng chứa giá trị bị khuyết


df1 = df.dropna()


print(df1.shape)


# xóa những dòng chứa toàn giá trị khuyết


df2 = df.dropna(how='all')


df2.shape


# giữ những dòng có ít nhất 7 giá trị không bị khuyết


df3 = df.dropna(thresh=7)


df3.shape


# xóa những hàng mà có giá trị bị khuyết trên cột CustomerID


df4 = df.dropna(subset=["CustomerID"])


# thay thế những giá trị bị khuyết trên cột CustomerID bằng giá trị -1


df5 = df


df5['CustomerID'] = df['CustomerID'].fillna(-1)


# hiển thị những dòng có CustomerID = -1 vừa được thay thế


df5[df5['CustomerID'] == -1]


# thay thế các giá trị bị khuyết ở cột Country bằng giá trị trước nó


df5['Country'] = df['Country'].fillna(method='ffill')


print(df5)


sns.boxplot(x=df1['Quantity'])  # vẽ box plot cho dữ liệu ở cột Quantity


Q1 = df1['Quantity'].quantile(0.25)


Q3 = df1['Quantity'].quantile(0.75)


IQR = Q3 - Q1
# xác định phần tử không phải ngoại lai
#df6 = df1
#df6['outlier'] = ~((df1['Quantity'] < (Q1 - 1.5*IQR)) | (df1['Quantity'] > (Q3 + 1.5*IQR)))

# xóa phần tử ngoại lai
#df6 = df6[df6['outlier'] == True]
#sns.boxplot(x=df6['Quantity'])  # vẽ box plot cho dữ liệu ở cột Quantity
# vẽ biểu đồ hộp cho cột Quantity
#sns.boxplot(x=df1['Quantity'])
print(df1['Quantity'].describe())
# chuẩn hóa dữ liệu với minmax scaling
scaler = MinMaxScaler()

# Chuẩn hóa dữ liệu trong df với MinMaxScaler ở 2 cột Quantity và UnitPrice
df_s = scaler.fit_transform(df1[['Quantity']])
# mô tả dữ liệu sau chuẩn hóa
pd.DataFrame(df_s).describe()
# chuẩn hóa dữ liệu với robust scaling
scaler = RobustScaler()

# Chuẩn hóa dữ liệu trong df với RobustScaler ở 2 cột Quantity và UnitPrice
df_s = scaler.fit_transform(df1[['Quantity']])