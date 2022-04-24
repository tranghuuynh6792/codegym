import pandas as pd
df =pd.read_csv('D:\Codegym\house_price_dống-da.csv',encoding = 'UTF-8')
df.head()
print (df.info())
df1 = df[(df['type_of_land'] == 'Bán nhà riêng')&(df['ward_name'] == 'Phường Trung Liệt')]
df2 = df[(df['type_of_land'] == 'Bán nhà riêng')&(df['ward_name'] == 'Phường Khâm Thiên')]
df3=df2.append(df1)
print('các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên:\n',df3)
df4 = df[(df['land_certificate'] == 'Sổ đỏ')&(df['bedroom'] >= 3)].filter(['address','price','house_direction','balcony_direction'])
print('các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên:\n',df4)
df_mean = df.groupby('type_of_land')['price'].mean()
df_min = df.groupby('type_of_land')['price'].min()
df_max = df.groupby('type_of_land')['price'].max()
df5 =pd.merge(df_mean,df_min, on='type_of_land')
df6 = pd.merge(df5,df_max, on='type_of_land')
print('trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất của mỗi loại nhà dất:\n',df6)
df7 = df.groupby('ward_name')['bedroom','toilet','floor'].mean()
print('trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường:\n',df7)