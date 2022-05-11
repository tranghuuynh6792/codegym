import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('GDPlist.csv',encoding = "ISO-8859-1")
df2= df.loc[df.Continent == 'South America']
a = plt.bar(df2['Country'],df2['GDP_(millions_of_US$)'])
plt.title('So sánh GDP các nước ở South America', fontsize = 16, color = 'r')
plt.xlabel('Nước', fontsize = 14)
plt.ylabel('GDP', fontsize = 14)
plt.bar_label(a)
plt.show()
df3 = df.query((df.Country == 'Vietnam')or (df.Country == 'Indonesia')or (df.Country == 'Cambodia')or (df.Country =='Thailand') or (df.Country =='Malaysia'))
#df3 = df[df.Country.get_level_values('GDP_(millions_of_US$)').isin(['Vietnam', 'Indonesia', 'Cambodia','Thailand','Malaysia'])]
print(df3)
