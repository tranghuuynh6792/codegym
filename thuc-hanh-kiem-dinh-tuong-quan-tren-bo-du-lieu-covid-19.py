import pandas as pd
from scipy import  stats
df = pd.read_csv("subset-covid-data.csv")
df.describe()
df1 = df.filter(['cases', 'population'])
df1 = df1.dropna()
r, pvalue = stats.pearsonr(df1.cases, df1.population)
print ("r: ", r, "; pvalue: ", pvalue)
#Nhận xét: do pvalue <5%, nên với mức ý nghĩa 5% bác bỏ giả thuyết không, chấp nhận giả thuyết đối
#Kết luận: Giữa dân số và số ca nhiễm có tương quan tuyến tính yếu với nhau
df2 = df.filter(['cases', 'deaths'])
df2 = df2.dropna()
r, pvalue = stats.pearsonr(df2.cases, df2.deaths)
print ("r: ", r, "; pvalue: ", pvalue)
#Nhận xét: do pvalue ~0, nên với mức ý nghĩa 5% bác bỏ giả thuyết không, chấp nhận giả thuyết đối
#Kết luận: Giữa số ca mắc và số ca tử vong có tương quan tuyến tính mạnh với nhau
q1, q2, q3  = df1.population.quantile(0.25), df1.population.quantile(0.5), df1.population.quantile(0.75)
def population_order(population):
    if population < q1:
        return 1
    elif population>=q1 and population <q2:
        return 2
    elif population>=q2 and population <q3:
        return 3
    else: 
        return 4

df1['population_ordinal']=df1.population.apply(population_order)
print(df1.head())
r, pvalue = stats.spearmanr(df1.cases, df1.population_ordinal)
print ("r: ", r, "; pvalue: ", pvalue)
#Nhận xét: do pvalue ~0, r~0.5 nên với mức ý nghĩa 5% bác bỏ giả thuyết không, chấp nhận giả thuyết đối
#Kết luận: Giữa số ca mắc và population_ordinal có tương quan tuyến tính với nhau