# open the input file and read the contents
text_file = open("curiosity_shop.txt")
text = text_file.read()

# find the position of the period which separates the sentences
period_position = text.find(".")

# extract the first sentence and write it to an output file
first_sentence = text[0:period_position+1]
first_sentence_file = open("first_sentence.txt", "w")
first_sentence_file.write(first_sentence)
first_sentence_file.close()

# extract the second sentence and write it to an output file
second_sentence = text[period_position+1:]
second_sentence_file = open("second_sentence.txt", "w")
second_sentence_file.write(second_sentence)
second_sentence_file.close()
