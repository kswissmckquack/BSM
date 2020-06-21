from openpyxl import Workbook, load_workbook

def main():
	file = './budgetSummary.xlsx'	
	wb = load_workbook(file, read_only=True, data_only=True)
	sheet = wb.active
	print('INSERT INTO Purchases (Cost,Date,FK_CategoryId) VALUES')
	for i,row in enumerate(sheet):
		if i == 0:
			pass # ignore header
		else:
			dateOf = str('\''+ str(row[0].value).strip()[0:10] + '\'')
			print(
				'(' + dateOf + ',' + str(row[2].value) + ',' + '@rent),\n'
				'(' + dateOf + ',' + str(row[3].value) + ',' + '@stdLoans),\n'
				'(' + dateOf + ',' + str(row[4].value) + ',' + '@isntLoans),\n'
				'(' + dateOf + ',' + str(row[5].value) + ',' + '@carIns),\n'
				'(' + dateOf + ',' + str(row[6].value) + ',' + '@electirc),\n'
				'(' + dateOf + ',' + str(row[7].value) + ',' + '@internet),\n'
				'(' + dateOf + ',' + str(row[8].value) + ',' + '@emergSav),\n'
				'(' + dateOf + ',' + str(row[9].value) + ',' + '@longSav),\n'
				'(' + dateOf + ',' + str(row[10].value) + ',' + '@shortSav),\n'
				'(' + dateOf + ',' + str(row[12].value) + ',' + '@cash),\n'
				'(' + dateOf + ',' + str(row[13].value) + ',' + '@rntIns),\n'
				'(' + dateOf + ',' + str(row[14].value) + ',' + '@spotify),\n'
				'(' + dateOf + ',' + str(row[15].value) + ',' + '@ntflx),\n'
				'(' + dateOf + ',' + str(row[17].value) + ',' + '@invst),\n'
				'(' + dateOf + ',' + str(row[18].value) + ',' + '@credit),\n'
			)

if __name__ == '__main__':
	main()