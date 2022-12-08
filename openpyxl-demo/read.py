import openpyxl as oxl
import matplotlib.pyplot as plt

wb = oxl.load_workbook('random.xlsx')
ws = wb['随机数']

LEVEL1 = '0~60'
LEVEL2 = '60~80'
LEVEL3 = '80~100'

cnt = {LEVEL1: 0, LEVEL2: 0, LEVEL3: 0}
for row in ws.values:
	for value in row:
		temp = int(value)
		if temp < 60:
			cnt[LEVEL1] += 1
		elif temp < 80:
			cnt[LEVEL2] += 1
		else:
			cnt[LEVEL3] += 1


# 用 matplotlib 作图
x = list(cnt.keys())
y = list(cnt.values())

# 作图
plt.plot(x, y, marker='s', c='r')
plt.xlabel('level', fontsize=16)
plt.ylabel('amount', fontsize=16)

# 在一个新窗口中显示折线图
plt.show()

