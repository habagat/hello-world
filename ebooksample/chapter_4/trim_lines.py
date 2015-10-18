# open the input file
file = open("two_cities.txt")

# open the output file
output = open("trimmed.txt", "w")

# process each line in turn
for line in file:
    # trim the line and add it to the output file
    trimmed_line = line[11:]
    output.write(trimmed_line)
    
    # print a message to the screen
    print("wrote a line with " + str(len(trimmed_line)) + " characters")

output.close()
