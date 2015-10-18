import csv
data = open("data.csv")
data_reader = csv.reader(data)
for row in data_reader:
    title = row[0] 
    year = int(row[1])
    type = row[2] 
    length = row[3]
    print(title + " published in " + str(year))
