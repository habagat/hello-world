import collections

# read the text and turn it into a list of words
text = open("great_expectations_complete.txt").read()
text = text.lower() 
for punctuation in [',', ':', '.','"', '!', '?', '--','(', ')', '\n', '\r']: 
    text = text.replace(punctuation, ' ') 
all_words = text.split(" ")

cnt = collections.Counter(all_words)
print(cnt.most_common(10))
