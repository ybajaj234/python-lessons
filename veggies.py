vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]
import csv
with open ('vegetables.csv', 'r') as f:
	reader= csv.DictReader(f)
	rows= list(reader)
print(rows)