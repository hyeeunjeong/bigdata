import geopandas as gpd
from geopandas import GeoDataFrame
import pandas as pd
import json
import requests, json, pprint

def get_address(lat, lng):
    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x="+lng+"&y="+lat
    headers = {"Authorization": "KakaoAK 2ab787c37f03349a696c88ff323d4815"}
    api_json = requests.get(url, headers=headers)
    full_address = json.loads(api_json.text)
    return full_address

geo=json.load(open('광진구_geojson.geojson',encoding='utf-8'))
f = pd.json_normalize(geo['features'])
geo_df=pd.DataFrame(data=f['geometry.coordinates'])
# print(geo_df)
# print(geo_df.loc[0])

for row in geo_df.iterrows():
    print(get_address(str(row[1][0][1]), str(row[1][0][0])))




