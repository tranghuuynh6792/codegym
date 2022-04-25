import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
# Hiển thị 5 dòng dữ liệu đầu tiên
print(df.head())
df1=pd.read_excel('house_price_dống-da.xlsx')
print(df1.head())
#df2 = pd.read_json('FoodPrice.json')
#print(df2.head())
#df=pd.read_hdf('FoodPrice.h5', 'table')
#df.head()
#url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_North_America'
#df = pd.read_html(url)
#df[0].head()