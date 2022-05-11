import pandas as pd
import matplotlib.pyplot as plt
d = pd.read_csv("FoodPrice_in_Turkey.csv")
data1 = d[(d['Year'] == 2019) & (d['Month'] == 12) & (d['ProductName'] == 'Rice - Retail')]
plt.bar(data1['Place'], data1['Price'])
plt.show()
plt.bar(data1['Place'], data1['Price'], width = 0.5)
plt.title('Rice Price in 12/2019', fontsize = 16, color = 'r')
plt.xlabel('Place', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()
data2 = d[(d['Place'] == 'National Average') & (d['Year'] == 2019) & (d['ProductName'] == 'Rice - Retail')]
plt.plot(data2['Month'], data2['Price'])
plt.show()
plt.plot(data2['Month'], data2['Price'], linewidth = 2, marker = '*', markersize=10, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.title('Rice Price of National Average in 2019', fontsize = 16, color = 'r')
plt.xlabel('Month', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()
x = d[(d['Place'] == 'National Average') & (d['ProductName'] == 'Fuel (gas) - Retail') & (d['Year'] == 2019)]
y = d[(d['Place'] == 'National Average') & (d['ProductName'] == 'Rice - Retail') & (d['Year'] == 2019)]
plt.scatter(x['Price'], y['Price'])
plt.show()
plt.scatter(x['Price'], y['Price'], s = 50)
plt.title('Relationship between Rice Price and Gas Price', fontsize = 16, color = 'r')
plt.xlabel('Gas', fontsize = 14)
plt.ylabel('Rice', fontsize = 14)
plt.show()
