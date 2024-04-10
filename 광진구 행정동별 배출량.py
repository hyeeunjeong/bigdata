# 년도별 행정구역 배출량 지도

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib
import re
import folium

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus'] = False

# Folium Map Visualization
# layers = {}
# df_sig=gpd.read_file('../sig.json')
# df_emd=gpd.read_file('../emd.json')
# df_res=pd.merge(df_sig, df_emd, left_on=df_sig['SIG_CD'], right_on=df_emd['EMD_CD'].str[:5], how='left')
# df_tmp=df_res[df_res['SIG_KOR_NM'].isin(['광진구'])].reset_index(drop=True)
# map = folium.Map(location=(37.51434733724219, 127.07303593988632), tiles="cartodbpositron", zoom_start=12)

# Refine
df0=pd.read_csv('../한국환경공단_서울특별시 광진구 행정동별 배출량 정보.csv', encoding='cp949', index_col='행정동 명')
df1=df0.loc[:,'2019년 07월':].T

new_index = []
for i in df1.index:
    tmp = re.sub(r'[ㄱ-ㅎ가-힣]+', '', i)
    new_index.append(tmp[:4])

df1.index = new_index
df1=df1.groupby(df1.index).sum()

print(df1)

# 구간 분할 1500
df2 = df1//1500
print(df2)

# 구간 분할 3000
df3 = df1//3000
print(df3)


# for idx, row in df_tmp.iterrows():
    
#     gu_name = row['SIG_KOR_NM']
#     dong_name = row['EMD_KOR_NM']
#     polygon_wkt = row['geometry_y']
    
#     # 한국어
#     t1 = folium.Choropleth(polygon_wkt, 
#                        style_function=lambda feature, color='blue': {
#                            'fillColor': color,
#                            'fillOpacity': 0.1,
#                            'color': 'black',
#                            'weight': 1,
#                            'opacity': 1
#                        })
    
#     t1.add_to(map)

# map.save("test.html")


