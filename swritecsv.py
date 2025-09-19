import csv
data=[
	['s.no','roll','name'],
	[1,101,'hari'],
	[2,102,'syam'],
	[3,103,'surya']]
with open('table.csv','w',newline='') as f:
	wf=csv.writer(f)
	wf.writerows(data)
