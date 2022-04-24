import pandas as pd
df=pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
df = df[['date_collected','shop_location','response_time']]
print(df)
df['District']=df['shop_location'].str.split(',').str[0]
df['City']=df['shop_location'].str.split(',').str[1]
print(df['District'])
print(df['City'])
print(df)
df['Day']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.day
df['Month']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.month
df['Year']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.year
print(df['Day'])
print(df['Month'])
print(df['Year'])
print(df)
df['Hour']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.hour
df['Minute']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.minute
df['Second']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.second
print(df['Hour'])
print(df['Minute'])
print(df['Second'])
print(df)