import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler
from scipy import stats
df = pd.read_csv("OnlineRetail.csv",encoding = "ISO-8859-1")
print(df.info())
print(df.describe())
testisna = df.isna()
print(testisna.info())
print(testisna.describe())
df2 = df.fillna(value = {"Description":"Không biết"})
z = np.abs(stats.zscore(df2))
threshold = 0
print(np.where(z > threshold))
