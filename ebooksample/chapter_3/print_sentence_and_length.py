my_file = open("first_line.txt")
my_file_contents = my_file.read()

# remove the newline from the end of the file contents
sentence = my_file_contents.rstrip("\n")

length = len(sentence)
print("sentence is " + sentence + " and length is " + str(length))
