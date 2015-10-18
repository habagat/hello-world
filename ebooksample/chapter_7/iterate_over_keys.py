ge = open("great_expectations_complete.txt").read()
all_counts = {}
 
words_file = open("common_words.txt")
 
for line in words_file:
    word = line.rstrip("\n")
    count = ge.count(" " + word + " ")
    if count > 0:
        all_counts[word] = count

for word in all_counts.keys(): 
    if all_counts.get(word) > 150: 
        print(word)
