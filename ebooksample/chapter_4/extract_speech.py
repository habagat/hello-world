# open the file which contains the whole text and read the contents
text = open("great_expectations.txt").read()

# open the file which contains the speech locations
speech_locations = open("speech.txt")

# open the output file where we want to save the dialogue
output = open("extracted_speech.txt", "w")

# process the speech locations one line at a time
for line in speech_locations:
    # get the start and stop positions as numbers
    split_line = line.split(',')
    start = int(split_line[0])
    stop = int(split_line[1])

    # extract the text and write it to the output file
    speech = text[start:stop]
    output.write(speech + "\n")

output.close()
