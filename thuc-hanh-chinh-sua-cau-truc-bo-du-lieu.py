import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
df.head()
df.rename(columns={'Place':'Địa điểm','ProductName':'Tên SP'},inplace=True)
df.head()
# Thêm một cột mới với tất cả các giá trị rỗng NaN
df['new_column'] = 'NaN'
df.head()
# Thêm cột giảm giá 10% cho tất cả các bản ghi
# Cách 1: Gán tên cột dưới dạng một chuỗi và thêm giá trị cho cột đó

df['Giảm giá']= pd.Series('10%', index=df.index)
df.head()
# Thêm cột giảm giá 12% cho tất cả các bản ghi
# Cách 2: Sử dụng phương thức insert() gồm 3 đối số
# - đối số đầu tiên là chỉ mục (vị trí) muốn chèn cột mới (chỉ mục là 10--> cột mới được thêm vào vị trí 11 của DataFrame)
# - đối số thứ hai là tên của cột mới muốn chèn 
# - đối số thứ ba giá trị của cột

df.insert(10,'Giảm giá 2',pd.Series('12%', index=df.index))
df.head()
# Sử dụng phương thức append() thêm một dòng vào cuối DataFrame
# Xóa một cột sử dụng hàm del
# Sử dụng phương thức append() thêm một dòng vào cuối DataFrame

df=df.append({'Địa điểm':'NA','ProductId':'RR','Tên SP':'Rice','UmId':10,'UmName':'KG','Month':6,'Year':2021,'Price':84.3785,'Giảm giá':'10%','Giảm giá 2':'12%'},ignore_index=True)
df.tail()  # Hiển thị 5 bản ghi cuối
del df['new_column']
df.head()
# Xóa một cột sử dụng phương thức pop()
# Phương thức pop trả về cột đã xóa

df.pop('Giảm giá 2')
# Xóa một cột sử dụng phương thức drop() 
# Cú pháp: df.drop('column_name', axis=1, inplace=True)
# Trong đó axis = 1 là xóa cột; inplace = True xóa trục tiếp trên dữ liệu gốc mà không phải tạo bản sao

df.drop('Giảm giá', axis=1, inplace=True)
# Xóa nhiều cột sử dụng phương thức drop()
df.drop(['Month','Year'], axis=1, inplace=True)
# Cú pháp: df.drop(Chỉ số dòng cần xóa, axis=0, inplace=True)
# axis = 0 là giá trị mặc định có thể viết tường minh hoặc không
# Xóa dòng có chỉ số 1 (dòng thứ 2) sử dụng phương thức drop()

df.drop(1, axis = 0, inplace=True)
# Xóa các dòng có chỉ số 7377 và 7379 sử dụng phương thức drop()
df.drop([7377,7379], inplace=True)