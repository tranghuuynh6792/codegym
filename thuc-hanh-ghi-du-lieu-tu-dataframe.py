# Đọc dữ liệu vào DataFrame
import pandas as pd
df=pd.read_csv(filepath_or_buffer = 'FoodPrice_in_Turkey.csv', sep = ',')
print(df.head())
df.to_csv('demo_FoodPrice.csv')
df.to_excel('demo_FoodPrice.xlsx')
df.to_json('demo_FoodPrice.json',orient='columns')
df.to_hdf('demo_FoodPrice.h5', 'table')
df.to_html('demo_FoodPrice.html')