ge = open("great_expectations_complete.txt").read()
words = [' aardvark ', ' abacus ', ' and ' , ' gentleman ', ' over ' , 
         ' ziggurat ', ' zoology ']
all_counts = []
for word in words:
    count = ge.count(word)
    all_counts.append(count)
print(all_counts)
