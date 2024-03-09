import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
import folium
import json

people = pd.read_csv('서울특별시_광진구_인구현황_20231231.csv', encoding='cp949') #index_col='행정기관'
new_people = people.drop(0, axis=0)
print(new_people)

geo='EMD_Seoul.geojson'
geo_str=json.load(open(geo, encoding='utf-8'))

gwangjin=folium.Map(location =[37.535,127.084],zoom_start=12,tiles='cartodbpositron' )
folium.Choropleth(geo_data=geo_str, data=new_people, columns=['행정기관', '계'],
                    fill_color='Blues',fill_opacity=1,line_opacity=0.5, key_on='feature.properties.ADM_DR_NM').add_to(gwangjin) 
gwangjin.save('gwangjin.html')


