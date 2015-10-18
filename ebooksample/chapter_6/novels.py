data = open("data.csv")

for line in data:
    
    # split the line up
    columns = line.rstrip("\n").split(",")

    # assign the columns to variables
    title = columns[0]
    year = columns[1]
    type = columns[2]
    length = columns[3]

    if type == 'novel' or type == 'novella':
        print(title)
