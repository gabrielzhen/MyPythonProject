import csv
from matplotlib import pyplot as plt
filename='sitka_weather_07-2014.csv'
with open(filename) as f: #使用上下文管理区with as来管理文件的打开和关闭
    reader=csv.reader(f)
    heard_row=next(reader)#获取第一行

  #  for index,colume_heard in enumerate(heard_row):
   #     print(index,colume_heard)

    highs=[]
    for row in reader:#会自动读取每一行数据
        high=int(row[1])
        highs.append(high)

plt.plot(highs,c='red')
plt.show()


