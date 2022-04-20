# Đọc file dữ liệu 'FoodPrice_in_Turkey.cs
import pandas as pd
import numpy as np
import json
df=pd.read_csv('FoodPrice_in_Turkey.csv')
df=df.drop_duplicates(['ProductId'], keep='last')
# Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi cuối cùng, thiết lập lại chỉ số
df=df.drop_duplicates(['ProductId'],keep='last').reset_index(drop=True)
# Tách file chứa thông tin sản phẩm
df_pro = df.loc[:,['ProductId','ProductName','UmId','UmName']]
# Tách file chứa thông tin giá
df_pri = df.loc[:,['ProductId','Place','Month','Year','Price']]
# Tách file chứa thông tin giá với số dòng từ bản ghi 10 đến 20
df_pri10 = df.loc[10:20,['ProductId','Place','Month','Year','Price']]
df1=pd.merge(df_pro,df_pri, on='ProductId')
df2=pd.concat([df_pro,df_pri], axis=1)
df2=pd.concat([df_pro,df_pri,df_pri10], axis=1)
print(df2)