import pandas as pd
import numpy as np
df=pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
df1 = df[['join_month', 'join_day','join_year','shop_location','rating_bad','rating_good','rating_normal']]
#Thêm các cột mới từ các cột có dữ liệu kiểu sốTa có thể sử dụng các phép toán số học: +, -, *, /
df['rating'] = df['rating_good'] * 2 + df['rating_normal'] - df['rating_bad'] * 3
#Thêm các cột mới từ các cột có dữ liệu kiểu chuỗiTa có thể sử dụng phép toán ghép chuỗi +Phép toán + dùng để nối các chuỗi lại với nhau, ta dùng hàm astype(str) để đổi một giá trị có kiểu bất kỳ về kiểu chuỗi
df['date'] = df['join_month'] + " " + df['join_day'].astype(str) + "," + df['join_year'].astype(str)
#Thêm các cột mới theo điều kiện
df['new'] = df['join_year'] == 2021
df['rate'] = np.where(df['rating_good'] >= 50000,'good','bad' )
conditions = [(df['rating_good'] >= 30000) & (df['rating_bad'] <= 100),
              (df['rating_good'] >= 10000) & (df['rating_good'] < 30000) & (df['rating_bad'] <= 1000) & (df['rating_bad'] > 100),
              (df['rating_good'] < 10000)]
choices = ['blue', 'yellow','red']
df['flag'] = np.select(conditions, choices, default='black')
print(df1)
print(df['rating'])
print(df['date'])
print(df['new'])
print(df['rate'])
print(conditions)
print(choices)