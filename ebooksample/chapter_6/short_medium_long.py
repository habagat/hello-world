data = open("data.csv") 
 
for line in data: 
    
    # split the line up 
    columns = line.rstrip("\n").split(",") 
 
    # assign the columns to variables 
    title = columns[0] 
    year = int(columns[1]) 
    type = columns[2] 
    length = int(columns[3]) 
 
 
    if length < 100000: 
        print(title + " is short") 
    elif 100000 <= length <= 300000:
        print(title + " is medium") 
    else: 
        print(title + " is long")
