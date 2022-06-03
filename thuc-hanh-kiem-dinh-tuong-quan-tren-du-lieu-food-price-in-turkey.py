import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
df = pd.read_csv("FoodPrice_in_Turkey.csv")
df_rice = df[(df.ProductName == "Rice - Retail") & ( df.Place == "National Average")]
print("kích thước bộ dữ liệu: " ,df_rice.shape)
print ("mô tả bộ dữ liệu")
df_rice.describe()
df_rice['time'] =  pd.to_datetime(df_rice['Year'].astype(str) + '/'+df_rice['Month'].astype(str))
plt.plot(df_rice['time'], df_rice['Price'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()
df_rice['time_processed'] = df_rice.Month + (df_rice.Year -2013)*12
plt.plot(df_rice['time_processed'], df_rice['Price'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()
print  ("hệ số tương quan và pvalue tương ứng là: \n",stats.pearsonr(df_rice.time_processed, df_rice.Price))

