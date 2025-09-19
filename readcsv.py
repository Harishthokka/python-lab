import csv
with open('table.csv','r') as f:
	rf=csv.reader(f)
	for row in rf:
		print(row)
	
