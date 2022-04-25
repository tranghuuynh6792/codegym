import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
df.head()
# Truy cập dòng có chỉ số 3 của dữ liệu
tg = df.iloc[3]
print(tg)
# Truy cập các dòng có chỉ số liên tục từ 3 tới 8 của dữ liệu
tg = df.iloc[3:8]
print(tg)
# Truy cập các dòng rời rạc của dữ liệu
tg = df.iloc[[3,5,7]]
print(tg)
# Truy cập cột thứ 4 của dữ liệu
# : được sử dụng để đại diện cho tất cả các dòng.
tg = df.iloc[:,4]
print(tg)
# Truy cập các cột liên tục từ cột 3 tới cột 8 của dữ liệu
tg = df.iloc[:,3:8]
print(tg)
# Truy cập tới phần tử tại dòng 3 cột 7 của dữ liệu
tg = df.iloc[3,7]
print(tg)
# Truy cập tới các phần tử từ dòng 3 đến dòng 4, cột 5 đến cột 6 của dữ liệu
tg = df.iloc[3:5,5:7]
print(tg)
# Truy cập dòng có chỉ số 3 của dữ liệu
tg = df.loc[3]
print(tg)
# Truy cập cột thứ 4 của dữ liệu
tg = df.loc[:,'UmName']
print(tg)
# Truy cập cột thứ 4,5 của dữ liệu
tg = df.loc[:,['UmName','Month']]
print(tg)
# Truy cập tới phần tử tại dòng 3 cột 7 của dữ liệu
tg = df.loc[3,'Price']
print(tg)
# Truy cập tới phần tử có Year >=2019
tg = df.loc[df.Year >= 2019]
print(tg)
# Thay số 5 bằng số 10 trong toàn bộ dữ liệu
df.replace(5,10,inplace = True)
print(df.head())
# Thay mã sản phẩm từ giá trị 52 thành RR trong toàn bộ dữ liệu
# RR là chuỗi ký tự nên được để trong cặp dấu nháy đơn
df.replace(52,'RR',inplace = True)
print(df.head())