import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus'] = False

df=pd.read_csv('../서울특별시 광진구_가정폐기물현황_20240131.csv', encoding='cp949')
new_df=pd.DataFrame({"year":(pd.to_datetime(df["발생년월"])).dt.strftime("%Y"), 
                     "domestic":df[" 재활용폐기물(톤) "],
                     "food":df[" 음식물폐기물(톤) "]})
print(new_df)

new_df.groupby("year")['domestic'].sum()

df1 = new_df.groupby("year")['domestic','food'].sum()
print(df1)

plot_domestics = plt.figure()
ax = plot_domestics.add_subplot(1,1,1)

plt.plot(df1['domestic'], color='green', marker='o', linestyle='solid', label='가정폐기물')
plt.plot(df1['food'], color='red', marker='o', linestyle='solid',label='음식폐기물')
plt.legend()

plt.title("광진구 가정 및 음식 폐기물 현황")
plt.show()


