import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# 创建一个图形并设置大小
plt.figure(figsize=(15, 6))

crude = np.load('crudelist.npy')
crude = crude[0:-1]
print(crude)

lightoil = np.load('lightlist.npy')
lightoil = lightoil[0:-1]
print(lightoil)

fabric = np.load('fabriclist.npy')
fabric = fabric[0:-1]
print(fabric)


date_index = pd.date_range('2020/12', '2023/10', freq='M')
print(date_index)

df_crude = pd.DataFrame({'Value': crude}, index=date_index)

df_light = pd.DataFrame({'Value1': lightoil}, index=date_index)

df_fabric = pd.DataFrame({'Value2': fabric}, index=date_index)


# 绘制月度时序折线图

plt.plot(df_crude.index, df_crude['Value'], label='Risk Value in Crude Oil Trading Layer(IO[1][1])', marker='o')

# 添加标题和标签
plt.xlabel('month',fontsize=15)
plt.ylabel('IO value',fontsize=15)

# 添加图例
plt.legend(fontsize=15)

# 自动调整日期格式
# plt.gcf().autofmt_xdate()
plt.xticks(rotation=0,fontsize=15)
plt.xticks(fontsize=15)
plt.xlim([date_index[0]-datetime.timedelta(days=31), date_index[-1]+datetime.timedelta(days=31)])

# 显示图形
plt.savefig('layeroil.svg', format='svg')
plt.show()

# 创建一个图形并设置大小
plt.figure(figsize=(15, 6))
plt.plot(df_light.index, df_light['Value1'], label='Risk Value of Man-made Fabric Trading Layer Influenced by Crude Oil Trading Layer(IO[2][1])', marker='o',color = 'green')
plt.plot(df_fabric.index, df_fabric['Value2'], label='Risk Value in Man-made Fabric Trading Layer(IO[2][2])', marker='o',color = 'red')

# 添加标题和标签
plt.xlabel('month',fontsize=15)
plt.ylabel('IO value',fontsize=15)

# 添加图例
plt.legend(fontsize=15)

# 自动调整日期格式
# plt.gcf().autofmt_xdate()
plt.xticks(rotation=0,fontsize=15)
plt.xticks(fontsize=15)
plt.xlim([date_index[0]-datetime.timedelta(days=31), date_index[-1]+datetime.timedelta(days=31)])
plt.ylim(340,2000)
# 显示图形
plt.savefig('layerfabric.svg', format='svg')
plt.show()