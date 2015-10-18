ge = open("great_expectations_complete.txt").read()
words = [' aardvark ', ' abacus ', ' and ' , ' gentleman ', ' over ',
         ' ziggurat ', ' zoology ']
all_counts = {}
for word in words:
    count = ge.count(word)
    if count > 0:
        all_counts[word] = count

print("count for gentleman is " + str(all_counts.get(' gentleman ', 0)))
print("count for aardvark is " + str(all_counts.get(' aardvark ', 0)))
print("count for zoology is " + str(all_counts.get(' zoology ', 0)))
print("count for and is " + str(all_counts.get(' and ', 0)))
