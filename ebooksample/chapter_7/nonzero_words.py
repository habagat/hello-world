ge = open("great_expectations_complete.txt").read()
words = [' aardvark ', ' abacus ', ' and ' , ' gentleman ', ' over ',
         ' ziggurat ', ' zoology ']
all_counts = {}
for word in words:
    count = ge.count(word)
    if count > 0:
        all_counts[word] = count
print(all_counts)
