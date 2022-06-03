import pandas as pd
from scipy import  stats
df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv", encoding="UTF-8")
df1 = df.filter(["rating_star", "follower_count"])
df1 = df1.dropna()
print(stats.pearsonr(df1.rating_star, df1.follower_count))
#do p value > 5% nên không có đủ cơ sở bác bỏ giả thuyết không
#Kết luận: giữa rating_star và follower_count không có mối tương quan tuyến tính
df1 = df.filter(["rating_star", "item_count"])
df1 = df1.dropna()
print(stats.pearsonr(df1.rating_star, df1.item_count))
#do p value > 5% nên không có đủ cơ sở bác bỏ giả thuyết không
#Kết luận: giữa rating_star và item_count không có mối tương quan tuyến tính
df1 = df.filter(["is_shopee_verified", "is_official_shop"])
df1 = df1.dropna()
print(stats.pearsonr(df1.is_shopee_verified, df1.is_official_shop))
#do p value > 5% nên không có đủ cơ sở bác bỏ giả thuyết không
#Kết luận: giữa is_shopee_verified và is_official_shop không có mối tương quan tuyến tính