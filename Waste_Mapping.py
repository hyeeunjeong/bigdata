# 년도별 행정구역 배출량 지도

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import re

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus'] = False

df0=pd.read_csv('../한국환경공단_서울특별시 광진구 행정동별 배출량 정보.csv', encoding='cp949', index_col='행정동 명')
df1=df0.loc[:,'2019년 07월':].T

new_index = []
for i in df1.index:
    tmp = re.sub(r'[ㄱ-ㅎ가-힣]+', '', i)
    new_index.append(tmp[:4])

df1.index = new_index
df1=df1.groupby(df1.index).sum()

print(df1)




