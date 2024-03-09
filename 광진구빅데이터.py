import pandas as pd
import matplotlib.pyplot as plt

domestic_df=pd.read_csv('../서울특별시 광진구_가정폐기물현황_20240131.csv', encoding='cp949')
months=[]
recycles=[]
foods=[]

for line in domestic_df:
    (month, recycle, food) = line.split(',')
    months.append(str(month))       
    recycles.append(int(recycle))
    foods.append(int(food))


plot_domestics = plt.figure()
ax = plot_domestics.add_subplot(1,1,1)

# plt.plot(domestic_df["발생년월"], domestic_df[" 재활용폐기물(톤) "], color='green', marker='o', linestyle='solid')
# plt.plot(domestic_df["발생년월"], domestic_df[" 음식물폐기물(톤) "], color='red', marker='o', linestyle='solid')

plt.title("Gwangjin Domestic Waste")
plt.show()