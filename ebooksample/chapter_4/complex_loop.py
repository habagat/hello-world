characters = ["Pip", "Joe", "Magwitch"]
for character in characters:
	name_length = len(character)
	first_letter = character[0]
	print(character + " is a character from Great Expectations")
	print("His name starts with " + first_letter)
	print("His name has " + str(name_length) + " letters")
