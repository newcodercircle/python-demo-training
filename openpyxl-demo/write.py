import random
import openpyxl as oxl

wb = oxl.Workbook()
ws = wb.active
ws.title = '随机数'

for i in range(30):
	ws.append([random.randint(0, 99) for _ in range(20)])

wb.save('random.xlsx')
