from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import pandas as pd
import matplotlib.pyplot as plt


#사용할 df 입력
df = pd.read_csv('.csv')
data = df[['위도', '경도']]

# 정규화
scaler = StandardScaler()
df_scale = pd.DataFrame(scaler.fit_transform(df), columns = data.columns)

